from setuptools import setup, find_packages

setup(
    name='django_admin_chart',
    version='1.0.2',
    description='django admin chart',
    long_description='django admin chart',
    author='ReimiBeta',
    author_email='reimi846@gmail.com',
    url='https://github.com/reimibeta/django_admin_chart',
    license='MIT',
    packages=find_packages(),
    # py_modules=['image_compress',],
    install_requires=[
        # other dependencies
        'Django==4.1.7'
    ],
    package_data={
        'django_admin_chart': [
            'templates/django_admin_chart/*.html',
            'templates/django_admin_chart/widgets/*.html',
            'templates/django_admin_chart/components/*.html',
        ]
    }
    # other optional arguments
)
