from flask import Flask, render_template, request
from post import Post
import requests
import smtplib

send_email = "oogwaytule@gmail.com"
password = "hello1234hello"
response = requests.get('https://api.npoint.io/a7fada21df7a05572117').json()
#
# posts = []
# details = []
# for obj in response:
#     temp = Post(obj['id'], obj['Book'], obj['about'], obj['intro'])
#     posts.append(temp)
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('index.html', post=posts)
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/post/<int:num>')
# def post(num):
#     file = posts[num-1]
#     return render_template('post.html', post=file)
#
# @app.route('/message', methods=["POST"])
# def collect_data():
#     Name = request.form['inputName']
#     Email = request.form['inputEmail']
#     Mess = request.form['inputMessage']
#     phone = request.form['inputPhone']
#
#     temp = {"name":Name, "email":Email, "phone":phone, "message":Mess}
#     details.append(temp)
#     send_email(Name, Email)
#     return "<h1>Your request has been submitted</h1>"



#
# if __name__ == "__main__":
#     app.run(debug=True)
