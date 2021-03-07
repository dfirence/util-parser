from json import loads, dumps
from os import path
from sys import exit
from random import randint
from csv import writer, QUOTE_ALL


def to_json(s):
  return loads(s)


def from_json(s):
  return dumps(s)


def to_csv_file(headers_list, records_list):
  if isinstance(headers_list, list) and isinstance(records_list, list):
    random = randint(100, 99999)
    outfile = 'parsed_csv_' + str(random) + '.csv'
    try:
    
      with open(outfile, 'w', encoding="utf-8") as fp:
        csv = writer(fp, quoting=QUOTE_ALL, delimiter=',')
        csv.writerows([headers_list])
        csv.writerows(records_list)
        if path.exists(outfile):
          print('\n[+] Successfully Created Outputfile: {0}'.format(outfile))
    
    except Exception as err:
      _error = "(?) Error in function: {0}\n{1}".format(to_csv_file.__name__, err)
      print(_error)
      exit([1])