#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def abc():
    return render_template('palindrome.html')

@app.route('/detail',methods=['GET','POST'])
def xyz():
    if request.method=='POST':
        x=request.form['a']
        z=x[::-1]
        
        if x==z:
            s='palindrome'
        else:
            s='not palindrome'
    return render_template('palindrome.html',answer=z,yesno=s)

if __name__=='__main__':
    app.run()


# In[ ]:




