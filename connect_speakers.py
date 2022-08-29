#!/usr/bin/python3

import bluetooth


def scan():
    """Scans for Bluetooth Devices"""
    print("Scanning for bluetooth devices:")
    devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
    number_of_devices = len(devices)
    print(number_of_devices, "devices found")
    for addr, name, device_class in devices:
        print("".join([
            "\n",
            "Device: \n",
            "\tDevice Name: ", name, "\n",
            "\tDevice MAC Address: ", addr, "\n",
            "\tDevice Class: ", device_class, "\n",
        ]))
    return


def scan_services():
    """Scans for Bluetooth services on found devices can also be created"""
    print("Scanning for bluetooth devices: ")
    devices = bluetooth.discover_devices(lookup_names=True)
    number_of_devices = len(devices)
    print(number_of_devices, "devices found")

    for addr, name in devices:
        print("".join([
            "\n",
            "Device Name: ", name, "\n",
            "Device MAC Address: ", addr, "\n",
        ]))

        services = bluetooth.find_service(address=addr)
        if len(services) <= 0:
            print("No services found on", addr)
        else:
            print("Services Found:")
            for serv in services:
                print(serv['name'])
                print("\n")
    return()
