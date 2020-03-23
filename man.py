
class Man:
    def __init__(self, name): # 클래스를 초기화하는 방법을 정의한다. 이 초기화용 메스드를 생성자 (constructor)라고 하며 클래스의 인스턴스가 만들어질 때 한번만 불린다.
        self.name = name # 파이썬에서는 메서드의 첫번째 인수로 자신(자신의 인스턴스)을 나타내는 self를 명시적으로 쓰는것이 특징
        print('Initialized!')

    def hello(self):
        print('Hello ' + self.name + '!')

    def goodbye(self):
        print('Good-bye ' + self.name + '!')

m = Man("Yunsoo")
m.hello()
m.goodbye()