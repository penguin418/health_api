from flask_restx import Api

from app.apis.v1.concept import api as concept_api
from app.apis.v1.search import api as search_api
from app.apis.v1.statistics import api as stats_api

# version
# api
api = Api(
    title='Patients info api',
    version='1.0',
    description='Notice: Patient info api is provided based on dummy data',
    contact_email='penguin418@naver.com',
)

# namespaces
api.add_namespace(stats_api, path='/v1/stats')
api.add_namespace(concept_api, path='/v1/concepts')
api.add_namespace(search_api, path='/v1/search')
