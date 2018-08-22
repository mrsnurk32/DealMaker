class TemplateMaker:
    result = list()
    def __init__(self, money):
        self.money = money
        
    def money_str(self):


        units = {0:'',1:'один ', 2:'два ', 3:'три ', 4:'четыре ', 5:'пять ', 6:'шесть ', 7:'семь ', 8:'восемь ', 9:'девять '}
        teens = {0:'',10:'десять', 11:'одиннадцать', 12:'двенадцать', 13:'тринадцать', 14:'четырнадцать',
            15:'пятнадцать',16:'шестнадцать', 17:'семнадцать',18:'восемнадцать',19:'девятнадцать'}
        tens = {0:'',2:'двадцать ',3:'тридцать ',4:'сорок ',5:'пятьдесят ',6:'шестьдесят ',7:'семьдесят ',8:'восемьдесят ',9:'девяносто '}
        hundreds = {0:'',1:'сто ',2:'двести ',3:'триста ',4:'четыриста ',5:'пятьсот ',6:'шестьсот ',7:'семьсот ',8:'восемьсот ',9:'девятьсот '}
        thousands = {0:'', 1:'одна тысяча ',2:'две тысячи ',3:'три тысячи ',4:'четыре тысячи ',5:'пять тысяч ',6:'шесть тысяч ',
            7:'семь тысяч ',8:'восемь тысяч ',9:'девять тысяч '}
        ten_thousands = {0:'тысяч '}
        millions = {0:'', 1:'миллион', 2:'миллиона', 3:'миллионов'}

        for i in range(1):

            num_slice = str(self.money)

            unit = (num_slice[-1])
            ten = (num_slice[-2:])
            hnd = num_slice[-3:-2]
            thd = num_slice[-4:-3]
            thd_10 = num_slice[-5:-3]
            thd_100 = num_slice[-6:-5]
            mln = num_slice[-7:-6]

            if len(num_slice) > 6:
                if int(mln) > 0 and int(mln) < 2:
                    mln = 1

                if int(mln) > 1 and int(mln) < 5:
                    mln = 2

                if int(mln) > 4:
                    mln = 3
                TemplateMaker.result.append(units[int(mln)])
                TemplateMaker.result.append(millions[mln])

            if len(num_slice) > 5:
                if int(thd_10) < 1 and int(thd_100) > 0:
                    TemplateMaker.result.append(hundreds[int(thd_100)])
                    TemplateMaker.result.append(ten_thousands[0])

                if int(thd_10) > 0:
                    TemplateMaker.result.append(hundreds[int(thd_100)])

            if len(num_slice) > 4:
                if int(thd_10) > 9 and int(thd_10) < 20:
                    TemplateMaker.result.append(teens[int(thd_10)])
                    TemplateMaker.result.append('тысяч')

                if int(thd_10) > 19 and int(thd_10) < 100:
                    TemplateMaker.result.append(tens[int(thd_10[0:1])])
                    if int(thd_10[1:2]) < 1:TemplateMaker.result.append('тысяч')

            if len(num_slice) > 3:
                if len(num_slice) > 4 and int(thd_10) > 20 and int(thd_10[-1]) != 0:TemplateMaker.result.append(thousands[int(thd)])
                if len(num_slice) < 5:TemplateMaker.result.append(thousands[int(thd)])

            if len(num_slice) > 2:
                if int(hnd) > 0:TemplateMaker.result.append(hundreds[int(hnd)])

            if len(num_slice) > 1:
                if int(ten) > 9 and int(ten) < 20:
                    TemplateMaker.result.append(teens[int(ten)])
                    continue

                if int(ten) > 19 and int(ten) < 100:
                    TemplateMaker.result.append(tens[int(ten[-2:-1])])
                    if int(unit) > 0: TemplateMaker.result.append(units[int(unit)])
                    continue

            if len(num_slice) > 0:TemplateMaker.result.append(units[int(unit)])
