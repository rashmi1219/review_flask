from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import ssl
import json


app = Flask(__name__)
@app.route('/')
def index():
    context = ssl._create_unverified_context()
    ineuron_url = "https://courses.ineuron.ai/"
    uClient = uReq(ineuron_url, context=context)
    ineuronPage = uClient.read()
    uClient.close()
    ineuron_html = bs(ineuronPage, "html.parser")
    courses = ineuron_html.findAll("script", type="application/json")
    for script in ineuron_html.findAll("script", type="application/json"):
        res_dict = json.loads(script.contents[0])
    l1 = list(res_dict['props']['pageProps']['initialState']['init']['categories'].values())
    l2 = list(l1[0]['subCategories'].values())
    courses_list = {"courses":[]}
    for i in range(len(l1)):
        l2 = list(l1[i]['subCategories'].values())
        for j in range(len(l2)):
            course = l2[j]['title']
            courses_list["courses"].append(course)
    return courses_list
@app.route('/instr')
def index1():
    context = ssl._create_unverified_context()
    ineuron_url = "https://courses.ineuron.ai/"
    uClient = uReq(ineuron_url, context=context)
    ineuronPage = uClient.read()
    uClient.close()
    ineuron_html = bs(ineuronPage, "html.parser")
    courses = ineuron_html.findAll("script", type="application/json")
    for script in ineuron_html.findAll("script", type="application/json"):
        res_dict = json.loads(script.contents[0])
    l1 = list(res_dict['props']['pageProps']['initialState']['init'].values())
    list_data = list(l1[1].values())

    result_data = {"Name": [], "Email": [], "Social": [], "Description": []}

    for i in range(20):#range is taken 20 because some data of desription, email and social are missing
        result_data["Name"].append(list_data[i]['name'])
        result_data["Email"].append(list_data[i]['email'])
        result_data["Social"].append(list_data[i]['social'])
        result_data["Description"].append(list_data[i]['description'])
    return result_data

if __name__ == '__main__':
    app.run()