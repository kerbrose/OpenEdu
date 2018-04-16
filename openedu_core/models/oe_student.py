# -*- coding: utf-8 -*-
###############################################################################
#
#    Core≡BPO Pvt. Ltd.
#    Copyright (C) 2009-TODAY Core≡BPO(<http://www.http://core-bpo.com/>).
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import Warning, ValidationError


class OeStudent(models.Model):
    _name = 'oe.student'
    _inherits = {'res.partner': 'partner_id'}

    birth_date = fields.Date('Birth Date')

    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string = 'Blood Group'
    )

    emergency_contact = fields.Many2one(
        'res.partner', 'Emergency Contact')

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        'Gender')
    
    id_number = fields.Char('ID Card Number', size=64)
    
    nationality = fields.Many2one('res.country', 'Nationality')

    partner_id = fields.Many2one(
        'res.partner', 'Partner', required=True, ondelete="restrict")
    
    #student_ids = fields.Many2many('op.student', string='Student(s)')

    @api.multi
    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    'Birth Date cannot be greater than the current date!'))