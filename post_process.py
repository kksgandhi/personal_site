import sys, os, datetime
from datetime import datetime
from os import path

MAIN_DIR = sys.argv[1]
TMP_DIR  = sys.argv[2]

def is_relevant(file_name):
    # not markdown
    if file_name[-3:] != ".md": return False 
    # git ignored file, doesn't exist in copied directory
    if not path.isfile(path.join(TMP_DIR, file_name)): return False 
    return True


relevant_files = filter(is_relevant, os.listdir(MAIN_DIR))

def insert(originalfile, string):
    with open(originalfile, 'r') as f:
        with open('/tmp/newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('/tmp/newfile.txt', originalfile)

for file_name in relevant_files:
    tmp_file = path.join(TMP_DIR, file_name)
    org_file = path.join(MAIN_DIR, file_name)

    orig_file_time_str = datetime.fromtimestamp(path.getmtime(org_file)).strftime("%B %e, %Y")
    insert(tmp_file, f'<center><em>Last Modified {orig_file_time_str}</em></center>\n\n-------------------------------\n\n')
