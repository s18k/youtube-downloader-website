from setuptools import setup

setup(
    name='youtube downloader website',
    packages=['youtube downloader website'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pytube',
    ],
	package_dir={"": "youtube downloader website"},
    packages=setuptools.find_packages(where="youtube downloader website"),
)