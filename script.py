from git import *
import os.path as osp
import git
import os

join = osp.join

remote_path = "https://github.com/renee0506/PythonGithub.git"

#The above should be obtained from GUI interface

# repo = Repo.clone_from(remote_path, "C:/Users/meiqi/Documents/maya/projects/PythonGithub")
repo = Repo(path="C:/Users/meiqi/Documents/maya/projects/PythonGithub")
config = repo.config_writer()
config.set_value("user", "email", "meiqianye@gmail.com")
config.set_value("user", "name", "Renee Mei")
print (repo)

repo.git.add("--all");

print (repo.git)

repo.index.commit("test username n email")
local_branch = 'master'
remote_branch = 'master'
remote = repo.remotes.origin.push(refspec="{}:{}".format(local_branch, remote_branch))
