"""

UTILIDADES DEL PROYECTO

"""
import os
from spire.doc import *
from spire.doc.common import *
import PyPDF2


def humanize_date(date):
    months = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    day = date.day
    month = months[date.month - 1]
    year = date.year
    return f"{day} de {month} de {year}"


def formatear_numero(num):
    # Convertir el número a cadena con formato de puntos decimales mexicanos
    num_str = "{:,.2f}".format(num)
    return num_str


def docx_to_pdf_convert(path_docx, path_save):
    #CONVIERTE UN DOCUMENTO DOCX EN PDF
    document_docx=Document()
    document_docx.load_from_file(path_docx)
    document_docx.save_to_file(path_save, FileFormat.PDF)
    document_docx.close()



def create_onlyone_pdf_file(path_files, path_save):
    # UNIR LOS PDF EN UN SOLO ARCHIVO
    convinator = PyPDF2.PdfMerger()

    for file_name in os.listdir(path_files):
        if file_name.endswith(".pdf"):
            convinator.append(os.path.join(path_files, file_name))

    convinator.write(path_save)
    convinator.close()
