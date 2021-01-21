# task = open("laoyou.txt")
# for chore in task:
# 	print(chore)
# task.close()

with open("laoyou.txt") as task:
	for chore in task:
		print(chore, end='')
task.close()