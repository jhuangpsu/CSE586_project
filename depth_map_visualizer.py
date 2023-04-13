from posixpath import dirname
import numpy as np
import cv2
import argparse
import os

parser = argparse.ArgumentParser('''Visualize .pfm depth maps''')
parser.add_argument('--depth_map', required=True, type=str, help='Path to the depth map file')
parser.add_argument('--display', default=False, action='store_true', help='Toggle to save the colored depth map instead of visualizing at the runtime')
args = parser.parse_args()

def visualize_depth(args):
    depth_map = cv2.imread(args.depth_map, cv2.IMREAD_UNCHANGED)
    colored_depth_map = cv2.applyColorMap(cv2.convertScaleAbs(depth_map, alpha=0.2), cv2.COLORMAP_JET)
    if args.display:
        cv2.imshow('depth', colored_depth_map)
        cv2.waitKey(0)
    else:
        basename = os.path.basename(args.depth_map).split('.')[0]
        dir_name = os.path.dirname(args.depth_map)
        saved_image = os.path.join(dir_name, f'{basename}_vis.png')
        cv2.imwrite(saved_image, colored_depth_map)

if __name__ == '__main__':
    visualize_depth(args)
