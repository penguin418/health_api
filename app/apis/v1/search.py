from flask_restx import Namespace, Resource, fields, reqparse

from app.models import ConditionOccurrence

api = Namespace('Search', '검색 기능 제공')

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

condition_occurrence = api.model('condition_occurrence', {
    'condition_occurrence_id': fields.Integer,
    'person_id': fields.Integer,
    'condition_concept_name': fields.String,
    'condition_start_date': fields.String,
    'condition_start_datetime': fields.String,
    'condition_end_date': fields.String,
    'condition_end_datetime': fields.String,
    'condition_type_concept_id': fields.String,
    'condition_status_concept_id': fields.String,
    'stop_reason': fields.String,
    'provider_id': fields.Integer,
    'visit_occurrence_id': fields.Integer,
    'visit_detail_id': fields.Integer,
    'condition_source_value': fields.String,
    'condition_source_concept_id': fields.String,
    'condition_status_source_value': fields.String,
})

condition_occurrence_result = api.model('condition_occurrence_result', {
    'table': fields.String,
    'search_query': fields.String,
    'page': fields.Integer,
    'limit': fields.Integer,
    'data': fields.List(fields.Nested(condition_occurrence)),
})


@api.route('/condition_occurrence')
class SearchConditionOccurrence(Resource):
    @api.marshal_list_with(condition_occurrence_result)
    @api.expect(parser)
    def get(self):
        """conditionOccurrence를 검색합니다"""
        args = parser.parse_args()
        search_query = args['q']
        if not search_query:
            pass
        page = args['page']
        limit = args['limit']
        response = {'table': ConditionOccurrence.get_name(), 'search_query': search_query, 'page': page, 'limit': limit,
                    'data': (ConditionOccurrence.search(search_query, page, limit))}
        return response

