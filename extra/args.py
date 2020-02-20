#!/apollo/sbin/envroot "$ENVROOT/python3.6/bin/python3.6"

import re
import sys
import os
import subprocess
import argparse
import collections
from dxd_tools_dev.modules import nsm
from multiprocessing import Pool
from prettytable import PrettyTable
from dxd_tools_dev.portdata import border as portdata

def main():
    parser = argparse.ArgumentParser(description="Script to find all available ports on border routers")
    parser.add_argument('-r','--regex', type=str, metavar = '', required = True, help = 'Please type in device regex such as fra53-br-agg-r*')

    args = parser.parse_args()
    return(available_border_port(args))

