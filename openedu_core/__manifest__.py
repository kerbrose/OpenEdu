# -*- coding: utf-8 -*-
{
    'name': 'OpenEdu Core',
    'author': 'Core BPO',
    'website': 'https://www.core-bpo.com',
    'category': 'Education',
    'description': """
OpenEdu Core:
====================
This module include the definition of third party partners that will be in an educational instituion.

    """,
    'depends': [
                'partner_second_lastname', # Found in https://github.com/OCA/partner-contact
    ],
    'data': [
             'security/openedu_groups.xml',
             'security/ir.model.access.csv',
             'views/openedu_core_views.xml',
             'views/oe_parent.xml',  
    ],
}
