import pyglet
from pyglet.window import mouse
window = pyglet.window.Window(width = 900, height = 600)

def startscreen():
    welcome = pyglet.text.Label('Welcome to Who\'s That Pokemon!',
            font_name='Times New Roman',
            font_size=36,
            x= window.width // 2,
            y= window.height // 2,
            anchor_x='center',
            anchor_y='center')

    go_on = pyglet.text.Label('Click anywhere to continue',
            font_name='Times New Roman',
            font_size=18,
            x= window.width // 2,
            y= 200,
            anchor_x= 'center')

    @window.event
    def on_draw():
        window.clear()
        welcome.draw()
        go_on.draw()


def difficultyscreen():
    difficulty = pyglet.text.Label('Select Difficulty',
                              font_name='Times New Roman',
                              font_size=36,
                               x=window.width // 2,
                               y=500,
                               anchor_x='center')

    easy = pyglet.text.Label('EASY',
                               font_name='Times New Roman',
                               font_size=26,
                               x=window.width // 2,
                               y=100,
                               anchor_x='center')

    average = pyglet.text.Label('AVERAGE',
                             font_name='Times New Roman',
                             font_size=26,
                             x=window.width // 2,
                             y=200,
                             anchor_x='center')

    difficult = pyglet.text.Label('DIFFICULT',
                             font_name='Times New Roman',
                             font_size=26,
                             x=window.width // 2,
                             y=300,
                             anchor_x='center')

    lunatic = pyglet.text.Label('LUNATIC',
                                  font_name='Times New Roman',
                                  font_size=26,
                                  x=window.width // 2,
                                  y=400,
                                  anchor_x='center')

    @window.event
    def on_draw():
        window.clear()
        difficulty.draw()
        easy.draw()
        average.draw()
        difficult.draw()
        lunatic.draw()

def terminalscreen():
    difficulty = pyglet.text.Label('START',
                                   font_name='Times New Roman',
                                   font_size=36,
                                   x=window.width // 2,
                                   y=500,
                                   anchor_x='center')

    quit = pyglet.text.Label('QUIT',
                             font_name='Times New Roman',
                             font_size=36,
                             x=window.width // 2,
                             y=100,
                             anchor_x='center')

    mechanics = pyglet.text.Label('MECHANICS',
                             font_name='Times New Roman',
                             font_size=36,
                             x=window.width // 2,
                             y=300,
                             anchor_x='center')

    @window.event
    def on_draw():
        window.clear()
        difficulty.draw()
        mechanics.draw()
        quit.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT and 480 < y < 520:
            difficultyscreen()


startscreen()
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        terminalscreen()


pyglet.app.run()