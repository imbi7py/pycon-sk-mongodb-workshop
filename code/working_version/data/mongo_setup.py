import mongoengine


def global_init(db_name: str):
    mongoengine.register_connection(alias='core', name=db_name)
    # mongoengine.register_connection(alias='analytics', name='pypi_history')
