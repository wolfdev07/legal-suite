"""

UTILIDADES DEL PROYECTO

"""

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