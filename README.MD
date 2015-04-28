#eGit

This is a Python script to automate my Github workflow while 
setting up a new repository.

I feel lazy to type the following commands everytime I set up 
a new repository:

```

git init
git remote add origin https://github.com/astronomersiva/repo.git
git add .
git commit -m "Commit message"
git push origin master
```

So I created eGit(easy Git) to automate this. This is my workflow
now.

* Run python egit.py RepoName
* Type in my credentials when prompted
* That's it!
