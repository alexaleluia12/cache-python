from marshmallow import Schema, fields


# como adiconar custon validation
# value deve ser maior que 100
#  2 < name < 150 chars
class PaymentSchema(Schema):
    name = fields.Str()
    date = fields.DateTime()
    value = fields.Float()
