from flask import Blueprint, request, make_response, jsonify

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/api/admin/')


# API for get and post data student about a single or multiple students

@admin_bp.route('get_all_students_data/', methods=['GET'])
def admin_get_all_students_data():
    return "get_all_students_data"

@admin_bp.route('get_student_data/<student_name/', methods=['GET'])
def admin_get_student_data(student_name):
    return "get_student_data"

@admin_bp.route('update_student_data/<student_name>/', methods=['POST'])
def admin_update_students_data(student_name):
    return "update_students_data"

# API for get and post data student about a single or multiple professor

@admin_bp.route('get_all_professors_data/', methods=['GET'])
def admin_get_all_professors_data():
    return "get_professor_data"

@admin_bp.route('get_professor_data/<professor_name>', methods=['GET'])
def admin_get_professor_data(professor_name):
    return "get_professor_data"

@admin_bp.route('update_professor_data/<professor_name>/', methods=['POST'])
def admin_update_professors_data(student_name):
    return "update_professors_data"

# API for get and post data related to admin
@admin_bp.route('get_admin_details', methods=['GET'])
def admin_get_admin_details():
    return "get_admin_details"


@admin_bp.route('update_admin_details/', methods=['POST'])
def admin_update_admin_details():
    return "update_admin_details"


# Blacklist students and professors
@admin_bp.route('blacklist_student/<student_name>/', methods=['POST'])
def admin_get_cv(student_name):
    return 'blacklisted %s' %student_name

@admin_bp.route('blacklist_professor/<professor_name>/', methods=['POST'])
def admin_get_cv(professor_name):
    return 'blacklisted %s' %professor_name