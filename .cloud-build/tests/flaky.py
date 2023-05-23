# grep PASSED tests.txt | cut -c 10-100 >passed.txt

import os

repo_dir = '/home/jupyter/vertex-ai-samples/'
repo_dir_len = len(repo_dir)
official_dir = f'{repo_dir}notebooks/official'

entries = os.scandir(official_dir)
folders = [entry.path for entry in entries if entry.is_dir()]
# Passing
with open('passed.txt', 'r') as pass_file:
    notebook_names = pass_file.readlines()

notebooks = []
for folder in folders:
    entries = os.scandir(folder)
    for entry in entries:
        notebooks.extend(
            entry.path[repo_dir_len:]
            for notebook in notebook_names
            if entry.name == notebook.rstrip()
        )
with open('passing_tests.txt', 'w') as f:
    for notebook in notebooks:
        f.write(notebook + '\n')


# Failing
with open('failed.txt', 'r') as fail_file:
    notebook_names = fail_file.readlines()

notebooks = []
for folder in folders:
    entries = os.scandir(folder)
    for entry in entries:
        notebooks.extend(
            entry.path[repo_dir_len:]
            for notebook in notebook_names
            if entry.name == notebook.rstrip()
        )
with open('failing_tests.txt', 'w') as f:
    for notebook in notebooks:
        f.write(notebook + '\n')