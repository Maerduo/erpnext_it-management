from __future__ import unicode_literals
from frappe import _


def get_data():
    return {
        'fieldname': 'location_room',
        'non_standard_fieldnames': {
            'IT Ticket': 'dynamic_name'
        },
        'transactions': [
            {
                'label': _('Configuration Items'),
                'items': ['Configuration Item']
            },
            {
                'label': _('Service'),
                'items': ['IT Ticket']
            }
        ]
    }
