p = '/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/AdventOfCode/InputFiles/day_4.txt'

def now_we_pounce(p):

    status_registry = {
        0:'wakes up',
        1:'falls asleep',
        2:'Guard begins shift' # should be noted that this will never hit.
    }

    #guard_sleep_by_minute = {"guard id": {"total_slept":X, {"xx:yy": Z, "aa:bb": D}}}
    guard_sleep_minutes = {}
    sleepers_by_minute = {}
    current_guard = -1
    sleep_min = 0
    current_state = None
    with open(p) as fp:
        fp = fp.readlines()
        fp.sort()
        for line in fp:
            components = line.split(' ', 2)
            date = components[0][1:]
            hourmin = components[1]
            (hour, minute) = hourmin.split(':')
            if hour == '00':
                hour = '24'
            second = second[:-1]
            status = components[2]
            # Dirty, but we'll assume that if the status isnt in the registry, that it's guard beginning it's shift.
            if status == status_registry[0]:
                #wakes up
                if sleep_min > 0:
                    #register this sleep session
                    if current_guard in guard_sleep_minutes:
                        guard_sleep_minutes[current_guard] += sleep_min
                        sleep_min = 0
                    else:
                        guard_sleep_minutes[current_guard] = sleep_min
                        sleep_min = 0

                    if minsec in sleepers_by_minute:
                        sleepers_by_minute[minsec] += 1
                    else:
                        sleepers_by_minute[minsec] = 1
            elif status == status_registry[1]:
                #falls asleep
                pass
            else:
                # Guard beginning shift
                status_segments = status.split(' ')
                if not len(status_segments) == 4:
                    # Problem
                    exit()
                else:
                    guard_id = status_segments[1]
                    current_guard = guard_id


now_we_pounce(p)