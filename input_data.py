import os

INPUT_IMAGES = 'input/pin_images.csv'
INPUT_PINS = 'input/pins.csv'
INPUT_REPINS = 'input/repins.csv'
INPUT_USERS = 'input/users.csv'

def files_exist(list):
    '''
    Checks whether the input data exists by given path
    '''
    input_data_exists = True
    for file in list:
        if not os.path.exists(file):
            print 'Input data not found:', file
            input_data_exists = False

    return input_data_exists

def check_input_data_exists():
    input_files = [INPUT_IMAGES, INPUT_PINS, INPUT_REPINS, INPUT_USERS]

    return files_exist(input_files)
