# class v:
#     class_variable = 0
#     def __init__(self):
#         self.instance_variable = 0
    

# if __name__ == "__main__":
#     obj =  v()
#     print(obj.instance_variable)
#     print(obj.class_variable)




import flask as f

app = f.Flask(__name__)

@app.route("/")
def vij():
    dic = {1:"vijay"}
    return f.render_template("index.html",word=str(dic))

if __name__ == "__main__":
    app.run()
