import connexion
import logging
from flask.ext.cors import CORS
from data.data_source import FTMDataSource

data_source = FTMDataSource()


def start_server():
    logging.basicConfig(level=logging.INFO)
    app = connexion.App(__name__, port=8080, specification_dir='swagger/', server='gevent')
    app.add_api('ftm_service.yaml')
    app.debug = True
    CORS(app.app)
    app.run()
    data_source.close()


if __name__ == '__main__':
    start_server()
