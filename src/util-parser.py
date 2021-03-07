#! /usr/bin/env python

#from sys import argv


from utils.file_handler import inspect_file
from utils.transform import to_csv_file, to_json
from modules.microsoft_cidrs import convert_microsoft_cidrs

def main():
  with open('../datasets/Microsoft_ServiceTags_Public_20210301.json', 'r', encoding="utf-8") as fp:
    content = fp.read()
    content = to_json(content)
    if isinstance(content, dict):

      if ('cloud' and 'changeNumber' and 'values' in content) \
        and isinstance(content['values'], list)               \
          and len(content['values']) > 0:

          csv_records = []
          for _r in content['values']:
            csv_records.extend(convert_microsoft_cidrs(_r))
          if len(csv_records) > 0:
            headers = ['ID','NAME','PLATFORM','NETWORK_FEATURES','NETWORK_PREFIX','NETWORK_TARGET']
            to_csv_file(headers, csv_records)


if __name__ == '__main__':
  main()