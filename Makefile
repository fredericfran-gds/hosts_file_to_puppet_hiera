install:
	pip install -r requirements.txt

test:
	python hosts_file_to_puppet_hiera.py -i tests/cmdline/sample_hosts_file -r tests/cmdline/actual_sample_results_file
	diff tests/cmdline/actual_sample_results_file tests/cmdline/expected_sample_results_file

lint:
	find . -path ./virtualenv -prune -o -iname "*.py" -print | xargs pylint

lint-fix:
	autopep8 --in-place --aggressive --aggressive  hosts_file_to_puppet_hiera.py
