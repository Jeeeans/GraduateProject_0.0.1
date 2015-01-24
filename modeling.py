import viz
import vizmat
import vizact


male = viz.add('vcc_male.cfg')
male.setEuler(180,0,0)
male.setPosition(-40.5,0,7)
head = male.getBone( 'Bip01 Head' )
r_upperarm = male.getBone( 'Bip01 R UpperArm' )
r_forearm = male.getBone('Bip01 R Forearm')
r_hand = male.getBone('Bip01 R Hand')
l_upperarm = male.getBone('Bip01 L UpperArm')
l_forearm = male.getBone('Bip01 L Forearm')
l_hand = male.getBone('Bip01 L Hand')

head.lock()
r_upperarm.lock()
r_forearm.lock()
r_hand.lock()
l_upperarm.lock()
l_forearm.lock()
l_hand.lock()
r_upperarm.setEuler(0,0,-30,viz.AVATAR_LOCAL)


def change_posture():
	r_upperarm.setEuler(-5.0, -26.0, 21.0, viz.AVATAR_LOCAL)
	r_forearm.setEuler(-35.0, -84.0, 28.0, viz.AVATAR_LOCAL)
	l_upperarm.setEuler(-16.0, -37.0, -14.0, viz.AVATAR_LOCAL)
	l_forearm.setEuler(33.0, 7.0, 47.0, viz.AVATAR_LOCAL)

count = 0
flag = 1

def move_posture():
	global count
	global flag
	if count >= 30:
		flag = 0
	elif count <= -30:
		flag = 1
	if flag == 0:
		count = count - 1
	elif flag == 1:
		count = count + 1
	
	r_hand.setEuler(0,0,count, viz.AVATAR_LOCAL)
	l_hand.setEuler(0,count,0, viz.AVATAR_LOCAL)


foothold_change_posture = viz.add('art/wall.ive')
foothold_change_posture.setEuler(0,90,0)
foothold_change_posture.setScale(0.5,0.5,1)
foothold_change_posture.setPosition(-39.5,0,4)
foothold_change_posture.collideMesh()

foothold_move_posture = viz.add('art/wall.ive')
foothold_move_posture.setEuler(0,90,0)
foothold_move_posture.setScale(0.5,0.5,1)
foothold_move_posture.setPosition(-41.5,0,4)
foothold_move_posture.collideMesh()


female = viz.add('vcc_female.cfg')
female.setEuler(180,0,0)
female.setPosition(-45.5,0,7)
female.state(1)

def change_state():
	female.clearActions()
	female.state(5)
	
def blend_state():
	female.blend(4,1,1)

def reset_state():
	female.reset()
	female.state(1)

foothold_change_state = viz.add('art/wall.ive')
foothold_change_state.setEuler(0,90,0)
foothold_change_state.setScale(0.5,0.5,1)
foothold_change_state.setPosition(-44,0,4)
foothold_change_state.collideMesh()

foothold_blend_state = viz.add('art/wall.ive')
foothold_blend_state.setEuler(0,90,0)
foothold_blend_state.setScale(0.5,0.5,1)
foothold_blend_state.setPosition(-45.5,0,4)
foothold_blend_state.collideMesh()

foothold_reset_state = viz.add('art/wall.ive')
foothold_reset_state.setEuler(0,90,0)
foothold_reset_state.setScale(0.5,0.5,1)
foothold_reset_state.setPosition(-47,0,4)
foothold_reset_state.collideMesh()