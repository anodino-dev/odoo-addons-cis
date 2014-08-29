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
from account_fiscal_company.account_parameters\
    import propagate_properties_to_fiscal_childs


class product_product(Model):
    _inherit = 'product.product'

    _PRODUCT_PRODUCT_FISCAL_PROPERTY_LIST = [
        'property_account_expense',
        'property_account_income',
    ]

    # Custom Function
    def _propagate_properties_to_fiscal_childs(
            self, cr, uid, ids, vals, creation, context=None):
        for property_name in self._PRODUCT_PRODUCT_FISCAL_PROPERTY_LIST:
            if (property_name in vals):
                for product in self.browse(cr, uid, ids, context=context):
                    if product.company_id.fiscal_type == 'fiscal_mother':
                        propagate_properties_to_fiscal_childs(
                            self.pool, cr, uid,
                            [product.product_tmpl_id.id],
                            product.company_id.id,
                            'product.template',
                            property_name,
                            vals[property_name],
                            context=context)

        # reset all property if the new company is a fiscal company
        if ('company_id' in vals) and not creation:
            for product in self.browse(cr, uid, ids, context=context):
                if product.company_id.fiscal_type == 'fiscal_mother':
                    domain = [
                        ('res_id', '=', '%s,%s' % (
                            'product.template', product.product_tmpl_id.id)),
                        ('name', 'in', (
                            'property_account_expense',
                            'property_account_income'))]
                    ip_ids = self.pool.get('ir.property').search(
                        cr, uid, domain, context=context)
                    self.pool.get('ir.property').unlink(
                        cr, uid, ip_ids, context=context)

    # Overwrite Section
    def create(self, cr, uid, vals, context=None):
        product_id = super(product_product, self).create(
            cr, uid, vals, context=context)
        self._propagate_properties_to_fiscal_childs(
            cr, uid, [product_id], vals, True, context=context)
        return product_id

    def write(self, cr, uid, ids, vals, context=None):
        res = super(product_product, self).write(
            cr, uid, ids, vals, context=context)
        self._propagate_properties_to_fiscal_childs(
            cr, uid, ids, vals, False, context=context)
        return res
