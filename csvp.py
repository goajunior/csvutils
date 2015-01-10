# -*- coding: utf-8 -*-
"""csvp.py

Manipulacao de arquivos csvs


"""

import csv, sys
import argparse
import codecs
import os

def filehandling(fin, convertedfile, outputfile):

    base          = os.path.splitext(fin)[0]
    convertedfile = base + '-utf8.csv'
    outputfile    = base + '-gamil.csv'

    return (convertedfile, outputfile)

def changecodec(fin, fconvert, filein):

    fout   = codecs.open(fconvert, 'w', encoding='utf-8')

    for line in filein:
        fout.write(line)

    fout.close()

    return 

#:TODO: 10.01.15 00:56:02, junior
# implementar a escrita de arquivo no formato csv para o gmail
def gmailcontactcsv(convertedfile, outputfile):

    fout   = codecs.open(outputfile, 'w', encoding='utf-8')

    return

def main():

    count         = 0
    convertedfile = None
    outputfile    = None

    # opcoes para linha de comando

    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('--fin', default='input.csv', help='arquivo de entrada csv')
    parser.add_argument('--convert', action='store_true', help='converte para utf8')
    parser.add_argument( '--gmail',  action='store_true', help='arquivo csv que pode ser importado no gmail')
    parser.add_argument( '--search', help='busca por uma string')

    args = parser.parse_args()

    convertedfile, outputfile = filehandling(args.fin, convertedfile, outputfile)
    print(convertedfile, outputfile)

    filein = open(args.fin, encoding='utf-8')

    if args.convert or args.search :
          changecodec(args.fin, convertedfile, filein)

    for linha in codecs.open(convertedfile, 'rb', encoding='utf-8'):
        matricula, nome, email = linha.split(';')
        if (nome.lower().find(args.search.lower()) >= 0):
            count = count + 1
            print(nome, email)

    if (count == 0):
        print('No match found !')


    filein.close()

if __name__ == '__main__':
    main()
