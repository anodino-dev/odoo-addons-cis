# -*- encoding: utf-8 -*-
##############################################################################
#
#    Fiscal Company for Account Module for Odoo
#    Copyright (C) 2013-2014 GRAP (http://www.grap.coop)
#    @author Julien WESTE
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

from openerp.osv.orm import Model
from account_fiscal_company.account_parameters \
    import propagate_properties_to_fiscal_childs


class product_category(Model):
    _inherit = 'product.category'

    _PRODUCT_CATEGORY_FISCAL_PROPERTY_LIST = [
        'property_account_income_categ',
        'property_account_expense_categ',
    ]

    # Custom Function
    def _propagate_properties_to_fiscal_childs(
            self, cr, uid, ids, vals, creation, context=None):
        current_company = self.pool.get('res.users').browse(
            cr, uid, uid, context=context).company_id

        if current_company.fiscal_type in ('fiscal_child', 'fiscal_mother'):
            for property_name in self._PRODUCT_CATEGORY_FISCAL_PROPERTY_LIST:
                if (property_name in vals):
                    propagate_properties_to_fiscal_childs(
                        self.pool, cr, uid, ids,
                        current_company.fiscal_company.id,
                        'product.category',
                        property_name,
                        vals[property_name],
                        context=context)

    # Overwrite Section
    def create(self, cr, uid, vals, context=None):
        category_id = super(product_category, self).create(
            cr, uid, vals, context=context)
        self._propagate_properties_to_fiscal_childs(
            cr, uid, [category_id], vals, True, context=context)
        return category_id

    def write(self, cr, uid, ids, vals, context=None):
        res = super(product_category, self).write(
            cr, uid, ids, vals, context=context)
        self._propagate_properties_to_fiscal_childs(
            cr, uid, ids, vals, False, context=context)
        return res
