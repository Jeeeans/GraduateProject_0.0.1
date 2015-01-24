import viz
viz.go()

#########################Make Background######################
ground = viz.add('art/sphere_ground3.ive')
ground.collidePlane(0,1,0,0)
env = viz.add(viz.ENVIRONMENT_MAP,'sky.jpg')

dome = viz.add('skydome.dlc')
dome.texture(env)


#######################Make Avatar#####################
male = viz.add('vcc_male.cfg')
male.setPosition([1,0,0])
male.setEuler(-90,0,0)
male.collideMesh()
#male.enable(viz.PHYSICS)
male.enable(viz.COLLIDE_NOTIFY)

head_bone = male.getBone('Bip01 Head')
head_bone.lock()

def onMouseMove(e):
	#print head_bone.getEuler()
	[x,y,z] = head_bone.getEuler()
	ey = y
	ez = z
	if y +(e.dx*0.5) > -60 and y +(e.dx*0.5) < 60 :
		ey = y +(e.dx*0.2)
	if z - (e.dy*0.5) >-30 and z - (e.dy*0.5) < 20 :
		ez = z - (e.dy*0.2)
	head_bone.setEuler(x, ey, ez)
viz.callback(viz.MOUSE_MOVE_EVENT, onMouseMove)

#def move(location):
#	[x,y,z] = male.getPosition()
#	[xr,yr,zr] = male.getEuler()
#	print [xr,yr,zr]
#	if location == 'forward':
#		male.setPosition(x-0.01,y,z)
#		male.state(2)
#	elif location == 'back':
#		male.setPosition(x+0.01,y,z)
#	elif location == 'left':
#		male.setPosition(x,y,z+0.01)
#		male.setEuler(xr-0.01,0,0, viz.REL_LOCAL)
#	elif location == 'right': 
#		male.setPosition(x,y,z-0.01)
#		male.setEuler(xr+0.01,0,0, viz.REL_LOCAL)

#vizact.whilekeydown('w', move, 'forward')
#vizact.whilekeydown('s', move, 'back')
#vizact.whilekeydown('a', move, 'left')
#vizact.whilekeydown('d', move, 'right')

########### MOVEMENT FOR TEST ############
def forward(location):
	[x,y,z] = male.getPosition()
	if location == 'w':
		male.setPosition(x-0.04,y,z)
		male.state(2)
	elif location == 's':
		male.setPosition(x+0.04,y,z)
		male.state(2)
	elif location == 'a':
		male.setPosition(x,y,z-0.04)
	else: 
		male.setPosition(x,y,z+0.04)

def move(location):
	vizact.ontimer2(.01,2,forward, location)

vizact.whilekeydown('w', forward, 'w')
vizact.whilekeydown('s', forward, 's')
vizact.whilekeydown('a', forward, 'a')
vizact.whilekeydown('d', forward, 'd')

############################################



foothold = viz.add('art/wall.ive')
foothold.setEuler(0,90,0)
foothold.setScale(0.5,0.5,1)
foothold.collideMesh()
#foothold.enable(viz.PHYSICS)



#vizact.onkeyup('w', male.stopAnimation, 2, 0)
#view_link = viz.link(head_bone, viz.MainView)
#viz.eyeheight(0)


#############################TEXTURE############################
import texture

################################################################




#############################GRAPH##############################
import graph
rotate_number = 0
coord_number = 0
obj_number = 0

################################################################


#############################TIMER##############################
import Timer
################################################################


############################MODELING############################

import modeling

################################################################

def onCollideBegin(e):
	###########graph footholds variable#############
	global rotate_number
	global coord_number
	global obj_number
	
	###################Texture######################
	if e.obj2 == texture.texture_foothold_1:
		texture.change_texture()
	elif e.obj2 == texture.texture_foothold_2:
		texture.wrap_repeat()
	elif e.obj2 == texture.texture_foothold_3:
		texture.show_move()
	elif e.obj2 == texture.texture_foothold_4:
		texture.show_blind()
		
	######################GRAPH#####################	
	elif e.obj2 == graph.foothold_object_parent:
		obj_number = 0
	elif e.obj2 == graph.foothold_object_child:
		obj_number = 1
	elif e.obj2 == graph.foothold_rotate_abs: 
		rotate_number = 0
	elif e.obj2 == graph.foothold_rotate_rel: 
		rotate_number = 1
	elif e.obj2 == graph.foothold_coord_parent: 
		coord_number = 0
	elif e.obj2 == graph.foothold_coord_local: 
		cood_number = 1
	elif e.obj2 == graph.foothold_rotate_action: 
		graph.rotate_action(obj_number, rotate_number, coord_number)
	elif e.obj2 == graph.foothold_link_action:
		graph.link_action()
	elif e.obj2 == graph.foothold_change_link:
		graph.change_link_position()	
		
		
		
	##################Timer##########################
	elif e.obj2 == Timer.timer_spin_slow:
		Timer.spin_slow()
	elif e.obj2 == Timer.timer_spin_fast:
		Timer.spin_fast()
		
	##################MODELING#####################		
	elif e.obj2 == modeling.foothold_change_posture:
		modeling.change_posture()
	elif e.obj2 == modeling.foothold_move_posture:
		vizact.ontimer(.01, modeling.move_posture)
	elif e.obj2 == modeling.foothold_change_state:
		modeling.change_state()
	elif e.obj2 == modeling.foothold_blend_state:
		modeling.blend_state()
	elif e.obj2 == modeling.foothold_reset_state:
		modeling.reset_state()
		
viz.callback(viz.COLLIDE_BEGIN_EVENT, onCollideBegin)

viz.phys.enable()