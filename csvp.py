# -*- coding: UTF-8 -*-
"""csvp.py

Manipulacao de arquivos csvs


"""

import csv, sys
import argparse
import codecs


def changecodec(fin, fconvert, filein):


#:TODO: 02.01.15 19:35:04, junior
# abrir o arquivo no formato csv
    fout   = codecs.open(fconvert, 'w', encoding='utf-8')

#:TODO: 02.01.15 19:36:11, junior
# escrever no formato do csv para importar no gmail
    for line in filein:
        fout.write(line)

    fout.close()

    return 

def main():

    # opcoes para linha de comando

    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('--fin', default='input.csv', help='arquivo de entrada csv')
    parser.add_argument('--convert', action='append', help='converte para utf8')
    parser.add_argument( '--output',  default='output.txt', help='arquivo de saida')
    parser.add_argument( '--search', help='busca por uma string')
    args = parser.parse_args()

#:FIXME: 27.12.14 23:35:23, junior
# o csv.reader nao suporta o utf8

    # with open('teste.csv', newline='', encoding='utf-8') as f:
    #     reader = csv.reader(f)
    #     for linha in reader:
    #         print(linha)
    # dialect = csv_mod.Sniffer().sniff(codecs.EncodedFile(file,"utf-8").read(1024))

#:FIXME: 02.01.15 19:35:44, junior
# o arquivo deve ser lido como csv

    filein = open(args.fin, encoding='utf-8')

    if args.convert :
        for item in args.convert:
            changecodec(args.fin, item, filein)


    for linha in codecs.open('teste.csv', 'rb', encoding='utf-8'):
        matricula, nome, email = linha.split(';')
        if (nome.lower().find(args.search.lower()) >= 0):
            print(nome.encode('utf-8'), email)

    filein.close()
    print ("à")


if __name__ == '__main__':
    main()
