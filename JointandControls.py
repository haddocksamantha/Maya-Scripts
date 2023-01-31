import maya.cmds as cmds

'''
THIS IS NOT MY CODE, THIS IS NOTES TAKEN BY A CLASSMATE BASED ON CLAYTON LANTZ's CODE 
NEED TO STUDY AND MODIFY
'''

def create_joints():
    """
    Creates joints at world orient
    :return:
    """
    sels = cmds.ls(sl=True)
    joints = []


    for sel in sels:
        cmds.select(clear=True)
        pos = cmds.xform(sel, q=True, worldSpace = True, translation=True)

        joint = cmds.joint(position=pos, absolute = True)
        joints.append(joint)

    cmds.select(joints clear=True) ##checkLine

    return joints

create_joints()

def create_control():
    """
    create control at selected object transform
    :return: [controls]
    """
    sels = cmds.ls(sl=True)
    ctrls = []

    for sel in sels:
        cmds.select(clear=True)

        ctrl = cmds.circle(center=[0, 0, 0], normal=[1, 0, 0], sweep=360, #creates a nurb circle
                    radius=1, d=3, ut=0, tolerance=.01, sections=8, ch=True) [0] #this returns only the first object in the list

        xform_data = get_xform(sel)


        pos = cmds.xform(sel,q=True, translation=True, worldSpace=True)
        rot = cmds.xform(sel, q=True, rotation=True, worldSpace=True)
        scale = cmds.xform(sel, q=True, scale=True, worldSpace=True)

        cmds.xform(ctrl,
                   worldSpace=True,
                   translation=xform_data[0],
                   rotation=xform_data[1],
                   scale=xform_data[2])

        prefix = sel.rpartition('_jnt')[0]
        ctrl = cmds.rename(ctrl,'%s_Ctrl' %(prefix))

        ctrl = group(ctrl)[0]
        ctrls.append(ctrl)
    cmds.select(ctrls, r=True)

    return ctrls

create_control()

def get_xform(obj):
    """
    :param obj: Return the transformation data for the object passed as argument
    :return: [position, rotation, scale]
    """
    pos = cmds.xform(obj, q=True, translation=True, worldSpace=True)
    rot = cmds.xform(obj, q=True, rotation=True, worldSpace=True)
    scale = cmds.xform(obj, q=True, scale=True, worldSpace=True)

    return ([pos,rot,scale])

get_xform()

def group(obj):
    """

    :param obj:
    :return: [obj, grp]
    """
    xform_data = get_xform(obj)
    parent = cmds.listRelatives(obj, parent=True, fullPath=True)

    cmds.select(cl = True)


    grp = cmds.group(world = True, empty=True)
    grp = cmds.rename(grp, '%s_Grp' % (obj))
    cmds.xform(grp,
               worldSpace=True,
               translation=xform_data[0],
               rotation=xform_data[1],
               scale=xform_data[2])
    if parent:
        grp = cmds.parent(grp, parent)[0]
    obj = cmds.select(obj, r=True)[0]
    cmds.selet(obj,r=True)
    return [obj,grp]

#group('nurbsCircle3')

#colorObj = cmds.ls(sl=True)

#colorObj = cmds.nurbsCircleShape2.overrideColor, 5