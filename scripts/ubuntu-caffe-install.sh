#!/bin/bash

sudo apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install -y libopencv-dev python-opencv
sudo apt-get install -y libboost1.55-all-dev

sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y python-dev
sudo apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev

if [ ! -f master.zip ];
then
	wget https://github.com/BVLC/caffe/archive/master.zip
fi
if [ ! -d caffe-master ];
then
	unzip master.zip
fi
cd caffe-master
cp Makefile.config.example Makefile.config
echo "CPU_ONLY := 1" >> Makefile.config
make all
make test
make runtest
