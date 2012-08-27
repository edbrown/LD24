import pyglet

class AnimationBuilder:

  @staticmethod
  def build(grid, row, start, finish, duration=0.1, loop=True):
    if finish < start:
      temp = start
      start = finish
      finish  = temp

    frames = []
    while start != finish:
      frames.append(grid[row, start]);
      start += 1

    return pyglet.image.Animation.from_image_sequence(frames, duration, loop)

