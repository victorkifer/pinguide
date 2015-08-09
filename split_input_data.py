from input_data import *

def __default_split():
    random_split()

def random_split():
    pass

def equal_share_split():
    pass

def time_split():
    pass

if __name__ == '__main__':
    if not check_input_data_exists():
        exit(-1)

    __default_split()
