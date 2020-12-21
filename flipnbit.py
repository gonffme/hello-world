import time

#计算以及做一个检查，看看我们推导的对不对。
def dochecks(ran=10):
    m = ran
    pairs = []
    timefunc = []
    for n in range(m):
        start = time.time()
        n += 1
        print('\n现在n={}'.format(n))
        pair = expectstep(n)
        pairs.append([n, pair])
        stop = time.time()
        totaltime = stop - start
        print('{}位计算总共用时{:.5f}s'.format(n, totaltime))
        timefunc.append([n, totaltime])
        time.sleep(5)
    print('结果',pairs)

    checks = []
    for n in range(m):
        n += 1
        check = n * (n + 1) / 4
        checks.append([n, check])
    print('预测',checks)
    return [pairs ,checks, timefunc]



def expectstep(n):
    tn = 2 ** n
    #初始化2^n内的所有数字，以字符串形式放在数组里。
    numbersbox = numbers(n, tn)
    total = 0
    for i in numbersbox:
        #翻转一个数到全0，所需的步数
        print('现在开始进行数字{}的翻转'.format(i))
        wordstep = flipword(i)
        
        #print(wordstep)
        
        total += wordstep
    expect = total / tn
    return expect
        



def numbers(n, tn):
    box = []
    for i in range(tn):
        #此处的符号转换比较关键，从左边补0，补足n位。不然后面计算完全不对。
        bina = f'{i:>0{n}b}'
        box.append(bina)
    return box

def flipword(i):
    step = 0

    while int(i) != 0:
        #如有需要可以把每步翻转的结果看一看形成链条
        print(i, end='-')
        c = i.count('1')
        #flipsingle只进行一位翻转
        i = i[:c-1] + flipsingle(i[c-1]) + i[c:]
        
        step += 1
    print(i)
    return step

def flipsingle(x):
    if x == '1':
        return '0'
    else:
        return '1'


        
if __name__  == "__main__":    
    result, predict, timefunc = dochecks(21)

    
