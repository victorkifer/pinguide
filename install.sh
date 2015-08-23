#!/bin/bash

sudo cp git_filters/clean_ipynb /usr/bin/clean_ipynb
sudo chmod a+X /usr/bin/clean_ipynb

git config filter.clean_ipynb.clean clean_ipynb
git config filter.clean_ipynb.smudge cat
