from odoo import models, fields, api

class ResourceCalendar(models.Model):
    _name = 'resource.calendar'
    _inherit = 'resource.calendar'

    hours_total = fields.Integer(string='Total horas por semana', compute='_compute_total_hours_per_week')

    @api.depends('attendance_ids.hour_from', 'attendance_ids.hour_to')
    def _compute_total_hours_per_week(self):
        for calendar in self:
            total_hours = 0
            for attendance in calendar.attendance_ids:
                # Suponemos que hour_from y hour_to están en formato de 24 horas (0.0 - 24.0)
                total_hours += attendance.hour_to - attendance.hour_from
            calendar.hours_total = total_hours