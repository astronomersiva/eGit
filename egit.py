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
commands = [
    'git init',
    'git remote add origin ' + user + repo + '.git',
    'git add .',
    'git commit -m "Initial Commit"',
    'git push origin master'
    ]

for command in commands:
    os.system(command)
