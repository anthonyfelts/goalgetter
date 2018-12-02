from flask import *
from flask_bootstrap import *
from mongoengine import *

app = Flask(__name__)
bootstrap = Bootstrap(app)


connect(db="goalgetterdb", username="tfoss", password="123456a",
        host="mongodb://tfoss:123456a@ds153815.mlab.com:53815/goalgetterdb")

class User(Document):
    userName = StringField(required=True, max_length=200)
    passWord = StringField(required=True, max_length=200)
    goalNames = ListField(StringField(required=True, max_length=200))
    descriptions = ListField(StringField(required=True, max_length=1000))
    desiredTimes = ListField(FloatField())
    timeCompleted = ListField(FloatField())
    status = ListField(IntField)






@app.route('/')
def index():
    return render_template('client.html')


@app.route('/',  methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return 'hello'

#
# # @app.route('/newuser', methods = ['POST', 'GET'])
# # def newuser():
# #     if request.method == 'POST':
# #         try:
# #             #...
# #             #...
# #
# #         except:
# #             con.rollback()
# #             msg = 'error in insert operation'
#
#
if __name__=='__main__':
    app.run(debug=True)
