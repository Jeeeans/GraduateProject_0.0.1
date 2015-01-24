import viz
import vizact

barrel = viz.add('art/barrel.ive')
barrel.setPosition(-10,0,6)

def spin():
	[x,y,z] = barrel.getEuler();
	if x == 360 : x = 0
	barrel.setEuler(x+2,0,0)
	
timer_spin_slow = viz.add('art/wall.ive')
timer_spin_slow.setEuler(0,90,0)
timer_spin_slow.setScale(0.5,0.5,1)
timer_spin_slow.setPosition(-9.5,0,4)
timer_spin_slow.collideMesh()

def spin_slow():
	vizact.ontimer2(0.1, 360, spin)
	
timer_spin_fast = viz.add('art/wall.ive')
timer_spin_fast.setEuler(0,90,0)
timer_spin_fast.setScale(0.5,0.5,1)
timer_spin_fast.setPosition(-10.5,0,4)
timer_spin_fast.collideMesh()

def spin_fast():
	vizact.ontimer2(0.01,360, spin)
	

