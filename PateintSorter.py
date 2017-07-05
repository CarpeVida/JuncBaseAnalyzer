#!/usr/bin/env python3
# Names: Daniel Schmelter(dschmelt) and Carmelle Catmura(mcatmura)
# Group Members: Carmelle Catmura(mcatmura) and Daniel Schmelter(dschmelt)

"""
command line usage:
python3 PatientSorter.py LUAD_495.tsv geneName
"""

import sys, csv, os

class PatientSorter:

    geneInput = str(sys.argv[2]) #sys.argv[2] is geneName
    mutFileName = "%s_MutatedPatients.txt" % geneInput
    WTFileName = "%s_WTPatients.txt" % geneInput
    mutGenePatients = open(mutFileName, 'w')
    WTGenePatients = open(WTFileName, 'w')
    geneFound =False


    with open(sys.argv[1], 'r') as datafile: #sys.argv[1] is KRAS_Juncbase_Output.tsv
        reader = csv.reader(datafile, dialect='excel-tab')
        for row in reader: #row is a list
            if "LUAD-TCGA-" in row[0]: # to skip reading the column headers
                if geneInput in row[8]: #row[8] is the Oncogene_Positive_Alteration column
                    mutFullID = row[0]
                    a,b,c,d = mutFullID.split("-")
                    mutGenePatients.write(b+"-"+c+"-"+d+'\n')
                    geneFound = True
                elif geneInput not in row[8]:
                    wtFullID = row[0]
                    a,b,c,d = wtFullID.split("-")
                    WTGenePatients.write(b+"-"+c+"-"+d+'\n')
    mutGenePatients.close()
    WTGenePatients.close()

    if geneFound:
        print("You have created {0} and {1}".format(WTFileName, mutFileName))
    else:
        os.remove(WTFileName)
        os.remove(mutFileName)
        print("{0} gene was not found in {1} and no files were created".format(geneInput, sys.argv[1]))

temp = PatientSorter()


"""
running JuncBase
python /pod/home/mgmarin/usr/JuncBASE/compareSampleSets.py --in_prefix=/pod/pstore/groups/brookslab/mgmarin/LUAD_Candidate_ID/recomputeSelection/LUAD_495_JuncBASE_UUID_to_TCGAbarcode/TCGAbarcoded_LUAD_RNA_495samples_CandidateExonSelectionOutput --all_psi_output=LUAD_495_PSI_U2AF1_HSmut_comparison.tsv --mt_correction BH --which_test Wilcoxon --thresh 10 --delta_thresh 10.0 --sample_set1 /pod/pstore/groups/brookslab/dschmelt/KRAS_file.txt --sample_set2 /pod/pstore/groups/brookslab/dschmelt/No_KRAS_file.txt

"""

