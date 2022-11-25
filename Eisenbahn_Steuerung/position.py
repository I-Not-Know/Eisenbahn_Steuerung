from server import get_position_from_pc

def get_start_end():
    vec_start_end = get_position_from_pc()

    return vec_start_end[0], vec_start_end[1]
