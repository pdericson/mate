from distutils.core import setup

setup(name='mate',
      packages=['mate'],
      package_data={'mate': ['data/kubernetes-json-schema/v1.8.1-local/*.json']},
     )
