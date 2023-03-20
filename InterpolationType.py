import maya.cmds as cmds

#print cmds.nodeType ('')

constraints = cmds.ls(type='parentConstraint')
cmds.select(constraints, r=True)

#now manually go to Interp Type in channel box/layer editor and select shortest

