from music21 import converter, stream


def get_stream(filename: str = "./Berceuse_op_57/corrected_midi_score.mid") -> 'music21.stream.Stream':
    """
    Get a music21 stream from a midi file.
    :param filename: str
    :return: music21.stream.Stream
    """
    my_stream = converter.parse(filename, format='midi', forceSource=True,
                                quantizePost=False, quarterLengthDivisors=(128, 48))
    return my_stream


def save_midi(my_stream: 'stream.Stream', filename: str = "./Berceuse_op_57/generated_midi_score.mid"):
    """
    Save a music21 stream to a midi file.
    :param my_stream: music21.stream.Stream
    :param filename: str
    """
    my_stream.write('midi', fp=filename)
