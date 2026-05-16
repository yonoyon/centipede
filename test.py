from moves.movetypes import AS

list = [1,2,3,4]

move = AS()
move.permute(3, "-", list)

print(list)

