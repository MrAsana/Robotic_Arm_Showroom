import sample_func
import handle_input
import sys

saved_point = 0
print("===================================================")
print("|         A sample program that provides          |\r\n"
      "|    key point recording and playback functions   |")
print("=================== USE KEYBOARD ==================")
print("| [P] Position Mode                               |\r\n"
      "| [S] Start dragging                              |\r\n"
      "| [E] End dragging                                |\r\n"
      "| [1-9] Write a key point                         |\r\n"
      "|           and record the number you pressed     |\r\n"
      "|               as the duration.                  |\r\n"
      "| [R] Replay All                                  |\r\n"
      "| [N] Play next point                             |\r\n"
      "| [Z] Back to Zero position                       |\r\n"
      "| [Q] Quit                                        |")
print("===================================================")
i = 0
# Wait for a single key press
while True:
    key = handle_input.get_key()
    if key in '123456789':
        sample_func.save_record(int(key))
        saved_point += 1
        print(f"Total {saved_point} points")
    if key in 'Ss':
        print("Waiting for mode switch... ")
        print("\033[33mW: DO NOT MOVE ANY JOINT NOW \033[0m", end="\r")
        if sample_func.start_drag_mode() != -1:
            print("===== Start Dragging =====                             ")
    if key in 'Ee':
        print("Waiting for mode switch... ")
        print("\033[33mW: DO NOT MOVE ANY JOINT NOW \033[0m", end="\r")
        if sample_func.end_drag_mode() != -1:
            print("===== Stop Dragging =====                              ")
    if key in 'Rr':
        sample_func.replay_record()
    if key in 'Nn':
        sample_func.replay_a_line(i)
        i += 1
    if key in 'Zz':
        sample_func.back_to_zero(2)
    if key in 'Qq':
        print("Bye!")
        sys.exit()
    if key in 'Pp':
        print("Waiting for mode switch... ")
        print("\033[33mW: DO NOT MOVE ANY JOINT NOW \033[0m", end="\r")
        if sample_func.start_position_mode()!= -1:
            print("===== Enable Position Mode =====                       ")
