import subprocess

def run_preprocessing():
    print("Running preprocessing.py...")
    subprocess.run(["python", "preprocessing.py"])

def run_processing():
    print("Running processing.py...")
    subprocess.run(["python", "processing.py"])

def run_output():
    print("Running output.py...")
    subprocess.run(["python", "output.py"])

def main():
    run_preprocessing()   # Runs preprocessing.py
    run_processing()      # Runs processing.py
    run_output()          # Runs output.py

if __name__ == "__main__":
    main()
