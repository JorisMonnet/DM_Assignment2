def change_duration_specific_beats_in_stream(s, start_measure: int, end_measure: int, target_beats: list,
                                             duration_factor: float):
    """
    Change the duration of notes in a stream at specific beats.
    :param s:  Stream
    :param start_measure: int
    :param end_measure: int
    :param target_beats: should be a list of beats where duration needs to be changed, e.g., [1, 3]
    :param duration_factor: float
    :return:
    """
    for measure_number in range(start_measure, end_measure + 1):
        measure = s.measure(measure_number)
        if measure is not None:
            for n in measure.notes:  # Iterating over notes directly
                if n.beat in target_beats:  # Check if the note's beat is in the list of target beats
                    n.duration.quarterLength *= duration_factor
    return s
