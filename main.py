from enum import Enum
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse


WINDOW_WIDTH     = 1280 
WINDOW_HEIGHT    = 720

# user available action flags
ALLOWS_FLIGHT    = 0x1
ALLOWS_JUMPING   = 0x2
ALLOWS_MOVEMENT  = 0x3
ALLOWS_CROUCHING = 0x4
ALLOWS_SPRINTING = 0x5
# user collision state
COLLISION_TOP = 0x1
COLLISION_BOTTOM = 0x2
COLLISION_LEFT = 0x3
COLLISION_RIGHT = 0x4

STATE = { ALLOWS_FLIGHT: False, ALLOWS_JUMPING: False, ALLOWS_MOVEMENT: False, ALLOWS_CROUCHING: False, ALLOWS_SPRINTING: False}
COLLISION_STATE = { COLLISION_TOP: False, COLLISION_BOTTOM: False, COLLISION_LEFT: False, COLLISION_RIGHT: False }


def toggle_state(currentState, flag):
  if flag in currentState:
    currentState[flag] = not currentState[flag]
  else:
    currentState[flag] = True
  return currentState[flag]


class Window(pyglet.window.Window):
  def __init__(self, *args, **kwargs) -> None:
    super(Window, self).__init__(*args, **kwargs)

    self.mouse_capture_enabled = False # Whether the mouse is captured by the window
    
  
  def collide(self, positionX: int, positionY: int, positionZ: int, playerHeight: float):
    # Checks to see if the player at the given `position` and `height` is colliding with any blocks in the world.
  



def main():
  window = Window(width=1280, height=720, caption="DeCraft", resizable=True)


if __name__ == "__main__":
  main()
  exit(0)