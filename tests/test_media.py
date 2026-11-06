import unittest

from mke.media import is_supported_media


class TestMedia(unittest.TestCase):

    def test_supported_video(self):
        self.assertTrue(is_supported_media("lecture.mp4"))

    def test_supported_audio(self):
        self.assertTrue(is_supported_media("interview.mp3"))

    def test_unsupported_file(self):
        self.assertFalse(is_supported_media("notes.pdf"))

    def test_uppercase_extension(self):
        self.assertTrue(is_supported_media("VIDEO.MP4"))


if __name__ == "__main__":
    unittest.main()