from setuptools import setup
import sdist_upip


setup(name='picoweb',
      version='1.5.2',
      description="A very lightweight, memory-efficient async web framework \
for MicroPython and its uasyncio module.",
      long_description=open('README.rst').read(),
      url='https://github.com/pfalcon/picoweb',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      packages=['picoweb'],
      # Note: no explicit dependency on 'utemplate', if a specific app uses
      # templates, it must depend on it. Likewise, don't depend on
      # micropython-ulogging as application might not use logging.
      install_requires=['micropython-uasyncio', 'micropython-pkg_resources'])
