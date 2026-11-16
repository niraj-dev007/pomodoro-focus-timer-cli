# 🍅 Pomodoro Focus Timer CLI

A robust, distraction-free command-line Pomodoro & Focus Timer built with Python. Designed to help developers and students maintain deep focus, manage study/work intervals, and automatically track daily focus history.

---

## ✨ Features

- **Dual Modes**:
  - `Standard Mode`: 25 min Focus, 5 min Short Break, 15 min Long Break (every 4 sessions).
  - `Demo / Test Mode`: Quick seconds-based cycle (10s Focus, 5s Break) for testing.
- **In-Place Live Countdown**: Real-time `MM:SS` timer display using carriage return (`\r`) without flooding the terminal.
- **Desktop Alert Popups**: Native Windows top-most notification dialogs (`ctypes`) when sessions or breaks finish.
- **Daily Focus Tracking**: Automatically tracks completed sessions and total focused minutes.
- **Smart Date Aggregation**: Merges sessions done on the same day into a single daily record in `Focus_time.json`.
- **Graceful Interrupt Handling**: Safely handles `Ctrl+C` (KeyboardInterrupt) without crashing and saves completed progress.

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/niraj-dev007/pomodoro-focus-timer-cli.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pomodoro-focus-timer-cli
   ```

3. Run the application:
   ```bash
   python focus_timer.py
   ```

> No third-party packages required! Built using Python standard libraries (`time`, `json`, `os`, `datetime`, `ctypes`).

---

## 🛠️ Tech Stack & Concepts

- **Language**: Python 3.x
- **Standard Modules**: `time`, `datetime`, `json`, `os`, `ctypes`
- **Concepts Implemented**:
  - Dynamic time formatting (`divmod` / integer division & modulo)
  - Control Flow & nested input validation
  - Persistent storage with JSON I/O
  - Windows API integration (`ctypes.windll.user32.MessageBoxW`)
  - Exception handling (`try-except KeyboardInterrupt`, `json.JSONDecodeError`)

---

## 📁 Project Structure

```
pomodoro-focus-timer-cli/
│
├── focus_timer.py      # Core timer application
├── Focus_time.json     # Auto-generated daily focus history
└── README.md           # Documentation
```

---

## 👨‍💻 Author

**Niraj** - [GitHub Profile](https://github.com/niraj-dev007)
