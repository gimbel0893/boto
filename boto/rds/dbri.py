import datetime


class RecurringCharge(object):

    def __init__(self, recurring_charge_amount=None,
                 recurring_charge_frequency=None):
        self.recurring_charge_amount = recurring_charge_amount
        self.recurring_charge_frequency = recurring_charge_frequency

class ReservedDBInstance(object):

    ATTR_MAP = {
        'ReservedDBInstanceId': ('id', str),
        'CurrencyCode': ('currency_code', str),
        'DBInstanceClass': ('db_instance_class', str),
        'DBInstanceCount': ('db_instance_count', int),
        'Duration': ('duration', int),
        'FixedPrice': ('fixed_price', float),
        'MultiAZ': ('multi_az', bool),
        'OfferingType': ('offering_type', str),
        'ProductDescription': ('product_description', str),
        'ReservedDBInstancesOfferingId': ('reserved_db_instances_offering_id',
                                          str),
        'StartTime': ('start_time',
         lambda v: datetime.datetime.strptime(v[:-5], '%Y-%m-%dT%H:%M:%S')),
        'State': ('state', str),
        'UsagePrice': ('usage_price', float),
    }

    def __init__(self, connection=None, id=None):
        self.connection = connection
        self.id = id
        self._extra = {}

    def __repr__(self):
        repr = ''
        for var in vars(self):
            attr = getattr(self, var)
            repr += "{}={} [{}]\n".format(var, attr, str(type(attr)))
        return repr

    def startElement(self, name, attrs, connection): pass

    def endElement(self, name, value, connection):
        if name == 'RecurringCharges':
            self.recurring_charges = []
            for charge in value:
                r = RecurringCharge(charge['RecurringChargeAmount'],
                                    charge['RecurringChargeFrequency'])
                self.recurring_charges.append(r)
        elif name in self.ATTR_MAP:
            name, _type = self.ATTR_MAP[name]
            value = _type(value)
            setattr(self, name, value)
        else:
            self._extra[name] = value
