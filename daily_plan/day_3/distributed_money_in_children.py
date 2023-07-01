class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        cur_money = money - children
        if cur_money < 6:
            return 0

        candidates = min(cur_money // 7, children)
        remanent = cur_money - candidates * 7

        if candidates == children and remanent > 0:
            return candidates - 1

        if children - candidates == 1 and remanent == 3:
            return candidates - 1

        return candidates


    #     money = 20. ch = 3

    #     cur_money =  17
    #     candidates = 2
    #     rem = 3



    #   cases: money.            children              remaining    result
    #           < children                                            -1
    #           < 7                                                    0
    #           money * 7 > ch.     cand = ch                          children - 1
    #           money * 7 < ch.     cand = money * ch


    #           cand < children                           rem in cand - children