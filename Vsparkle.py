def sparkle(color, color1, loop = 10, delay=0.1):
  for i in range(loop):
    rgb.fill(color)
    for q in range(rgb.n / 4):
      rgb[random.randint(0, rgb.n-1)] = color1
    rgb.show()
    time.sleep(delay)
