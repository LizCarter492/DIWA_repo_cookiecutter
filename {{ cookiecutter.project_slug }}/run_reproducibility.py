#!/srv/conda/envs/notebook/bin/python

import subprocess
from path import Path

# Get all standard element files and put them in order
se_list = sorted(Path("notebooks").glob("SE*.ipynb"))

# Run each 
for se_path in se_list:
    print(f"Running {se_path}")
    subprocess.run(
        f"jupyter nbconvert --execute --to notebook --inplace {se_path}", 
        shell=True, check=True)

print("Workflow complete")
