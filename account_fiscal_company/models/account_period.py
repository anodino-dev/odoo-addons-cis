# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author:
#    Julien WESTE
#    Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp.osv.orm import Model
from openerp.addons.account_fiscal_company.decorator import \
    switch_company_period


class account_period(Model):
    _inherit = 'account.period'

    @switch_company_period
    def find(self, cr, uid, dt=None, context=None):
        return super(account_period, self).find(
            cr, uid, dt=dt, context=context)
