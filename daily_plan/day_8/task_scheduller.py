class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def finished(counter):
            values = counter.values()
            return sum(values) == 0
        def update_timer(timmer, letter, n):
            for key in timmer:
                if timmer[key] > 0: timmer[key] -= 1
            if letter != "idle": timmer[letter] = n
            return timmer
        def choose_letter(counter, timmer):
            char = "idle"
            candidates = []
            for key in timmer:
                wait = timmer[key]
                if wait == 0: candidates.append(key)

            if candidates == []: return char

            max_num = 0
            char = "idle"

            for key in candidates:
                quantity = counter[key]
                if quantity > max_num:
                    max_num = quantity
                    char = key

            return char

        result = []
        counter = {}
        timmer = {}
        for letter in tasks:
            if not timmer.get(letter): timmer[letter] = 0

            if counter.get(letter):
                counter[letter] += 1
            else:
                counter[letter] = 1

        count = 0
        while(not finished(counter)):
            choosen = choose_letter(counter, timmer)
            if choosen != "idle": counter[choosen] -= 1
            result.append(choosen)
            update_timer(timmer, choosen, n)
            count += 1

        return count