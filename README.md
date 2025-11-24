# Symbolic-Mathematical-AI-Manifest-Mini (SSM-AIM Mini)

*A tiny, transparent, deterministic, offline AI reflection kernel.*

![License](https://img.shields.io/badge/license-Open%20Standard-brightgreen?style=flat&logo=open-source-initiative) ![CI](https://github.com/OMPSHUNYAYA/Symbolic-Mathematical-AI-Manifest-Mini/actions/workflows/aimmini-ci.yml/badge.svg) ![Stars](https://img.shields.io/github/stars/OMPSHUNYAYA/Symbolic-Mathematical-AI-Manifest-Mini?style=flat&logo=github)

---

## **Executive overview**

**AIM stands for *Artificial Intelligence Manifest* — a fully transparent, rule-based, manifest-driven form of intelligence built on Shunyaya Symbolic Mathematics.**

The **SSM-AIM Mini** console is a tiny, fully local, deterministic reflection tool built from only three Python files. It is:

- **Offline-only** (no network, no external calls)  
- **Stdlib-only** (zero dependencies)  
- **Rule-based** (transparent reply patterns)  
- **Symbolic** (alignment lane `a` in (-1,+1))  
- **Auditable** (file-based memory + SHA-256 tamper-evident hashing)  
- **Deterministic** (same input → same symbolic posture values)

Its goal is clarity, transparency, and reproducibility — not advice or prediction.  
This is a safe, minimal, reflective console designed for open understanding and inspection.

---

## **FAQ**
A growing list of common questions is available in the FAQ inside the `docs/` folder.  
This document will be expanded over time as AIM Mini evolves.

You can view it here:  
[docs/FAQ.md](docs/FAQ.md)

---

## **Example Session (Real Output)**
To understand how SSM-AIM Mini behaves in practice, a fully real transcript  
(starting from folder setup → running the console → history → exit)  
is available here:

[examples/example_session_01.md](examples/example_session_01.md)

---

## **File Integrity (SHA-256)**

To ensure authenticity and prevent accidental modification, verify that the downloaded scripts match these SHA-256 digests:

```
aim_core.py
d33a09eeeabfe4d8d0c3c5a07bc289090d475c14e16135c4562557c105c4e5fc

aim_utils.py
06b08af812ad3f1d909ac8386d0953397e0a8eda802d53244d07c3c9ee70756d

test_aim_utils.py
3df32ce5bce73ca026c77d9e7ce386e98ab677c9f4357012fe7d1384b2c21a47
```

These values allow anyone to independently validate that the files have not been altered.

---

## **Size snapshot (plain Python)**

- **16 KB** — Original minimal console (basic loop + alignment lane)  
- **19 KB** — Added SHA-256 verification and utility refinements  
- **23 KB** — Current full manifest console with hashing, export, tests, and improved safety  
- **108 KB** — Full AIM personal AI concept (philosophy, manifests, deeper symbolic logic)

**The 23 KB version is the official public Mini release.**

---

## **1. Quick start**

### **Requirements**
- Python **3.8+**
- Three files placed in the same folder:
  - `aim_core.py`
  - `aim_utils.py`
  - `test_aim_utils.py` (optional tester)

---

### **Run full test suite**

Before using the console, run all tests to verify integrity:

```
python test_aim_utils.py
```

You should see output similar to:

```
Turn 1 | text = 'hello'
  raw align value: -0.26
  formatted align: -0.26

sanitize_text OK
Short SHA: 70289b4b3295
Full SHA: 70289b4b32956aab125fb22b76f02ab6...
All tests completed.
```

If every block ends with **OK**, the Mini console is fully operational.

---

### **Launch AIM-Mini**

Start the fully local AIM Manifest Console:

```
python aim_core.py
```

You will see:

```
SSM-AIM (Mini Version) — Shunyaya Symbolic Mathematical AI
----------------------------------------------------------
- Fully local, file-based mini personal console
- No internet, no remote calls, no tracking
- One JSON memory file: memory.json

Commands:
  :quit
  :history
  :help
  :clear
  :verify
  :verify full
  :lane
  :export
```

After the banner appears, type any message to begin:

```
you>
```

AIM Mini will compute:

- the symbolic alignment lane `a`  
- a deterministic rule-based reply  
- memory hash verification  
- tamper-evident storage  

---

## **2. Commands overview**

All commands work **with or without** the leading colon.

### **General**
```
quit       | :quit        → Exit the mini console
help       | :help        → Show banner and command list
```

### **Memory**
```
history    | :history     → Show the last 10 stored interactions
clear      | :clear       → Erase local memory after confirmation
```

### **Verification (tamper-evident SHA-256)**
```
verify          | :verify          → Show short SHA-256 prefix of memory.json
verify full     | :verify full     → Show full 64-hex SHA-256 digest
```

### **Symbolic lane**
```
lane       | :lane         → Show the alignment lane tutorial
```

### **Export**
```
export     | :export       → Export full history to aim_export.md
```

---

### **Any other input triggers:**
- **Symbolic alignment lane** computation  
- **Deterministic rule-based reply**  
- **Automatic memory append**  
- **Updated SHA-256 verification**  

Example:

```
you> hello
[verify] memory_sha256 = 2b565b5835b3
aim[-0.24]> Thank you for sharing…
```

---

## **3. Verifiable mini demo**

Representative AIM-Mini session:

```
you> hello
[verify] memory_sha256 = 2b565b5835b3
aim[-0.24]> Thank you for sharing…

you> I am thinking about a plan…
[verify] memory_sha256 = d9d64219b411
aim[-0.12]> I hear you are thinking…
```

To verify memory integrity manually (Windows example):

```
certutil -hashfile memory.json SHA256
```

---

## **4. Core behavior (ASCII)**

### **4.1 Local memory model**

Each turn is stored as a JSON entry:

```
{
  "ts": "2025-11-19T12:34:37Z",
  "user": "hello",
  "ai": "Thank you for sharing...",
  "align": -0.24
}
```

- ISO UTC timestamps  
- Alignment lane rounded to 4 decimals  
- Memory auto-prunes to the **last 50 entries**  

Clear memory anytime:

```
you> clear
```

---

### **4.2 Alignment lane (symbolic posture)**

AIM-Mini computes a symbolic “posture signal”  
`a_out` in **(-1,+1)**.

Logic:

```
norm_len = clamp(len(text)/400, 0, 1)

if endswith("?"):
    norm_len -= 0.2

raw_center = norm_len - 0.3
drift      = min(turn_index/50, 0.3)

a_raw = raw_center + drift
a_out = tanh( clamp(a_raw, -1+eps_a, +1-eps_a) )
```

**Interpretation:**
- `+1.0` → detailed, grounded  
- ` 0.0` → neutral  
- `-1.0` → brief, questioning  

Console prints compact alignment:

```
aim[-0.24]> ...
```

---

## **5. Minimal example session**

```
you> hello
[verify] memory_sha256 = 2b565b5835b3
aim[-0.24]> Thank you for sharing…

you> I have a new project idea about symbolic maths
[verify] memory_sha256 = 8d73f48b5741
aim[-0.01]> Nice — try stating the core goal…

you> what should I focus on today?
[verify] memory_sha256 = d42f69e5026b
aim[-0.28]> You asked a question…
```

A full transcript is available in `examples/` (optional future addition).

---

## **6. Key benefits**

- **Tiny & local** — runs anywhere, no installation  
- **Zero network** — fully offline, no remote access  
- **Deterministic symbolic posture** — same input → same response class  
- **Tamper-evident memory** — SHA-256 verification every turn  
- **Transparent rules** — all logic visible in 3 files  
- **Safe, reflective design** — non-advisory and intentionally simple  
- **Gateway to deeper Shunyaya symbolic systems** — alignment lanes, manifests, and symbolic kernels  

---

## **7. Safety**

The **SSM-AIM Mini** console is:

- **Offline-only**  
- **Non-advisory**  
- **Educational / reflective**  
- **Deterministic and transparent**  
- **Small and auditable**

It must **not** be used for:

- medical  
- legal  
- financial  
- safety-critical  
- operational  

decisions or automation.

AIM Mini is intentionally symbolic, reflective, and minimal.

---

## **8. Licensing — Critical Differentiation**

### **SSM-AIM Mini — Open Standard License**
- Free to use, modify, adapt  
- No fees, no registration, no exclusivity  
- Provided strictly *as-is* with no warranty  
- Intended for education, reflection, and symbolic understanding  
- No commercial restrictions  
- Recommended attribution:  
  **"Shunyaya Symbolic Mathematical AI — SSM-AIM (Mini Version)"**

---

### **SSM-AIM (Full Version) — CC BY 4.0**
- Requires attribution  
- Allows commercial use  
- Contains advanced symbolic, safety, and governance modules  
- Includes deeper alignment, memory, and manifest layers  
- Not included in the Mini console  

---

### **SSM-AI (Core) — CC BY 4.0**
- Foundational symbolic intelligence layer  
- Hyperstructures, alignment lanes, symbolic fusers  
- Underpins AIM Full and future symbolic kernels  
- Not part of the Mini release  

Mini is intentionally decoupled to ensure safe public release.

---

## **9. Related core systems**

- **SSM-AI** — Core symbolic intelligence (CC BY 4.0)  
- **SSM-AIM (Full)** — Full personal AI  
- **SSM-NET** — Symbolic networking  
- **SSM-EQ** — Electrical quantities  
- **SSM-Clock** — Stability clock  
- **SSMDE** — Symbolic data exchange  
- **SSM-Audit / SSM-Align** — Stability & drift analytics  
- **…and many more across the Shunyaya ecosystem**

For a complete overview of all Shunyaya Symbolic Mathematics systems, visit:  
**https://github.com/OMPSHUNYAYA/Shunyaya-Symbolic-Mathematics-Master-Docs**

---

## **10. Topics**

AIM-Mini, symbolic AI, offline AI, zero-centric alignment lane,  
reflection kernels, tamper-evident memory, deterministic hashing,  
Shunyaya Symbolic Mathematics, manifest-driven AI.


