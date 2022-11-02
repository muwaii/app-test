from odoo import models, fields

class AppTest(models.Model): 
    _name = "app_test.my_table"
    _description = 'app_test.my_table description'

    name = fields.Char(string="The Name", required=True)
    age = fields.Integer()








# from odoo import models, fields, api


# class app_test(models.Model):
#     _name = 'app_test.app_test'
#     _description = 'app_test.app_test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
