"""
Basic tests for SSM-AIM Mini utilities.
This file is intentionally tiny and runs without any external deps.
"""

from aim_utils import (
    compute_alignment_simple,
    format_align,
    sanitize_text,
    file_sha256,
    file_sha256_full,
    load_config,
    detect_hash_change,
)


# -------------------------------------------
# 1) Alignment + formatting tests
# -------------------------------------------

tests = [
    ("hello", 1),
    ("this is a slightly longer, more detailed message.", 3),
    ("what should I focus on today?", 5),
    ("a very short?", 10),
    (
        "this is a much longer reflective note meant to simulate a user "
        "writing something more detailed after a few turns, to see how the "
        "alignment lane behaves over time.",
        25,
    ),
]

print("Testing compute_alignment_simple + format_align\n")

for text, turn in tests:
    a = compute_alignment_simple(text, turn)
    print(f"Turn {turn} | text = {text!r}")
    print(f"  raw align value: {a}")
    print(f"  formatted align: {format_align(a)}")
    print()


# -------------------------------------------
# 2) Test sanitize_text
# -------------------------------------------

print("\nTesting sanitize_text...\n")

dirty = "hello\u0001\u0002 world 😀" + ("x" * 5000)
cleaned = sanitize_text(dirty)

assert "😀" in cleaned  # printable
assert "\u0001" not in cleaned  # control removed
assert len(cleaned) <= 4000  # trimming limit

print("sanitize_text OK (unicode normalized, control chars removed, trimmed)\n")


# -------------------------------------------
# 3) Test hashing helpers
# -------------------------------------------

print("Testing file_sha256 and file_sha256_full...\n")

short_hash = file_sha256()
full_hash = file_sha256_full()

print(f"Short SHA: {short_hash}")
print(f"Full SHA:  {full_hash}")

# If memory.json does not exist, hashes may be "NA".
if short_hash != "NA":
    assert len(short_hash) >= 4
if full_hash != "NA":
    assert len(full_hash) == 64

print("Hash helpers OK\n")


# -------------------------------------------
# 4) Test config loader
# -------------------------------------------

print("Testing load_config...\n")

cfg = load_config()
assert "max_sessions" in cfg
assert "hash_length" in cfg

print(f"Config loaded: {cfg}")
print("Config loader OK\n")


# -------------------------------------------
# 5) Test hash change detection
# -------------------------------------------

print("Testing detect_hash_change...\n")

memory1 = {"last_hash": "aaaa"}
warn1 = detect_hash_change(memory1, "bbbb")
warn2 = detect_hash_change(memory1, "aaaa")

assert "changed" in warn1
assert warn2 == ""

print("detect_hash_change OK\n")

print("All tests completed.")
