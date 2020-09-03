from flask import Blueprint, request, make_response, jsonify

professor_bp = Blueprint('professor_bp', __name__, url_prefix='/api/professor/')


@professor_bp.route('get_requirements', methods=['GET'])
def professor_get_requirements():
    return "get_requirements"

@professor_bp.route('update_requirements', methods=['POST'])
def professor_update_requirements():
    return "update_requirements"

@professor_bp.route('get_recommends', methods=['GET'])
def professor_get_recommends():
    return "get_recommends"

@professor_bp.route('update_recommends', methods=['POST'])
def professor_update_recommends():
    return "update_recommends"

@professor_bp.route('get_professor_details', methods=['GET'])
def professor_get_professor_details():
    return "get_professor_details"


@professor_bp.route('update_professor_details', methods=['POST'])
def professor_update_professor_details():
    return "update_professor_details"


@professor_bp.route('blacklist', methods=['POST'])
def professor_get_cv():
    return 'blacklisted'
