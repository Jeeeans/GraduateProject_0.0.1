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
male.setEuler([0,0,0],viz.REL_LOCAL)
male.collideMesh()
#male.enable(viz.PHYSICS)
male.enable(viz.COLLIDE_NOTIFY)

head_bone = male.getBone('Bip01 Head')
head_bone.lock()

########Avatar Move##########
def onMouseMove(e):
	[x,y,z] = head_bone.getEuler()
	ey = y
	ez = z
	if y +(e.dx*0.5) > -60 and y +(e.dx*0.5) < 60 :
		ey = y +(e.dx*0.2)
	if z - (e.dy*0.5) >-30 and z - (e.dy*0.5) < 20 :
		ez = z - (e.dy*0.2)
	head_bone.setEuler(x, ey, ez)
viz.callback(viz.MOUSE_MOVE_EVENT, onMouseMove)

########### MOVEMENT FOR TEST ############
def move(location):
	[x,y,z] = male.getPosition()
	[xr,yr,zr] = male.getEuler()
	if location == 'forward':
		male.setPosition([0, 0, 0.05], viz.ABS_LOCAL)
		male.state(2)
	elif location == 'back':
		male.setPosition([0, 0, -0.05], viz.ABS_LOCAL)
	elif location == 'left_turn':
		male.setEuler([-2, 0, 0], viz.REL_GLOBAL)
	elif location == 'right_turn': 
		male.setEuler([2, 0, 0], viz.REL_GLOBAL)
	elif location == 'left':
		male.setPosition([-0.05,0,0],viz.ABS_LOCAL)
	elif location == 'right':
		male.setPosition([0.05,0,0], viz.ABS_LOCAL)

def stop():
	male.clearActions()

vizact.whilekeydown('w', move, 'forward')
vizact.whilekeydown('s', move, 'back')
vizact.whilekeydown('a', move, 'left_turn')
vizact.whilekeydown('d', move, 'right_turn')
vizact.whilekeydown('q', move, 'left')
vizact.whilekeydown('e', move, 'right')
vizact.onkeyup('w', stop)



############################################




view_link = viz.link(head_bone, viz.MainView)
viz.eyeheight(0)


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

#############################LIGHT##############################
import Light
################################################################

#############################PHYSICS############################
import Physics
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
	
	##################Light##########################
	elif e.obj2 == Light.light_off_foothold:
		Light.light_off()
		ground.visible(viz.OFF)
		dome.visible(viz.OFF)
	elif e.obj2 == Light.light_on_foothold:
		Light.light_on()
		ground.visible(viz.ON)
		dome.visible(viz.ON)
		
	#################Physics########################
	elif e.obj2 == Physics.ball_foothold:
		Physics.jumping();
	elif e.obj2 == Physics.ball_foothold2:
		Physics.shoot_ball();
	
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