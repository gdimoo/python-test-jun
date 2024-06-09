"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        thai_number_words = {
    0: 'ศูนย์',
    1: 'หนึ่ง',
    2: 'สอง',
    3: 'สาม',
    4: 'สี่',
    5: 'ห้า',
    6: 'หก',
    7: 'เจ็ด',
    8: 'แปด',
    9: 'เก้า'
}
        ten_number = {
        0:'',
        1:'',
        2:'สิบ',
        3:'ร้อย',
        4:'พัน',
        5:'หมื่น',
        6:'แสน',
        7:'ล้าน',
}
        word = ''
        if number < 0:
            return 'number can not less than 0'
        else:
            if number < 10:
                return thai_number_words[number]
            elif number==10000000:
                return 'สิบล้าน'
            else:
                for index,i in enumerate(str(number)):
                    if i != '0':
                        if len(str(number))-index == 2:
                            if i == '2':
                                word+='ยี่'
                                
                        elif (len(str(number))-index) == 1 and i == '1':
                            word+='เอ็ด'
                        else:
                            word+=thai_number_words[int(i)]
                        
                        word+=ten_number[len(str(number))-index]
        return word
