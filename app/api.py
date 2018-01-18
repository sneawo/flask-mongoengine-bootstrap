import structlog

from flask import Blueprint, jsonify, request, g
from .models import RequestLog

logger = structlog.get_logger(__name__)
api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        logger.info('create')
        request_log = RequestLog(request_id=g.request_id, headers=dict(request.headers.items()))
        request_log.save()
        return jsonify(request=request_log)

    return jsonify(requests=RequestLog.objects.all()[:10])
