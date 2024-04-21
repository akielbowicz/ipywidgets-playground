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
        self.model=init()
        self._update = update
        self._view = view
        self.view = w.Box([view(self,self.model)])
    
    def _ipython_display_(self):
        display(self.view)

    def update(self,msg):
        self._update(msg,self.model)


def onClick(app, msg):
    def update_(w):
        app.update(msg)
    
    def setup(widget):
        widget.on_click(update_)
    return setup

def onInput(app, msgC, continuous_update=True):
    #https://package.elm-lang.org/packages/elm/html/latest/Html-Events#onInput

    def update_(w):
        app.update(msgC(w.new))
    
    def setup(widget):
        widget.observe(update_,"value")
        widget.continuous_update = continuous_update
    return setup

def linkInput(model, model_attr, view_attr="value"):
    #https://package.elm-lang.org/packages/elm/html/latest/Html-Events#onInput
    def setup(widget):
        w.link((widget, view_attr),(model, model_attr))
    return setup

def div(attrs, content):
    return w.VBox(content)

def text(model, attributes="value", transform=str):
    t = w.Text(disabled=True)
    def set(change):
        t.value = transform(change)
    model.observe(set,attributes)
    return t

def button(setup, text):
    b=w.Button(description=text)
    setup(b)
    return b

def input(setup, placeholder):
    i = w.Text(placeholder=placeholder)
    setup(i)
    return i

def password(setup, placeholder):
    i = w.Password(placeholder=placeholder)
    setup(i)
    return i