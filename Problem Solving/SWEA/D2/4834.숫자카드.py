#0~9까지 숫자가 적힌 N장의 카드가 주어진다.
#가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
#카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
for tc in range(1, int(input())+1):
    N=int(input())
    num=list(str(input()))
    for i in num:
        #N개의 숫자 중에 중복되는 수가 있는지 확인

    card_num=0
    numbers=0

    print('#{} {}'.format(tc, card_num, numbers))