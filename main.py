
import pygame
pygame.init()

from math import sin , sqrt
from musicmaker.ToneTrack import ToneTrack
from musicmaker.Tone import Tone

BPM = 150
beat = 60 / BPM

def get_x_inputs(starting_point:int , ending_point:int , interval:float):
    result_array = [starting_point]
    current_point = starting_point
    while current_point < ending_point:
        # if (current_point + interval) > ending_point and current_point != ending_point:
        #     raise ValueError
        current_point += interval
        result_array.append(current_point)

    return result_array

def get_x_inputs_with_union(first_staring_point: int , first_ending_point:int , second_starting_point:int , second_ending_point :int , interval : float):
    result_array = [first_staring_point]
    current_point = first_staring_point
    while current_point < first_ending_point:
        # if (current_point + interval) > ending_point and current_point != ending_point:
        #     raise ValueError
        current_point += interval
        result_array.append(current_point)

    result_array.append(second_starting_point)
    current_point = second_starting_point
    while current_point < second_ending_point:
        current_point += interval
        result_array.append(current_point)

    return result_array

def get_mathemathic_expression(variable_input):
    try:
        mathemathic_expression = lambda x : sin(x) #<-------------------------------------! HERE !-----------------------------------
        return mathemathic_expression(variable_input)
    except ValueError:
        print("This function took a false value")
        exit()

def mathemathic_function(inputs:list):
    return_array = []
    for input in inputs:
        return_array.append(get_mathemathic_expression(input))

    return return_array

def turn_values_into_frequencies(function_results ,  lowest_frequency = 164.81 , highest_frequency = 1318.51 ):
    new_frequency_array = []

    if lowest_frequency > highest_frequency:
        raise ValueError

    frequency_difference = highest_frequency - lowest_frequency

    highest_value = max(function_results)
    lowest_value = min(function_results)
    value_interval = highest_value - lowest_value
    if value_interval != 0:
        frequency_interval = frequency_difference / value_interval

    for result in function_results:
        if value_interval == 0:
            new_frequency = highest_frequency
        else:
            new_frequency = ((result-lowest_value)*frequency_interval) + lowest_frequency
        new_frequency_array.append(new_frequency)

    return new_frequency_array

def tonify(frequency_array , frequency_duration):
    tone_array = []
    if min(frequency_array) == max(frequency_array):
        tone = Tone(tone_frequency=min(freq_arrray) , tone_duration=5)
        tone.sine(tone.tone_frequency ,tone.tone_duration , "r" )
        exit()
    for frequency in frequency_array:
        tone = Tone(frequency ,frequency_duration)
        tone_array.append(tone)
    
    tone_track_r = ToneTrack(tone_array , "r")
    tone_track_l = ToneTrack(tone_array , "l")
    
    return [tone_track_r , tone_track_l]





freq_arrray = turn_values_into_frequencies(mathemathic_function(get_x_inputs( -5 , 5 , 0.2)))
# freq_arrray = turn_values_into_frequencies(mathemathic_function(get_x_inputs_with_union(-6.5 , -0.25 , 0.25 , 6.5 , 0.25)))

tone_tracks = tonify(freq_arrray , beat/4)
tone_tracks[0].play()


tone_tracks[0].stop()
