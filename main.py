from seqbio.calculation.SeqCal import atContent,countBase,gcContent,countBasesDict
from seqbio.pattern.SeqPattern import cpgSearch, complementSeq, reverseComplementSeq, enzTargetsScan, reverseSeq
from seqbio.seqman.dnaconvert import dna2rna, dna2protein, loadCodons

def argparserLocal():
    from argparse import ArgumentParser
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subpaesers = parser.add_subparsers(
        title='command', description='Please choose command below:',
        dest='command'
    )
    subpaesers.required = True

    gcContent_command = subpaesers.add_parser('gcContent', help='Calculate GC content')
    gcContent_command.add_argument('-s', '--seq', type=str, default=None, help='Provide sequence')

    countBases_command = subpaesers.add_parser('countBases', help='Count number of each base')
    countBases_command.add_argument('-s', '--seq', type=str, default=None, help='Provide sequence')
    countBases_command.add_argument('-r', '--revcomp', action='store_true', default=False, help='Convert DNA to reverse-complementary')
    
    enzTargets_command = subpaesers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzTargets_command.add_argument('-s', '--seq', type=str, default=None, help='Provide sequence')
    enzTargets_command.add_argument('-e', '--enz', type=str, default=None, help='Provide enzyme name')
    enzTargets_command.add_argument('-r', '--revcomp', action='store_true', default=False, help='Convert DNA to reverse-complementary')

    transcription_command = subpaesers.add_parser('transcription', help='Convert DNA -> RNA')
    transcription_command.add_argument('-s', '--seq', type=str, default=None, help='Provide sequence')
    transcription_command.add_argument('-r', '--revcomp', action='store_true', default=False, help='Convert DNA to reverse-complementary')

    translation_command = subpaesers.add_parser('translation', help='Convert DNA -> Protein')
    translation_command.add_argument('-s', '--seq', type=str, default=None, help='Provide sequence')
    translation_command.add_argument('-r', '--revcomp', action='store_true', default=False, help='Convert DNA to reverse-complementary')
    
    return parser
               
def main():
    parser = argparserLocal()
    args = parser.parse_args()
    if args.command == 'gcContent':
        if args.seq == None:
            print('\n--------------------\n\nERROE: No input sequence\n\n--------------------\n')
            exit(parser.parse_args(['gcContent','-h']))
        print('Input'),args.seq, ('\nGC content ='),gcContent(args.seq.upper())
    if args.command == 'countBases':
        if args.seq == None:
            print('\n--------------------\n\nERROE: No input sequence\n\n--------------------\n')
            exit(parser.parse_args(['countBases','-h']))
        elif args.revcomp:
            print ('Input'), args.seq, ('\ncountBases ='), countBasesDict(reverseComplementSeq(args.seq.upper()))
        else:
            print('Input'), args.seq, ('\ncountBases ='), countBasesDict(args.seq.upper())
    elif args.command == 'enzTargetsScan':
        if args.seq == None or args.enz == None:
            print('\n--------------------\n\nERROE: No input sequence or enzName\n\n--------------------\n')
            exit(parser.parse_args(['enzTargetsScan','-h']))
        elif args.revcomp:
            print ('Input'), args.seq, ('\n'), args.enz, ('sites ='), enzTargetsScan(reverseComplementSeq(args.seq.upper()), args.enz)
        else:
            print('Input'), args.seq, ('\n'), args.enz, ('sites ='), enzTargetsScan(args.seq.upper(), args.enz)
    elif args.command == 'transcription':
        if args.seq == None:
            print('\n--------------------\n\nERROE: No input sequence\n\n--------------------\n')
            exit(parser.parse_args(['transcription','-h']))
        elif args.revcomp:
            print('Input'),args.seq, ('\nTranscription ='), dna2rna(reverseComplementSeq(args.seq.upper()))
        else:
            print('Input'), args.seq, ('\nTranscription ='), dna2rna(args.seq.upper())
    elif args.command == 'translation':
        if args.seq == None:
            print('\n--------------------\n\nERROE: No input sequence\n\n--------------------\n')
            exit(parser.parse_args(['translation','-h']))
        elif args.revcomp:
            print('Input'), args.seq, ('\nTranslation ='), dna2protein(reverseComplementSeq(args.seq.upper()))
        else:
            print('Input'), args.seq, ('\nTranslation ='), dna2protein(args.seq.upper())
    else:
        pass

if __name__ == "__main__":
    main()