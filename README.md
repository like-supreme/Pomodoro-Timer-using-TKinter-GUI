# Pomodoro-Timer-using-TKinter-GUI
Pomodoro Timer (Tkinter)  A **Pomodoro productivity timer** built with Python’s Tkinter GUI library.   The app follows the classic Pomodoro technique:
- 25 minutes work
- 5 minutes short break (repeated 3 times)
- 20 minutes long break after the 4th work session

✔ Marks are shown after each completed work session.

---

## ✨ Features
- **GUI built with Tkinter**: clean and simple layout.
- **Automatic session switching**: no need to manually start breaks.
- **Checkmarks**: every two reps (one work session completed) adds a ✔ symbol.
- **Start / Reset buttons**:
  - **Start**: begins the timer.
  - **Reset**: cancels the active timer, clears marks, and resets everything to the initial state.
- **Bug fixes implemented**:
  - Fixed a bug where clicking the **Start** button multiple times created overlapping timers.
  - Fixed reset so it now cancels the running session and cleanly resets reps and UI.
  - Fixed ✔ checkmarks so they appear **after work sessions**, not after breaks.

---

## 🧰 Requirements
- Python 3 or higher 
- Tkinter (comes with Python standard library, no extra install needed)

---

## ▶️ Usage
1. Clone the repository:
   git clone https://github.com/your-username/pomodoro-timer.git
   cd pomodoro-
   you can also download the zip file for faster result.
Make sure the tomato.png file is available in the correct path.

By default, the script contains:

tomato_img = PhotoImage(file="C:/Users/.../tomato.png")
Important note for Windows users:
In Python, the backslash \ in file paths is interpreted as an escape sequence (e.g. \n, \t).
To avoid issues:

Use forward slashes / instead of backslashes \.
Example:
"C:/Users/username/Desktop/tomato.png"
Or mark the string as a raw string with r"":
r"C:\Users\username\Desktop\tomato.png"
Alternatively, place tomato.png in the same directory as main.py and simplify the path:
tomato_img = PhotoImage(file="tomato.png")
Run the app:
python main.py


📂 Project Structure
├──images
  📸 Screenshots.
├── main.py       # Pomodoro timer implementation
└── tomato.png    # Tomato icon used in the GUI



🚀 Future Improvements
Allow users to customize work/break durations via input fields.

Add sound notifications when a session ends.

Provide statistics of completed Pomodoro cycles.
