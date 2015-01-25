import viz
import vizmat
import vizact
import math
import time



parent = viz.add('art/tower.ive')
child = parent.add( 'art/turbine.ive')
parent.setPosition(-11.5,0,12)
child.setPosition(  [ 0.0 , 7.75 , 0.0 ] )
#parent.setEuler(180,0,0)
black = viz.addTexture('art/black.jpg')
white = viz.addTexture('art/white.jpg')
pink = viz.addTexture('art/pink.jpg')



select_rotate = ['ABS', 'REL']
select_coord = ['_PARENT', '_LOCAL']
select_obj = [parent, child]


def rotate_action(obj_number, rotate_number, coord_number):
	select_mode = 'viz.'+select_rotate[rotate_number]+select_coord[coord_number]
	select_obj[obj_number].setEuler([90,0,0], eval(select_mode))

foothold_object_parent = viz.add('art/wall.ive')
foothold_object_parent.texture(black, '', 1)
foothold_object_parent.setEuler(0,90,0)
foothold_object_parent.setScale(0.5,0.5,1)
foothold_object_parent.setPosition(-8.5,0,3)
foothold_object_parent.collideMesh()

foothold_object_child = viz.add('art/wall.ive')
foothold_object_child.texture(white, '', 1)
foothold_object_child.setEuler(0,90,0)
foothold_object_child.setScale(0.5,0.5,1)
foothold_object_child.setPosition(-8.5,0,5)
foothold_object_child.collideMesh()

foothold_rotate_abs = viz.add('art/wall.ive')
foothold_rotate_abs.texture(black, '', 1)
foothold_rotate_abs.setEuler(0,90,0)
foothold_rotate_abs.setScale(0.5,0.5,1)
foothold_rotate_abs.setPosition(-10.5,0,3)
foothold_rotate_abs.collideMesh()

foothold_rotate_rel = viz.add('art/wall.ive')
foothold_rotate_rel.texture(white, '', 1)
foothold_rotate_rel.setEuler(0,90,0)
foothold_rotate_rel.setScale(0.5,0.5,1)
foothold_rotate_rel.setPosition(-10.5,0,5)
foothold_rotate_rel.collideMesh()

foothold_coord_parent = viz.add('art/wall.ive')
foothold_coord_parent.texture(black, '', 1)
foothold_coord_parent.setEuler(0,90,0)
foothold_coord_parent.setScale(0.5,0.5,1)
foothold_coord_parent.setPosition(-12.5,0,3)
foothold_coord_parent.collideMesh()

foothold_coord_local = viz.add('art/wall.ive')
foothold_coord_local.texture(white, '', 1)
foothold_coord_local.setEuler(0,90,0)
foothold_coord_local.setScale(0.5,0.5,1)
foothold_coord_local.setPosition(-12.5,0,5)
foothold_coord_local.collideMesh()

foothold_rotate_action = viz.add('art/wall.ive')
foothold_rotate_action.texture(pink, '', 1)
foothold_rotate_action.setEuler(0,90,0)
foothold_rotate_action.setScale(0.5,0.5,1)
foothold_rotate_action.setPosition(-14.5,0,4)
foothold_rotate_action.collideMesh()


avatar = viz.add('vcc_male.cfg')
bees = viz.add('art/bees.ive')
bees.setPosition(-17,1.8,9)

def swarm():
	bori = [5,0,0]
	bees.setEuler(bori, viz.REL_GLOBAL)
vizact.ontimer(.01, swarm)


avatar.state(11)
def run_around():
	newX = -math.cos(time.clock()) * 1.21
	newZ = math.sin(time.clock()) * 1.2
	avatar.setPosition([-17 + newX,0, 9 + newZ], viz.ABS_GLOBAL)
	avatar.setEuler([time.clock()/math.pi*180,0,0], viz.ABS_GLOBAL)
vizact.ontimer(.01, run_around)

def link_action():
	global link_bees
	link_bees = viz.link(avatar, bees)
	link_bees.setMask(viz.LINK_POS)
	link_bees.setOffset([0,1.8,0])
	
def change_link_position():
	link_bees.setPos([None,0.9,9])
	
foothold_link_action = viz.add('art/wall.ive')
foothold_link_action.setEuler(0,90,0)
foothold_link_action.setScale(0.5,0.5,1)
foothold_link_action.setPosition(-16.5,0,4)
foothold_link_action.collideMesh()

foothold_change_link = viz.add('art/wall.ive')
foothold_change_link.setEuler(0,90,0)
foothold_change_link.setScale(0.5,0.5,1)
foothold_change_link.setPosition(-17.5,0,4)
foothold_change_link.collideMesh()