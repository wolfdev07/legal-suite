import datetime

def humanize_date(date):
    months = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    day = date.day
    month = months[date.month - 1]
    year = date.year
    return f"{day} de {month} de {year}"

# Ejemplo de uso
#fecha = datetime.date(2024, 7, 5)
#fecha_humanizada = humanizar_fecha(fecha)
#print(fecha_humanizada)  #

def formatear_numero(num):
    # Convertir el número a cadena con formato de puntos decimales mexicanos
    num_str = "{:,.2f}".format(num)
    return num_str

# Ejemplo de uso
print(formatear_numero(1000000))       # Salida: 5,000.00
