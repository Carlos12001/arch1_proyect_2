
if __name__ == "__main__":
  pixelbyletter = 5
  letterbyword = 8
  minwords = 100
  minparraph = 25
  paddingpixelbyletter = 1
  spaceword = 5
  paddingpixelbypagraph = 2


  horizontal_pixels = ( (paddingpixelbyletter + pixelbyletter) * letterbyword * minwords + 
                (spaceword + pixelbyletter) * minwords )
  vertical_pixels = ( pixelbyletter + paddingpixelbypagraph ) * minparraph

  print(f"horizontal_pixels: {horizontal_pixels}")
  print(f"horizontal_pixels/minparraph: {horizontal_pixels / minparraph}")
  print(f"vertical_pixels: {vertical_pixels}")
