# -*- coding: utf-8 -*-
###############################################################################
#
#    Core≡BPO Pvt. Ltd.
#    Copyright (C) 2009-TODAY Core≡BPO(<http://www.http://core-bpo.com/>).
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class OeStage(models.Model):
    _name = 'oe.stage'

    name = fields.Char('Stage')

    
    