#!/bin/bash

sudo apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler\
	libopencv-dev python-opencv libboost1.55-all-dev libatlas-base-dev clang python-dev\
	libgflags-dev libgoogle-glog-dev liblmdb-dev\
	python-skimage python-pip

sudo pip install protobuf

if [ ! -d caffe ];
then
	if [ ! -f master.zip ];
	then
		wget https://github.com/BVLC/caffe/archive/master.zip
	fi

	rm -R caffe-master
	unzip master.zip
	rm master.zip
	mv caffe-master caffe
fi

cd caffe
cp Makefile.config.example Makefile.config
echo "CPU_ONLY := 1" >> Makefile.config
make all
make test
make runtest
make pycaffe

wget http://dl.caffe.berkeleyvision.org/bvlc_reference_caffenet.caffemodel
mv bvlc_reference_caffenet.caffemodel models/bvlc_reference_caffenet/

