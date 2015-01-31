#!/usr/bin/env python

"""
Make dummy data and fixtures and stuff.
"""

from pynsot import client
try:
    import faker
except ImportError:
    print "The 'fake-factory' module is required! (Hint: pip install fake-factory)"
    raise


fake = faker.Factory.create()


def generate_site_data(num_items=100):
    """
    Return a list of dicts of {name: description}.

    :param num_items:
        Number of items to generate
    """
    names = set()
    while len(names) < num_items:
        names.add(fake.word().title())
    data = []
    for name in names:
        description = ' '.join(fake.words()).capitalize()
        item = {'name': name, 'description': description}
        data.append(item)
    return data


def populate_sites(site_data):
    """Populate sites from fixture data."""
    api = client.Client('http://localhost:8990/api', email='jathan@localhost')
    results = []
    for d in site_data:
        try:
            result = api.sites.post(d)
        except Exception as err:
            print err, d['name']
        else:
            results.append(result)
    print 'Created', len(results), 'sites.'
