import viz
import vizact

lantern = viz.add('art/flashlight.ive')
lantern.setPosition(-15.5,.5,7)
lantern.setEuler(0,180,0)

lantern_light = viz.addLight()

lantern_light.position(0,0,0,1)

lantern_light.color(viz.YELLOW)
lantern_light.spread(45)
lantern_light.spotexponent(0)

viz.link(lantern, lantern_light)
lantern_light.disable()

light_off_foothold = viz.add('art/wall.ive')
light_off_foothold.setEuler(0,90,0)
light_off_foothold.setScale(0.5,0.5,1)
light_off_foothold.setPosition(-14.5,0,4)
light_off_foothold.collideMesh()

def light_off():
	viz.MainView.getHeadLight().disable()
	lantern_light.enable()

light_on_foothold = viz.add('art/wall.ive')
light_on_foothold.setEuler(0,90,0)
light_on_foothold.setScale(0.5,0.5,1)
light_on_foothold.setPosition(-15.5,0,4)
light_on_foothold.collideMesh()

def light_on():
	viz.MainView.getHeadLight().enable()
	viz.MainView
	lantern_light.disable()