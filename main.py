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
    
    # user available modes {flying_enabled, walking_enabled, standing_enabled}
    self.user_modes = (0, 0, 0)

    self.user_is_flying = False        # Whether the user is flying
    self.user_is_jumping = False       # Whether the user is jumping


def main():
  window = Window(width=1280, height=720, caption="DeCraft", resizable=True)


if __name__ == "__main__":
  main()
  exit(0)