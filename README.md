# Hosts File to Puppet Hiera

This is a basic utility to convert the `/etc/hosts` file of the Ubuntu server to
create a Puppet Hiera config file.

## Usage

To run the utility:
```
python hosts_file_to_puppet_hiera.py -i <path_to_etc_hosts_file> -r <path_to_results_file>
```
where `<path_to_etc_hosts_file>` is the path to the `/etc/hosts` file that needs to be processed
and `<path_to_results_file>` is the path to store the results, i.e. the hiera config file snippet
