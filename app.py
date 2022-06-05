import os
from prettytable import PrettyTable
from html import unescape
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    f = open(os.environ.get('DATA_FILE_PATH'), 'r')
    col = int(f.readline())
    col += 1
    f.close()
    f = open(os.environ.get('DATA_FILE_PATH'), 'w')
    f.write(str(col))
    f.close()
    table = PrettyTable()
    table.field_names = ['Name', 'Age', 'City']
    table.add_row(["Alice", 20, "Adelaide"])
    table.add_row(["Bob", 20, "Brisbane"])
    table.add_row(["Chris", 20, "Cairns"])
    table.add_row(["David", 20, "Sydney"])
    table.add_row(["Ella", 20, "Melbourne"])
    table = str(table).replace('\n', '<br>')
    unescaped = unescape(table)
    return render_template('index.html', name=os.environ.get('YOUR_NAME'), n=col, t=unescaped)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
