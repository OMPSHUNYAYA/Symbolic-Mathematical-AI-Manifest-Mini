"""
Shunyaya Symbolic Mathematical AI (SSM-AIM) — Mini Version
Utility helpers for the public AIM demo.

Intentionally tiny:
- Local JSON memory only
- Simple symbolic-style alignment lane in (-1, +1)
- No external dependencies, no network calls
- Configurable max_sessions + hash_length if config.json exists

Used by: aim_core.py
"""

import json
import os
import math
import hashlib
import unicodedata
from datetime import datetime

# --------------------------------------
# Defaults + config loader
# --------------------------------------

DEFAULT_MEMORY_PATH = "memory.json"
DEFAULT_CONFIG_PATH = "config.json"

DEFAULT_MAX_SESSIONS = 50
DEFAULT_HASH_LENGTH = 12
MAX_INPUT_CHARS = 4000  # safety cap for console cleanliness


def load_config(path: str = DEFAULT_CONFIG_PATH) -> dict:
    """
    Load basic config (max_sessions, hash_length) if present.
    Otherwise return defaults.
    """
    cfg = {
        "max_sessions": DEFAULT_MAX_SESSIONS,
        "hash_length": DEFAULT_HASH_LENGTH,
    }
    if not os.path.exists(path):
        return cfg
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        if isinstance(raw, dict):
            if "max_sessions" in raw:
                cfg["max_sessions"] = int(raw["max_sessions"])
            if "hash_length" in raw:
                cfg["hash_length"] = int(raw["hash_length"])
    except Exception:
        pass
    return cfg


# --------------------------------------
# File + time helpers
# --------------------------------------

def current_utc_iso() -> str:
    """Return current UTC time in ISO 8601 format."""
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def load_memory(path: str = DEFAULT_MEMORY_PATH) -> dict:
    """
    Load AIM mini memory from JSON.
    Start fresh if file invalid.
    """
    if not os.path.exists(path):
        return {"sessions": [], "last_hash": ""}

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "sessions" in data:
            data.setdefault("last_hash", "")
            return data
    except Exception:
        pass

    return {"sessions": [], "last_hash": ""}


def save_memory(memory: dict, path: str = DEFAULT_MEMORY_PATH) -> None:
    """Persist memory to disk."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(memory, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def file_sha256(path: str = DEFAULT_MEMORY_PATH, length: int = DEFAULT_HASH_LENGTH) -> str:
    """
    Return SHA-256 digest (shortened for console).
    """
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        full = h.hexdigest()
        return full[: max(4, length)]
    except Exception:
        return "NA"


def file_sha256_full(path: str = DEFAULT_MEMORY_PATH) -> str:
    """Return full SHA-256 hex digest."""
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return "NA"


def detect_hash_change(memory: dict, current_hash: str) -> str:
    """
    Compare stored memory['last_hash'] with current_hash and
    return a short warning message if mismatch.
    """
    try:
        prev = memory.get("last_hash", "")
        if prev and prev != current_hash:
            return "[verify] memory hash changed since last run"
    except Exception:
        pass
    return ""


# --------------------------------------
# Text cleaning
# --------------------------------------

def sanitize_text(text: str) -> str:
    """
    Basic safety cleaning:
    - Unicode normalization
    - Remove control chars except whitespace
    - Trim overly long input (>4000 chars)
    """
    if not isinstance(text, str):
        text = str(text)

    # Unicode normalize
    t = unicodedata.normalize("NFC", text)

    # Remove control characters
    cleaned = []
    for ch in t:
        if ch.isprintable() or ch in ("\n", "\t", " "):
            cleaned.append(ch)
    out = "".join(cleaned)

    # Trim if excessively long
    if len(out) > MAX_INPUT_CHARS:
        out = out[:MAX_INPUT_CHARS]

    return out


# --------------------------------------
# Session entry mgmt
# --------------------------------------

def append_session_entry(
    memory: dict,
    user_text: str,
    ai_text: str,
    align_value: float,
    ts: str,
    max_sessions: int,
) -> None:
    """
    Append a single interaction to memory["sessions"], with pruning.
    """
    entry = {
        "ts": ts,
        "user": user_text,
        "ai": ai_text,
        "align": round(float(align_value), 4),
    }
    sessions = memory.setdefault("sessions", [])
    sessions.append(entry)

    if isinstance(max_sessions, int) and max_sessions > 0:
        if len(sessions) > max_sessions:
            memory["sessions"] = sessions[-max_sessions:]


# --------------------------------------
# Alignment lane
# --------------------------------------

def _clamp(a: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, a))


def compute_alignment_simple(text: str, turn_index: int, eps_a: float = 1e-6) -> float:
    """
    Tiny alignment lane in (-1, +1).
    """
    stripped = (text or "").strip()
    length = len(stripped)

    # Normalized length up to 400 chars
    norm_len = min(length / 400.0, 1.0)

    # Slight reduction if question
    is_question = stripped.endswith("?")
    raw = norm_len
    if is_question:
        raw -= 0.2

    raw_center = raw - 0.3

    # Gentle drift
    drift = min(turn_index / 50.0, 0.3)
    a_raw = raw_center + drift

    lo, hi = -1.0 + eps_a, 1.0 - eps_a
    a_c = _clamp(a_raw, lo, hi)
    return float(math.tanh(a_c))


def format_align(a: float) -> str:
    """Return compact sign+2dec string like '+0.42'."""
    try:
        val = float(a)
    except Exception:
        val = 0.0
    return f"{val:+.2f}"
