from map import Map

h, w = map(int, input().split())
map = Map((h, w))
print(map.render())