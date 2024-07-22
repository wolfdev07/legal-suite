from flask import Flask, request, render_template
from forms import NewPromiseForm
from utils import humanize_date
from pay_promises import CreatePayPromises
from create_doc_promises import create_pay_promises_docx


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NewPromiseForm(request.form)
    if request.method == 'POST' and form.validate():
        # GRUADAMOS EL DICT DEL FORM EN data
        data = form.data
        print(data)
        # HUMANIZAMOS LA FECHA DE FIRMA PARA EL PRERENDERIZADO
        data['signature_date'] = humanize_date(data['signature_date'])
        # LE DAMOS FORMATO AL MONTO DE RENTA
        data["amount_rent"] = "{:,.2f}".format(data["amount_rent"])

        # CREAMOS UN DICT CON LA FECHA BASE DE LAS PROMESAS
        date_dict =  {"date": data["date_promise"]}
        # CREAMOS LA INSTANCIA
        promises_instance = CreatePayPromises(date_dict)
        # AGREGAMOS LOS DIAS
        promises_instance.add_pay_days(pays=11)
        # GUARDAMOS EN PROMISES LA LISTA DE FECHAS HUMANIZADAS
        promises = promises_instance.humanize_date()

        # EJECUTAMOS LA CREACION DE DOCUMENTOS PROMESA
        template_path = 'media/layout/pay_promises.docx'
        create_pay_promises_docx(template_path=template_path, data=data, dates_promises=promises)
    

    return render_template('index/index.html', form=form)

@app.route('/hello')
def hello_world():
    return 'Hello World!'



if __name__ == '__main__':
    app.run(debug=True)