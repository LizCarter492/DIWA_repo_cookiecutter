import subprocess
from glob import glob

nb_list = sorted(glob("SE*.ipynb"))

for nb in nb_list:
    print("Running nb")
    subprocess.run(
        f"jupyter nbconvert --execute --to notebook --inplace notebooks/{nb}", 
        shell=True, check=True)

print("Workflow complete")
