from flask import Flask, render_template, url_for, request
from flask_talisman import Talisman
from item import Item
import data

app = Flask(__name__)
https_only = False

@app.route("/", methods=["GET", "POST"])
def index():
    list_status = None
    data_list = data.default_user
    todo = data_list.get_as_python_list()

    if todo:
        if request.method == 'POST':
            for index in range(len(todo)):
                checked = f'{index}' in request.form

                if todo[int(index)].is_done is not checked:
                    todo[int(index)].set_is_done(checked)

            new = request.form.get('new_item', '', type=str)
            if new != '':
                data_list.add(Item(new))

        done = 0
        not_done = 0
        for item in todo:
            if item.is_done:
                done += 1
            else:
                not_done += 1
        
        list_status = f'{done} tasks done, {not_done} tasks not yet done. {len(todo)} tasks in total'

    return render_template('index.html.j2', list_status=list_status, list=todo)

if https_only:
    Talisman(app, content_security_policy=None)

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))
