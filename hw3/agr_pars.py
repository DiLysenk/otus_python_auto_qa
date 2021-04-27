import argparse


parser = argparse.ArgumentParser()


parser.add_argument('--url', '-u',
                    type = str,
                    default='google',
                    help='url to make req',
                    required=False)


args = parser.parse_args()

print("All params available:", args)