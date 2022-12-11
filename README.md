Python School Final Project

## Content
***script.py***
The file contains convert_dna_to_rna and convert_rna_to_protein functions that takes sequences as strings and converts the DNA to RNA, RNA to Proteins respectively. They both return resuling sequences in strings.

gc_ratio_plot is another function that has been implemented here to plot GC content ratio for the different DNA sequences. This fucntion comes together with two helper functions(gc_content_ratio, reas_fasta)

***tests***
* This folder contains tests for the script.py file's functions

***data/description.py***
* dna_to_rna dictionary that shows what changes need s to be done in the sequence to change it from dna to rna sequence
* rna_to_protein dictionary shows conbinations of codons that gives amino acid codes that will lead to different combinations of proteins

***data/first_database.db***
The database that was used for the genome investigation and converting DNA, RNA sequences to get proteins.

***data/sql_script.sql***
The script of the database(first_database.db) that has been created above.

***data/gc_content_ratio_sars_cov_2.png***
The resulting picture of the function gc_ratio_plot in script.py that was created for Task 3.
