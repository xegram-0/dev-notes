class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiantQ = deque()
        direQ = deque()

        for i, senator in enumerate(senate):
            if senator == 'R':
                radiantQ.append(i)
            else:
                direQ.append(i)
        
        while radiantQ and direQ:
            radiantP = radiantQ.popleft()
            direP = direQ.popleft()

            if radiantP < direP:
                radiantQ.append(radiantP + len(senate))
            else:
                direQ.append(direP + len(senate))
        return "Radiant" if radiantQ else "Dire"
