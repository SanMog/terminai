
***

# 🚀 TerminAI (FixIt) — AI-Powered SRE Co-Pilot

**TerminAI** is an intelligent CLI wrapper designed for Systems Engineers, DevOps, and Developers. It intercepts terminal errors (`stderr`), performs rapid Root Cause Analysis (RCA) using high-speed LLMs, and suggests actionable, context-aware command fixes.

![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq / Llama 3](https://img.shields.io/badge/LLM-Groq%20%7C%20Llama%203-F56565?style=for-the-badge)
![Docker Sandbox](https://img.shields.io/badge/Testing-Docker%20Sandbox-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> *"Transforming terminal errors from roadblocks into automated solutions with sub-second AI inference."*

---

## 🏛 Philosophy & Architecture

TerminAI is built on three core engineering principles:
1.  **Ultra-Low Latency RCA:** By leveraging the Groq API (Llama 3), error analysis and solution generation happen in milliseconds, preserving the developer's state of flow.
2.  **Deep Contextual Awareness:** The agent understands the specific environments failing (e.g., Python tracebacks, Docker daemon issues, Git conflicts, or system permission denials).
3.  **Human-in-the-Loop (HITL) Security:** TerminAI will *never* execute a system-modifying command without explicit user confirmation, ensuring safe automated remediation.

---

## ✨ Core Features

*   🤖 **AI-Driven Diagnostics:** Parses raw terminal output and identifies the exact root cause of the failure.
*   ⚡ **Instant Command Injection:** Suggests the precise command needed to fix the state (e.g., adding `sudo`, installing missing `pip` packages, correcting typos).
*   🛡️ **Execution Safety:** Built-in interactive prompt (`Apply this fix? [Y/n]`) guarantees human oversight.
*   🐳 **Containerized Sandbox:** Includes a dedicated Docker environment for safely testing edge cases and destructive commands without compromising the host machine.

---

## 🛠 Installation & Setup

### 1. Clone & Install
```bash
git clone https://github.com/SanMog/terminai.git
cd terminai
pip install -e .
```

### 2. Configure LPU / LLM Engine (Groq)
TerminAI utilizes Groq's LPU inference engine for maximum speed.
*   Obtain a free API Key from [console.groq.com](https://console.groq.com).
*   Inject the key into your environment variables:

```bash
# Linux / macOS
export OPENAI_API_KEY="gsk_your_api_key_here"

# Windows (PowerShell)
$env:OPENAI_API_KEY="gsk_your_api_key_here"
```

---

## 💻 Usage Protocol

Simply prefix any standard terminal command with `fixit`.

**Example:**
```bash
fixit "apt-get install python3"
```

If the command fails (e.g., due to missing root privileges), TerminAI intercepts the exit code and `stderr`, triggering the LLM pipeline:

```text
🔴 Problem: Permission denied. You need root privileges.
🟢 Suggested Fix: sudo apt-get install python3

Apply this fix? [Y/n]: 
```

### Typical Use Cases
| Scenario | User Command | AI Diagnostic & Fix |
| :--- | :--- | :--- |
| **Syntax Typo** | `git comit` | `git commit` |
| **Missing Dependency**| `python3 -c 'import numpy'`| `pip install numpy` |
| **Permission Denied** | `cat /root/secret` | `sudo cat /root/secret` |
| **Service Down** | `docker ps` | Recognizes daemon is inactive. |

---

## 🧪 Isolated Testing (Docker Sandbox)

To ensure system integrity while experimenting with the AI, a Dockerized Sandbox is provided. You can intentionally "break" things here safely.

**1. Navigate to the test suite:**
```bash
cd tests
```

**2. Pass your API key and spin up the sandbox:**
```bash
# Windows PowerShell example
$env:OPENAI_API_KEY="gsk_your_key_here"
docker-compose build
docker-compose run terminai-test
```

Once inside the container, you can test various failing scenarios (e.g., `fixit "cat /nonexistent.txt"`) to observe the AI's real-time remediation strategies.

---

**Architect:** SanMog  
**Domain:** SRE / CLI Automation  
**License:** MIT

***
