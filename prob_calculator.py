import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        # print(balls)
        for i in balls:
            # print(i, balls[i])
            for j in range(balls[i]):
                self.contents.append(i)
        # print(self.contents)
    def draw (self, n):
        temparray=[]
        initialLength = len(self.contents)
        for i in range(n):
            if(i<initialLength):
                # print("initial itni hai", initialLength)
                # print(i)
                rin=random.randint(0, len(self.contents)-1)
                # print("yeh hai index", rin)
            
                temparray.append(self.contents.pop(rin))
            
        # print(self.contents)
        # print(temparray.count("blue"))
        # print(temparray)
        # print("ye iske contents hain", self.contents)
        return temparray
        




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    another_temp_array=[]
    counter=0
    temphat = hat.contents.copy()
    # print("ye temp hat hai", temphat)

    for i in expected_balls:
            # print("ok then", i, expected_balls[i])
            for j in range(expected_balls[i]):
                another_temp_array.append(i)
    # print("ye another temp array hai", another_temp_array)

    for i in range(num_experiments):
        # print(num_experiments)
        hat.contents=temphat.copy()
        a_temp_array = hat.draw(num_balls_drawn)
        yet_another_temp = another_temp_array.copy()
        for i in another_temp_array:
            try:
                index = a_temp_array.index(i)
                a_temp_array.pop(index)
                yet_another_temp.remove(i)
                # print(i, a_temp_array)
                # print("ye dekhna ek baar", yet_another_temp)
            except:
                continue
        if (yet_another_temp==[]):
            counter+=1
    # print ('ye hai counter tumhara', counter )
    return counter/num_experiments

hat1 = Hat(yellow=5,red=1,green=3,blue=9,test=1)

# print(experiment(hat1,{"blue":1,"green":2}, 5, 100 ))
print(experiment(hat=hat1, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100))