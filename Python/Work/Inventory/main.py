import subprocess
import uuid
import platform
import getpass
import pyautogui as pg
from geolocation import geolocation as gl


def get_mac():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac_address = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac_address


def clear_info(info, device_type):
    buffer = info
    array_remove = ["b'Name", "\\r", "\\n", "'", "", "Name",
                    "bBankLabel", "Capacity", "DeviceLocator", "Speed", "P0 CHANNEL", "DIMM 0",
                    "bModel", "SerialNumber", "\\\\\\\\.\\\\PHYSICALDRIVE", "bMaxClock          "]
    for i in array_remove:
        buffer = buffer.replace(i, "")
    buffer = buffer.strip()
    buffer = device_type + buffer
    return buffer


if __name__ == "__main__":
    flag = True
    while flag:
        try:
            geo_info = gl()
            user = pg.prompt("Введите ФИО владельца ПК", "Ruslab: Inventory")
            if len(user) > 10:
                inventory = open("Inventory.txt", "a+", encoding="utf-8")
                str_out = "\n______________________________________________________________\nИНФОРМАЦИЯ О ЖЕЛЕЗЕ\n"

                # Вытаскиваем информацию по материнской плате
                motherboard = str(subprocess.check_output('wmic csproduct get name', shell=True))
                motherboard = clear_info(motherboard, "Motherboard: ")

                # Вытаскиваем информацию по видеокарте
                video = str(subprocess.check_output('wmic path win32_VideoController get name', shell=True))
                video = clear_info(video, "Video: ")

                # Вытаскиваем информацию по CPU
                cpu = str(subprocess.check_output('wmic cpu get name,maxclockspeed', shell=True))
                cpu = clear_info(cpu, "CPU: ")

                # Вытаскиваем информацию по оперативной памяти
                memory = str(subprocess.check_output('wmic MEMORYCHIP get BankLabel,DeviceLocator,Capacity,Speed',
                                                     shell=True))
                memory = clear_info(memory, "Memory: ")

                # Вытаскиваем информацию по HDD\SSD
                diskdrive = str(subprocess.check_output('wmic diskdrive get model,name,serialnumber,size', shell=True))
                diskdrive = clear_info(diskdrive, "Drive: ")

                # Инфо о пользователе компьютера
                user = "\nИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ\nUser: "+str(getpass.getuser())+"\nВладелец ПК: "+user+"\n"

                # Инфа о сетке, операционной системе и т.д.
                network = "ОСТАЛЬНОЕ\n"+"IP: "+geo_info[0]+" \nLocation: "+geo_info[1]+"\nMAC-Address: "+get_mac()
                os = "OS: "+str(platform.platform())+"\n______________________________________________________________"

                # Собираем информацию в единую строку
                str_out += motherboard+"\n"+video+"\n"+cpu+"\n"+memory+"\n"+diskdrive+"\n"+"\n"+user+"\n"+network+"\n"+os
                print(str_out)
                inventory.write(str_out)
                inventory.close()

                pg.alert("Данные о ПК отправлены", "Ruslab: Inventory")
                flag = False
            else:
                pg.alert("Введены некорректные данные", "Ruslab: Inventory")
        except TypeError:
            flag = False
