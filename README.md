# Plant-P-status-16s-analysis

This is the workflow for the processing of short reads generated for the plant P status project. The raw reads are available via accession number X.
Prior to upstream analysis in R, forward and reverse primer sequences where removed with cutadapt version 2.6. 
Files were proccessed in batch via the "batch_trim_primers.py" bash script with python 3.12.2 in a fresh miniconda 25.3.1 environment.
Further proccessing was done in RStudio 2025.05.0+496 for windows, running R 4.5.0, following the workflow 


