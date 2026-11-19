class CountSquares:

    def __init__(self):
        self.posCount= defaultdict(int)
        self.pos = []

    def add(self, point: List[int]) -> None:
        self.posCount[tuple(point)] += 1
        self.pos.append(point)

    def count(self, point: List[int]) -> int:
        
        px, py = point
        res = 0
        for x, y in self.pos:
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            res += self.posCount.get((x, py), 0) * self.posCount.get((px, y), 0) 

        return res