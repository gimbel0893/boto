class ReservedDBInstance(dict):

    def __setattr__(self, attr, value):
        self[attr] = value

    def startElement(self, name, attrs, connection):
        pass

    def endElement(self, name, value, connection):
        setattr(self, name, value)
