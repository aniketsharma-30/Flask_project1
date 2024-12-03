from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/first')
def first():
    return 'Hello this is Flask first response'


@FAI.route('/hello')
def hello():
    return render_template('hello.html')
if __name__=='__main__':
    FAI.run(debug=True)