from odoo import models, fields

class Empleado(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    #_description = 'Empleado'

    years_of_service = fields.Integer(string='Años de antigüedad')