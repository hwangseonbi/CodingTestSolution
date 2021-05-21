import argparse
import importlib
import baekjoon
import programmers

parser = argparse.ArgumentParser(
    description='Hi! I can help you to solve problem.')
parser.add_argument('source', metavar='S', type=str,
                    help='Supported source : [baekjoon|programmers]')

parser.add_argument('id', metavar='I', type=str,
                    help='Problem id')

args = parser.parse_args()


def main(args):
    switcher = {
        "programmers": programmers,
        "baekjoon": baekjoon
    }
    source_modele = switcher.get(args.source, None)
    source_modele.run(args.id)


main(args)
# programmers_module = importlib.import_module("programmers")
# print(programmers_module.run("1"))
# print(args.sum(args.integers))
