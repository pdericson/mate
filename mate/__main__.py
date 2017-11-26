"""Mate

Aye Aye, Captain!

Usage:
  mate

"""

from __future__ import print_function

import docopt

import mate


def main():
    args = docopt.docopt(__doc__, version=mate.__version__)
    print("Aye Aye, Captain!")


if __name__ == '__main__':
    main()
