from tkinter import *
#http://www.portugal-a-programar.pt/forums/topic/17566-python-simpleclock-rel%C3%B3gio-que-usa-o-canvas-do-tkinter/
class Relogio(object):
    def __init__(self, conteiner):
        self.conteiner = conteiner
        self.w = 200
        self.h = 200
        self.relogio = Canvas(self.conteiner, width = self.w, height = self.h)
        self.relogio.pack()
        self.relogio.create_oval(4, 4, self.relogio['height'], self.relogio['width'])

        centrox = (self.w/2)+4
        centroy = (self.h/2)+4
        n = 12
        self.relogio.create_text(centrox, n, text = "12" )
        
        self.relogio.create_text(self.w-(n*2+30), ((centroy//2)//2), text = "1")
        self.relogio.create_text(self.w-(n+15), (centroy//2), text = "2")

        self.relogio.create_text(self.w-n, centroy, text = "3" )
        

        self.relogio.create_text(centrox, self.h-n, text = "6" )
        


        self.relogio.create_text(n, centroy, text = '9')
        
        self.relogio.create_text(n+(n+15), (centroy//2), text = '10')
        self.relogio.create_text((n*3+30), ((centroy//2)//2), text = '11')
        
        
if __name__ == '__main__':
    Relogio(Tk())
        
        
