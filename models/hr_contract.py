from odoo import models, fields, api

class Contract(models.Model):
    _name = 'hr.contract'
    _inherit = 'hr.contract'

    wage_per_hour = fields.Float(string='Salario por hora', compute='_compute_wage_per_hour', digits=(16, 3))

    @api.depends('wage','resource_calendar_id.hours_total')
    def _compute_wage_per_hour(self):
        for contract in self:
            contract.wage_per_hour = round(contract.wage/contract.resource_calendar_id.hours_total/4.33,3)

    prime_de_poste = fields.Integer(string='Prima de puesto')
    prime_velo = fields.Integer(string='Prima bicicleta')
    transport_omit = fields.Boolean(string='Subsidio de transporte OMIT')