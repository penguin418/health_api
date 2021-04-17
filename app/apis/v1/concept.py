from flask_restx import Namespace, Resource, fields, reqparse

from app.models import Person, Concept

api = Namespace('Concept', 'concept 이름을 검색하는 기능')

parser = reqparse.RequestParser()
parser.add_argument(
    'q',
    type=str,
    required=True,
    help='필수 값입니다. 검색 키워드입니다.',
)
parser.add_argument(
    'page',
    type=int,
    default=1,
    required=False,
    help='필수 값은 아닙니다. 검색 결과 중 받아볼 페이지의 번호를 지정할 수 있습니다'
)
parser.add_argument(
    'limit',
    type=int,
    default=20,
    required=False,
    help='필수 값은 아닙니다. 페이지의 최대 길이를 지정할 수 있습니다'
)

concept = api.model('concept', {
    'concept_id': fields.Integer,
    'concept_name': fields.String,
    # 'domain_id': fields.String,
    # 'vocabulary_id': fields.String,
    # 'concept_class_id': fields.String,
    # 'standard_concept': fields.String,
    # 'concept_code': fields.String,
    # 'valid_start_date': fields.Date,
    # 'valid_end_date': fields.Date,
    # 'invalid_reason': fields.String,
})

concept_result = api.model('concept_result', {
    'table': fields.String,
    'search_query': fields.String,
    'page': fields.Integer,
    'limit': fields.Integer,
    'data': fields.List(fields.Nested(concept)),
})


@api.route('/')
class SearchConceptName(Resource):
    @api.marshal_list_with(concept_result)
    @api.expect(parser)
    def get(self):
        """concept_id를 검색할 수 있습니다"""
        args = parser.parse_args()
        search_query = args['q']
        if not search_query:
            pass
        page = args['page']
        limit = args['limit']
        response = {'table': Concept.get_name(), 'search_query': search_query, 'page': page, 'limit': limit,
                    'data': (Concept.search_by_id(search_query, page, limit))}
        return response
