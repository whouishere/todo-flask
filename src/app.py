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
            for key, value in request.form.items():
                if key == 'new_item' and value != '':
                    data.user1.list_items.append(Item(value))
                elif key == 'new_item' and value == '':
                    pass
                else:
                    # i honestly don't know why flask doesn't return unchecked form boxes
                    # and i certainly have no idea for the workaround for this
                    if value is not data.user1.list_items[int(key)].is_done:
                        data.user1.list_items[int(key)].set_is_done(value)
                        print(f'{type(value)}: {value}')

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