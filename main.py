from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse


class Window(pyglet.window.Window):
  def __init__(self, *args, **kwargs) -> None:
    super(Window, self).__init__(*args, **kwargs)


def main():
  window = Window(width=1280, height=720, caption="DeCraft", resizable=True)

if __name__ == "__main__":
  main()
  exit(0)