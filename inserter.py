import yaml
import json
from elasticsearch import Elasticsearch, helpers

def gen_data(arr, index):
    for idx, reg in enumerate(arr):
        print('Inserting register #{} on index: {}'.format(idx+1, index))
        yield {
            '_index': index,
            '_type': 'document',
            'doc': reg,
        }

with open('settings.yml', 'r') as settings_file:
    try:
        settings = yaml.safe_load(settings_file)
        with open(settings['file'], 'r') as json_arr:
            es = Elasticsearch()
            helpers.bulk(es, gen_data(json.load(json_arr), settings['elastic_index']))
    except yaml.YAMLError as e:
        print('Yaml {}'.format(e))
    except Exception as e:
        print('Fuck {}'.format(e))
