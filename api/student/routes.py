from flask import Blueprint, request, make_response, jsonify

student_bp = Blueprint('student_bp', __name__, url_prefix='/api/student/')


@student_bp.route('get_cv', methods=['GET'])
def student_get_cv():
    return "get_cv"

@student_bp.route('update_cv', methods=['POST'])
def student_update_cv():
    return "update_cv"

@student_bp.route('get_all_data', methods=['GET'])
def student_get_all_data():
    return "get_all_data"


@student_bp.route('get_student_details', methods=['GET'])
def student_get_student_details():
    return "get_student_details"


@student_bp.route('update_student_details', methods=['POST'])
def student_update_student_details():
    return "update_student_details"

@student_bp.route('update_student_progress', methods=['POST'])
def student_update_student_progress():
    return "update_student_progress"

@student_bp.route('blacklist', methods=['POST'])
def student_blacklist():
    return 'blacklisted'

