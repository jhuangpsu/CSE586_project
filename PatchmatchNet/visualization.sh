#!/usr/bin/env bash

CHECKPOINT_FILE="./checkpoints/params_000007.ckpt"

# test on DTU's evaluation set
DTU_TESTING="./lists/customized/lab"
python visualization.py --scan_list ./lists/customized/test.txt --input_folder=$DTU_TESTING --output_folder=$DTU_TESTING \
--checkpoint_path $CHECKPOINT_FILE --num_views 4 --image_max_dim 1600 --geo_mask_thres 3 --photo_thres 0.8 "$@"