from flask import Flask, render_template, request
from logging import root
from translate import Translator
from tkinter import *
from tkinter.filedialog import asksaveasfilename

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dicionario.html')

@app.route('/traduzir', methods=['POST'])
def traduzir():
    tradulen = request.form['tradulen']
    tradupass = ''
    
    if 'run_en' in request.form:
        s = Translator(from_lang="english", to_lang="pt-br")
        convert = s.translate(tradulen)
        tradupass = convert
    elif 'run_pt' in request.form:
        s = Translator(from_lang="pt-br", to_lang="english")
        convert = s.translate(tradulen)
        tradupass = convert
    
    return render_template('index.html', tradulen=tradulen, tradupass=tradupass)

if __name__ == '__main__':
    app.run()
