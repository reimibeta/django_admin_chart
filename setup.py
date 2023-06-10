from setuptools import setup, find_packages

setup(
    name='django_admin_chart',
    version='1.0.0',
    description='django admin chart',
    long_description='django admin chart',
    author='ReimiBeta',
    author_email='reimi846@gmail.com',
    url='https://github.com/reimibeta/django_html_render',
    license='MIT',
    packages=find_packages(),
    # py_modules=['image_compress',],
    install_requires=[
        # other dependencies
        'Django==4.1.7'
    ],
    package_data={
        'django_admin_chart': [
            # 'templates/*.html',
            # 'templates/components/*.html',
            # 'templates/widgets/*.html'
            'templates'
        ]
    }
    # other optional arguments
)
