from __future__ import absolute_import

from operator import itemgetter

mapping = {
    'has_header': True,
    'is_split': False,
    'bank': 'Jetstar Australia',
    'currency': 'AUD',
    'delimiter': ',',
    'account': 'Jetstar CC',
    'date': itemgetter('Transaction Date'),
    'amount': lambda tr: tr.get('Debit') or tr.get('Credit'),
    'type': lambda tr: 'DEBIT' if tr.get('Debit') else 'CREDIT',
    'payee': itemgetter('Description'),
    'notes': itemgetter('Notes'),
}
