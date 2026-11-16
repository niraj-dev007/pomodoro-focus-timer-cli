import time
import ctypes
import json
import os
import datetime

filename = "Focus_time.json"
file = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(file, filename)

def notify(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1000)

def countdown(seconds, title):
    print(f"\n--- {title} Started! ---")
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"\r⏳ {title}: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
        
    print(f"\n✅ {title} Finished!")

def load():
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save(data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def start_pomodoro():
    data = load()
    
    print(f"\n{'-'*10} Welcome TO Focus Timer {'-'*10}")
    print("Choose Mode:")
    print("1. Standard (25 min Focus, 5 min Break)")
    print("2. Quick Demo / Test (10 sec Focus, 5 sec Break)")
    
    mode = input("Select mode (1 or 2, default is 1) ==> ").strip()
    if mode == "2":
        focus_seconds = 10
        short_break = 5
        long_break = 10
        print("\n⚡ Test Mode Active (Seconds)")
    else:
        focus_seconds = 25 * 60
        short_break = 5 * 60
        long_break = 15 * 60
        print("\n🍅 Standard Mode Active (25 mins)")
        
    completed_sessions = 0
    current_round = 1
    
    try:
        while True:
            input(f"\nPress ENTER to start FOCUS #{current_round} (or Ctrl+C to quit)...")
            countdown(focus_seconds, f"FOCUS #{current_round}")
            
            completed_sessions += 1
            notify("Focus Done! 🎯", f"Session #{completed_sessions} complete! Take a break.")
            
            if completed_sessions % 4 == 0: 
                print("\n🔥 Great work! You completed 4 sessions! Time for a LONG BREAK!")
                input("\nPress ENTER to start Long Break...")
                countdown(long_break, "Long Break")
                notify("Break Over! ⚡", "Break finished! Ready for the next focus session?")
            else:
                input("\nPress ENTER to start Short Break...")
                countdown(short_break, "Short Break")
                notify("Break Over! ⚡", "Back to work!")

            while True:
                choice = input("\nContinue to next session? (y/n) ==> ").strip().lower()
                if choice in ['y', 'n']:
                    break
                print("Invalid input! Please enter only 'y' or 'n'.")

            if choice == 'n':
                print(f"\n🎉 Awesome job today! Total sessions completed: {completed_sessions}")
                break
                
            current_round += 1

    except KeyboardInterrupt:
        print("\n\n⚠️ Timer stopped by user (Ctrl+C).")

    if completed_sessions > 0:
        today = datetime.date.today().strftime("%d-%m-%Y")
        total_mins = round((focus_seconds * completed_sessions) / 60, 2)
        
        found = False
        for entry in data:
            if entry["date"] == today:
                entry["sessions"] += completed_sessions
                entry["Total_minute"] = round(entry["Total_minute"] + total_mins, 2)
                found = True
                break
        
        if not found:
            data.append({
                "date": today,
                "sessions": completed_sessions,
                "Total_minute": total_mins
            })
            
        save(data)
        print("💾 Your focus history has been saved successfully!")

if __name__ == "__main__":
    start_pomodoro()
