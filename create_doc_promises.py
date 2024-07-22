import os
from docxtpl import DocxTemplate

def create_pay_promises_docx(template_path, data, dates_promises):
    # DEFNIR UN CONTADOR
    counter = 0
    # ITERAR LA LISTA DE FECHAS QUE NOS DIO pay_promises.py
    for date in dates_promises:
        data["promises"] = len(dates_promises)
        data["date_promise"] = date
        counter += 1
        data["counter"] = counter

        # RENDERIZAR LOS DATOS EN LA TEMPLATE
        doc_promises = DocxTemplate(template_path)
        doc_promises.render(data)
        
        # PONER NOMBRE
        name = data["lessor_name"].lower()
        name = name.replace(" ", "_")
        
        # CREAR DIREACTORIO
        if not os.path.exists(f'media/{name}'):
            os.mkdir(f'media/{name}')
        
        # GUARDAR EL DOCUMENTO
        doc_promises.save(f'media/{name}/{name}_promises_{data["counter"]}.docx')