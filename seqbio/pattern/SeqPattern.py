import re
# SeqPattern module
def cpgSearch(seq):
    cpgs = []
    for m in re.finditer(r'CG', seq, re.I):
        cpgs.append((m.group(), m.start(), m.end()))
    return cpgs

def enzTargetsScan(seq, enz):
    resEnzyme = dict(EcoRI='GAATTC', BamHI='GGATCC', 
                 HindIII='AAGCTT',AccB2I='[AG]GCGC[CT]',
                 AasI='GAC[ATCG][ATCG][ATCG][ATCG][ATCG][ATCG]GTC',
                 AceI='GC[AT]GC')
    
    out = []
    if enz in resEnzyme:
        for m in re.finditer(resEnzyme.get(enz,),seq):
            out.append((m.group(0),m.start(),m.end()))
    return out

def reverseSeq(seq):
    return seq[::-1]

def complementSeq(seq):
    compl = {"A": "T", "T": "A",
             "G": "C", "C": "G"}
    complementary = "".join([ compl[base] for base in seq ])
    return complementary

def reverseComplementSeq(seq):
    revComp = complementSeq(reverseSeq(seq))
    return revComp