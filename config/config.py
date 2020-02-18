import argparse
import yaml


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--yaml", default="_config.yml", help="yaml file")
    args = parser.parse_args()
    return args


def get_config(yaml_file):
    with open(yaml_file) as f:
        params = yaml.safe_load(f)
    return params


if __name__ == "__main__":
    args = get_args()
    params = get_config(args.yaml)

    for arg in vars(args):
        print("arg: {}={}".format(arg, getattr(args, arg)))

    for param in params:
        print("param: {}={}".format(param, params[param]))
