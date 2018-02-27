from google.appengine.ext import ndb

class Tick(ndb.Expando):
    last = ndb.StringProperty()

    @classmethod
    def find_previous(cls):
        return ndb.Key(cls, 'current').get()

    @classmethod
    def update_current(cls, tick):
        return cls(id = 'current', **tick).put()
