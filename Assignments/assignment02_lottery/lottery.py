import random

MSG_PURCHASE = "> 구입 금액을 입력해주세요: "
MSG_DTYPE_ERROR = "> 숫자를 입력해주세요!"
MSG_RANGE_ERROR = "> 1 ~ 45 까지의 숫자를 입력하세요!"
MSG_INPUT_LOT_NUM = "> 지난 주 당첨 번호를 입력해주세요: "


def input_purchase_price():
    purchase_price = input(MSG_PURCHASE)
    while(purchase_price.isdigit() == False) :
        print(MSG_DTYPE_ERROR)
        purchase_price = input(MSG_PURCHASE)

    return purchase_price

def input_lotteryNum():    
    # input 범위 지정.
    lotteryNum = [] 
    for i in range(6):
        temp = input(MSG_INPUT_LOT_NUM)
        while(temp.isdigit() == False):
            print(MSG_RANGE_ERROR)
            temp = input(MSG_INPUT_LOT_NUM)
        while (int(temp) not in range(1, 46)):
            print(MSG_RANGE_ERROR)
            temp = input(MSG_INPUT_LOT_NUM)
        lotteryNum.append(temp)

    lotteryNum.sort()
    
    return lotteryNum
    
def compute_purchase_amount(purchase_price):
    purchase_amount = int(purchase_price) / 1000
    return int(purchase_amount)

def print_purchase_amount(purchase_amount):
    print("{}장의 로또를 구입하셨습니다.".format(purchase_amount))

def print_lottery(lotteryArr):
    for i in range(len(lotteryArr)):
        print(lotteryArr[i])


def run_lottery(purchase_amount):
    lotteryArr = []
    for i in range(purchase_amount):
        lotteryArr.append(random.sample(range(1, 46), 6))
        lotteryArr[i].sort()
            
    return lotteryArr
    # print(lotteryArr)

def run():
    purchase_price = input_purchase_price()
    purchase_amount = compute_purchase_amount(purchase_price)

    print_purchase_amount(purchase_amount)

    lotteryArr = run_lottery(purchase_amount)

    print_lottery(lotteryArr)

    lotteryNum = input_lotteryNum()

    
    for i in range(purchase_amount):
        count = 0
        for j in range(6):
            print(lotteryNum[i][j])
            if (lotteryArr[i][j] in lotteryNum):
                count += 1
        print(i + 1, "번째", count, "개 일치")



run()
