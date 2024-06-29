def sayhi():
    print("Hello User") #함수 안에 있으면 print 터미널에서 안나옴


sayhi() #이렇게 따로 빼줘야함 마치 void 변수처럼

def say_hi():
    print("Hi User")


say_hi() #이렇게 쓰는게 더 파워풀함


def say_hi1(name, age):
    print("Hi " + name + ", you are " + age) #+안쓰고 , 해도 왜 되는지는 모르겠네


say_hi1("주호", "21") #void draw에서 괄호 안에 변수 지정 해주듯이
say_hi1("차주호", "19") 


def say_hi1(name, age):
    print("Hi " + name + ", you are " + str(age)) #이렇게 해주면 그냥 상수도 쓸 수 있따.


say_hi1("주호", 21) 
