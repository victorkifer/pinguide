#!/usr/bin/python2.7

from input_data import *
import csv
import random

__TRAIN_SET_SIZE__ = 2. / 3.

def __default_split():
    train_set_file = 'input/repins.train.csv'
    test_set_file = 'input/repins.test.csv'

    time_split(INPUT_REPINS, train_set_file, test_set_file)

def random_split(full, train, test):
    '''
    Implements split of input set into train and test sets using random arrangement
    train_size = int (__TRAIN_SET_SIZE__ * len(full))
    test_size = len(full) - train_size
    '''
    with open(full, 'rb') as in_file, open(train, 'wb+') as train_file, open(test, 'wb+') as test_file:
        reader = csv.reader(in_file, delimiter='|')
        train_writer = csv.writer(train_file, delimiter='|')
        test_writer = csv.writer(test_file, delimiter='|')

        for row in reader:
            if random.random() <= __TRAIN_SET_SIZE__:
                train_writer.writerow(row)
            else:
                test_writer.writerow(row)

def equal_share_split():
    pass

def time_split(full, train, test):
    '''
    Implements split of input set into train and test sets using time history arrangement

    train_size = int (__TRAIN_SET_SIZE__ * len(full))
    test_size = len(full) - train_size

    NOTE: function assumes that records in input set are already sorted
    '''
    input_set_size = sum(1 for line in open(full))

    train_set_size = int(input_set_size * __TRAIN_SET_SIZE__)

    with open(full, 'rb') as in_file, open(train, 'wb+') as train_file, open(test, 'wb+') as test_file:
        reader = csv.reader(in_file, delimiter='|')
        train_writer = csv.writer(train_file, delimiter='|')
        test_writer = csv.writer(test_file, delimiter='|')

        index = 0
        for row in reader:
            index += 1
            if index <= train_set_size:
                train_writer.writerow(row)
            else:
                test_writer.writerow(row)


if __name__ == '__main__':
    if not check_input_data_exists():
        exit(-1)

    __default_split()
