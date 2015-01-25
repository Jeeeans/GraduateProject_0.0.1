import viz
import vizact

ball1 = viz.add('soccerball.ive')
ball1.setPosition(-17,0,7)
ball1_col = ball1.collideSphere()
ball1_col.setBounce(1.5)

ball2 = viz.add('soccerball.ive')
ball2.setPosition(-20,-3,7.1)
ball2_col = ball2.collideSphere()
#ball2_col.set
ball2.enable(viz.COLLIDE_NOTIFY)

ball_foothold = viz.add('art/wall.ive')
ball_foothold.setEuler(0,90,0)
ball_foothold.setScale(0.5,0.5,1)
ball_foothold.setPosition(-18.5,0,4)
ball_foothold.collideMesh()

def jumping():
	ball1.setVelocity([0,5,0], viz.ABS_GLOBAL)
	ball2.setVelocity([0,5,0], viz.ABS_GLOBAL)

ball_foothold2 = viz.add('art/wall.ive')
ball_foothold2.setEuler(0,90,0)
ball_foothold2.setScale(0.5,0.5,1)
ball_foothold2.setPosition(-19.5,0,4)
ball_foothold2.collideMesh()

def shoot_ball():
	ball1.setVelocity([-3,0,0],viz.ABS_GLOBAL)

def reset():
	ball1.setPosition(-17,0,7)
	ball2.setPosition(-20,-3,7.1)
vizact.onkeydown(' ', reset)