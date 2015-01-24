import viz
import vizmat
import vizact

model = viz.add('art/window.ive')
window = model.getChild('glass')
wall = viz.addTexture('art/stone wall.jpg')
clouds = viz.addTexture('art/tileclouds.jpg')
moon = viz.addTexture('art/full moon.jpg')
matrix = vizmat.Transform()
blend = 0.65
model.setPosition(-3,0,5)


###############Changing Texture##############
texture_foothold_1 = viz.add('art/wall.ive')
texture_foothold_1.setEuler(0,90,0)
texture_foothold_1.setScale(0.5,0.5,1)
texture_foothold_1.setPosition(-1.5,0,4)
texture_foothold_1.collideMesh()

def change_texture():
	window.texture(clouds, '', 1)
	window.texture(moon, '', 0)
	window.texblend(0.65, '', 1)

############Texture Copy################
texture_foothold_2 = viz.add('art/wall.ive')
texture_foothold_2.setEuler(0,90,0)
texture_foothold_2.setScale(0.5,0.5,1)
texture_foothold_2.setPosition(-2.5,0,4)
texture_foothold_2.collideMesh()

def wrap_repeat():
	matrix.setScale(2, 2)
	window.texmat(matrix, '', 0)
	moon.wrap(viz.WRAP_S, viz.REPEAT)
	moon.wrap(viz.WRAP_T, viz.REPEAT)
	clouds.wrap(viz.WRAP_S, viz.REPEAT)
	clouds.wrap(viz.WRAP_T, viz.REPEAT)

##########moving clouds############
texture_foothold_3 = viz.add('art/wall.ive')
texture_foothold_3.setEuler(0,90,0)
texture_foothold_3.setScale(0.5,0.5,1)
texture_foothold_3.setPosition(-3.5,0,4)
texture_foothold_3.collideMesh()

def show_move():
	def move_clouds():
		matrix.postTrans(0.001, 0.001, 0)
		window.texmat(matrix,'',1)
	vizact.ontimer(.005, move_clouds)

##########Blinding Moon##############
texture_foothold_4 = viz.add('art/wall.ive')
texture_foothold_4.setEuler(0,90,0)
texture_foothold_4.setScale(0.5,0.5,1)
texture_foothold_4.setPosition(-4.5,0,4)
texture_foothold_4.collideMesh()

def show_blind():
	def blind_moon():
		global blend
		blend = blend - 0.025
		window.texblend(blend, '', 1)
	vizact.ontimer2(0.1, 26, blind_moon)
	
	

	