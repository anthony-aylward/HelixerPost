import os
import tomllib
from argparse import ArgumentParser
from pathlib import Path
from subprocess import run
from rare_helixerpost.version import __version__
# from rare_helixerpost.helixer_post_bin import ...

HELIXER_POST_BIN_CONFIG_FILE = os.environ.get(
    'HELIXER_POST_BIN_CONFIG_FILE',
    Path.home() / '.helixer_post_bin_config.toml'
)
if Path(HELIXER_POST_BIN_CONFIG_FILE).is_file():
    with open(HELIXER_POST_BIN_CONFIG_FILE, 'rb') as f:
        helixer_post_bin_config = tomllib.load(f)
else:
    helixer_post_bin_config = {}

HELIXER_POST_BIN_PATH = os.environ.get(
    'HELIXER_POST_BIN',
    helixer_post_bin_config.get('helixer_post_bin_path')
)

# <genome.h5> <predictions.h5> <windowSize> <edgeThresh> <peakThresh> <minCodingLength> <gff>
def parse_arguments():
    parser = ArgumentParser(description='sliding window assessment to determine regions of the genome which are likely gene containing')
    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('genome_h5', metavar='<genome.h5>')
    parser.add_argument('predictions_h5', metavar='<predictions.h5>')
    parser.add_argument('window_size')
    parser.add_argument('edge_threshold')
    parser.add_argument('peak_threshold')
    parser.add_argument('min_coding_length')
    parser.add_argument('gff')
    return parser.parse_args()


def main():
    args = parse_arguments()
    if (HELIXER_POST_BIN_PATH is not None or 'helixer_post_bin' in str(os.environ.get('PATH'))):
        run(
            (
                HELIXER_POST_BIN_PATH or 'helixer_post_bin',
                args.genome_h5,
                args.predictions_h5,
                args.window_size,
                args.edge_threshold,
                args.peak_threshold,
                args.min_coding_length,
                args.gff
            ),
            check=False
        )
    else:
        raise RuntimeError('Path to helixer_post_bin not defined')
