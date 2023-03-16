import maya.cmds as cmds

sels = cmds.ls(sl=True)

for sel in sels:
    shapes = cmds.listRelatives(sel, children=True, shapes=True)

    for shape in shapes:
        cmds.setAttr('%s.overrideEnabled' % (shape), 1)
        cmds.setAttr('%s.overrideColor' % (shape), 6) #royal blue is 6