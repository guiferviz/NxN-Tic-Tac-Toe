
"""Python implementation of Tic-Tac-Toe with boards of any size.

Author: guiferviz
GitHub: https://github.com/guiferviz/NxN-Tic-Tac-Toe
"""


from setuptools import setup

from nxntictactoe import __version__


setup(name='nxntictactoe',
      version=__version__,
      description='Python implementation of Tic-Tac-Toe with boards of any size.',
      long_description=open('README.md').read(),
      keywords='tic tac toe tic-tac-toe game play',
      url='https://github.com/guiferviz/NxN-Tic-Tac-Toe',
      author='guiferviz',
      author_email='guiferviz@gmail.com',
      license='MIT',
      packages=['nxntictactoe'])
