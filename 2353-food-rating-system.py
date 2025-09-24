import heapq

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heap = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_heap:
                self.cuisine_heap[c] = []
            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        c = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_heap[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisine_heap[cuisine]:
            rating, food = self.cuisine_heap[cuisine][0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(self.cuisine_heap[cuisine])
