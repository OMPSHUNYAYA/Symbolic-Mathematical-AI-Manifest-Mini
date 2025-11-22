"""
Shunyaya Symbolic Mathematical AI (SSM-AIM) — Mini Version

This is a tiny, fully local personal console:
- No network calls
- No external dependencies beyond Python standard library
- One JSON memory file (memory.json) in the same folder
- Light symbolic-style alignment lane per turn in (-1, +1)

It is NOT the full internal SSM-AI or AIM engine.
It is a public demo that shows:
- a small conversational loop,
- a tiny memory of past interactions,
- a gentle alignment lane for each message.
"""

from typing import Optional

from aim_utils import (
    load_memory,
    save_memory,
    append_session_entry,
    compute_alignment_simple,
    format_align,
    current_utc_iso,
    file_sha256,
    file_sha256_full,
    load_config,
    sanitize_text,
    detect_hash_change,
)


BANNER = r"""
SSM-AIM (Mini Version) — Shunyaya Symbolic Mathematical AI
----------------------------------------------------------
- Fully local, file-based mini personal console
- No internet, no remote calls, no tracking
- One JSON memory file: memory.json

Commands:
  :quit           exit this mini console
  :history        show recent interactions
  :help           show this help again
  :clear          erase local mini memory (with confirmation)
  :verify         show short SHA256 of memory.json
  :verify full    show full SHA256 of memory.json
  :lane           tiny tutorial on the alignment lane
  :export         export full history to a markdown file

Type your message and press Enter to talk to SSM-AIM (Mini).
"""


def add_alignment_suffix(reply: str, align_hint: Optional[float]) -> str:
    """
    Optionally add a short suffix based on the alignment lane.

    This keeps behavior deterministic and very small:
    - For lower alignment, we gently suggest slowing down.
    - For higher alignment, we acknowledge focus and stability.
    """
    if align_hint is None:
        return reply

    try:
        a = float(align_hint)
    except Exception:
        return reply

    if a < -0.3:
        return reply + " You can pause, breathe, and take it one small step at a time."
    if a > 0.3:
        return reply + " This looks reasonably focused; you can build on it steadily."
    return reply


def generate_reply(user_text: str, align_hint: Optional[float] = None) -> str:
    """
    Generate a simple, friendly reply.

    This is a tiny rule-based core by design.
    It is not a large model. It is intentionally transparent.

    The goal:
    - reflect the user's intent,
    - be encouraging,
    - stay grounded and simple,
    - fit in a small script that anyone can inspect.

    The alignment lane is used only as a light hint to optionally
    append a short suffix (via add_alignment_suffix).
    """
    text = (user_text or "").strip()

    if not text:
        base = "I did not receive any content. Try typing a question, idea, or plan."
        return add_alignment_suffix(base, align_hint)

    lower = text.lower()
    base: str

    # Very small patterns to keep behavior readable and deterministic

    if "plan" in lower or "schedule" in lower:
        base = (
            "I hear you are thinking in terms of plans or schedules. "
            "Try breaking it into 3 small steps you can start soon. "
            "If you like, describe Step 1 and I will help you refine it."
        )
        return add_alignment_suffix(base, align_hint)

    if "stress" in lower or "tired" in lower or "overwhelmed" in lower:
        base = (
            "It sounds like you may be under some stress. "
            "One option is to list just one small thing you can do next, "
            "not everything at once. I can help you think through that next step."
        )
        return add_alignment_suffix(base, align_hint)

    if "idea" in lower or "project" in lower:
        base = (
            "Nice, you are in idea or project mode. "
            "Try stating the core goal in one sentence. "
            "From there, we can outline support, risks, and next moves."
        )
        return add_alignment_suffix(base, align_hint)

    # Symbolic / math / formula thinking
    if (
        "math" in lower
        or "symbolic" in lower
        or "equation" in lower
        or "formula" in lower
    ):
        base = (
            "You are thinking in a symbolic or mathematical way. "
            "It can help to name your key variables, write a simple equation, "
            "and separate assumptions from results. I can mirror that structure "
            "with you in plain text."
        )
        return add_alignment_suffix(base, align_hint)

    # Curiosity about alignment lane or score
    if "alignment" in lower or "lane" in lower or "score" in lower:
        base = (
            "You mentioned alignment or a lane. In this mini console, each message "
            "gets a tiny lane value a in (-1,+1) as a posture hint, not a judgment. "
            "You can type :lane to see a brief tutorial on how it is computed."
        )
        return add_alignment_suffix(base, align_hint)

    # Journaling or notes
    if "journal" in lower or "diary" in lower or "note" in lower:
        base = (
            "Treat this like a tiny journal if you wish. "
            "You can write short notes about what happened, what you feel, "
            "and one small thing you might try next. I will reflect it back "
            "and keep a compact local memory for you."
        )
        return add_alignment_suffix(base, align_hint)

    if text.endswith("?"):
        base = (
            "You asked a question. I cannot see the full world, but I can help you "
            "think through it step by step. Try telling me what you already know, "
            "and what is uncertain. We can separate facts, options, and next actions."
        )
        return add_alignment_suffix(base, align_hint)

    # Default: reflective mirror with gentle nudge
    base = (
        "Thank you for sharing. I have recorded this in the mini memory. "
        "If you want, you can now ask a question about it, or say :history "
        "to see recent interactions."
    )
    return add_alignment_suffix(base, align_hint)


def show_history(memory: dict, max_items: int = 10) -> None:
    """
    Print the last few interactions in a compact form.
    """
    sessions = memory.get("sessions", [])
    if not sessions:
        print("\n[history] No previous sessions stored yet.\n")
        return

    print(f"\n[history] Showing up to last {max_items} entries:\n")

    for entry in sessions[-max_items:]:
        ts = entry.get("ts", "?")
        user = entry.get("user", "")
        ai = entry.get("ai", "")
        align = entry.get("align", 0.0)
        print(f"Time:    {ts}")
        print(f"Align:   {format_align(align)}")
        print(f"User:    {user}")
        print(f"SSM-AIM: {ai}")
        print("-" * 40)

    print()


def show_lane_tutorial() -> None:
    """
    Print a tiny tutorial about the alignment lane a in (-1,+1).
    """
    print("\n[lane] Mini alignment lane overview:\n")
    print("This mini console keeps a tiny symbolic lane a in (-1,+1) per message.")
    print("It is a posture hint, not a sentiment score or judgment.\n")
    print("Roughly, for each message:")
    print("  - norm_len = clamp(len(text) / 400, 0, 1)")
    print("  - raw starts from norm_len (questions are a bit lower)")
    print("  - raw is centered around 0 and a small drift term is added")
    print("  - we clamp into a safe range and map with tanh(raw)")
    print()
    print("So in this demo:")
    print("  - a near +1.00 suggests detailed, settled, sustained input,")
    print("  - a near -1.00 suggests short, questioning, or unsettled input,")
    print("  - values near 0.00 are neutral.")
    print("\nIt is only a tiny symbolic posture signal for reflection.\n")


def export_history(memory: dict, path: str = "aim_export.md") -> None:
    """
    Export full history to a small markdown file.
    """
    try:
        sessions = memory.get("sessions", [])
        with open(path, "w", encoding="utf-8") as f:
            f.write("# SSM-AIM Mini Export\n\n")
            if not sessions:
                f.write("_No sessions stored._\n")
                return
            for entry in sessions:
                ts = entry.get("ts", "?")
                user = entry.get("user", "")
                ai = entry.get("ai", "")
                align = entry.get("align", 0.0)
                f.write(f"- Time:  {ts}\n")
                f.write(f"  Align: {format_align(align)}\n")
                f.write(f"  User:  {user}\n")
                f.write(f"  AI:    {ai}\n\n")
        print(f"[export] History written to {path}\n")
    except Exception:
        print("[export] Could not write export file.\n")


def main() -> None:
    """
    Entry point for the SSM-AIM (Mini Version) console.
    """
    print(BANNER)

    # Load basic config (max_sessions, hash_length)
    cfg = load_config()
    max_sessions = int(cfg.get("max_sessions", 50))
    hash_length = int(cfg.get("hash_length", 12))

    # Load previous memory (if any)
    memory = load_memory()

    # Detect hash change since last run (if possible)
    current_hash = file_sha256(length=hash_length)
    warning = detect_hash_change(memory, current_hash)
    if warning:
        print(warning)

    # Turn index: number of existing sessions is our starting point
    sessions = memory.get("sessions", [])
    turn_index = len(sessions)

    while True:
        try:
            raw_input_text = input("you> ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting SSM-AIM (Mini Version). Goodbye.")
            break

        # Sanitize and trim
        user_text = sanitize_text(raw_input_text).strip()

        if not user_text:
            # Ignore empty lines
            continue

        cmd = user_text.lower()

        # Commands
        if cmd in {":quit", "quit", "exit"}:
            print("Exiting SSM-AIM (Mini Version). Goodbye.")
            break

        if cmd in {":help", "help"}:
            print(BANNER)
            continue

        # lane tutorial
        if cmd in {":lane", "lane", ":tutorial", "tutorial"}:
            show_lane_tutorial()
            continue

        # verify (short/full)
        if cmd.startswith(":verify") or cmd.startswith("verify"):
            cleaned = cmd.lstrip(":")
            parts = cleaned.split()
            if len(parts) > 1 and parts[1] == "full":
                full_hash = file_sha256_full()
                print(f"[verify] full SHA256 (memory.json) = {full_hash}")
            else:
                mem_hash = file_sha256(length=hash_length)
                print(f"[verify] memory_sha256 (short) = {mem_hash}")
            continue

        if cmd in {":history", "history"}:
            show_history(memory)
            continue

        if cmd in {":export", "export"}:
            export_history(memory)
            continue

        if cmd in {":clear", "clear"}:
            confirm = input(
                "This will erase local mini memory. "
                "Type 'yes' to confirm: "
            ).strip().lower()
            if confirm == "yes":
                memory = {"sessions": [], "last_hash": ""}
                turn_index = 0
                save_memory(memory)
                print("[clear] Mini memory erased.\n")
            else:
                print("[clear] Cancelled; memory preserved.\n")
            continue

        # Normal conversational turn
        turn_index += 1
        ts = current_utc_iso()
        align_value = compute_alignment_simple(user_text, turn_index)
        reply = generate_reply(user_text, align_value)

        append_session_entry(memory, user_text, reply, align_value, ts, max_sessions)

        # First save updated sessions
        save_memory(memory)

        # Lightweight verification: show short SHA256 of memory.json
        mem_hash = file_sha256(length=hash_length)
        if mem_hash != "NA":
            # Store hash in memory for next-run comparison
            memory["last_hash"] = mem_hash
            save_memory(memory)
            print(f"[verify] memory_sha256 = {mem_hash}")

        print(f"aim[{format_align(align_value)}]> {reply}\n")

    # Final save (defensive)
    save_memory(memory)


if __name__ == "__main__":
    main()
