from pymongo import MongoClient
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

##원하는 Key값을 보유한 List만 뽑기
entire_list = list(db.mobile_price.find({},{'_id':0}))
pet_name_list = list(db.mobile_price.find({},{'_id':0, 'pet_name':1}))
model_name_list = list(db.mobile_price.find({},{'_id':0, 'model_name':1}))
device_price_origin_list = list(db.mobile_price.find({},{'_id':0, 'device_price_origin':1}))


test= pet_name_list[3]['pet_name']

print(test)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/getData', methods=['POST'])
def test_post():
    return jsonify({**{ 'data2': entire_list}})



if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
    