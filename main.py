from enum import Enum
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

WINDOW_WIDTH     = 720 
WINDOW_HEIGHT    = 1080

# user available action flags
ALLOWS_FLIGHT    = 0x1
ALLOWS_JUMPING   = 0x2
ALLOWS_MOVEMENT  = 0x3
ALLOWS_CROUCHING = 0x4
ALLOWS_SPRINTING = 0x5
# user collision state
COLLISION_TOP    = 0x1
COLLISION_BOTTOM = 0x2
COLLISION_LEFT   = 0x3
COLLISION_RIGHT  = 0x4

WALKING_SPEED = 5
JUMP_SPEED    = 15
GRAVITY       = -10
MAX_JUMP_TIME = 0.5

class KeyboardEventHandler(object):
  pass

STATE = { ALLOWS_FLIGHT: False, ALLOWS_JUMPING: False, ALLOWS_MOVEMENT: False, ALLOWS_CROUCHING: False, ALLOWS_SPRINTING: False}
COLLISION_STATE = { COLLISION_TOP: False, COLLISION_BOTTOM: False, COLLISION_LEFT: False, COLLISION_RIGHT: False }

class Command:
  def __init__(self, name, action, state):
    self.name = name
    self.action = action
    self.state = state

class JumpCommand(Command):
  def __init__(self, name, action, state):
    super().__init__(name, action, state)

  def execute(self, player):
    if player.jump_time == 0:
      player.velocity_y = JUMP_SPEED
      player.jump_time = MAX_JUMP_TIME


def handle_input(command):
  if isinstance(command, Command):
    if isinstance(command, JumpCommand):
      command.execute()
    

def get_cube_vertices(x, y, z, n):
  # Return the vertices of the cube at position x, y, z with size 2*n.
  return [
      x-n,y+n,z-n, x-n,y+n,z+n, x+n,y+n,z+n, x+n,y+n,z-n,  # top
      x-n,y-n,z-n, x+n,y-n,z-n, x+n,y-n,z+n, x-n,y-n,z+n,  # bottom
      x-n,y-n,z-n, x-n,y-n,z+n, x-n,y+n,z+n, x-n,y+n,z-n,  # left
      x+n,y-n,z+n, x+n,y-n,z-n, x+n,y+n,z-n, x+n,y+n,z+n,  # right
      x-n,y-n,z+n, x+n,y-n,z+n, x+n,y+n,z+n, x-n,y+n,z+n,  # front
      x+n,y-n,z-n, x-n,y-n,z-n, x-n,y+n,z-n, x+n,y+n,z-n,  # back
  ]


def toggle_state(currentState, flag):
  if flag in currentState:
    currentState[flag] = not currentState[flag]
  else:
    currentState[flag] = True
  return currentState[flag]


class Model(object):

  def __init__(self):
    pass


class Window(pyglet.window.Window):
  def __init__(self, *args, **kwargs) -> None:
    super(Window, self).__init__(*args, **kwargs)

    self.mouse_capture_enabled = False # Whether the mouse is captured by the window

  
  def collide(self, positionX: int, positionY: int, positionZ: int, playerHeight: float):
    # Checks to see if the player at the given `position` and `height` is colliding with any blocks in the world.
    pass



class KeyboardEventHandler:
  """
  Encapsulates the logic for handling keyboard events.
  """
  def __init__(self, window):
    pass


def main():
  window = Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, caption="DeCraft", resizable=True)
  KeyboardEventHandler(window)

  @window.event
  def on_key_press(symbol, modifiers):
    print("Key pressed:", symbol)

  @window.event
  def on_mouse_motion(x, y, dx, dy):
    # log debug info
    print(f"MOUSE_MOTION_EVENT -> X({x}) Y({y}) DX({dx}) DY({dy})")

  pyglet.app.run()


if __name__ == "__main__":
  main()
  exit(0)