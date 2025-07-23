import os
import subprocess
from glob import glob

# Primer sequences
FWD_PRIMER="^AACMGGATTAGATACCCKG"
REV_PRIMER="^ACGTCATCCCCACCTTCC"

# Output directory
output_dir = "trimmed"
os.makedirs(output_dir, exist_ok=True)

# Find all R1 gzipped FASTQ files
r1_files = sorted(glob("*_1.fastq.gz"))

for r1 in r1_files:
    r2 = r1.replace("_1.fastq.gz", "_2.fastq.gz")
    sample = r1.replace("_1.fastq.gz", "")
    
    out_r1 = os.path.join(output_dir, f"{sample}_trimmed_1.fastq.gz")
    out_r2 = os.path.join(output_dir, f"{sample}_trimmed_2.fastq.gz")
    
    cmd = [
        "cutadapt",
        "-g", FWD_PRIMER,
        "-G", REV_PRIMER,
        "-o", out_r1,
        "-p", out_r2,
        r1, r2
    ]
    
    print(f"🔧 Trimming primers for sample: {sample}")
    subprocess.run(cmd, check=True)

