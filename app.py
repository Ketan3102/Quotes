from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key="Your API Key"

def generate_quote(category='Love',language='english',token=30, author='Anonymous'):
    response=openai.Completion.create(engine="text-davinci-002",
                                      prompt=f"Hello, ChatGPT! Show me a quote of {category} in {language} by {author} within {token} words",
                                      max_tokens=token, temperature=0.5)
    return response.choices[0].text

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        cat=request.form['category']
        lang=request.form['language']
        aut=request.form['author']
        tok=int(request.form['token'])
        quotes=generate_quote(category=cat,language=lang,token=tok, author=aut)
        return render_template('index.html', quotes=quotes)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)