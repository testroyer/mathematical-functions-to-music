#initial commit

def get_x_inputs(starting_point:int , ending_point:int , interval:float):
    result_array = [starting_point]
    current_point = starting_point
    while current_point < ending_point:
        if (current_point + interval) > ending_point:
            return "Error"
        current_point += interval
        result_array.append(current_point)

    return result_array
        

print(get_x_inputs(10 , 15 , 0.5)) 