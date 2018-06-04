#!/bin/bash

travis_ip=$(hostname -I | awk -F' ' '{print $1}')
echo '#########' $travis_ip
