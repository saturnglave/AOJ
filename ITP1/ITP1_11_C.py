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

    # 右の面を求める
    def right_side(self, up, front):
        if ((up == self.d[0] and front == self.d[1]) or (up == self.d[1] and front == self.d[5]) or 
        (up == self.d[5] and front == self.d[4]) or (up == self.d[4] and front == self.d[0])):
            return self.d[2]

        elif ((up == self.d[3] and front == self.d[1]) or (up == self.d[4] and front == self.d[3]) or 
        (up == self.d[2] and front == self.d[4]) or (up == self.d[1] and front == self.d[2])):
            return self.d[0]

        elif ((up == self.d[3] and front == self.d[5]) or (up == self.d[5] and front == self.d[2]) or 
        (up == self.d[2] and front == self.d[0]) or (up == self.d[0] and front == self.d[3])):
            return self.d[1]

        elif ((up == self.d[4] and front == self.d[5]) or (up == self.d[5] and front == self.d[1]) or 
        (up == self.d[1] and front == self.d[0]) or (up == self.d[0] and front == self.d[4])):   
            return self.d[3]

        elif ((up == self.d[2] and front == self.d[5]) or (up == self.d[5] and front == self.d[3]) or 
        (up == self.d[3] and front == self.d[0]) or (up == self.d[0] and front == self.d[2])):   
            return self.d[4]
        
        else:
            return self.d[5]

    #サイコロが同一か判断する
    def is_same_dice(self, dice, direction):
        ret = False

        for i in range(len(direction)):
            self.rotate(direction[i])
            flag = True
            for j in range(6):
                if self.d[j] != dice.d[j]:
                    print(self.d[j], dice.d[j])
                    flag = False
                    break
            if flag == True:
                return True

        return ret



def main():
    num1 = [int(i) for i in input().split()]
    num2 = [int(i) for i in input().split()]
    #q = int(input())

    direction = 'NNNNWNNNWNNNENNNENNNWNNN'
    #print(num)
    #print(direction)
    dice1 = Dice(num1)
    dice2 = Dice(num2)

    if dice1.is_same_dice(dice2, direction):
        print("Yes")
    else:
        print("No")

'''
    #ITP1_11_Bの部分なので略
    for j in range(q):
        up, front = map(int, input().split())
        ans = dice.right_side(up, front)
        print(ans)
'''
        
'''
    #ITP1_11_Aの部分なので略
    for i in direction:
        dice.rotate(i)
    print(dice.d[0])
'''
if __name__ == "__main__":
    main()