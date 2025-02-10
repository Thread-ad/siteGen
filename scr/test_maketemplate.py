import unittest

from title import *


class TeastMakeTemplate(unittest.TestCase):

    def test_Template(self):

        generate_page("/root/workspace/github.com/Thread-ad/siteGen/static/content/index.md", "/root/workspace/github.com/Thread-ad/siteGen/template.html", "/root/workspace/github.com/Thread-ad/siteGen/public/")

        



if __name__ == "__main__":
    unittest.main()