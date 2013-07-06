__author__ = 'vincent'

import os


class Browser:
    def docmd(self,url):
        os.system("firefox %s"%url)
