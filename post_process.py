import sys, os, datetime
from datetime import datetime
from os import path
import re
from itertools import chain

MAIN_DIR = sys.argv[1]
TMP_DIR  = sys.argv[2]

def is_relevant(file_name):
    """
    Which files do we need to analyze?
    We don't want any non-markdown files, nor do we want any files ignored by git
    """
    # not markdown
    if file_name[-3:] != ".md": return False 
    # check if the file exists in the temp dir. If it doesn't, it means it is git ignored and we can ignore it
    if not path.isfile(path.join(TMP_DIR, file_name)): return False 
    return True


all_files      = os.listdir(MAIN_DIR)
relevant_files = filter(is_relevant, all_files)

def insert(originalfile, string):
    """Insert string at the beginning of originalfile"""
    with open(originalfile, 'r') as f:
        with open('/tmp/newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('/tmp/newfile.txt', originalfile)

def add_file_modified_time(org_file, tmp_file):
    """
    Modify tmp_file to include a note about last modify date at the top
    (using last modify date from org_file)
    """
    orig_file_time_str = datetime\
        .fromtimestamp(path.getmtime(org_file))\
        .strftime("%B %e, %Y")
    insert(tmp_file, f'<center><em>This note last modified {orig_file_time_str}</em></center>\n\n-------------------------------\n\n')

def create_empty_files(org_file):
    print(org_file)
    wikilink_regex = r'\[\[([^\]|]+)(?:\||\]\])'
    a = chain(*[re.findall(wikilink_regex, line) for line in open(org_file)])
    print(list(a))

for file_name in relevant_files:
    tmp_file = path.join(TMP_DIR, file_name)
    org_file = path.join(MAIN_DIR, file_name)

    create_empty_files(org_file)
    if file_name != "index.md":
        add_file_modified_time(org_file, tmp_file)
