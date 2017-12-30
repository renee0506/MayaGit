from git import *
import os.path as osp
import git
import maya.cmds as cmds

#------------Start with User-Interface----------------------
#define id string for the window

winID = 'GitIntegrationUI'

#verify window existance

if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)
    
#create fresh UI window
cmds.window(winID, title='GitHub Integration', widthHeight=[500, 1000] )

#Add 1st column
cmds.rowColumnLayout(numberOfColumns=3, columnAttach=[(1, 'right', 20),(3, 'left', 20)], columnWidth=[(1, 200), (2, 250)])

#Add controls to the layout
cmds.text(label='Remote Repository URL')
RemoteURL = cmds.textField()
cmds.button( label='Link', command='printTxtField(RemoteURL)' )

#Add 2nd column
cmds.rowColumnLayout(numberOfColumns=3, columnAttach=[(1, 'right', 20),(3, 'left', 20)], columnWidth=[(1, 200), (2, 250)])

#Add controls to the layout
cmds.text(label='Local Repository')
LocalRepository = cmds.textField()
cmds.button( label='Link', command='linkLocalRepo(LocalRepo)' )

cmds.showWindow()

#------------------Back-End Functions------------------------
#preparation
join = osp.join

#initialize variable remote_path
remote_path =''

#Function: examine if user information exists
def userInformation(Repository):
    config_reader = repo.config_reader()
    
#Function: obtain text input, create repo and print text input into History pane in script editior
def printTxtField( fieldID ):
    remote_path = cmds.textField( fieldID, query=True, text=True)
    print 'Remote GitHub Repository URL: ' + remote_path
    repo = Repo(path='C:/Users/meiqi/Documents/maya/projects/PythonGithub')

#Function: link local repo to this file
def linkLocalRepo(fieldID):
    local_repo = cmds.textField( fieldID, query=True, text=True)
    print local_repo

# repo = Repo.clone_from(remote_path, "C:/Users/meiqi/Documents/maya/projects/PythonGithub")
    
    config_reader = repo.config_reader()
#config.set_value('user', 'email', 'meiqianye@gmail.com')
#config.set_value('user', 'name', 'Renee Mei')
    print (repo)
    print config_reader.get_value("user", "email")
    

repo.git.add('--all');

print (repo.git)

repo.index.commit('test username n email')
local_branch = 'master'
remote_branch = 'master'
remote = repo.remotes.origin.push(refspec='{}:{}'.format(local_branch, remote_branch))
