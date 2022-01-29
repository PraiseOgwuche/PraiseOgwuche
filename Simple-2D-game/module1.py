import pymunk
import pymunk.pygame_util
import pygame

GRAY = (220, 220, 220)

class App:
    #Androis aspect ratio 16:10
    def __init__(self,size=(1200,568),g=(0,500)):
        self.space = pymunk.Space()
        self.gravity = g
        self.size = size
        self.running = True
        self.shapes_list = []

    def add(self,shape):
        if type(shape) is list:
            for s in shape:
                self.space.add(s.body,s.shape)
            self.shapes_list.extend(shape)
        else:
            self.space.add(shape.body,shape.shape)
            self.shapes_list.append(shape)

    def update_func(self):
        pass

    def mainloop(self,*args):

        pygame.init()
        self.space.gravity = self.gravity
        self.screen = pygame.display.set_mode(self.size)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)

        print(f"Window size: {self.size}")
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if args:
                    for f in args:
                        f(event)

            self.screen.fill(GRAY)
            self.space.debug_draw(self.draw_options)
            pygame.display.update()
            self.update_func()
            self.space.step(0.01)

            for s in self.shapes_list:
                s.velocity = s.body.velocity
                #print(s,s.shape.elasticity)
        pygame.quit()






if __name__ == '__main__':
    A = App()
    b0 = A.space.static_body
    p0, p1 = (0, 400), (700, 400)
    segment = pymunk.Segment(b0, p0, p1, 4)
    segment.elasticity = 1

    body = pymunk.Body(mass=1, moment=10)
    body.position = (100, 200)

    circle = pymunk.Circle(body, radius=30)
    circle.elasticity = 0.95
    A.space.add(body, circle, segment)

    A.mainloop()