class Datatable:
	def __init__(self, *points: list[tuple[int, int]]) -> None:
		self.points = points
		
	def __len__(self) -> int:
		return len(self.points)
	
	def __getitem__(self, index: int) -> tuple[int, int]:
		return self.points[index]
		
	def __iter__(self) -> None:
		self.n = -1
		return self
	
	def __next__(self) -> tuple[int, int]:
		self.n += 1
		
		if self.n == len(self):
			raise StopIteration
			
		return self[n]
	
	def derivative(self) -> Datatable:
		pts = []
		for index in range(1, len(self)):
			
			pts.append((self[index] - 
