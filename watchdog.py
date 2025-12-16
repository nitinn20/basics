import subprocess, time, os

SCRIPT_PATH = r"C:\Users\NITIN\Desktop\Contour\diameter.py"

while True:
    # Start the main script
    process = subprocess.Popen(["python", SCRIPT_PATH])
    print("Started main script...")

    # Wait until it exits
    process.wait()

    # Restart delay (20 seconds)
    print("Script stopped. Restarting in 20 seconds...")
    time.sleep(20)
