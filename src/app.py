from flask import Flask, render_template, url_for, request
from flask_talisman import Talisman
from item import Item
import data

app = Flask(__name__)
https_only = False

@app.route("/", methods=["GET", "POST"])
def index():
    list_status = None
    todo = None

    if data.user1.get_as_python_list():
        if request.method == 'POST':
            for index in range(len(data.user1.get_as_python_list())):
                is_checked = f'{index}' in request.form

                if data.user1.list_items[int(index)].is_done is not is_checked:
                    data.user1.list_items[int(index)].set_is_done(is_checked)

            new = request.form.get('new_item', '', type=str)
            if new != '':
                data.user1.add(Item(new))

        todo = data.user1.get_as_python_list()
        done = 0
        not_done = 0
        for item in todo:
            if item.is_done:
                done += 1
            else:
                not_done += 1
        
        list_status = f'{done} tasks done, {not_done} tasks not yet done. {len(todo)} tasks in total'

    return render_template('index.html', list_status=list_status, list=todo)

if https_only:
    Talisman(app, content_security_policy=None)

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))