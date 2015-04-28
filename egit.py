#!/usr/bin/python

import sys
import os

arguments = sys.argv

if len(arguments) == 1:
    print 'Enter repo name'
    sys.exit(0)

repo = arguments[1]
username = 'astronomersiva'

try:
    os.chdir(repo)
except:
    print 'Create master first'
    sys.exit(0)

user = 'https://github.com/astronomersiva/'

os.system('git init')
os.system('git remote add origin ' + user + repo + '.git')
os.system('git add .')
os.system('git commit -m "Initial Commit"')
os.system('git push origin master')
