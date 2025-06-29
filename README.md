# 🕒 IdleLaunch — Auto Trigger OpenRGB Profiles on Idle

**IdleLaunch** is a lightweight background tool that automatically switches OpenRGB profiles when your system becomes idle. It's ideal for users who want their LEDs to turn off after a period of inactivity and turn back on when activity resumes. This is mostly for Windows, but you can modify the python file for other systems.

---

## ✨ Why?

I switched to [OpenRGB](https://openrgb.org/) to control the LEDs on my system, but there wasn’t a simple way to **turn everything off when the computer goes idle**.

I tried [this project](https://github.com/brunoherrera/OpenRGB-Monitor-Status), but it didn’t work reliably for my setup. So I made a lightweight alternative using Python.

---

## ⚙️ How It Works

- Monitors keyboard and mouse activity.
- After a set number of idle minutes (configured via `idletime.txt`), it:
  - Executes `openrgb-off.lnk` with your **suspend** profile.
- When activity resumes, it:
  - Executes `openrgb-on.lnk` with your **default** profile.

All `.lnk` shortcut files must be placed in the same directory as the `.exe` or `.py` file.

---

## 📁 File Structure

Place these files in the same folder:
- idlelaunch.exe ← compiled version (or run idlelaunch.py)
- idletime.txt ← idle timeout in minutes (e.g., 10)
- openrgb-on.lnk ← shortcut to OpenRGB with --profile default
- openrgb-off.lnk ← shortcut to OpenRGB with --profile suspend

If `idletime.txt` is missing or invalid, it defaults to **10 minutes**.

---

## 🚀 Usage

1. Create two OpenRGB profiles:  
   - `default` (normal lighting)  
   - `suspend` (all LEDs off or minimal)

2. Create two `.lnk` shortcuts:
   - `openrgb-on.lnk` → `OpenRGB.exe --profile default`
   - `openrgb-off.lnk` → `OpenRGB.exe --profile suspend`

3. Place both shortcuts in the same folder as the script or `.exe`.

4. Optionally:
   - Add `idlelaunch.exe` to **Startup**
   - Or create a Task in **Task Scheduler** for silent launch at login

---

## 🐍 Source & Build

You can run the Python source directly:

```bash
python src/idlelaunch.py

To compile into an .exe (requires PyInstaller):

pyinstaller --noconsole --onefile --icon=icon.ico idlelaunch.py

⚠️ Note: The .exe is not code-signed, so antivirus software may flag it as a false positive. You can build it yourself using PyInstaller to avoid this.
```
---

## 📄 License

This project is licensed under the GNU General Public License v3.0.

