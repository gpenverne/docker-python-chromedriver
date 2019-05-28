#!/usr/bin/python3
from . import Test
import os, yaml, asyncio, sys

def test_features(file):
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_path, '..', 'scenarios', file + '.yml')
    with open(file_path, 'r') as stream:
        try:
            tests = []
            scenarios = yaml.safe_load(stream)
            for key, scenario in scenarios['scenarios'].items():
                tests.append(Test(os.path.join(current_path, 'scenarios', scenario)))

        except yaml.YAMLError as exc:
            print(exc)
            quit()
    for test in tests:
        asyncio.get_event_loop().run_until_complete(test.start())

if ".feature" in sys.argv[1]:
    asyncio.get_event_loop().run_until_complete(Test(sys.argv[1]).start())
else:
    test_features(sys.argv[1])
