import time

import amber_api.cmd_1
import amber_api.cmd_4
import amber_api.cmd_10
import csv

# = SETTINGS BELOW =


IP_ADDR = "192.168.50.235"
PORT = 26001
FILE_NAME = 'KeyPoints'
DEFAULT_TIMEOUT = 10
DEFAULT_ACCURACY = 0.0175  # rad, for every joint, 0.0175 rad= 1 degree


# ==================


class Global:
    record_list = []


def check_if_done(target, timeout=DEFAULT_TIMEOUT, accuracy=DEFAULT_ACCURACY):
    delta_flag = [0, 0, 0, 0, 0, 0, 0, 0]

    use_time = 0
    while True:
        delta_all = 0
        now = amber_api.cmd_1.get_status(IP_ADDR=IP_ADDR, port=PORT)
        for i in range(8):
            delta = abs(now[i] - target[i])
            delta_all+=delta
            #print(delta)
            if delta < accuracy:
                delta_flag[i] = 1
            else:
                delta_flag[i] = 0
        #print("==========================")
        print(f"Delta All = {round(delta_all, 4)}", end="\r")
        flag = 0
        for i in range(8):
            flag += delta_flag[i]
        if flag > 7:
            print(f"Delta All = {round(delta_all,4)}, done!")
            break

        time.sleep(0.1)
        use_time += 0.1
        if use_time > timeout:
            print("TimeOut!")
            break


def start_position_mode():
    result = amber_api.cmd_10.on_position_mode(IP_ADDR=IP_ADDR, port=PORT)
    if result != -1:
        pass
    else:
        print("Socket Timeout! ")


def start_drag_mode():
    result = amber_api.cmd_10.on_current_mode(IP_ADDR=IP_ADDR, port=PORT)
    if result != -1:
        pass
    else:
        print("Socket Timeout! ")


def end_drag_mode():
    result = amber_api.cmd_10.on_position_mode(IP_ADDR=IP_ADDR, port=PORT)
    if result != -1:
        write_record_to_csv()
    else:
        print("Socket Timeout! ")


def write_record_to_csv():
    print(f"Write {len(Global.record_list)} points                 ")
    # readyFilename = "rec-" + datetime.now().strftime('%y-%m-%d-%H-%M-%S')
    if len(Global.record_list) >= 1:
        print(f"Saving file: Name = {'./' + FILE_NAME + '.csv'} , length = {len(Global.record_list)} ")
        # print(f"Saving file: Name = {readyFilename}, length = {len(record_list)} ")
        with open('./' + FILE_NAME + '.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(Global.record_list)


def save_record(duration):
    print("Save a key point")
    pos = amber_api.cmd_1.get_status(IP_ADDR=IP_ADDR, port=PORT)
    if pos != -1:
        pos.append(duration)
        Global.record_list.append(pos)
    else:
        print("Socket Timeout! ")


def replay_record():
    point_count = 0
    print(f"Replaying {('./' + FILE_NAME + '.csv')}...")
    csv_reader = csv.reader(open('./' + FILE_NAME + '.csv'))
    for line in csv_reader:
        point_count+=1
        pos = line[:8]
        for i in range(len(pos)):
            pos[i] = float(pos[i])
        duration = float(line[8])
        print(f"Replaying point {point_count}")
        result = amber_api.cmd_4.move_joint(IP_ADDR=IP_ADDR, port=PORT, pos=pos, duration=duration)
        if result != -1:
            check_if_done(pos)
        else:
            print("Socket Timeout! ")
    print("Finish!")


def replay_a_line(i):
    lines = []

    csv_reader = csv.reader(open('./' + FILE_NAME + '.csv'))
    for line in csv_reader:
        lines.append(line)
    i = i % len(lines)

    pos = lines[i]
    duration = float(pos[8])
    pos = pos[:8]
    for j in range(len(pos)):
        pos[j] = float(pos[j])
    result = amber_api.cmd_4.move_joint(IP_ADDR=IP_ADDR, port=PORT, pos=pos, duration=duration)
    if result != -1:
        print(f"Executing point {i}")
        check_if_done(pos)

    else:
        print("Socket Timeout! ")


def back_to_zero(duration):
    print("Go to Zero")
    result = amber_api.cmd_4.move_joint(IP_ADDR=IP_ADDR, port=PORT, pos=[0, 0, 0, 0, 0, 0, 0, 0], duration=duration)
    if result != -1:
        check_if_done([0, 0, 0, 0, 0, 0, 0, 0])
    else:
        print("Socket Timeout! ")
