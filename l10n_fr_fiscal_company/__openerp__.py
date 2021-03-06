# -*- encoding: utf-8 -*-
##############################################################################
#
#    Fiscal Company for l10n_fr Module for Odoo
#    Copyright (C) 2015 GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'CIS - l10n_fr Fiscal Company',
    'version': '1.1',
    'category': 'CIS',
    'summary': 'Glue Module between CIS and l10n_fr',
    'description': """
Glue Module between CIS and l10n_fr
===================================

Features :
----------
    * Manage SIRET during the creation of a new company;

Copyright, Author and Licence :
-------------------------------
    * Copyright : 2015-Today, Groupement Régional Alimentaire de Proximité;
    * Author :
        * Sylvain LE GAL (https://twitter.com/legalsylvain);
    * Licence : AGPL-3 (http://www.gnu.org/licenses/)
    """,
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'base_fiscal_company',
        'l10n_fr',
    ],
    'auto_install': True,
    'data': [
        'view/view.xml',
    ]

}
