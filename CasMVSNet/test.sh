#!/usr/bin/env bash

TESTPATH="./mvs_customized/lab"
#TESTPATH="./mvs_testing"

TESTLIST="./mvs_customized/test.txt"
#TESTLIST="./lists/dtu/test.txt"

#CKPT_FILE="./casmvsnet.ckpt"
CKPT_FILE="./casmvsnet.ckpt"

python test.py --dataset=general_eval --batch_size=1 --testpath=$TESTPATH  --testlist=$TESTLIST --loadckpt $CKPT_FILE ${@:2}
