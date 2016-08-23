from math import radians, cos, sin, asin, sqrt, pi

def closest_pair(cities_list):
    
    cities_list.sort(key=lambda tup: tup[2])
    
    closest_locations = closest_points(cities_list)
    
    closest_locations = prime_meridian(closest_locations,cities_list)

    return closest_locations
    
def prime_meridian(delta_pair,point_list):
    
    border_points1 = []
    border_points2 = []
    
    delta = delta_to_degree(delta_pair)
        
    for point in point_list:
        
        if point[2] <= -180 + delta:
        
            border_points1 += [point]
        
        else:
            
            break
        
    for point in reversed(point_list):
         
        if point[2] >= 180 - delta:
        
            border_points2 += [point]
        
        else:
            
            break
   
    min_pair = delta_pair
    
    for point1 in border_points1:
        
        point_lat = point1[1]
        
        candidate_points = [point for point in border_points2 if (point[1] >= point_lat - delta) and (point[1] <= point_lat + delta)]
        
        if candidate_points != []:
        
            min_pair = min_(calculate_closest_points(point1, candidate_points),min_pair)
            
    return min_pair
        
def closest_points(point_list):
    
    if len(point_list) > 3: 
    
        index = int(len(point_list)/2)
        
        list1 = point_list[:index]
        list2 = point_list[index:]
        
        delta_pair = min_(closest_points(list1),closest_points(list2))
        
        return min_(closest_border_points(list1,list2,delta_pair),delta_pair)
    
    
    if len(point_list) == 3:
        
        return min_(calculate_closest_points(point_list[1],[point_list[2]]),calculate_closest_points(point_list[0],point_list[1:]))
    
    else:
        
        return calculate_closest_points(point_list[0],[point_list[1]])
        
    
def closest_border_points(list1,list2,delta_pair):
    
    
    delta = delta_to_degree(delta_pair)
    
    border_long = list1[-1][2]
    
    border_points1 = []
    
    for point in reversed(list1):
            
        if point[2] >= border_long - delta:
                
            border_points1 += [point]
            
        else:
                
            break
                
    border_points2 = []
    
    for point in list2:
            
        if point[2] <= border_long + delta:
                
            border_points2 += [point]
            
        else:
                
            break           
        
    min_pair = delta_pair
   
    for point1 in border_points1:
        
        point_lat = point1[1]
        
        candidate_points = [point for point in border_points2 if (point[1] >= point_lat - delta) and (point[1] <= point_lat + delta)]
        
        if candidate_points != []:
        
            min_pair = min_(calculate_closest_points(point1, candidate_points),min_pair)
            
    return min_pair
    
def calculate_closest_points(ref_point, point_list):
    
    second_point = point_list[0]
    min_dist = distance(ref_point, second_point)
    
    
    if point_list[1:] != []:
    
        for point in point_list[1:]:
        
            dist = distance(ref_point, point)
            min_dist = min(min_dist, dist)
        
            if dist < min_dist:
                second_point = point
        
    return (min_dist,ref_point,second_point)
    

def min_(pair1, pair2):
    
    if pair1[0] > pair2[0]:
        
        return pair2
    
    else:
        
        return pair1



def distance(point1, point2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees). Code from stackoverflow.com.
    """
    lon1 = point1[2]
    lon2 = point2[2]
    lat1 = point1[1]
    lat2 = point2[1]
    
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6371 * c
    return km    
    

    
    
def delta_to_degree(delta_pair):
    
    return delta_pair[0]/(2*6371*pi/360)
    

def main():
    
    cities_list = [('A',1,45),('b',-2,12),('c',5,-7),('d',65,12),('e',55,43),('f',25,-100),('g',-5,-24),('h',-5,9),('j',-5,-179)]
    
    closest_locations = closest_pair(cities_list)
    
    print("Closest locations: " + closest_locations[1][0] + " and " + closest_locations[2][0] + ", " + str(round(closest_locations[0],1)) + "km apart." )   




main()
