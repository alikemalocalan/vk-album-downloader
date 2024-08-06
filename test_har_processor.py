import os
import unittest

from vk_downloader import process_har_file


def count_jpg_files() -> int:
    """Checks if there are 5 JPG files in the current directory's 'photos' folder."""
    photo_folder = "photos"
    jpg_count: int = 0

    # Check if the 'photos' folder exists
    if os.path.isdir(photo_folder):
        for filename in os.listdir(photo_folder):
            # Check if the file is a JPG file
            if filename.lower().endswith(".jpg"):
                jpg_count += 1

    return jpg_count


class TestHARProcessing(unittest.TestCase):

    def test_process_har_file_parses_file(self):
        har_file_path = "test.har"

        with open(har_file_path, 'r'):
            pass

        process_har_file(har_file_path)

        self.assertEqual(count_jpg_files(), 5)


if __name__ == '__main__':
    unittest.main()
