class Category:

    def __init__(self, id_category, name, limit):
        self.id = id_category
        self.name = name
        self.limit = limit

    def __repr__(self):
        attrs = [
            ('id', self.id),
            ('name', self.name),
            ('user_limit', self.limit)
        ]
        return '<%s %s>' % (self.__class__.__name__, ' '.join('%s=%r' % t for t in attrs))


class CountUsers:

    def __init__(self, id_channel, count, limit):
        self.id = id_channel
        self.count = count
        self.limit = limit
        self.vacancy = limit-count

    def __repr__(self):
        attrs = [
            ('id', self.id),
            ('count', self.count),
            ('user_limit', self.limit),
            ('vacancy', self.vacancy)
        ]
        return '<%s %s>' % (self.__class__.__name__, ' '.join('%s=%r' % t for t in attrs))
