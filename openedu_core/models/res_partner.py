# -*- coding: utf-8 -*-
###############################################################################
#
#    Core≡BPO Pvt. Ltd.
#    Copyright (C) 2009-TODAY Core≡BPO(<http://www.http://core-bpo.com/>).
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_faculty = fields.Boolean('Faculty')

    is_parent = fields.Boolean('Parent')

    is_student = fields.Boolean('Student')
    
    