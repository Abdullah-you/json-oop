# def alphabet_position(text):
#     string = '' 
#     dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
#     sentence = text.lower()
#     for chr in sentence:
#         if not chr.isalpha():
#             pass
#         else:
#             string += str(dic[chr]) + ' '
#     return string

# print(alphabet_position('this is a clock'))
def find_it(seq):
    i = 1
    count = 0
    for digit in seq:
        var = digit
        for num in seq:
            if num == var:
                count += 1
        i += 1
        if count %  2 != 0:
            return digit
            
        #if len(number) % 3 == 0:
         #   return number

a = [1,2,3,3,3,3,4,4,5,4,5,6,2,4,6]       
print(find_it(a))