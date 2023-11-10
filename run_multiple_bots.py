import subprocess

num_instances = 50

for i in range(num_instances):
    subprocess.Popen(["python", "check.py"])
