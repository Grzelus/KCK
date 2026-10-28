
import numpy as np
import matplotlib.pyplot as plt

def paint_map_adv(raw_matrix, norm_matrix, x, y, distance, sun_vec):
    colors = [
        (120,1,1),
        (60,1,1),
        (0,1,1)
    ]
    value = norm_matrix[y, x]
    hue, s, v = gradient(colors, value)
    
    if x < raw_matrix.shape[1] - 1 and y < raw_matrix.shape[0] - 1:
        #checking difference between neighbours
        dz_dx = raw_matrix[y, x+1] - raw_matrix[y, x]
        dz_dy = raw_matrix[y+1, x] - raw_matrix[y, x] 

        #creating reflecting vector
        vector = np.array([-dz_dx, -dz_dy, distance])
        vector = vector / np.linalg.norm(vector)

        cos_alpha = np.dot(sun_vec, vector)
        diff = cos_alpha - sun_vec[2]
        
        intensity = 2  
        if diff > 0:
            s = max(0.0, min(1.0, s - diff * intensity))
        else:
            v = max(0.0, min(1.0, v + diff * intensity))

    return hsv2rgb(hue, s, v)
        


def hsv2rgb(h: float, s: float, v: float):
    if s == 0.0:
        return (v, v, v)

    if h >= 360:
        h %= 360
    
    base_color = int(np.floor(h/60))
    color_fraction = h/60 - base_color

    p = v * (1.0 - s)
    t = v * (1.0 - (s * (1.0 - color_fraction)))
    q = v * (1.0 - s * color_fraction)

    if base_color == 0:     #(1,0,0) => (1,1,0)
        return(v,t,p)
    elif base_color == 1:   #(1,1,0) => (0,1,0)
        return(q,v,p)
    elif base_color == 2:   #(0,1,0) => (0,1,1)
        return(p,v,t)
    elif base_color == 3:   #(0,1,1) => (0,0,1)
        return(p,q,v)
    elif base_color == 4:   #(0,0,1) => (1,0,1)
        return (t,p,v)
    else:                   #(1,0,1) => (1,0,0)
        return (v,p,q)



def linear_interpolation(x1, x2, v):
    return x1 + v * (x2 - x1)


def linear_interpolation_color(colour_1, colour_2, v):
    r = linear_interpolation(colour_1[0], colour_2[0], v)
    g = linear_interpolation(colour_1[1], colour_2[1], v)
    b = linear_interpolation(colour_1[2], colour_2[2], v)
    return(r,g,b)


def gradient(colours: list[tuple[float,float,float]], v):
 
    num_of_transition = len(colours)-1
    index = min(int(np.floor(v*num_of_transition)), num_of_transition -1)
    t = v * num_of_transition - index

    colour_1 = colours[index]
    colour_2 = colours[index+1]

    return linear_interpolation_color(colour_1, colour_2, t)


with open('lab2/pliki/big.dem.txt') as file:
    width, height, distance = [int(value) for value in file.readline().split(' ')]
    distance /= 100
    matrix = np.loadtxt(file)

max_value = np.max(matrix)
min_value = np.min(matrix)

normalized_matrix = (matrix - min_value)/(max_value - min_value) 
img = np.zeros((height, width, 3))
sun = np.array([-1,-1,1])
sun = sun / np.linalg.norm(sun)

for h in range(height):
    for w in range(width):
        img[h, w] = paint_map_adv(matrix, normalized_matrix, w, h, distance, sun)
        

fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(img)
    
plt.savefig('map.pdf', bbox_inches='tight')
plt.show()
    
    
