from wtforms import Form, StringField, DateField, IntegerField, validators, SelectField

class NewPromiseForm(Form):
    lessor_name = StringField(
        "Arrendador",
        [validators.Length(min=1, max=100)],
        render_kw={"class": "form-control"}
    )
    lessor_address = StringField(
        "Dirección (arrendador)",
        [validators.Length(min=1, max=500)],
        render_kw={"class": "form-control"}
    )
    amount_rent = IntegerField(
        "Importe:",
        render_kw={"class": "form-control"}
    )
    amount_rent_letter = StringField(
        "Importe con letra:",
        [validators.Length(min=1, max=50)],
        render_kw={"class": "form-control"}
    )
    tenant_name = StringField(
        "Arrendatario",
        [validators.Length(min=1, max=100)],
        render_kw={"class": "form-control"}
    )
    tenant_address = StringField(
        "Dirección (arrendatario)",
        [validators.Length(min=1, max=500)],
        render_kw={"class": "form-control"}
    )
    jointly_obligated_name = StringField(
        "Obligado Solidario Nombre:",
        [validators.Length(min=1, max=100)],
        render_kw={"class": "form-control"}
    )
    jointly_obligated_address = StringField(
        "Obligado Solidario Dirección:",
        [validators.Length(min=1, max=500)],
        render_kw={"class": "form-control"}
    )
    signature_date = DateField(
        "Fecha de Firma:",
        format='%Y-%m-%d',
        render_kw={"class": "form-control"}
    )
    date_promise = DateField(
        "Fecha de inicio:",
        format='%Y-%m-%d',
        render_kw={"class": "form-control"}
    )
    municipality = SelectField(
        "Lugar de Firma",
        choices=[
            "Toluca",
            "Metepec",
            "San Mateo Atenco",
            "Huixquilucan",
            "Nezahualcóyotl"
        ],
        render_kw={"class": "form-control"}
    )
