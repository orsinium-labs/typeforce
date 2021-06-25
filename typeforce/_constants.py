from types import MappingProxyType


# https://github.com/python/mypy/blob/master/mypy/stubinfo.py
STUBS = MappingProxyType({
    'aiofiles': 'types-aiofiles',
    'atomicwrites': 'types-atomicwrites',
    'attr': 'types-attrs',
    'backports': 'types-backports',
    'backports_abc': 'types-backports_abc',
    'bleach': 'types-bleach',
    'boto': 'types-boto',
    'cachetools': 'types-cachetools',
    'certifi': 'types-certifi',
    'characteristic': 'types-characteristic',
    'chardet': 'types-chardet',
    'click_spinner': 'types-click-spinner',
    'concurrent': 'types-futures',
    'contextvars': 'types-contextvars',
    'croniter': 'types-croniter',
    'dataclasses': 'types-dataclasses',
    'dateparser': 'types-dateparser',
    'datetimerange': 'types-DateTimeRange',
    'dateutil': 'types-python-dateutil',
    'decorator': 'types-decorator',
    'deprecated': 'types-Deprecated',
    'docutils': 'types-docutils',
    'emoji': 'types-emoji',
    'enum': 'types-enum34',
    'fb303': 'types-fb303',
    'filelock': 'types-filelock',
    'first': 'types-first',
    'freezegun': 'types-freezegun',
    'frozendict': 'types-frozendict',
    'geoip2': 'types-geoip2',
    'gflags': 'types-python-gflags',
    'google.protobuf': 'types-protobuf',
    'ipaddress': 'types-ipaddress',
    'kazoo': 'types-kazoo',
    'markdown': 'types-Markdown',
    'maxminddb': 'types-maxminddb',
    'mock': 'types-mock',
    'OpenSSL': 'types-pyOpenSSL',
    'orjson': 'types-orjson',
    'paramiko': 'types-paramiko',
    'pathlib2': 'types-pathlib2',
    'pkg_resources': 'types-setuptools',
    'polib': 'types-polib',
    'pycurl': 'types-pycurl',
    'pymssql': 'types-pymssql',
    'pymysql': 'types-PyMySQL',
    'pyrfc3339': 'types-pyRFC3339',
    'python2': 'types-six',
    'pytz': 'types-pytz',
    'pyVmomi': 'types-pyvmomi',
    'redis': 'types-redis',
    'requests': 'types-requests',
    'retry': 'types-retry',
    'routes': 'types-Routes',
    'scribe': 'types-scribe',
    'simplejson': 'types-simplejson',
    'singledispatch': 'types-singledispatch',
    'six': 'types-six',
    'slugify': 'types-python-slugify',
    'tabulate': 'types-tabulate',
    'termcolor': 'types-termcolor',
    'toml': 'types-toml',
    'tornado': 'types-tornado',
    'typed_ast': 'types-typed-ast',
    'tzlocal': 'types-tzlocal',
    'ujson': 'types-ujson',
    'waitress': 'types-waitress',
    'yaml': 'types-PyYAML',

    # https://github.com/typeddjango/awesome-python-typing/#stub-packages
    'boto3': 'boto3-stubs',
    'django': 'django-stubs',
    'djangorestframework': 'djangorestframework-stubs',
    'grpc': 'grpc-stubs',
    'lxml': 'lxml-stubs',
    'matplotlib': 'data-science-types',
    'numpy': 'data-science-types',
    'ordered_set': 'ordered-set-stubs',
    'pandas': 'data-science-types',
    'pyqt5': 'PyQt5-stubs',
    'pyspark': 'pyspark-stubs',
    'pythonista': 'pythonista-stubs',
    'sqlalchemy': 'sqlalchemy-stubs',
})
