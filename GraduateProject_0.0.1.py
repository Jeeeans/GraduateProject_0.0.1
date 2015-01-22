import viz
viz.go()


ground = viz.add('art/sphere_ground3.ive')
env = viz.add(viz.ENVIRONMENT_MAP,'sky.jpg')

dome = viz.add('skydome.dlc')
dome.texture(env)

male = viz.add('vcc_male.cfg')
male.setPosition([1,0,0])
male.setEuler(-90,0,0)

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

def forward(location):
	[x,y,z] = male.getPosition()
	if location == 'w':
		male.setPosition(x-0.01,y,z)
		male.state(2)
	elif location == 's':
		male.setPosition(x+0.01,y,z)
		male.state(2)
	elif location == 'a':
		male.setPosition(x,y,z-0.01)
	else:
		male.setPosition(x,y,z+0.01)

def move(location):
	vizact.ontimer2(.01,2,forward, location)

vizact.onkeydown('w', move, 'w')
vizact.onkeydown('s', move, 's')
vizact.onkeydown('a', move, 'a')
vizact.onkeydown('d', move, 'd')


#vizact.onkeyup('w', male.stopAnimation, 2, 0)
#view_link = viz.link(head_bone, viz.MainView)
#viz.eyeheight(0)