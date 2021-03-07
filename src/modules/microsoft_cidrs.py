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