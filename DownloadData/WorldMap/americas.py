import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North American', ['ca', 'mx', 'us'])
wm.add('Central', ['bx', 'cr', 'gt', 'hn', 'ni'])
wm.add('South', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy'])

wm.render_to_file('americas.svg')