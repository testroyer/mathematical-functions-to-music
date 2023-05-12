import musicmaker

BPM = 150
beat = 60 / 150

def get_x_inputs(starting_point:int , ending_point:int , interval:float):
    result_array = [starting_point]
    current_point = starting_point
    while current_point < ending_point:
        if (current_point + interval) > ending_point:
            return "Error"
        current_point += interval
        result_array.append(current_point)

    return result_array

def get_mathemathic_expression(variable_input):
    mathemathic_expression = lambda x : x**3
    return mathemathic_expression(variable_input)

def mathemathic_function(inputs):
    return_array = []
    for input in inputs:
        return_array.append(get_mathemathic_expression(input))

    return return_array

def turn_values_into_frequencies():
    lowest_note = 82.41



print(mathemathic_function(get_x_inputs(-10 , 10 , 1)))
