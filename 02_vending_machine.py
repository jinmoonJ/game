print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액

while True:
    print()
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

    # 여기부터 코드를 작성하세요.
    # 1-1. 투입한 금액의 누적 금액
    if money > 0:
        budget += money
        print(f"현재 누적 금액은 {budget}원입니다.")
    elif money < 0:
        print("금액은 1원 이상 넣어주세요.")
    else:
        break

if budget < min(costs):
    print(f"{budget}원으로 구매 가능한 메뉴가 없습니다.")
else:
    list1 = []
    for i in range(len(costs)):
        if budget >= costs[i]:
            print(f"{i+1}. {menus[i]} {costs[i]}원")
            list1.append(i+1)
    print()
    
    while True:
        a = int(input("구매하실 메뉴의 번호를 입력하세요 : "))
        if a not in list1:
            print("구매할 수 없는 메뉴입니다.")
        else:
            print(f"{menus[a-1]}를 구매하셨습니다.")
            print(f"거스름돈은 {budget - costs[a-1]}원입니다. 감사합니다.")
            break
        



'''
    for i in list1:
        if a == i:
            print(f"{menus[i-1]}를 구매하셨습니다.")
            print(f"거스름돈은 {budget - costs[i-1]}원입니다. 감사합니다.")
            break
        else:
            print("구매할 수 없는 메뉴입니다.")
            break
'''
    


    
