from flask import *
from flask_bootstrap import *
from mongoengine import *
from pw import *

app = Flask(__name__)
bootstrap = Bootstrap(app)


connect(db="goalgetterdb", username="tfoss", password=pw_,
        host=host_)

class User(Document):
    userName = StringField(required=True, max_length=200)
    passWord = StringField(required=True, max_length=200)
    goalNames = ListField(StringField(required=True, max_length=200))
    descriptions = ListField(StringField(required=True, max_length=1000))
    desiredTimes = ListField(FloatField())
    timeCompleted = ListField(FloatField())
    status = ListField(IntField())






@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        user = request.form['usr']
        pw1 = request.form['pword']
        pw2 = request.form['pword2']# no check to see if they are the smae
        tempuser = User(userName=user, passWord=pw1)
        tempuser.save()
        #print("Hello")
        print(User.objects.count())
        for ppl in User.objects:
            print(ppl.userName)
        return render_template('app.html', user=user)





@app.route('/goal',  methods = ['POST'])
def update(user):
    print("hello")
    if request.method == 'POST':
        tempUser = User.objects(userName=user)

        goal = request.form.get('title')
        print(goal)
        # desc = request.form['desc']
        # time = request.form['time']

        # tempUser.goalNames.append(goal)
        # tempUser.descriptions.append(desc)
        # tempUser.desiredTimes.append(time)

        tempUser.save()
        return("")

        # for ppl in User.objects:
        #     print(ppl.userName)
        #     print(ppl.goalNames[0])
        #     pritn(ppl.descriptions[0])
        #     print(ppl.desiredTimes[0])
        #     print()
        #print(goal)



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
