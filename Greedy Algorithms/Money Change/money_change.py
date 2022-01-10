# python3

def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = 0
    for i in [10, 5, 1]:
        if money == 0:
            return coins
        coins += money // i
        money %= i
    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
