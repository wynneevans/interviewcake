def merge_ranges(meetings):
    """
    :param meetings: the beginning and end of meetings. E.g. [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    :type meetings: a python list of integer tuples.
    :return: the occupied times. E.g. [(0, 1), (3, 8), (9, 12)]
    :rtype: a python list of integer tuples.

    """

    sorted_meetings = sorted(meetings)
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        merged_meeting_start, merged_meeting_end = merged_meetings[-1]

        if current_meeting_start <= merged_meeting_end:

            merged_meetings[-1] = (merged_meeting_start, max(merged_meeting_end, current_meeting_end))

        else:

            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings
