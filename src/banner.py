import os.path

def print_banner():
    with open(os.path.dirname(__file__) + '\\..\\resources\\banner.txt', 'r') as banner_file:
        print(banner_file.read())

