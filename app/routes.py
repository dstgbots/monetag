from flask import Blueprint, jsonify, request
from app.services import MonetagService
from app.utils import validate_date_range

api_bp = Blueprint('api', __name__)
monetag_service = MonetagService()

@api_bp.route('/create')
def create():
    try:
        result = monetag_service.create_zone()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/check')
def check():
    try:
        date_range = request.args.get('date', 'total')
        if not validate_date_range(date_range):
            return jsonify({"error": "Invalid date range"}), 400
            
        result = monetag_service.get_stats(date_range)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

