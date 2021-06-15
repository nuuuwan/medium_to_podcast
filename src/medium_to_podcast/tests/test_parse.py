"""Test."""
import unittest
import os

from utils import www

from medium_to_podcast import parse

TEST_HTML_URL = os.path.join(
    'https://raw.githubusercontent.com/nuuuwan/medium/main/posts/',
    '2021-03-15_Heaven-on-Earth-6a68b69c149a.html',
)


class TestParse(unittest.TestCase):
    """Tests."""

    def test_parse(self):
        """Test."""
        data = parse.parse(TEST_HTML_URL)
        self.assertEqual(
            data['title'],
            'Heaven on Earth',
        )
        self.assertEqual(
            data['subtitle'],
            'On freedom from Chocolate and Mosquitos',
        )
        self.assertEqual(len(data['paragraphs']), 17)


if __name__ == '__main__':
    unittest.main()
