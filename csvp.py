# -*- coding: utf-8 -*-
"""csvp.py

Manipulacao de arquivos csvs


"""

# def filehandling(fin, convertedfile, outputfile) -> funcao para gerenciamento dos arquivos
# def changecodec(fin, fconvert, filein) -> funcao para conversao de latin1 para utf8
# def gmailcontactcsv(convertedfile, outputfile) -> funcao para gerar um arquivo csv para importar no gmail

import csv, sys
import argparse
import codecs
import os

def filehandling(fin, convertedfile, outputfile):

    # geracao dos nomes dos arquivos

    base          = os.path.splitext(fin)[0]  #pega o radical do arquivo de entrada
    convertedfile = base + '-utf8.csv' 
    outputfile    = base + '-gmail.csv'

    return (convertedfile, outputfile)

def changecodec(fin, fconvert, filein):

    fout   = codecs.open(fconvert, 'w', encoding='utf-8')

    # percorre o arquico de entrada linha a linha e escreve no arquivos temporario

    for line in filein:
        fout.write(line)

    fout.close()

    return 

def gmailcontactcsv(convertedfile, outputfile):

    fout = codecs.open(outputfile, 'w', encoding='utf-8')

    fout.write('nome, email\n') #o gmail importa arquivos de contato no formato csv com esse cabecalho

    for linha in codecs.open(convertedfile, 'rb', encoding='utf-8'):
        matricula, nome, email = linha.split(';')
        fout.write('%s, %s' % (nome, email))

    fout.close()
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

    if args.search:
      for linha in codecs.open(convertedfile, 'rb', encoding='utf-8'):
          matricula, nome, email = linha.split(';')
          if (nome.lower().find(args.search.lower()) >= 0):
              count = count + 1
              print(nome, email)

      if (count == 0):
          print('No match found !')

    if args.gmail:
      gmailcontactcsv(convertedfile, outputfile)

    filein.close()

if __name__ == '__main__':
    main()
