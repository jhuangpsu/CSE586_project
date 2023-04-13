import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser('''Display the probability map of depth hypotheses''')
parser.add_argument('--data_file', type=str, required=True, help='path to the probability file')
parser.add_argument('--output', type=str, default='', help='output path to save the figure, default to the same path as the input file')
args = parser.parse_args()

def display(args):
    # the file should contain 4 lines
    # depths, probabilities, estimated_depth, true depth
    with open(args.data_file, 'r') as f:
        lines = f.readlines()
    depths = np.fromstring(lines[0], sep=' ').reshape(-1)
    probs = np.fromstring(lines[1], sep=' ').reshape(-1)
    estimated_depth = np.fromstring(lines[2], sep=' ').reshape(-1)[0]
    true_depth = np.fromstring(lines[3], sep=' ').reshape(-1)[0]
    fig, ax = plt.subplots()
    ax.set_title('Probabilities for depth hypotheses', fontsize=15)
    ax.plot(depths, probs, marker='o')
    ax.set_xlabel('depth hypothesis (mm)', fontsize=15)
    ax.set_ylabel('probability', fontsize=15)
    ax.set_ylim(0.0)

    ax.vlines(true_depth, ymin=0.0, ymax=ax.get_ylim()[1], color='red', label='True depth')
    ax.vlines(estimated_depth, ymin=0.0, ymax=ax.get_ylim()[1], color='blue', label='Estimated depth')

    ax.annotate(f'{true_depth:.2f}', xy=(true_depth, ax.get_ylim()[1] / 2.0), xytext=(true_depth, ax.get_ylim()[1] / 2.0))
    ax.annotate(f'{estimated_depth:.2f}', xy=(estimated_depth, ax.get_ylim()[1] / 2.0), xytext=(estimated_depth, ax.get_ylim()[1] / 2.0))

    # xticks = ax.get_xticks()
    # for v in [true_depth, estimated_depth]:
    #     xticks = np.append(xticks, v)
    # xticks_labels = xticks.tolist()
    # xticks_labels[-1] = estimated_depth[0]
    # xticks_labels[-2] = true_depth[0]
    # ax.set_xticks(xticks)
    # ax.set_xticklabels(xticks_labels, fontsize=15)

    plt.legend(loc='best', fontsize=15)
    plt.show()
    if args.output == '':
        output_name = os.path.join(os.path.dirname(args.data_file), 'probability.png')
    else:
        output_name = args.output
    fig.savefig(output_name, bbox_inches='tight')

if __name__ == '__main__':
    display(args)
        