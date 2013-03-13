import os

def get_template_path(input_path):
    path = os.path.join(os.path.dirname(__file__))
    path_length = path.__len__()
    final_path = path[0:path_length-7] + input_path
    return final_path
