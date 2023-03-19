from shemas import DayPD
from math import sin, pi
import unittest


def process_mission(points):
    results = []
    day = 1
    base_weight = 192
    use_oxi = 0
    use_power_percent = 0
    for point in points:
        now_sh = 8
        now_dist_to = point["distance"]
        need_sh = point["SH"]
        flag = True
        while flag:
            for r_power in range(80, 0, -1):
                speed = 2 * (r_power / 80) * (200 / (base_weight + now_sh))
                if now_dist_to - speed > 0:
                    now_dist_to -= speed
                    use_oxi += now_sh * 2
                    use_power_percent += r_power
                    day += 1
                    use_power_percent += 20
                    results.append(
                        DayPD(num=day, current_sh=now_sh, current_power=use_power_percent, current_oxi=use_oxi,
                              use_power=20 + r_power, use_oxi=now_sh * 2,
                              distribution_engine=r_power, distribution_autoclave=20))
                    if r_power != 80:
                        flag = False
                    break
            else:
                flag = False

        flag = True
        while flag:
            for oxi in range(20, 0, -1):
                k = sin(-pi / 2 + (pi * (30 + 0.5 * oxi) / 40))
                if now_sh + now_sh * k <= need_sh + 8:
                    use_oxi += now_sh * oxi
                    now_sh = now_sh + now_sh * k
                    day += 1
                    use_power_percent += 43
                    results.append(
                        DayPD(num=day, current_sh=now_sh, current_power=use_power_percent, current_oxi=use_oxi,
                              use_power=43, use_oxi=now_sh * oxi,
                              distribution_engine=0, distribution_autoclave=43))
                    if oxi != 20:
                        flag = False
                    break
                else:
                    flag = False

        flag = True
        while flag:
            for r_power in range(1, 81):
                speed = 2 * (r_power / 80) * (200 / (base_weight + now_sh))
                if now_dist_to - speed < 0:
                    now_dist_to -= speed
                    use_oxi += now_sh * 2
                    use_power_percent += r_power
                    day += 1
                    use_power_percent += 20
                    results.append(
                        DayPD(num=day, current_sh=now_sh, current_power=use_power_percent, current_oxi=use_oxi,
                              use_power=r_power + 20, use_oxi=now_sh * 2,
                              distribution_engine=r_power, distribution_autoclave=20))
                    flag = False
                    break
            else:
                r_power = 80
                speed = 2 * (r_power / 80) * (200 / (base_weight + now_sh))
                now_dist_to -= speed
                use_oxi += now_sh * 2
                use_power_percent += r_power
                day += 1
                use_power_percent += 20

    return results


tests = [
    [
        {
            "SH": 56, 
            "distance": 44
        }
    ],
    [
        {
            "SH": 4088, 
            "distance": 28
        }, 
        {
            "SH": 504, 
            "distance": 43
        }, 
        {
            "SH": 120, 
            "distance": 20
        }
    ],
    [
        {
            "SH": 6, 
            "distance": 10
        }, 
        {
            "SH": 3, 
            "distance": 19
        }
    ]
]



expected_output = [[{'num': 2, 'current_sh': 8, 'current_power': 100, 'current_oxi': 16, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 3, 'current_sh': 8, 'current_power': 200, 'current_oxi': 32, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 4, 'current_sh': 8, 'current_power': 300, 'current_oxi': 48, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 5, 'current_sh': 8, 'current_power': 400, 'current_oxi': 64, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 6, 'current_sh': 8, 'current_power': 500, 'current_oxi': 80, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 7, 'current_sh': 8, 'current_power': 600, 'current_oxi': 96, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 8, 'current_sh': 8, 'current_power': 700, 'current_oxi': 112, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 9, 'current_sh': 8, 'current_power': 800, 'current_oxi': 128, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 10, 'current_sh': 8, 'current_power': 900, 'current_oxi': 144, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 11, 'current_sh': 8, 'current_power': 1000, 'current_oxi': 160, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 12, 'current_sh': 8, 'current_power': 1100, 'current_oxi': 176, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 13, 'current_sh': 8, 'current_power': 1200, 'current_oxi': 192, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 14, 'current_sh': 8, 'current_power': 1300, 'current_oxi': 208, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 15, 'current_sh': 8, 'current_power': 1400, 'current_oxi': 224, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 16, 'current_sh': 8, 'current_power': 1500, 'current_oxi': 240, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 17, 'current_sh': 8, 'current_power': 1600, 'current_oxi': 256, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 18, 'current_sh': 8, 'current_power': 1700, 'current_oxi': 272, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 19, 'current_sh': 8, 'current_power': 1800, 'current_oxi': 288, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 20, 'current_sh': 8, 'current_power': 1900, 'current_oxi': 304, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 21, 'current_sh': 8, 'current_power': 2000, 'current_oxi': 320, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 22, 'current_sh': 8, 'current_power': 2100, 'current_oxi': 336, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 23, 'current_sh': 8, 'current_power': 2199, 'current_oxi': 352, 'use_power': 99, 'use_oxi': 16, 'distribution_engine': 79, 'distribution_autoclave': 20}, {'num': 24, 'current_sh': 16, 'current_power': 2242, 'current_oxi': 512, 'use_power': 43, 'use_oxi': 320, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 25, 'current_sh': 32, 'current_power': 2285, 'current_oxi': 832, 'use_power': 43, 'use_oxi': 640, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 26, 'current_sh': 64, 'current_power': 2328, 'current_oxi': 1472, 'use_power': 43, 'use_oxi': 1280, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 27, 'current_sh': 64, 'current_power': 2350, 'current_oxi': 1600, 'use_power': 22, 'use_oxi': 128, 'distribution_engine': 2, 'distribution_autoclave': 20}], [{'num': 2, 'current_sh': 8, 'current_power': 100, 'current_oxi': 16, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 3, 'current_sh': 8, 'current_power': 200, 'current_oxi': 32, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 4, 'current_sh': 8, 'current_power': 300, 'current_oxi': 48, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 5, 'current_sh': 8, 'current_power': 400, 'current_oxi': 64, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 6, 'current_sh': 8, 'current_power': 500, 'current_oxi': 80, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 7, 'current_sh': 8, 'current_power': 600, 'current_oxi': 96, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 8, 'current_sh': 8, 'current_power': 700, 'current_oxi': 112, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 9, 'current_sh': 8, 'current_power': 800, 'current_oxi': 128, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 10, 'current_sh': 8, 'current_power': 900, 'current_oxi': 144, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 11, 'current_sh': 8, 'current_power': 1000, 'current_oxi': 160, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 12, 'current_sh': 8, 'current_power': 1100, 'current_oxi': 176, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 13, 'current_sh': 8, 'current_power': 1200, 'current_oxi': 192, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 14, 'current_sh': 8, 'current_power': 1300, 'current_oxi': 208, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 15, 'current_sh': 8, 'current_power': 1399, 'current_oxi': 224, 'use_power': 99, 'use_oxi': 16, 'distribution_engine': 79, 'distribution_autoclave': 20}, {'num': 16, 'current_sh': 16, 'current_power': 1442, 'current_oxi': 384, 'use_power': 43, 'use_oxi': 320, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 17, 'current_sh': 32, 'current_power': 1485, 'current_oxi': 704, 'use_power': 43, 'use_oxi': 640, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 18, 'current_sh': 64, 'current_power': 1528, 'current_oxi': 1344, 'use_power': 43, 'use_oxi': 1280, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 19, 'current_sh': 128, 'current_power': 1571, 'current_oxi': 2624, 'use_power': 43, 'use_oxi': 2560, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 20, 'current_sh': 256, 'current_power': 1614, 'current_oxi': 5184, 'use_power': 43, 'use_oxi': 5120, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 21, 'current_sh': 512, 'current_power': 1657, 'current_oxi': 10304, 'use_power': 43, 'use_oxi': 10240, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 22, 'current_sh': 1024, 'current_power': 1700, 'current_oxi': 20544, 'use_power': 43, 'use_oxi': 20480, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 23, 'current_sh': 2048, 'current_power': 1743, 'current_oxi': 41024, 'use_power': 43, 'use_oxi': 40960, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 24, 'current_sh': 4096, 'current_power': 1786, 'current_oxi': 81984, 'use_power': 43, 'use_oxi': 81920, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 25, 'current_sh': 4096, 'current_power': 1828, 'current_oxi': 90176, 'use_power': 42, 'use_oxi': 8192, 'distribution_engine': 22, 'distribution_autoclave': 20}, {'num': 26, 'current_sh': 8, 'current_power': 1928, 'current_oxi': 90192, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 27, 'current_sh': 8, 'current_power': 2028, 'current_oxi': 90208, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 28, 'current_sh': 8, 'current_power': 2128, 'current_oxi': 90224, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 29, 'current_sh': 8, 'current_power': 2228, 'current_oxi': 90240, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 30, 'current_sh': 8, 'current_power': 2328, 'current_oxi': 90256, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 31, 'current_sh': 8, 'current_power': 2428, 'current_oxi': 90272, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 32, 'current_sh': 8, 'current_power': 2528, 'current_oxi': 90288, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 33, 'current_sh': 8, 'current_power': 2628, 'current_oxi': 90304, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 34, 'current_sh': 8, 'current_power': 2728, 'current_oxi': 90320, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 35, 'current_sh': 8, 'current_power': 2828, 'current_oxi': 90336, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 36, 'current_sh': 8, 'current_power': 2928, 'current_oxi': 90352, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 37, 'current_sh': 8, 'current_power': 3028, 'current_oxi': 90368, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 38, 'current_sh': 8, 'current_power': 3128, 'current_oxi': 90384, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 39, 'current_sh': 8, 'current_power': 3228, 'current_oxi': 90400, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 40, 'current_sh': 8, 'current_power': 3328, 'current_oxi': 90416, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 41, 'current_sh': 8, 'current_power': 3428, 'current_oxi': 90432, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 42, 'current_sh': 8, 'current_power': 3528, 'current_oxi': 90448, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 43, 'current_sh': 8, 'current_power': 3628, 'current_oxi': 90464, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 44, 'current_sh': 8, 'current_power': 3728, 'current_oxi': 90480, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 45, 'current_sh': 8, 'current_power': 3828, 'current_oxi': 90496, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 46, 'current_sh': 8, 'current_power': 3928, 'current_oxi': 90512, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 47, 'current_sh': 8, 'current_power': 3987, 'current_oxi': 90528, 'use_power': 59, 'use_oxi': 16, 'distribution_engine': 39, 'distribution_autoclave': 20}, {'num': 48, 'current_sh': 16, 'current_power': 4030, 'current_oxi': 90688, 'use_power': 43, 'use_oxi': 320, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 49, 'current_sh': 32, 'current_power': 4073, 'current_oxi': 91008, 'use_power': 43, 'use_oxi': 640, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 50, 'current_sh': 64, 'current_power': 4116, 'current_oxi': 91648, 'use_power': 43, 'use_oxi': 1280, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 51, 'current_sh': 128, 'current_power': 4159, 'current_oxi': 92928, 'use_power': 43, 'use_oxi': 2560, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 52, 'current_sh': 256, 'current_power': 4202, 'current_oxi': 95488, 'use_power': 43, 'use_oxi': 5120, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 53, 'current_sh': 512, 'current_power': 4245, 'current_oxi': 100608, 'use_power': 43, 'use_oxi': 10240, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 54, 'current_sh': 512, 'current_power': 4269, 'current_oxi': 101632, 'use_power': 24, 'use_oxi': 1024, 'distribution_engine': 4, 'distribution_autoclave': 20}, {'num': 55, 'current_sh': 8, 'current_power': 4369, 'current_oxi': 101648, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 56, 'current_sh': 8, 'current_power': 4469, 'current_oxi': 101664, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 57, 'current_sh': 8, 'current_power': 4569, 'current_oxi': 101680, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 58, 'current_sh': 8, 'current_power': 4669, 'current_oxi': 101696, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 59, 'current_sh': 8, 'current_power': 4769, 'current_oxi': 101712, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 60, 'current_sh': 8, 'current_power': 4869, 'current_oxi': 101728, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 61, 'current_sh': 8, 'current_power': 4969, 'current_oxi': 101744, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 62, 'current_sh': 8, 'current_power': 5069, 'current_oxi': 101760, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 63, 'current_sh': 8, 'current_power': 5169, 'current_oxi': 101776, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 64, 'current_sh': 8, 'current_power': 5268, 'current_oxi': 101792, 'use_power': 99, 'use_oxi': 16, 'distribution_engine': 79, 'distribution_autoclave': 20}, {'num': 65, 'current_sh': 16, 'current_power': 5311, 'current_oxi': 101952, 'use_power': 43, 'use_oxi': 320, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 66, 'current_sh': 32, 'current_power': 5354, 'current_oxi': 102272, 'use_power': 43, 'use_oxi': 640, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 67, 'current_sh': 64, 'current_power': 5397, 'current_oxi': 102912, 'use_power': 43, 'use_oxi': 1280, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 68, 'current_sh': 128, 'current_power': 5440, 'current_oxi': 104192, 'use_power': 43, 'use_oxi': 2560, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 69, 'current_sh': 128, 'current_power': 5462, 'current_oxi': 104448, 'use_power': 22, 'use_oxi': 256, 'distribution_engine': 2, 'distribution_autoclave': 20}], [{'num': 2, 'current_sh': 8, 'current_power': 100, 'current_oxi': 16, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 3, 'current_sh': 8, 'current_power': 200, 'current_oxi': 32, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 4, 'current_sh': 8, 'current_power': 300, 'current_oxi': 48, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 5, 'current_sh': 8, 'current_power': 400, 'current_oxi': 64, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 6, 'current_sh': 8, 'current_power': 499, 'current_oxi': 80, 'use_power': 99, 'use_oxi': 16, 'distribution_engine': 79, 'distribution_autoclave': 20}, {'num': 7, 'current_sh': 13, 'current_power': 542, 'current_oxi': 88, 'use_power': 43, 'use_oxi': 13, 'distribution_engine': 0, 'distribution_autoclave': 43}, {'num': 8, 'current_sh': 13, 'current_power': 564, 'current_oxi': 115, 'use_power': 22, 'use_oxi': 27, 'distribution_engine': 2, 'distribution_autoclave': 20}, {'num': 9, 'current_sh': 8, 'current_power': 664, 'current_oxi': 131, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 10, 'current_sh': 8, 'current_power': 764, 'current_oxi': 147, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 11, 'current_sh': 8, 'current_power': 864, 'current_oxi': 163, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 12, 'current_sh': 8, 'current_power': 964, 'current_oxi': 179, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 13, 'current_sh': 8, 'current_power': 1064, 'current_oxi': 195, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 14, 'current_sh': 8, 'current_power': 1164, 'current_oxi': 211, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 15, 'current_sh': 8, 'current_power': 1264, 'current_oxi': 227, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 16, 'current_sh': 8, 'current_power': 1364, 'current_oxi': 243, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 17, 'current_sh': 8, 'current_power': 1464, 'current_oxi': 259, 'use_power': 100, 'use_oxi': 16, 'distribution_engine': 80, 'distribution_autoclave': 20}, {'num': 18, 'current_sh': 8, 'current_power': 1523, 'current_oxi': 275, 'use_power': 59, 'use_oxi': 16, 'distribution_engine': 39, 'distribution_autoclave': 20}, {'num': 19, 'current_sh': 8, 'current_power': 1545, 'current_oxi': 291, 'use_power': 22, 'use_oxi': 16, 'distribution_engine': 2, 'distribution_autoclave': 20}]]


class TestMethods(unittest.TestCase):

    def test_algorithm(self):
        for i in range(len(tests)):
            self.assertEqual(process_mission(tests[i]), expected_output[i])



if __name__ == '__main__':
    unittest.main()