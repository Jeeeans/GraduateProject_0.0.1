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

def move(location):
	[x,y,z] = male.getPosition()
	[xr,yr,zr] = male.getEuler()
	print [xr,yr,zr]
	if location == 'forward':
		male.setPosition(x-0.01,y,z)
		male.state(2)
	elif location == 'back':
		male.setPosition(x+0.01,y,z)
	elif location == 'left':
		male.setPosition(x,y,z+0.01)
		male.setEuler(xr-0.01,0,0, viz.REL_LOCAL)
	elif location == 'right': 
		male.setPosition(x,y,z-0.01)
		male.setEuler(xr+0.01,0,0, viz.REL_LOCAL)

vizact.whilekeydown('w', move, 'forward')
vizact.whilekeydown('s', move, 'back')
vizact.whilekeydown('a', move, 'left')
vizact.whilekeydown('d', move, 'right')





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

################################################################


#############################TIMER##############################
import Timer
################################################################

#############################LIGHT##############################
import Light
################################################################

def onCollideBegin(e):
	###################Texture######################
	if e.obj2 == texture.texture_foothold_1:
		texture.change_texture()
	elif e.obj2 == texture.texture_foothold_2:
		texture.wrap_repeat()
	elif e.obj2 == texture.texture_foothold_3:
		texture.show_move()
	elif e.obj2 == texture.texture_foothold_4:
		texture.show_blind()
		
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
		
viz.callback(viz.COLLIDE_BEGIN_EVENT, onCollideBegin)

viz.phys.enable()