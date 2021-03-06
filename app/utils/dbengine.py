import json
from sqlalchemy import create_engine
import psycopg2

def config_setup():
    """
    Read config.json and create dictionary with the json data
    """
    configurationFileName = '.\\config.json'

    try:
        with open(configurationFileName, encoding='utf-8') as config_file:
            config = json.load(config_file)
            # print("Configuration file:'" + os.path.realpath(config_file.name) + "' loaded successfully.")
    except:
        print('Error processing configuration file: ' + configurationFileName + '. Exiting.')
        exit(-1)

    return config

def engine_setup():
    """
    Create connection with database
    """
    config = config_setup()
    engine = create_engine(
        'postgresql+psycopg2://' + config['username'] + ':' + config['password'] +
        '@' + config['servername'] + ":" + str(config["port"]) + '/postgres')

    return engine
