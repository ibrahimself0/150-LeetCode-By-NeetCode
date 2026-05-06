class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> float:
        cars = []
        for i in range(len(position)):
            pos = position[i]
            spd = speed[i]
            time = (target - pos) / spd
            cars.append([pos, spd, time])

        cars.sort(key=lambda x: x[0], reverse=True)
        print(cars)

        lastCarInFleet = cars[0]
        print(lastCarInFleet)

        count = 1

        for i in range(1, len(position)):
            print(lastCarInFleet[2])
            if cars[i][2] > lastCarInFleet[2]:
                count += 1
                lastCarInFleet = cars[i]

        return count