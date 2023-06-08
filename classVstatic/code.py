class ClassTest:
    def instance_method(self):
        print(f"instance of this class {self}")
    
    @classmethod
    def class_method(cls):
        print(f"class method {cls}")

    # this method doesn't take the instance or a class when we call it
    @staticmethod
    def static_method():
        print("calling static method")

# declare the class
test = ClassTest()
# call the method on the instance
# test.instance_method()
# call the method on the class, passing in the instance
# ClassTest.instance_method(test)


# testing the class method
ClassTest.class_method()

# testing the static method
ClassTest.static_method()
