import random

MSG_PURCHASE = "> 구입 금액을 입력해주세요: "
MSG_VALUE_ERROR = "> 숫자만 입력해주세요!"
MSG_RANGE_ERROR = "> 1 ~ 45 까지의 숫자를 입력하세요!"
MSG_INAPPROPRIATE_NUMBERS_OF_INPUT = "> 6개의 숫자를 입력하세요."
MSG_INPUT_OVERLAPPED = "> 중복된 숫자가 존재합니다!"
MSG_INPUT_LOT_NUM = "> 지난 주 당첨 번호를 입력해주세요: "
MSG_RESULT = "> 로또 당첨 결과"

def main():
    run()

# 얼마 구입할 건지 입력
def input_purchase_price():
    purchase_price = input(MSG_PURCHASE)
    while(purchase_price.isdigit() == False) :
        print(MSG_VALUE_ERROR)
        purchase_price = input(MSG_PURCHASE)

    return purchase_price

# 당첨 번호 입력
def input_lotteryNum():    
    lotteryNum = []

    while True:
        count = 0
        lotteryNum = []
        try: 
            temp = input(MSG_INPUT_LOT_NUM).split(',')

            if len(temp) != 6:
                print(MSG_INAPPROPRIATE_NUMBERS_OF_INPUT)
                continue
            for i in range(6):
                if int(temp[i]) not in range(1, 46):
                    print(MSG_RANGE_ERROR)
                    break
                elif int(temp[i]) in lotteryNum:
                    print(MSG_INPUT_OVERLAPPED) 
                    break
                else: 
                    lotteryNum.append(int(temp[i]))
                    count += 1
            if count == 6:
                break
        except ValueError:
            print(MSG_VALUE_ERROR)
            continue
    lotteryNum.sort()  
    return(lotteryNum)
    
# 몇 장 구입했는지 계산
def compute_purchase_amount(purchase_price):
    purchase_amount = int(purchase_price) / 1000
    return int(purchase_amount)

# 몇 장 구매했는지 출력
def print_purchase_amount(purchase_amount):
    print("{}장의 로또를 구입하셨습니다.".format(purchase_amount))

# 구매한 로또 번호 출력
def print_lottery(lotteryArr):
    for i in range(len(lotteryArr)):
        print(lotteryArr[i])

# 로또 결과 출력
def print_result(count_first, count_second, count_third, count_fourth):
    print(MSG_RESULT)
    print("4등 - 5000원 - {}개".format(count_fourth))
    print("3등 - 20000원 - {}개".format(count_third))
    print("2등 - 100000원 - {}개".format(count_second))
    print("1등 - 5000000원 - {}개".format(count_first))

# 로또 결과 출력2 (구매금액, 당첨금액, 거스름돈, 수익률)
def print_yield(count_first, count_second, count_third, count_fourth, purchase_price, purchase_amount):
    lottery_prize = (5000 * count_fourth + 20000 * count_third + 100000 * count_second + 5000000 * count_first)
    purchase_change = int(purchase_price) % 1000
    lottery_yield =  lottery_prize / (int(purchase_price) - purchase_change)

    print("> 구매금액: {}원\n> 당첨금액: {}원\n> 거스름돈: {}원".format(purchase_price, lottery_prize, purchase_change)) 
    print("> 수익률")
    print(lottery_yield, "배")
    
# 구매 매수 만큼 로또 번호 추첨. 
def run_lottery(purchase_amount):
    lotteryArr = []
    for i in range(purchase_amount):
        lotteryArr.append(random.sample(range(1, 46), 6))
        lotteryArr[i].sort()
            
    return lotteryArr

# 로또 결과 확인
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
            
    return [count_first, count_second, count_third, count_fourth]

# run 함수
def run():
    purchase_price = input_purchase_price()
    purchase_amount = compute_purchase_amount(purchase_price)

    print_purchase_amount(purchase_amount)

    lotteryArr = run_lottery(purchase_amount)

    print_lottery(lotteryArr)
    print("\n")

    lotteryNum = input_lotteryNum()
    print(lotteryNum, "\n")

    count_first, count_second, count_third, count_fourth = count_win(lotteryArr, lotteryNum, purchase_amount)

    print_result(count_first, count_second, count_third, count_fourth)
    print("\n")

    print_yield(count_first, count_second, count_third, count_fourth, purchase_price, purchase_amount)

if __name__ == "__main__" :
    main()