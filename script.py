from git import *
import os.path as osp
import git
import maya.cmds as cmds

#------------Start with User-Interface----------------------
#initialize variable
LocalRepoField = None
LocalPathButton = None


#define id string for the window

winID = 'GitIntegrationUI'

#verify window existance
if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)
    
#create fresh UI window
cmds.window(winID, title='GitHub Integration', widthHeight=[800, 500] )

#Add 1st column
cmds.rowColumnLayout(numberOfColumns=3, columnAttach = [(1,'right',10), (3,'left', 10)], columnWidth=[(1, 250), (2, 250), (3,250)])

#Add controls to the layout
cmds.text(label='Remote Repository URL')
RemoteURL = cmds.textField()
cmds.button( label='Link', command='printTxtField(RemoteURL)' )

#Add controls to the layout
cmds.text(label='Local Repository')
CreateLocalButton = cmds.button( label='Create Local Repo', command='CreateLocalRepo()' )
LocalPathButton =cmds.button(label='Local Directory Path', command='LoadLocalDirectoryPath()')

cmds.showWindow()

#------------------Back-End Functions------------------------
#preparation
join = osp.join

#initialize
remote_path = None
repo = None

#Function: examine if user information exists
def userInformation(Repository):
    config_reader = repo.config_reader()
    
#Function: obtain text input, create repo and print text input into History pane in script editior
def printTxtField( fieldID ):
    global remote_path
    remote_path = cmds.textField( fieldID, query=True, text=True)
    print 'Remote GitHub Repository URL: ' + remote_path
    

#Function: LoadLocalDirectoryPath
def LoadLocalDirectoryPath():
    singleFilter = "All Files (*.*)"
    local_repo = cmds.fileDialog2(fileFilter=singleFilter, dialogStyle=2, fm=3)[0]
    print 'Local Repository Location: ' +  local_repo
    global repo
    repo = Repo(path=local_repo)
    print repo
    global LocalPathButton
    if cmds.button(CreateLocalButton, query=True, exists=True):
        
        cmds.deleteUI(CreateLocalButton, LocalPathButton)
        global LocalRepoField
        LocalRepoField = cmds.textField( editable=False, tx=local_repo)
        LocalPathButton = cmds.button(label='Local Directory Path', command='LoadLocalDirectoryPath()')
    else:
        global LocalRepoField
        cmds.deleteUI(LocalRepoField, LocalPathButton)
        LocalRepoField = cmds.textField(editable=False, tx=local_repo)
        LocalPathButton = cmds.button(label='Change Local Directory Path', command='LoadLocalDirectoryPath()')     

def FindRepoName(remotePathName, index):
    name = ''
    i = index
    found = False
    print i
    print remotePathName
    while found == False:
        if remotePathName[i] == '/':
            found = True
        else:
            name = remotePathName[i] + name
            i = i-1
    return name
    
#Function: CreateLocalRepo
def CreateLocalRepo():
    print '!!!!!' + remote_path
    index = remote_path.find('.git')
    name = FindRepoName(remote_path, index)
    print name
    singleFilter = "All Files (*.*)"
    local_repo = cmds.fileDialog2(fileFilter=singleFilter, dialogStyle=2, fm=3)[0] + '/' + name 
    global repo
    print local_repo
    repo = Repo.clone_from(remote_path, local_repo)
    cmds.deleteUI(CreateLocalButton, LocalPathButton)
    global LocalRepoField
    global LocalPathButton
    LocalRepoField = cmds.textField( editable=False, tx=local_repo)
    LocalPathButton = cmds.button(label='Change Local Directory Path', command='LoadLocalDirectoryPath()')

        
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

