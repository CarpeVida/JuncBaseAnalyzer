#!/usr/bin/env python3
# Names: Carmelle Catmura(mcatmura) and Daniel Schmelter(dschmelt)
# Group Members: Carmelle Catmura(mcatmura) and Daniel Schmelter(dschmelt)

"""
@author: Carmelle and Daniel

command line usage:
python3 PatientSorter.py LUAD_495.tsv KRAS.txt nonKRAS.txt
"""

import sys, csv

KRAS = open(sys.argv[2], 'w') #sys.argv[2] is KRAS.txt
NoKRAS = open(sys.argv[3], 'w') #sys.argv[3] is NoKRAS.txt


with open(sys.argv[1], 'r') as datafile: #sys.argv[1] is KRAS_Juncbase_Output.tsv
    reader = csv.reader(datafile, dialect='excel-tab')
    for row in reader: #row is a list
        if "LUAD-TCGA-" in row[0]: # to skip reading the column headers
            if "KRAS" in row[8]: #row[8] is the Oncogene_Positive_Alteration column
                mutFullID = row[0]
                a,b,c,d = mutFullID.split("-")
                KRAS.write(b+"-"+c+"-"+d+'\n')
            elif "KRAS" not in row[8]:
                wtFullID = row[0]
                a,b,c,d = wtFullID.split("-")
                NoKRAS.write(b+"-"+c+"-"+d+'\n')


def LastLineDeleter(file):
    writer = open(file, "w")
    lines = writer.readlines()
    writer.writelines([item for item in lines[:-1]])
    writer.close()


#LastLineDeleter(sys.argv[2])
#LastLineDeleter(sys.argv[3])


"""
running JuncBase
python /pod/home/mgmarin/usr/JuncBASE/compareSampleSets.py --in_prefix=/pod/pstore/groups/brookslab/mgmarin/LUAD_Candidate_ID/recomputeSelection/LUAD_495_JuncBASE_UUID_to_TCGAbarcode/TCGAbarcoded_LUAD_RNA_495samples_CandidateExonSelectionOutput --all_psi_output=LUAD_495_PSI_U2AF1_HSmut_comparison.tsv --mt_correction BH --which_test Wilcoxon --thresh 10 --delta_thresh 10.0 --sample_set1 /pod/pstore/groups/brookslab/dschmelt/KRAS_file.txt --sample_set2 /pod/pstore/groups/brookslab/dschmelt/No_KRAS_file.txt

"""
