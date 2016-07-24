import os
import subprocess

if not os.path.exists("models"):
    os.makedirs("models")

if os.path.exists("models_compressed"):
    for filename in os.listdir("models_compressed"):
        print("Uncompressed %s..."%filename)
        if filename.endswith(".7z"):
            subprocess.call(['7z','x','models_compressed/'+filename,"-omodels"])
    print("All files uncompressed")


