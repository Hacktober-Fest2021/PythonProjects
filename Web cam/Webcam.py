import pygame, pygame.camera
from pygame.camera import Camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

class CameraDisplay(object):
	def __init__(self, size=(640, 480)):
		self.size = size
		# create a display surface. standard pygame stuff
		self.display = pygame.display.set_mode(self.size, 0)
		self.framerate = 30
		# this is the same as what we saw before
		self.clist = pygame.camera.list_cameras()
		if not self.clist:
			raise ValueError("Sorry, no cameras detected.")
		self.cam = pygame.camera.Camera(self.clist[0], self.size)
		self.cam.start()
		# create a surface to capture to.  for performance purposes
		# bit depth is the same as that of the display surface.
		self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
		self.main()
			
	def updateInput(self):
		""" Checks the event queue and responds to relevant events. """
		events = pygame.event.get((pygame.QUIT, pygame.KEYDOWN))
		for event in events:
			if event.type == pygame.QUIT:
				self.going = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.going = False
				if event.key == pygame.K_q:
					self.going = False
	
	def updateLogic(self, time):
		""" Does any computations or import state changes necessary for the next render """
		pass
	
	def updateDisplay(self):
		""" Figures out how to render the screen """
		# if you don't want to tie the framerate to the camera, you can check 
		# if the camera has an image ready.  note that while this works
		# on most cameras, some will never return true.
		
		# Can have this in a seperate thread that updates the main thread with the
		# most recent picture (then the main thread locks it to draw).
		# This would allow updateLogic to perform vision algorithms easily enough
		
		self.snapshot = self.cam.get_image(self.snapshot)
		# blit it to the display surface.  simple!
		self.display.blit(self.snapshot, (0,0))

	def main(self):
		time = 0
		clock = pygame.time.Clock()
		self.going = True
		while self.going:
			# clock.tick gives us the number of milliseconds
			# since the last time it was called
			time = clock.tick(self.framerate) / 1000.0
			self.updateInput()
			self.updateLogic(time)
			self.updateDisplay()
			
			pygame.display.flip()
			pygame.event.pump()
		
		pygame.quit()

def makeCamViewer():
	from multiprocessing import Process
	CamViewer = Process(target=CameraDisplay, name="CamViewer")
	CamViewer.daemon = True
	CamViewer.start()
	return CamViewer
		
if __name__ == "__main__":
	CamViewer = makeCamViewer()
	CamViewer.join()
