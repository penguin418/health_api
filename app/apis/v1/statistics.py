from flask_restx import Namespace, Resource, fields, reqparse

from app.models import Person, VisitOccurrence

api = Namespace('Stats', '통계와 관련된 기능')

parser = reqparse.RequestParser()
parser.add_argument(
    'stat_type',
    type=str,
    required=True,
    default='sum',
    help='필수 값입니다. 통계 타입을 입력할 수 있습니다. 현재는 `sum`만 제공합니다.'
)  # 현재는 count 만 지원
parser.add_argument(
    'by',
    type=str,
    required=False,
    help='필수 값은 아닙니다, 통계의 기준을 지정할 수 있습니다.'
)

stats = api.model('stats', {
    'label': fields.String,
    'data': fields.Integer,
})

stats_list = api.model('stats_list', {
    'table': fields.String,
    'stat_type': fields.String,
    'by': fields.String,
    'data': fields.List(fields.Nested(stats)),
})


@api.route('/patients')
class PersonStats(Resource):
    @api.marshal_list_with(stats_list)
    @api.expect(parser)
    def get(self):
        """환자와 관련된 통계를 제공합니다"""
        args = parser.parse_args()
        stat_type = 'sum'
        by = args['by'] if args['by'] else 'none'
        response = {'table': Person.get_name(), 'stat_type': stat_type, 'by': by}
        if stat_type == 'sum':
            response['data'] = pack_data(PersonStats.calculate_sum[by]())
        return response

    """by 옵션과 함께 사용되는 메서드"""
    calculate_sum = {
        'none': Person.count_all_patients,
        'gender': Person.count_patients_by_gender,
        'race': Person.count_patients_by_race,
        'ethnicity': Person.count_patients_by_ethnicity,
    }


def pack_data(data):
    if len(data) == 1:
        return [{'label': 'none', 'data': data[0][0]}]
    else:
        return list(map(lambda kv: {'label': kv[0], 'data': kv[1]}, data.items()))

