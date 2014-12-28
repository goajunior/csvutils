"""csvp.py

Manipulacao de arquivos csvs

"""
import csv
import argparse
import codecs

def changecodec(fin,fileout):

    fout   = codecs.open(fileout, 'w', encoding='utf-8')

    for line in fin:
        fout.write(line)

    return fout

def main():

    # opcoes para linha de comando
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("--fin", default="input.csv", help="arquivo de entrada csv")
    parser.add_argument("--convert",  default="output-utf8.csv", help="arquivo convertido para utf8")
    parser.add_argument("--output",  default="output.txt", help="arquivo de saida")
    args = parser.parse_args()

    filein = open(args.fin, encoding='latin1')

#:TODO: 27.12.14 23:31:05, junior
# implementar a associacao do argumento com essa tarefa

    filetemp = changecodec(filein,args.convert)
    filetemp.close()

#:FIXME: 27.12.14 23:35:23, junior
# o csv.reader nao suporta o utf8

    f = open('output-utf8.csv','rb')
    csv_file = csv.reader(f)

    for linha in csv_file:
        print(linha)
    
    filein.close()


if __name__ == "__main__":
    main()
