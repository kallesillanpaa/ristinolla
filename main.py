#python -m venv env
#env\scripts\activate
#pip install kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Game(App):
    def __init__(self):
        super().__init__()
        self.buttons=[]

    def build(self):
        layout = GridLayout(cols=3)       
        for i in range(9):
            self.buttons.append(Button(text="", background_normal="",background_color=(0,0,1,1) ))
            #ilman parametreja funktion kutsu:
            #self.buttons[i].bind(on_press=self.set_text)
            #parametrien kanssa funktion kutsu:
            self.buttons[i].bind(on_press=lambda dummy, index=i:self.set_text(index))
            layout.add_widget(self.buttons[i])                       
        return layout
    # "ilman" parametreja:
    #def set_text(self,btn):
    #    print(btn.text)
    def set_text(self, i):
        self.buttons[i].text = "X"
game = Game()
game.run()

