import viz
import vizact

ball1 = viz.add('soccerball.ive')
ball1.setPosition(-17,0,5)
ball1.collideSphere()

ball2 = viz.add('soccerball.ive')
ball2.setPosition(-20,0,5.1)
ball2.collideSphere()
ball2.enable(viz.COLLIDE_NOTIFY)

ball_foothold = viz.add('art/wall.ive')
ball_foothold.setEuler(0,90,0)
ball_foothold.setScale(0.5,0.5,1)
ball_foothold.setPosition(-18.5,0,4)
ball_foothold.collideMesh()

def shoot_ball():
	ball1.setVelocity([-3,0,0],viz.ABS_GLOBAL)
	
vizact.onkeydown(' ', shoot_ball)