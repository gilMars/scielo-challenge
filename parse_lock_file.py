import json
for k, v in json.load(open('Pipfile.lock'))['default'].items():
    print(f'{k}{v["version"]}')
