import threading


class ToneTrack:
    def __init__(self, tone_array:list, speaker=None):
        self.tone_array = tone_array
        self.thread = None
        self.speaker = speaker

    def play(self):
        def play_tones():
            for tone in self.tone_array:
                if tone is None:
                    continue
                
                tone.sine(tone.tone_frequency ,tone.tone_duration , self.speaker )

        self.thread = threading.Thread(target=play_tones)
        self.thread.start()

    def stop(self):
        self.thread.join()