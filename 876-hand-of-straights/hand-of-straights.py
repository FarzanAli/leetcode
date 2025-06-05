class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        heapq.heapify(hand)
        current = set()
        prev = hand[0] - 1
        
        while hand:
            card = heapq.heappop(hand)
            temp = []
            while card in current and hand:
                temp.append(card)
                card = heapq.heappop(hand)
            if abs(card - prev) != 1:
                return False
            current.add(card)
            prev = card
            while temp: heapq.heappush(hand, temp.pop())
            if len(current) == groupSize and hand:
                prev = hand[0] - 1
                current = set()

        return True