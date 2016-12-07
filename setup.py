from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

install_requires = [
    'mockredispy'
]

tests_require = [
    'coverage',
    'pytest',
    'pytest-asyncio',
    'pytest-cov',
]

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Operating System :: POSIX',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import sys
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(name='mockaioredis',
      version='0.0.3',
      description=("Mock implementation of aioredis"),
      long_description="Mock implementation of aioredis",
      classifiers=classifiers,
      platforms=["POSIX"],
      author="Kai Blin",
      author_email="kblin@biosustain.dtu.dk",
      url="https://github.com/kblin/mockaioredis",
      license="Apache Software License",
      packages=find_packages(exclude=["tests"]),
      install_requires=install_requires,
      tests_require=tests_require,
      cmdclass={'test': PyTest},
      include_package_data=True,
      extras_require={
        'testing': tests_require,
      },
)
