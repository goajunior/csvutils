"""csvp.py

Manipulacao de arquivos csvs

"""
import csv
import argparse
import codecs

def changecodec(fin):
    


    return fout

def main():

    # opcoes para linha de comando
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--fin", default="input.csv", help="arquivo de entrada csv")
    parser.add_argument("--output",  default="output.txt", help="arquivo de saida")
    args = parser.parse_args()

    filein = open(args.fin, encoding='latin1')
    fout = changecodec(filein)
    print(args.fout)
    csv_file = csv.reader(fout, dialect='excel')



    # print(csv_file)

    for linha in csv_file:
        print(linha.decode('latin1').encode('utf8'))
    
if __name__ == "__main__":
    main()

