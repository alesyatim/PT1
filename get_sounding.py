__all__ = ['int_to_word']

dict1 = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', \
       '6':'six', '7':'seven', '8':'eight', '9':'nine', '11':'eleven', '12':'twelve', \
       '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', \
       '18':'eighteen', '19':'nineteen', \
       '10':'ten', '20':'twenty', '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', \
       '70':'seventy', '80':'eighty', '90':'ninety'}

dict2 = {1:'one_digit', 2:'two_digit', 3:'three_digit', 4:'four_digit', 5:'five_digit', 6:'six_digit'}

def one_digit(s_number):
    word = dict1[s_number]
    return word

def two_digit(s_number):
    word=''
    if s_number[0]=='0' and not s_number[1]=='0': # 0x (1..9)
        word = one_digit(s_number[1])
    elif s_number[0]=='0' and s_number[1]=='0': # 00 (0)
        word = ''
    elif s_number[1]=='0' or s_number[0]=='1': #10..90 or   #11..19
        word = dict1[s_number]
    else: #others
        # part1 = s_number[0]+'0' #20..90
        word = dict1[s_number[0]+'0']  + ' ' + one_digit(s_number[1])

    return word

def three_digit(s_number):
    if s_number[0]=='0': # 0xy (000...099)
        word = two_digit(s_number[1:])
    elif s_number[1]=='0' and s_number[2]=='0': # x00 (100..900)
        word = one_digit(s_number[0]) + ' hundred'
    else: # others + exceptions
        word =  one_digit(s_number[0]) + ' hundred ' + two_digit(s_number[1:])

    return word

def digit_four_five_six(s_number):
    if len(s_number) == 4:
        s_number = '00' + s_number
    elif len(s_number) == 5:
        s_number = '0' + s_number
    word = three_digit(s_number[:3]) + ' thousand and ' + three_digit(s_number[3:])
    return word

def int_to_word(number):
    word=''
    if  type(number) not in [int]:
        return 'Input data is not integer number'
    if number>1000000:
        return 'Input number is out of range'
    if number==1000000:
        return 'one million'
    if number==0:
        return 'zero'


    s_number = str(number)
    if len(s_number)<4:
        word = eval(dict2[len(s_number)]+'(s_number)')
    else: word = digit_four_five_six(s_number)
    return word

if __name__ == '__main__':
    f = open('test.txt', 'w')
    for i in range(1000000):
        word =  int_to_word(i)
        f.write(str(i) + ' : ' + word + '\n' )
    f.close()