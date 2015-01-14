from jsonconverter import JsonConverter

class Test(JsonConverter):

    def __init__(self, test_prop1, test_prop2, test_prop3):
        self.test_prop1 = test_prop1
        self.test_prop2 = test_prop2
        self.test_prop3 = test_prop3


class AnotherTest():

    def __init__(self, at_prop1, at_prop2):
        self.at_prop1 = at_prop1
        self.at_prop2 = at_prop2

    def simple_method(self):
        print('this is a simple method')


class ExampleClass():
    def __init__(self,property):
        self.__secret_prop = 123
        self.property = property

    def __test__(self):
        print('just a test')

    def __not_allowed_method(self):
        print("<Gandalf>You shall not pass!</Gandalf>")

if __name__ == "__main__":
    import json
    x = Test(1, 2, AnotherTest({'key1':3.1,'key2':None},[4,5,ExampleClass('example')]))
    cvt = x.convert()
    z = json.dumps(cvt)
    print(z)