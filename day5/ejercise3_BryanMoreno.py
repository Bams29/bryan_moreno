import math

def check_collision(sphere1, sphere2):
    # Calculate the distance between the centers of the spheres
    distance = math.sqrt((sphere1['center'][0] - sphere2['center'][0])**2 + (sphere1['center'][1] - sphere2['center'][1])**2 + (sphere1['center'][2] - sphere2['center'][2])**2)

    # Check if the distance is less than or equal to the sum of the radii
    if distance <= sphere1['radius'] + sphere2['radius']:
        return True
    else:
        return False

# Example usage
sphere1 = {'center': [1, 3, 6], 'radius': 2}
sphere2 = {'center': [4, 5, 6], 'radius': 1}
print(check_collision(sphere1, sphere2))  # Should print False

sphere1 = {'center': [1, 2, 3], 'radius': 1}
sphere2 = {'center': [3, 4, 5], 'radius': 1}
print(check_collision(sphere1, sphere2))  # Should print True