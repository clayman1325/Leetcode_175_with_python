class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = []
        i = 0
        while i < len(asteroids):
            asteroid = asteroids[i]
            if len(q) > 0 and q[-1] > 0 and asteroid < 0:
                if q[-1] == abs(asteroid):
                    q.pop()
                elif q[-1] < abs(asteroid):
                    q.pop()
                    i -= 1
            else:
                q.append(asteroid)
            i += 1
        return q