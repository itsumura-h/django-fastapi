import os
from orator import DatabaseManager

config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': os.environ.get('DB_PATH'),
        'foreign_keys': True
    }
}

db = DatabaseManager(config)
