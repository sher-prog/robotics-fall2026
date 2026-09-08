import math

def front_distance(ranges, angle_min, angle_increment, half_width_radians):
    valid_distances = []
    for index, distance in enumerate(ranges):
        angle = angle_min + index * angle_increment
        if abs(angle) <= half_width_radians and math.isfinite(distance) and distance > 0:
            valid_distances.append(distance)
            
    if not valid_distances:
        return None
    return min(valid_distances)

def decide_velocity(distance, stop_distance, forward_speed):
    if distance is None or distance <= stop_distance:
        return 0.0
    else:
        return max(0.0, min(float(forward_speed), 0.18))