# Solution
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            destroyed = False

            while not destroyed and ans and ans[-1] > 0 and asteroid < 0:
                if ans[-1] < -asteroid:
                    ans.pop()
                elif ans[-1] == -asteroid:
                    ans.pop()
                    destroyed = True
                else:
                    destroyed = True
            if not destroyed:
                ans.append(asteroid)
        return ans



# Reference
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            alive=True
            while stack and asteroid<0 and stack[-1]>0:
                if stack[-1]<-asteroid:
                    stack.pop()
                    
                elif stack[-1]==-asteroid:
                    stack.pop()
                    alive=False
                    break
                else:
                    alive=False
                    break
            if alive:
                stack.append(asteroid)
        return stack

        
