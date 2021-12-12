import yaml
from yaml import load, dump
from yaml.loader import SafeLoader

with open('fail.yml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)