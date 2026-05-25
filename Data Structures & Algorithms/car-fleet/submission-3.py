class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(pos, sped) for pos, sped in zip(position, speed)]
        cars = sorted(cars, reverse=True)


        import math 
        # time = floor(desti - pos/ speed)
        stack = []
        count = 0
        for pos, sped in cars: 
            time = math.floor(target - pos) / sped
            if len(stack) == 0:
                stack.append(time)
            else:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)
        return len(set(stack)) + count
