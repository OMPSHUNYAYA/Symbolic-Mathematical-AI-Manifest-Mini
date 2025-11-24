# Example Session 01 — SSM-AIM Mini (Real Output Walkthrough)

This example demonstrates a **full real session** with  
**Shunyaya Symbolic Mathematical AI Manifest — SSM-AIM (Mini Version)**  
starting from downloading the script files, preparing the folder,  
and running the mini console.

It includes:

- downloading the correct three files  
- verifying folder structure  
- launching the console  
- interacting with the AI  
- computing hashes  
- viewing history  
- observing symbolic alignment behavior  

This is a **verbatim-style transcript** of a real run,  
cleaned only to remove personal machine identifiers.

---

# 1. Prepare the Project Folder

Download the following **three files** from the GitHub repository:

### From `core/`:
```
aim_core.py
aim_utils.py
```

### From `tests/`:
```
test_aim_utils.py
```

Place all **three files together** inside any folder on your system.  
This will be your SSM-AIM Mini working directory.

Your folder should look like:

```
SSM-AIM-MINI/
    aim_core.py
    aim_utils.py
    test_aim_utils.py
```

When the console runs for the first time, it automatically creates:

```
memory.json
```

---

# 2. Run the Mini Console

From inside the folder, run:

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
  :quit           exit this mini console
  :history        show recent interactions
  :help           show this help again
  :clear          erase local mini memory (with confirmation)
  :verify         show short SHA256 of memory.json
  :verify full    show full SHA256 of memory.json
  :lane           tiny tutorial on the alignment lane
  :export         export full history to a markdown file

Type your message and press Enter to talk to SSM-AIM (Mini).

[verify] memory hash changed since last run
```

---

# 3. Full Real Session Transcript

Below is the **exact real output** captured during an actual Mini session.

---

### **you> hello**
```
[verify] memory_sha256 = 35d19c36ec63
aim[+0.01]> Thank you for sharing. I have recorded this in the mini memory. 
If you want, you can now ask a question about it, or say :history to see recent interactions.
```

---

### **you> I have a new idea about symbolic maths**
```
[verify] memory_sha256 = d6dc4066bc9e
aim[+0.09]> Nice, you are in idea or project mode. Try stating the core goal 
in one sentence. From there, we can outline support, risks, and next moves.
```

---

### **you> The goal is to split the plan into three symbolic layers**
```
[verify] memory_sha256 = aa8eca9c69cb
aim[+0.14]> I hear you are thinking in terms of plans or schedules. 
Try breaking it into 3 small steps you can start soon. If you like, 
describe Step 1 and I will help you refine it.
```

---

### **you> what should I focus on today?**
```
[verify] memory_sha256 = a1eda644318d
aim[-0.13]> You asked a question. I cannot see the full world, but I can help 
you think through it step by step. Try telling me what you already know, 
and what is uncertain. We can separate facts, options, and next actions.
```

---

### **you> I will focus on the core alignment logic**
```
[verify] memory_sha256 = eca795075316
aim[+0.10]> You mentioned alignment or a lane. In this mini console, each 
message gets a tiny lane value a in (-1,+1) as a posture hint, not a judgment. 
You can type :lane to see a brief tutorial on how it is computed.
```

---

### **you> what is my age?**
```
[verify] memory_sha256 = cc2fed32d71c
aim[-0.16]> You asked a question. I cannot see the full world, but I can help 
you think through it step by step. Try telling me what you already know, 
and what is uncertain. We can separate facts, options, and next actions.
```

---

### **you> what is the weather in my city?**
```
[verify] memory_sha256 = 7e19c4f51860
aim[-0.12]> You asked a question. I cannot see the full world, but I can help 
you think through it step by step. Try telling me what you already know, 
and what is uncertain. We can separate facts, options, and next actions.
```

---

### **you> Here is my long reflection…**
```
[verify] memory_sha256 = 52d52f0d93f5
aim[+0.53]> I hear you are thinking in terms of plans or schedules. Try breaking 
it into 3 small steps you can start soon. If you like, describe Step 1 and 
I will help you refine it. This looks reasonably focused; you can build on it steadily.
```

---

### **you> ok**
```
[verify] memory_sha256 = 2534a6313550
aim[+0.00]> Thank you for sharing. I have recorded this in the mini memory. 
If you want, you can now ask a question about it, or say :history to see recent interactions.
```

---

# 4. Using `:history`

### **you> :history**
```
[history] Showing up to last 10 entries:

Time:    2025-11-24T18:08:56Z
Align:   +0.01
User:    ok
SSM-AIM: Thank you for sharing...
----------------------------------------
Time:    2025-11-24T18:11:26Z
Align:   +0.01
User:    hello
SSM-AIM: Thank you for sharing...
----------------------------------------
Time:    2025-11-24T18:11:34Z
Align:   +0.09
User:    I have a new idea about symbolic maths
SSM-AIM: Nice, you are in idea or project mode...
----------------------------------------
Time:    2025-11-24T18:11:43Z
Align:   +0.14
User:    The goal is to split...
SSM-AIM: I hear you are thinking in terms of plans...
----------------------------------------
Time:    2025-11-24T18:11:51Z
Align:   -0.13
User:    what should I focus on today?
SSM-AIM: You asked a question...
----------------------------------------
Time:    2025-11-24T18:11:58Z
Align:   +0.10
User:    I will focus on the core alignment logic
SSM-AIM: You mentioned alignment or a lane...
----------------------------------------
Time:    2025-11-24T18:12:06Z
Align:   -0.16
User:    what is my age?
SSM-AIM: You asked a question...
----------------------------------------
Time:    2025-11-24T18:12:12Z
Align:   -0.12
User:    what is the weather in my city?
SSM-AIM: You asked a question...
----------------------------------------
Time:    2025-11-24T18:13:01Z
Align:   +0.53
User:    Here is my long reflection...
SSM-AIM: I hear you are thinking in terms of plans...
----------------------------------------
Time:    2025-11-24T18:13:15Z
Align:   +0.01
User:    ok
SSM-AIM: Thank you for sharing...
----------------------------------------
```

**Note:**  
`:history full` is *not supported* in the current minimal 23 KB Mini version.

---

# 5. Exit the Console

Use:

```
:quit
```

The console exits cleanly without modifying memory.

---

# End of Example Session 01

This file demonstrates how the SSM-AIM Mini behaves in real usage:
deterministic, offline, symbolic, transparent, and perfectly reproducible.

---

This example is based on a real run of SSM-AIM Mini.
Your alignment values and SHA256 hashes may differ each time.
The shifting alignment value (a ∈ -1..+1) is what makes this a symbolic AI —
each message carries posture, context, and drift, not fixed scripted replies.

