#The code has to display any non-negative integer number entered by the user.
#Using a list containing patterns of all ten digits may be very helpful.

def led_display(num):
    nums = str(num)
    digit = {
        0:['###','# #','# #','# #','###'],
        1:['  #','  #','  #','  #','  #'],
        2:['###','  #','###','#  ','###'],
        3:['###','  #','###','  #','###'],
        4:['# #','# #','###','  #','  #'],
        5:['###','#  ','###','  #','###'],
        6:['###','#  ','###','# #','###'],
        7:['###','  #','  #','  #','  #'],
        8:['###','# #','###','# #','###'],
        9:['###','# #','###','  #','###']
    }

    new_list = []
    for d in nums:
        d = int(d)
        if d in digit:
            new_list.append(digit[d])

    for i in range(5):
        for l in new_list:
            print(l[i], end= "  ")
        print("")

def get_num():
    n = int(input("Please enter digits: "))
    return n

num = get_num()
led_display(num)
