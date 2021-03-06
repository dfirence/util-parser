
```python
# Microsoft CIDRS JSON
'id': 'ActionGroup',
 'name': 'ActionGroup',
 'properties': {'addressPrefixes': ['13.66.60.119/32',
   '13.66.143.220/30',
   '13.66.202.14/32',
   '13.66.248.225/32',
   '13.66.249.211/32',
   '13.67.10.124/30',
   '13.69.109.132/30',
   '13.71.199.112/30',
   '13.77.53.216/30',
   '13.77.172.102/32',
   '13.77.183.209/32',
   '13.78.109.156/30',
   '13.84.49.247/32',
   '13.84.51.172/32',
   '13.84.52.58/32',
   '13.86.221.220/30',
   '13.106.38.142/32',
   '13.106.38.148/32',
   '13.106.54.3/32',
   '13.106.54.19/32',
   '13.106.57.181/32',
   '13.106.57.196/31',
   '20.38.149.132/30',
   '20.42.64.36/30',
   '20.43.121.124/30',
   '20.44.17.220/30',
   '20.45.123.236/30',
   '20.72.27.152/30',
   '20.150.172.228/30',
   '20.192.238.124/30',
   '20.193.202.4/30',
   '40.68.195.137/32',
   '40.68.201.58/32',
   '40.68.201.65/32',
   '40.68.201.206/32',
   '40.68.201.211/32',
   '40.68.204.18/32',
   '40.115.37.106/32',
   '40.121.219.215/32',
   '40.121.221.62/32',
   '40.121.222.201/32',
   '40.121.223.186/32',
   '51.12.101.172/30',
   '51.12.204.244/30',
   '51.104.9.100/30',
   '52.183.20.244/32',
   '52.183.31.0/32',
   '52.183.94.59/32',
   '52.184.145.166/32',
   '191.233.50.4/30',
   '191.233.207.64/26',
   '2603:1000:4:402::178/125',
   '2603:1000:104:402::178/125',
   '2603:1010:6:402::178/125',
   '2603:1010:101:402::178/125',
   '2603:1010:304:402::178/125',
   '2603:1010:404:402::178/125',
   '2603:1020:5:402::178/125',
   '2603:1020:206:402::178/125',
   '2603:1020:305:402::178/125',
   '2603:1020:405:402::178/125',
   '2603:1020:605:402::178/125',
   '2603:1020:705:402::178/125',
   '2603:1020:805:402::178/125',
   '2603:1020:905:402::178/125',
   '2603:1020:a04:402::178/125',
   '2603:1020:b04:402::178/125',
   '2603:1020:c04:402::178/125',
   '2603:1020:d04:402::178/125',
   '2603:1020:e04:402::178/125',
   '2603:1020:f04:402::178/125',
   '2603:1020:1004:800::f8/125',
   '2603:1020:1104:400::178/125',
   '2603:1030:f:400::978/125',
   '2603:1030:10:402::178/125',
   '2603:1030:104:402::178/125',
   '2603:1030:107:400::f0/125',
   '2603:1030:210:402::178/125',
   '2603:1030:40b:400::978/125',
   '2603:1030:40c:402::178/125',
   '2603:1030:504:802::f8/125',
   '2603:1030:608:402::178/125',
   '2603:1030:807:402::178/125',
   '2603:1030:a07:402::8f8/125',
   '2603:1030:b04:402::178/125',
   '2603:1030:c06:400::978/125',
   '2603:1030:f05:402::178/125',
   '2603:1030:1005:402::178/125',
   '2603:1040:5:402::178/125',
   '2603:1040:207:402::178/125',
   '2603:1040:407:402::178/125',
   '2603:1040:606:402::178/125',
   '2603:1040:806:402::178/125',
   '2603:1040:904:402::178/125',
   '2603:1040:a06:402::178/125',
   '2603:1040:b04:402::178/125',
   '2603:1040:c06:402::178/125',
   '2603:1040:d04:800::f8/125',
   '2603:1040:f05:402::178/125',
   '2603:1040:1104:400::178/125',
   '2603:1050:6:402::178/125',
   '2603:1050:403:400::1f8/125'],
  'changeNumber': 7,
  'networkFeatures': ['API', 'NSG', 'UDR', 'FW'],
  'platform': 'Azure',
  'region': '',
  'regionId': 0,
  'systemService': 'ActionGroup'}}
```

<br />

## Fields To Keep

```text
# CSV Headers: Ideal EndState
platform,systemService,id,name,region,networkFeatures

# Field Types
platform        string
systemService   string
id              string
name            string
region          string
networkFeatures array[string]
addressPrefixes array[string] *network information
```

<br />
<br />

## **Parsing the Record**

```python
# This function parses the JSON
from os import path
from json import loads
from random import randint
rom csv import writer, QUOTE_ALL

def to_csv(headers_list, records_list):
  if isinstance(headers_list, list) and isinstance(records_list, list):
    random = randint(100, 99999)
    outfile = 'parsed_csv_' + str(random) + '.csv'
    with open(outfile, 'w', encoding="utf-8") as fp:
      csv = writer(fp, quoting=QUOTE_ALL, delimiter=',')
      csv.writerows([headers_list])
      csv.writerows(records_list)
      if path.exists(outfile):
        print('\n[+] Successfully Created Outputfile: {0}'.format(outfile))


def convert_microsoft_cidrs(json_record):
  if isinstance(json_record, dict):
    _keys = json_record.keys()
    if 'id' and 'name' and 'properties' in _keys:
      _csv = "{0},{1}".format(json_record['id'], json_record['name'])
      if 'networkFeatures' and 'platform' and 'region' \
        and 'systemService' and 'addressPrefixes' in json_record['properties']:
          network_features = ''
          if isinstance(json_record['properties']['networkFeatures'], list):
            network_features = '|'.join(json_record['properties']['networkFeatures'])
          
          if isinstance(json_record['properties']['networkFeatures'], str):
            network_features = json_record['properties']['networkFeatures']
          
          _csv += "{0},{1},{2}".format(
              json_record['properties']['systemService'],
              json_record['properties']['platform'],
              network_features
            )
          _records = []
          _prefix_type = 'ipv4'
          for _record in json_record['properties']['addressPrefixes']:
            if ':' in _record:
              _prefix_type = 'ipv6'
            _row = "{0},{1},{2}".format(_csv, _prefix_type, _record)
            _records.append(_row.split(','))
          _result = _records
  return _result
```
