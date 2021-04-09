import random

MSG_PURCHASE = "> 구입 금액을 입력해주세요: "
MSG_DTYPE_ERROR = "> 숫자를 입력해주세요!"
MSG_RANGE_ERROR = "> 1 ~ 45 까지의 숫자를 입력하세요!"
MSG_INPUT_LOT_NUM = "> 지난 주 당첨 번호를 입력해주세요: "
MSG_RESULT = "> 로또 당첨 결과"


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
    # 기존에 뽑은 번호는 못 뽑게 제한할 것. 
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

def print_result(count_first, count_second, count_third, count_fourth):
    print(MSG_RESULT)
    print("4등 - 5000원 - {}개".format(count_fourth))
    print("3등 - 20000원 - {}개".format(count_third))
    print("2등 - 100000원 - {}개".format(count_second))
    print("1등 - 5000000원 - {}개".format(count_first))

def print_yield(count_first, count_second, count_third, count_fourth, purchase_price):
    lottery_yield = (5000 * count_fourth + 20000 * count_third + 100000 * count_second + 5000000 * count_win) / purchase_price
    print("> 수익률")
    print(lottery_yield, "배")

def run_lottery(purchase_amount):
    lotteryArr = []
    for i in range(purchase_amount):
        lotteryArr.append(random.sample(range(1, 46), 6))
        lotteryArr[i].sort()
            
    return lotteryArr

def count_win(lotteryArr, lotteryNum, purchase_amount):
    count_first, count_second, count_third, count_fourth = 0, 0, 0, 0
    
    for i in range(purchase_amount):
        win_count = 0

        for j in range(6):
            if (lotteryNum[j] in lotteryArr[i]):
                win_count += 1
               
        if win_count == 6: 
            count_first += 1
        elif win_count == 5:
            count_second += 1
        elif win_count == 4:
            count_third += 1
        elif win_count == 3:
            count_fourth += 1
            
    return(count_first, count_second, count_third, count_fourth)



def run():
    purchase_price = input_purchase_price()
    purchase_amount = compute_purchase_amount(purchase_price)

    print_purchase_amount(purchase_amount)

    # 구입한 금액에 비례해서 lottery를 생성
    lotteryArr = run_lottery(purchase_amount)

    print_lottery(lotteryArr)

    # user가 입력한 lottery 번호 
    lotteryNum = input_lotteryNum()
    print(lotteryNum)

    count_first, count_second, count_third, count_fourth = count_win(lotteryArr, lotteryNum, purchase_amount)
    
    print(count_first, count_second, count_third, count_fourth)
    

run()

# lotteryNum = input_lotteryNum()
# print(lotteryNum)
# print(type(lotteryNum))
