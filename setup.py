from setuptools import setup


def _md(filename):
    '''
    Load md file and sanitize it for PyPI.
    Remove unsupported github tags:
     - code-block directive
     - all badges
    '''
    content = open(filename).read()
    return content


long_description = '\n'.join((
    _md('README.md'),
    _md('CHANGELOG.md'),
    ''
))

exec(compile(
    open('devpi_semantic_ui/__about__.py').read(),
    'devpi_semantic_ui/__about__.py',
    'exec'
))

setup(
    name="devpi-semantic-ui",
    description=__description__,
    url="https://github.com/apihackers/devpi-semantic-ui",
    version=__version__,
    maintainer="API Hackers",
    maintainer_email="github@apihackers.com",
    license="MIT",
    entry_points={
        'devpi_server': [
            "devpi-semantic-ui = devpi_semantic_ui"
        ]
    },
    install_requires=['devpi-web'],
    include_package_data=True,
    zip_safe=False,
    packages=['devpi_semantic_ui'],
    keywords='devpi semantic-ui',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ],
)
