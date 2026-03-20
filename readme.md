# AutoHeal-Playwright: AI-Powered Self-Healing Automation 🚀

An intelligent end-to-end testing framework that uses **Google Gemini 1.5 Flash** to automatically repair broken CSS selectors in real-time. Built to reduce test maintenance costs and improve CI/CD stability.

## 🛠️ The Problem
In enterprise automation, UI changes (like a developer changing a button ID) often cause "flaky tests." Traditional scripts crash, requiring manual intervention and hours of debugging.

## 💡 The Solution: AI-Driven Healing
This framework wraps Playwright actions in a logic layer that:
1. **Detects Failure:** Identifies when a selector fails to find an element.
2. **Contextual Analysis:** Captures a snapshot of the current Page HTML.
3. **AI Reasoning:** Sends the broken selector and HTML context to **Gemini 1.5 Flash**.
4. **Auto-Repair:** Receives the corrected selector and re-attempts the action instantly.

## 🧰 Tech Stack (2026 Update)

* **Language:** Python 3.9+ (Active venv)
* **Automation:** Playwright (Synchronous API)
* **AI Engine:** Google Gemini 2.5 Flash (via `google-genai` SDK)
* **Configuration:** Pytest with custom `pytest.ini` to silence environment warnings.

## 🚀 How to Run

1. **Clone the repo:**
   `git clone https://github.com/coderpriya-raj/autoheal-playwright.git`
2. **Setup Environment:**
   `source .venv/bin/activate`
   `pip install -r requirements.txt`
3. **Configure API:**
   Add your `GEMINI_API_KEY` to a `.env` file in the root directory.
4. **Run Healed Test:**
   `pytest tests/test_login.py -s`