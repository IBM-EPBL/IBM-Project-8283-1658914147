from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template('index.html',name='Home')
@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/products")
def products():
  return render_template('products.html')

@app.route("/product1")
def product1():
  return render_template('product1.html')

@app.route("/product2")
def products2():
  return render_template('product2.html')

@app.route("/blog")
def blog():
  return render_template('blog.html')

@app.route("/blog1")
def blog1():
  return render_template('blog1.html')

@app.route("/blog2")
def blog2():
  return render_template('blog2.html')

@app.route("/blog3")
def blog3():
  return render_template('blog3.html')

@app.route("/blog4")
def blog4():
  return render_template('blog4.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/contact")
def contact():
  return render_template('contact.html')

@app.route("/cart")
def cart():
  return render_template('cart.html')

@app.route("/cart1")
def cart1():
  return render_template('cart1.html')

@app.route("/cart2")
def cart2():
  return render_template('cart2.html')

@app.route("/sproduct")
def sproducts():
  return render_template('sproduct.html')

@app.route("/register")
def registerhome():
  return render_template('register.html')

@app.route("/adminpage")
def adminpage():
    return render_template('adminpage.html')

@app.route("/shoppingcart")
def shoppingcart():
    return render_template('shoppingcart.html')

@app.route("/payment")
def payment():
    return render_template('payment.html')


@app.route("/registerUser",methods=['GET','POST'])
def register():
  return render_template('registerUser.html',name='Home')



@app.route("/loginUser",methods=['GET','POST'])
def login():
    return render_template('loginUser.html',name='Home')

@app.route("/registerAdmin",methods=['GET','POST'])
def adregister():
  return render_template('registerAdmin.html',name='Home')

@app.route("/loginAdmin",methods=['GET','POST'])
def adlogin():
    return render_template('loginAdmin.html',name='Home')


@app.route("/addproduct",methods=['GET','POST'])
def addproduct():       
  return render_template('addproduct.html',success="You have entered the details")

@app.route("/data")
def display():
  col1_list=[]
  col2_list=[]
  col3_list=[]
  col4_list=[]
  #returning to HTML
  return render_template('pro.html',col1= col1_list,col2=col2_list,col3=col3_list,col4=col4_list)


if __name__ == "__main__":
    app.run(debug=True)
