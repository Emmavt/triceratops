from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name = "triceratops",
      version = '1.0.8',
      description = "Statistical Validation of TESS Objects of Interest",
      long_description = readme(),
      author = "Steven Giacalone",
      author_email = "steven_giacalone@berkeley.edu",
      url = "https://github.com/stevengiacalone/triceratops",
      packages = find_packages(),
      package_data = {'triceratops': ['data/*']},
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
   	'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Astronomy'
        ],
      install_requires=['numpy>=1.18.1','pandas>=0.23.4', 'scipy>=1.1.0', 'matplotlib>=3.0.3',
                        'astropy>=4.0', 'astroquery>=0.4', 'pytransit>=2.2',
                        'mechanicalsoup>=0.12.0', 'emcee>=3.0.2', 'seaborn>=0.11.1',
                        'numba>=0.52.0', 'pyrr>=0.10.3'],
      zip_safe=False
)
