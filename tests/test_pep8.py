import fnmatch
import unittest
import os.path
import pep8


class TestPep8(unittest.TestCase):
    """Run PEP8 on all files in this directory and subdirectories."""

    # ignore stuff in virtualenvs or version control directories
    ignore_patterns = ('.svn', 'bin', 'lib' + os.sep + 'python')


    def ignore_dir(self, dir):
      for pattern in self.ignore_patterns:
        if pattern in dir:
          return True
      return False

    def get_files_py(self):
        matches = []
        for root, dirnames, filenames in os.walk('../'):
            if self.ignore_dir(root):
                continue
            for filename in fnmatch.filter(filenames, '*.py'):
                matches.append(os.path.join(root, filename))
        return matches


    def test_pep8(self):
        matches = self.get_files_py()
        for file in matches:
            fchecker = pep8.Checker(file, show_source=False)
            fchecker.check_all()

if __name__ == '__main__':
    unittest.main()