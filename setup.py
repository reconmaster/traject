from setuptools import setup, find_packages

setup(name='traject',
      version='1.0.0',
      packages=find_packages(),

      # install_requires=['matplotlib>=1.5'],

      # entry_points={
      #     'console_scripts': [
      #         'traject = traject.ui:shell_main',
      #     ],
      # },

      # supposedly installs git controlled files
      include_package_data=True,
      # package_data={
      #     # Include any *.ini files in the packages
      #     '': ['*.ini'],
      # },

      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False,

      # metadata (say if going to PyPI)
      description='developer mode trajectory generation',
      url='https://github.com/reconmaster/traject',
      author='Andrew M. Davis')
