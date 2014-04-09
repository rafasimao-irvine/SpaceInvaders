from input_listener import InputListener

class State(InputListener):
    
    def __init__(self, screen, inputManager): 
        self.screen = screen
        self.inputManager = inputManager
        inputManager.attach(self)
        
    def destroy(self): pass
    
    def update(self): return 0
    def render(self): pass
