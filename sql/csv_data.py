# coding=utf-8

import csv

key_list = {"T": "摄氏度", "U": "相对湿度",
            "DD": "风向", "Ff": "风速", "当地时间 昆明市": "时间"}


def del_time(string):
    l1 = string.split(" ")
    l2 = l1[0].split(".")
    return l2[2] + "-" + l2[1] + "-" + l2[0] + " " + l1[1] + ":00"


def get_list():

    csv_file = open("weather.csv", "rb")
    reader = csv.DictReader(csv_file, delimiter=';')

    data_list = list()
    for info in reader:
        new_info = dict()
        for (key, item) in key_list.items():
            if key == "当地时间 昆明市":
                new_info[item] = del_time(info[key])
            else:
                new_info[item] = info[key]
        data_list.append(new_info)
    return data_list


