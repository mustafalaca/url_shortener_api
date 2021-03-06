from flask import jsonify, Blueprint, request, redirect, abort
from api.controllers import *

bp = Blueprint("url_shortener", __name__)


@bp.route('/api/shorten_url', methods=['POST'])
def url_shortener():
    original_url = request.get_json()['original_url']
    shortened_url_data = url_shortener_processor(original_url)
    return jsonify({'result': shortened_url_data})  # TODO localhost:5001/short_url


@bp.route('/<short_url>', methods=['GET'])
def redirect_to_shortened_url(short_url):
    url_to_go = redirect_to_domain(short_url)
    if url_to_go:
        return redirect(url_to_go)
    return abort(400)


@bp.route('/api/list_shortened_url', methods=['GET'])
def list_of_shortened_url():
    list_of_urls = list_of_urls_processor()
    return jsonify({'result': list_of_urls})
