lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$',
       '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '/', '?', ',', '.', '>', '<', '/', '*', '`', '~', ' ']

7
def frmt(a):
    sr = ''
    a = list(a)
    for i in range(0,5):
        if a[i] == '1':
            try:
                b = int(a[i + 1]) + 2
            except:
                sr += str(a[i])
                return sr

            if b <= 3:
                sr += str('0')
                a[i + 1] = str(b)
            else:
                sr += str(a[i])

        else:
            sr += a[i]
    return sr


def encrypt(a):
    cd = ''
    for i in a:
        if cd != '':
            cd += '4'
        ss = ''
        x = lst.index(i)
        b = 16
        for k in range(5):

            for j in range(3, -1, -1):
                if x >= b * j:
                    ss += str(j)
                    x -= b * j
                    break
            b = b / 2
        cd += frmt(ss)
    return cd


def decrypt(a):
    a = a.split('4')

    cd = ''

    for i in a:
        n = 0
        b = 16
        for j in i:
            n += b * int(j)

            b = int(b / 2)
        cd += lst[n]
    return cd

if __name__ == '__main__':
    a = input("Enter Your Message : ")
    print("Your Code Is :", encrypt(a))
    b = input("Enter The Code : ")
    print("Your Message Is :", decrypt(b))
