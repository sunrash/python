# -*- coding: utf-8 -*-
"""
Example code to call Rosette API to deduplicate a list of names.
"""
from __future__ import print_function

import argparse
import json
import os

from rosette.api import API, NameDeduplicationParameters, RosetteException


def run(key, alt_url='https://api.rosette.com/rest/v1/'):
    """ Run the example """
    # Create an API instance
    api = API(user_key=key, service_url=alt_url)

    name_dedupe_data = "Alice Terry,Alice Thierry,Betty Grable,Betty Gable,Norma Shearer,Norm Shearer,Brigitte Helm,Bridget Helem,Judy Holliday,Julie Halliday"
    threshold = 0.75
    params = NameDeduplicationParameters()
    params["names"] = name_dedupe_data.split(',')
    params["threshold"] = threshold
    try:
        return api.name_deduplication(params)
    except RosetteException as exception:
        print(exception)


PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description='Calls the ' +
                                 os.path.splitext(os.path.basename(__file__))[0] + ' endpoint')
PARSER.add_argument('-k', '--key', help='Rosette API Key', required=True)
PARSER.add_argument('-u', '--url', help="Alternative API URL",
                    default='https://api.rosette.com/rest/v1/')

if __name__ == '__main__':
    ARGS = PARSER.parse_args()
    RESULT = run(ARGS.key, ARGS.url)
    print(json.dumps(RESULT, indent=2, ensure_ascii=False, sort_keys=True).encode("utf8"))
