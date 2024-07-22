import os
from docxtpl import DocxTemplate

dates_promises = ['5 de agosto de 2024', '5 de septiembre de 2024', '7 de octubre de 2024', '5 de noviembre de 2024', '5 de diciembre de 2024', '6 de enero de 2025', '6 de febrero de 2025', '5 de marzo de 2025', '7 de abril de 2025', '6 de mayo de 2025', '5 de junio de 2025']

data = {
        "counter": 0,
        "amount_rent": "5,000.00",
        "signature_date" : "5 de agosto de 2024",
        "promises": 0,
        "date_promise": "",
        "lessor_name": "Chancito Feliz",
        "lessor_address": "La Michocana 135, Metepec, Mexico.",
        "amount_rent_letter": "Cinco mil",
        "tenant_name": "Chanchito Juarez",
        "jointly_obligated_name": "Obligado Chanchito Gasrcia",
        "tenant_address": "Quinta Avenida 50, Toluca, México.",
        "jointly_obligated_address": "Quinta Avenida 50, Toluca, México.",
        "municipality": "Toluca"
        }

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