import unittest

from title import extract_title


class TeastFirstHeader(unittest.TestCase):

    def test_header(self):

        text = '''# This is title
        
        ## This is second title
        
        ### This is third title'''

        self.assertEqual(
            "This is title",
            extract_title("/root/workspace/github.com/Thread-ad/siteGen/scr/text.md")
        )

        



if __name__ == "__main__":
    unittest.main()