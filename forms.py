from wtforms import Form, BooleanField, StringField, DateField, IntegerField, validators, SelectField


class NewPromiseForm(Form):

    lessor_name = StringField("Arrendador", [validators.Length(min=1, max=100)])
    lessor_address = StringField("Dirección (arrendador)", [validators.Length(min=1, max=500)])
    amount_rent = IntegerField("Importe:")
    amount_rent_letter = StringField("Importe con letra:", [validators.Length(min=1, max=50)])
    tenant_name = StringField("Arrendatario", [validators.Length(min=1, max=100)])
    tenant_address = StringField("Dirección (arrendatario)", [validators.Length(min=1, max=500)])
    jointly_obligated_name = StringField("Obligado Solidario Nombre:", [validators.Length(min=1, max=100)])
    jointly_obligated_address = StringField("Obligado Solidario Dirección:", [validators.Length(min=1, max=500)])
    signature_date = DateField("Fecha de Firma:", format='%Y-%m-%d')
    date_promise = DateField("Fecha de inicio:", format='%Y-%m-%d')
    municipality = SelectField("Lugar de Firma", choices=["Toluca", "Metepec", "San Mateo Atenco", "Huixquilucan", "Nezahualcóyotl"])
