#!/usr/bin/env python

import re
import argparse
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

PROGRAM_NAME = "Hosts File to Puppet Hiera Config Utility"

def convert(hosts_file_path, results_file_path):
	with open(hosts_file_path) as hosts_file:
		with open(results_file_path, "w+") as results_file:
			for line in hosts_file:
				if line.startswith("#"):
					continue
				line_sanitized = line.rstrip('\n')
				logging.info("processing line: %s", line_sanitized)
				line_components=re.split(' |\t', line_sanitized)
				num_hostnames = len(line_components) - 1
				if num_hostnames >= 1:
					results_file.write("%s:\n" % line_components[1].rstrip('\n'))
					results_file.write("  ip: %s\n" % line_components[0].rstrip('\n'))
				if num_hostnames > 1:
					results_file.write("  host_aliases:\n")
					for host_alias_index in range(2, num_hostnames+1):
						results_file.write("    - %s\n" % line_components[host_alias_index].rstrip('\n'))

def get_args():
    """
    function to retrieve command arguments from the command line
    """

    parser = argparse.ArgumentParser(prog='{}'.format(PROGRAM_NAME),
                                     description=
                                     'This utility a /etc/hosts file to be converted to a Puppet Hiera config')
    parser.add_argument("-i", "--hosts_file", required=True,
                        help="path of the hosts file", dest="hosts_file_path")
    parser.add_argument("-r", "--results_file", required=True,
                        help="path where to store the results file, i.e. the hiera config file", dest="results_file_path")

    args = parser.parse_args()

    return args

if __name__ == "__main__":
	logging.info("Starting %s...", PROGRAM_NAME)
	args=get_args()
	logging.info("Hosts File Path: %s and Results File Path: %s", args.hosts_file_path, args.results_file_path)
	convert(args.hosts_file_path, args.results_file_path)
