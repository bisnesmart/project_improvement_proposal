# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "improvement Proposal",
    "version": "1.0",
    "author": "bisnesmart",
    "category": "Generic Modules/Projects & Services",
    "website": "http://www.bisnesmart.com",
    "license": 'AGPL-3',
    "depends": [
        "project",
    ],
    "data": [
        "report/report_improvement_proposal.xml",
        "views/task_view.xml",
        "edi/project_task_improvement_proposal.xml",

    ],
    'installable': True
}
