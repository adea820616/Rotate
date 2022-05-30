def rotate(array, angle_in_degrees):
    import itertools
    (h,w) = array.shape[:2]
    
    result=np.zeros((new_height, new_width, array.shape[2])).astype(np.uint8)
    
    angle = angle_in_degrees * math.pi / 180
    (cosine, sine) = np.cos(angle), np.sin(angle)
    rotation_matrix = [[cosine, sine], [-sine, cosine]]

    # Define the height and width of the new image that will be formed
    new_height = int(round(abs(h*cosine)+abs(w*sine)))
    new_width = int(round(abs(w*cosine)+abs(h*sine)))

    # Find the centre of the image
    original_centre_height = round(h/2)
    original_centre_width = round(w/2)

    # Find the centre of the new image
    new_centre_height = round(new_height/2)
    new_centre_width = round(new_width/2)
    
    for x,y in itertools.product(range(w), range(h)):
        
        if 0 <= new_x < w and 0 <= new_y < h:
            result[new_y, new_x, :] = pixels
            
    return result