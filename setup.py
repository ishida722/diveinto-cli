from setuptools import setup

setup(name='diveinto-cli',
      version='0.0.1',
      url='https://github.com/paragraph14/diveinto-cli',
      description='Task manager',
      author='chu',
      author_email='they.know.who.is.the.strongest@gmail.com',
      license='MIT',
      packages=['diveinto_cli'],
      test_suite='tests',
      entry_points="""
      [console_scripts]
      diveinto = diveinto_cli.cli:Main
      """,
      )
