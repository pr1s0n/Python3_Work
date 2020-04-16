from collections import namedtuple
Result = namedtuple('Result','Count average')
li = [40.9,38.5,44.3,42.2,45.2,41.7,44.5,38.0,40.6,44.5]
def average():
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield
		if term is None:
			break
		total += term
		count += 1
		average = total/count
	return Result(count,average)

def grouper(result,key):
	while True:
		result[key] = yield from average()

def main():
	results = {}
	group  = grouper(results,"kg")
	next(group)
	for value in li:
		group.send(value)
	group.send(None)
if __name__ == "__main__":
	main()