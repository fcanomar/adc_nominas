from odoo import models, fields

class Empleado(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    #_description = 'Empleado'

    years_of_service = fields.Integer(string='Años de antigüedad', compute='_compute_years_of_service')

    def _compute_years_of_service(self):
        for record in self:
            if record.first_contract_date:
                record.years_of_service = (fields.Date.today() - record.first_contract_date).days // 365
            else:
                record.years_of_service = 0

