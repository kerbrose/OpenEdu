# -*- coding: utf-8 -*-
###############################################################################
#
#    Core≡BPO Pvt. Ltd.
#    Copyright (C) 2009-TODAY Core≡BPO(<http://www.http://core-bpo.com/>).
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class OeParent(models.Model):
    _name = 'oe.parent'

    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', 'Partner', required=True, ondelete="restrict")
    
    #student_ids = fields.Many2many('op.student', string='Student(s)')
    
    
    @api.model
    def create(self, vals):
        if vals.get('company_type', 'person') == 'person':
            vals['company_type'] = 'person'
        return super(OeParent, self).create(vals)