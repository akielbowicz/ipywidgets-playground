import ipywidgets as w

app = None

def set_app(a):
    global app
    app = a

def get_app():
    global app
    return app

class App:

    def __init__(self, init, update, view):
        set_app(self)
        self.model=init()
        self._update = update
        self._view = view
        self.view = w.Box()
        self.refresh_view()

    def _ipython_display_(self):
        display(self.view)

    def refresh_view(self):
        self.view.children=(self._view(self.model),)
    
    def call_update(self,msg):
        self.model = self._update(msg,self.model)
        self.refresh_view()

def onClick(msg):

    def update_(w):
        get_app().call_update(msg)
    
    def setup(widget):
        widget.on_click(update_)
    return setup

def onInput(msgC, continuous_update=True):
    #https://package.elm-lang.org/packages/elm/html/latest/Html-Events#onInput

    def update_(w):
        get_app().call_update(msgC(w.new))
    
    def setup(widget):
        widget.observe(update_,"value")
        widget.continuous_update = continuous_update
    return setup


def div(attrs, content):
    return w.VBox(content)

def text(txt):
    return w.Text(txt, disabled=True)

def button(setup, text):
    b=w.Button(description=text)
    setup(b)
    return b

def input(setup, text, placeholder):
    i = w.Text(value=text, placeholder=placeholder)
    setup(i)
    return i