#-*- coding:utf-8 -*-

import MySQLdb

class AutoCloseCursorConnection(object):

    def __init__(self, conn):
        super(AutoCloseCursorConnection,self).__init__()
        self.conn = conn

    def __getattr__(self, key):
        return getattr(self.conn, key)

    def cursor(self, *args, **kwargs):
        self.cursor = self.conn.cursor(*args, **kwargs)
        return self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()
        self.conn.close()