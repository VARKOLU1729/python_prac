class v:
    class_variable = 0
    def __init__(self):
        self.instance_variable = 0
    

if __name__ == "__main__":
    obj =  v()
    print(obj.instance_variable)
    print(obj.class_variable)
