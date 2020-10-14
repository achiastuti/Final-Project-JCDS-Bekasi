from contextlib import nullcontext
from flask import Flask, render_template, request, send_from_directory
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.htm")

@app.route("/prediction")
def prediction():
    return render_template("prediction.htm")

@app.route("/visual")
def visual():
    return render_template("visual.htm")

@app.route("/author")
def author():
    return render_template("author.htm")

@app.route('/data/<path:x>')
def data(x):
    return send_from_directory("data", x)

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        input = request.form
        #Age
        age = int(input["age"])
        #Default
        default = input["default"]
        strDefault = ""
        if default == "y":
            defa = 1
            strDefault = "Yes"
        else:
            defa = 0
            strDefault = "No"
        #Housing
        housing = input["housing"]
        strHousing = ""
        if housing == "y":
            hou = 1
            strHousing = "Yes"
        else:
            hou = 0
            strHousing = "No"
        #Loan
        loan = input["loan"]
        strHousing = ""
        if loan == "y":
            loa = 1
            strLoan = "Yes"
        else:
            loa = 0
            strLoan = "No"
        #Duration
        dur = int(input["duration"])
        #Campaign
        camp = int(input["campaign"])
        #Previous
        prev = int(input["previous"])
        #Job
        job = input["job"]
        strJob = ""
        if job == "mgt":
            mgt = 1
            blu = 0
            tech = 0
            adm = 0
            srv = 0
            ret = 0
            self = 0
            std = 0
            unemp = 0
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Management"
        if job == "blu":
            mgt = 0
            blu = 1
            tech = 0
            adm = 0
            srv = 0
            ret = 0
            self = 0
            std = 0
            unemp = 0
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Blue Corral"
        if job == "tech":
            mgt = 0
            blu = 0
            tech = 1
            adm = 0
            srv = 0
            ret = 0
            self = 0
            std = 0
            unemp = 0
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Technician"
        if job == "adm":
            mgt = 0
            blu = 0
            tech = 0
            adm = 1
            srv = 0
            ret = 0
            self = 0
            std = 0
            unemp = 0
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Admin"
        if job == "srv":
            mgt = 0
            blu = 0
            tech = 0
            adm = 0
            srv = 1
            ret = 0
            self = 0
            std = 0
            unemp = 0
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Services"
        if job == "ret":
            mgt = 0
            blu = 0
            tech = 0
            adm = 0
            srv = 0
            ret = 1
            self = 0
            std = 0
            unemp = 0
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Retired"
        if job == "self":
            mgt = 0
            blu = 0
            tech = 0
            adm = 0
            srv = 0
            ret = 0
            self = 1
            std = 0
            unemp = 0
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Self Employed"
        if job == "std":
            mgt = 0
            blu = 0
            tech = 0
            adm = 0
            srv = 0
            ret = 0
            self = 0
            std = 1
            unemp = 0
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Student"
        if job == "unemp":
            mgt = 0
            blu = 0
            tech = 0
            adm = 0
            srv = 0
            ret = 0
            self = 0
            std = 0
            unemp = 1
            ent = 0
            hmd = 0
            unk = 0
            strJob = "Unemployed"
        if job == "ent":
            mgt = 0
            blu = 0
            tech = 0
            adm = 0
            srv = 0
            ret = 0
            self = 0
            std = 0
            unemp = 0
            ent = 1
            hmd = 0
            unk = 0
            strJob = "Enterprenership"
        if job == "hmd":
            mgt = 0
            blu = 0
            tech = 0
            adm = 0
            srv = 0
            ret = 0
            self = 0
            std = 0
            unemp = 0
            ent = 0
            hmd = 1
            unk = 0
            strJob = "House Maid"
        if job == "unk":
            mgt = 0
            blu = 0
            tech = 0
            adm = 0
            srv = 0
            ret = 0
            self = 0
            std = 0
            unemp = 0
            ent = 0
            hmd = 0
            unk = 1
            strJob = "Other"
        #Marital
        marital = input["marital"]
        strMarital= ""
        if marital == "mar":
            mar = 1
            sin = 0
            div = 0
            strMarital = "Married"
        if marital == "sin":
            mar = 0
            sin = 1
            div = 0
            strMarital = "Single"
        if marital == "div":
            mar = 0
            sin = 0
            div = 1
            strMarital = "Divorced"
        #Education
        education = input["education"]
        strEducation = ""
        if education == "pri":
            pri = 1
            sec = 0
            ter = 0
            oth = 0
            strEducation = "Primary"
        if education == "sec":
            pri = 0
            sec = 1
            ter = 0
            oth = 0
            strEducation = "Secondary"
        if education == "ter":
            pri = 0
            sec = 0
            ter = 1
            oth = 0
            strEducation = "Tertiery"
        if education == "oth":
            pri = 0
            sec = 0
            ter = 0
            oth = 1
            strEducation = "Other"
        #Poutcome
        poutcome = input["poutcome"]
        strPoutcome = ""
        if poutcome == "suc":
            suc = 1
            fai = 0
            othe = 0
            unkw = 0
            strPoutcome = "Success"
        if poutcome == "fai":
            suc = 0
            fai = 1
            othe = 0
            unkw = 0
            strPoutcome = "Failure"
        if poutcome == "othe":
            suc = 0
            fai = 0
            othe = 1
            unkw = 0
            strPoutcome = "Other"
        if poutcome == "unkw":
            suc = 0
            fai = 0
            othe = 0
            unkw = 1
            strPoutcome = "Unknown"
        #Result
        datainput = [[age,defa, hou, loa, dur, camp, prev, adm, blu, ent, hmd, mgt, ret, self, srv, std, tech, unemp, unk, div, mar, sin, pri, sec, ter, oth, fai, othe, suc, unkw]]
        print(datainput)
        pred = model.predict(datainput)[0]
        proba = model.predict_proba(datainput)
        proba1 = proba[:,1]
        new_pred=[0 if x < 0.983463 else 1 for x in proba1][0]
        if new_pred == 0:
            prbb = round((proba[0][0]*100), 2)
            rslt = "Not Potential"
            mssg = "Sorry, this customer is not potential to open term deposito"
        else:
            prbb = round((proba[0][1]*100), 2)
            rslt = "Potential"
            mssg = "Congratulation, this customer is potential to open term deposito"
        return render_template(
            "prediction.htm", job= strJob, marital= strMarital,
            education= strEducation, poutcome= strPoutcome, default= strDefault, housing= strHousing,
            loan= strLoan, age = age, duration= dur, campaign=camp, previous=prev,
            result= rslt, proba = prbb, mssg = mssg
        )


if __name__ == "__main__":
    model = joblib.load("bestmodel")
    app.run(debug=True, port=8000)