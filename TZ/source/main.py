from flask import Flask
from json import dumps
from os import listdir
from os.path import getctime
from config import ROOT_PATH

app = Flask(__name__)


def getFoldersAndFiles():
    data = []
    for current_file_or_folder in listdir(path=ROOT_PATH):
        obj = {"name": current_file_or_folder,
               "type": "file" 
                       if (current_file_or_folder.find('.') != -1)
                       else "folder",
               "time": int(getctime(current_file_or_folder))}
        data.append(obj)
    return dumps({"data": data})


@app.route('/api/meta', methods=['GET'])
def index():
    return getFoldersAndFiles()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
