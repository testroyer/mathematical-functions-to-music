import pygame
pygame.init()

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

def get_mathemathic_expression(variable_input):
    mathemathic_expression = lambda x : 1
    return mathemathic_expression(variable_input)

def mathemathic_function(inputs):
    return_array = []
    for input in inputs:
        return_array.append(get_mathemathic_expression(input))

    return return_array

def turn_values_into_frequencies(function_results ,  lowest_frequency = 82.41 , highest_frequency = 659.25 ):
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
        Tone.sine(min(frequency_array) , 2)
        exit()
    for frequency in frequency_array:
        tone = Tone(frequency ,frequency_duration)
        tone_array.append(tone)
    
    tone_track_r = ToneTrack(tone_array , "r")
    tone_track_l = ToneTrack(tone_array , "l")
    
    return [tone_track_r , tone_track_l]





freq_arrray = turn_values_into_frequencies(mathemathic_function(get_x_inputs(-10 , 10 , 0.1)))

tone_tracks = tonify(freq_arrray , beat/8)
tone_tracks[0].play()


tone_tracks[0].stop()