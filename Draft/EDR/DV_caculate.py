def calculate_dv(lsb, ms):
    time = int(ms / 10)
    print('DV1 = 0x7F')
    for i in range(time):
        current_dv = round(lsb / 16 * 9.8 * (i + 1) * 10 / 1000 / 1000 * 3600) + 127
        print('DV' + str(i + 2) + ' = ' + hex(current_dv))
    dv = round(lsb / 16 * 9.8 * ms / 1000 / 1000 * 3600 + 127)
    dv_square = round((lsb / 16 * 9.8 * ms / 1000 / 1000 * 3600) * (lsb / 16 * 9.8 * ms / 1000 / 1000 * 3600))
    print("Max dv = " + hex(dv))
    print("Max dv time = " + hex(round(ms / 2.5)))
    print('ac = ' + hex(round(lsb / 16 + 127)))
    print('Square DV = ' + str(hex(dv_square)))
    print("Tend = " + hex(round((ms + 40) / 2.5)))
    print("-------------------------------------------------------" )

def calculate_dv2(lsb, ms,gapTime, lsb2, ms2):
    print("-----------------------1st event--------------------------------")
    time = int(ms / 10)
    print('DV1 = 0x7F')
    for i in range(time):
        current_dv = round(lsb / 16 * 9.8 * (i + 1) * 10 / 1000 / 1000 * 3600) + 127
        print('DV' + str(i + 2) + ' = ' + hex(current_dv))
    dv = round(lsb / 16 * 9.8 * ms / 1000 / 1000 * 3600 + 127)
    dv_square = round((lsb / 16 * 9.8 * ms / 1000 / 1000 * 3600) * (lsb / 16 * 9.8 * ms / 1000 / 1000 * 3600))
    print("Max dv = " + hex(dv))
    print("Max dv time = " + hex(round(ms / 2.5)))
    print('ac = ' + hex(round(lsb / 16 + 127)))
    # print('Square DV = ' + str(hex(dv_square)))
    # print("Tend = " + hex(round((ms + 40) / 2.5)))

    print("-----------------------2nd event--------------------------------")

    time1 = int((ms + gapTime) / 10)
    print('DV1 = 0x7F')
    for i in range(time1):
        print('DV' + str(i + 2) + ' = 0x7F' )
    j = i
    time2 = int(ms2 / 10)
    for i in range(time2):
        current_dv = round(lsb2 / 16 * 9.8 * (i + 1) * 10 / 1000 / 1000 * 3600) + 127
        print('DV' + str(j + i + 3) + ' = ' + hex(current_dv))
    dv = round(lsb2 / 16 * 9.8 * ms2 / 1000 / 1000 * 3600 + 127)
    dv_square = round((lsb / 16 * 9.8 * ms / 1000 / 1000 * 3600) * (lsb2 / 16 * 9.8 * ms2 / 1000 / 1000 * 3600))
    print("Max dv = " + hex(dv))
    print("Max dv time = " + hex(round((ms + gapTime + ms2 ) / 2.5)))
    print('ac = ' + hex(round(lsb2 / 16 + 127)))
    print('Square DV = ' + str(hex(dv_square)))
    print("Tend = " + hex(round((ms + gapTime + ms2 + 40) / 2.5)))
    print("-------------------------------------------------------" )


def calculate_rsu(front_l, front_r, side_left, Side_right, ped_p_left, ped_p_right, side_p_l, side_p_r, ped_a_left,
                  ped_a_right):
    print('Side_right Before T0= ' + str(round((0 / 2 * (-1) + 240) / 2)) + "    " + 'Side_right= ' + str(round((Side_right / 2 * (-1) + 240) / 2)))
    print('side_left  Before T0= ' + str(round((0 / 2 + 240) / 2)) +  "    " + 'side_left= ' + str(round((side_left / 2 + 240) / 2)))
    print('ped_p_right  Before T0= ' + str((0 * 0.048828 + 5) * 10) +  "    " + 'ped_p_right= ' + str((ped_p_right * 0.048828 + 5) * 10))
    print('ped_p_left  Before T0= ' + str((0 * 0.048828 + 5) * 10) +  "    " + 'ped_p_left= ' + str((ped_p_left * 0.048828 + 5) * 10))
    print('ped_a_right  Before T0= ' + str(round((0 * (-1) + 480) / 4)) +  "    " + 'ped_a_right= ' + str(round((ped_a_right * (-1) + 480) / 4)))
    print('ped_a_left Before T0= ' + str(round((0 * (-1) + 480) / 4)) +  "    " + 'ped_a_left= ' + str(round((ped_a_left * (-1) + 480) / 4)))
    print('front_r  Before T0= ' + str(round((0 * (-1) + 480) / 4)) + "    " +  'front_r= ' + str(round((front_r * (-1) + 480) / 4)))
    print('front_l  Before T0= ' + str(round((0 * (-1) + 480) / 4)) +  "    " + 'front_l= ' + str(round((front_l * (-1) + 480) / 4)))
    print('side_p_r Before T0= ' + str((0 * 0.048828 + 5) * 10) +  "    " + 'side_p_r= ' + str((side_p_r * 0.048828 + 5) * 10))
    print('side_p_l  Before T0= ' + str((0 * 0.048828 + 5) * 10) +  "    " + 'side_p_l= ' + str((side_p_l * 0.048828 + 5) * 10))


def Caculate(Yaw,Y,X):

    print('X = ' + str(round(X / 500 + 50)))
    print('Y = ' + str(round(Y / 500 + 50)))
    print("Yaw = " + str(round(Yaw / 10 + 3000)))
    print("%"*30)

if __name__ == "__main__":
    calculate_dv(-200, 10)
    # calculate_dv2(-400, 20, 35, -375, 50)
    # # calculate_rsu(125, 150, 6, 16, 10, 35, 14, 45, 28, 40)
    # calculate_rsu(125, 150, 6, 8, 14, 16, 10, 12, 18, 20)
    # # calculate_rsu(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    # Caculate(30000,-12000,1000)
    # Caculate(-30000	,-10000	,2000)
    # Caculate(-29000,	-9000,	3000)
    # Caculate(29000	,-8000	,4000)