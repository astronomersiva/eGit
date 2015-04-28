#!/usr/bin/python

import sys
import os

arguments = sys.argv

if len(arguments) < 3:
    print 'Usage: python egit.py RepoName username'
    sys.exit(0)

repo = arguments[1]
username = arguments[2]

try:
    os.chdir(repo)
except:
    print 'Create master first'
    sys.exit(0)

userlink = 'https://github.com/' + username + '/'
commands = [
    'git init',
    'git remote add origin ' + userlink + repo + '.git',
    'git add .',
    'git commit -m "Initial Commit"',
    'git push origin master'
    ]

for command in commands:
    os.system(command)
