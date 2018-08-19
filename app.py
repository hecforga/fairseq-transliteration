import os
import requests
import json
import config
import traceback
from flask import Flask, render_template,request,flash
from forms import TranslitForm
from flask_mail import Message, Mail
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads, patch_request_class



from fairseq import options, tasks, tokenizer, utils
from interactive import get_translation_from_string

base_host_name = config.BASE_HOST_NAME

mail = Mail()
app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = config.SECRET_KEY

app.config['DEBUG'] = config.DEBUG
app.config['MAIL_SERVER'] = config.MAIL_SERVER
app.config['MAIL_PORT'] = config.MAIL_PORT
app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD

app.config['MAX_CONTENT_LENGTH'] = config.MAX_CONTENT_LENGTH
app.config['UPLOADS_DEFAULT_DEST'] = config.UPLOADS_DEFAULT_DEST

ALLOWED_EXTENSIONS = config.ALLOWED_EXTENSIONS

cv_set = UploadSet('cv', ALLOWED_EXTENSIONS)
configure_uploads(app, cv_set)
patch_request_class(app)  # set maximum file size, default is 16MB

mail.init_app(app)

base_args = config.base_args


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/translit', methods=['GET', 'POST'])
def upload():
    form = TranslitForm()
    try:

        if request.method == 'POST':
            if form.validate() == False:
                flash('All fields are required.')
                return render_template('upload.html', form=form)
            else:

                if form.save.data and "Incorrect" in form.message.data:
                     msg = Message("Incorrect entry", sender='erik@teamable.com', recipients=['erik@teamable.com','nataly@teamable.com'])
                     msg.body = """Name: %s \n Location: %s \n Email: %s \n Education: %s \n Phone: %s""" % (form.name.data, form.location.data, form.email.data, form.education.data, form.phone.data)
                     msg.body += '\n'
                     msg.body += form.message.data
                     mail.send(msg)
                     return render_template('upload.html', form=form)

                elif form.upload.data:
                    translit_result = str(get_translit(form.translit.data))

                    form.translit.data = str(form.translit.data)
                    if translit_result:
                        translit_result = translit_result.replace("ո ւ", "ու")

                    form.translit_arm.data = translit_result


                    return render_template('upload.html', success=True,  form = form)
                else:
                     return render_template('upload.html', form=form)


        elif request.method == 'GET':
            return render_template('upload.html', form=form)

    except Exception as e:
        print(traceback.format_exc())
        return render_template('upload.html', form=form)



def get_translit(query_string):
    translit = ""
    try:

        translit = get_translation_from_string(base_args, query_string)

        if not translit:
            raise Exception('Translit Model Unavailable')

    except Exception as e:
        print(e)
        return None

    return translit



if __name__ == '__main__':

    parser = options.get_generation_parser(interactive=True)
    args = options.parse_args_and_arch(parser)
    base_args = args

    app.run(debug=True)
