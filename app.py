import requests
from flask import Flask,render_template,request
from twilio.rest import Client
import requests_cache

acc='AC0f384b6414025258a00a29f16189af06'
tok='ff32b9ae1fe194f4f64de35a3299b865'

client =Client(acc,tok)
app=Flask(__name__,static_url_path='/static')
@app.route('/')
def regstration_form():
    return render_template('one.html')
@app.route('/login_page2',methods=['POST','GET'])

def login_registration_details():
    name=request.form['nameid']
    email=request.form['mailid']
    source=request.form['cityid']
    state=request.form['stateid']
    dest=request.form['destid']
    deststate = request.form['deststateid']
    phone=request.form['contactid']
    aadhar=request.form['aadharid']
    date=request.form['dateid']

    r=requests.get('https://api.covid19india.org/v4/data.json')
    json_data=r.json()

    cnt=json_data[deststate]['districts'][dest]['total']['confirmed']
    pop= json_data[deststate]['districts'][dest]['meta']['population']


    if ((cnt)/(pop))*100 <30 and request.method=='POST':
        status='confirmed'
        client.messages.create(to="whatsapp:+917659911748",
                               from_="whatsapp:+14155238886",
                                body="Hello "+name+" "+"Your travel from "+source+" to"+dest+" on "+date+ "has been approved")
        return render_template('user_registration_details.html',var1=name,var2=email,var3=source,var4=dest,var5=phone,var6=aadhar,var7=date,var8=status,var9=state,var10=deststate)
    else:
        status='Not confirmed'
        client.messages.create(to="whatsapp:+917659911748",from_="whatsapp:+14155238886",
                                body = "Hello " + name + " " + "Your travel from " + source + " to" + dest + " on " + date + "has NOT approved")
        return render_template('user_registration_details.html',var1=name, var2=email, var3=source, var4=dest, var5=phone,var6=aadhar, var7=date,var8=status,var9=state,var10=deststate)


if __name__=="__main__":
    app.run(port=9001,debug=True)

