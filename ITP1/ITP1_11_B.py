# coding: utf-8
class Dice:
    # 初期化
    def __init__(self, num):
        self.d = num

    # 転がした時の動作
    def rotate(self, direction):
        if direction == "N":
            self.d[0], self.d[1], self.d[5], self.d[4] = self.d[1], self.d[5], self.d[4], self.d[0]

        elif direction == "S":
            self.d[0], self.d[1], self.d[5], self.d[4] = self.d[4], self.d[0], self.d[1], self.d[5]

        elif direction == "E":
            self.d[0], self.d[2], self.d[5], self.d[3] = self.d[3], self.d[0], self.d[2], self.d[5]
        else:
            self.d[0], self.d[2], self.d[5], self.d[3] = self.d[2], self.d[5], self.d[3], self.d[0]



def main():
    num = [int(i) for i in input().split()]
    q = int(input())
    direction = str(input())
    #print(num)
    #print(direction)
    dice = Dice(num)

    for i in direction:
        dice.rotate(i)
    print(dice.d[0])

if __name__ == "__main__":
    main()