#!/usr/bin/env python3

'''
File: jlink_flasher.py

Copyright (c) 2019 Diego Asanza <f.asanza@gmail.com>

SPDX-License-Identifier: Apache-2.0
'''

import argparse
from warnings import catch_warnings
import pylink
from pylink.errors import JLinkException
from sys import exit

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Flash a file using JLink')

    parser.add_argument('-erase', action=argparse.BooleanOptionalAction)
    parser.set_defaults(erase=False)
    parser.add_argument('-select', default='USB')
    parser.add_argument('-iface', default='SWD', help='SWD or JTAG interface')
    parser.add_argument('-speed', default='auto',
                        help='Interface speed or auto')
    parser.add_argument('-jlinkpath', default=None, help='Path to jlink tools')
    parser.add_argument('-address', default=0x08000000,
                        help='Memory address where to load the file')
    parser.add_argument('-idcode', default=None,
                help='IDCode for code protected devices with IDCODE protection')
    parser.add_argument(
        'file', help='binary file path. Only .bin, .hex and .elf supported')

    required = parser.add_argument_group('required named arguments')
    required.add_argument(
        '-device', help='Microcontroller device. See JLINK Doc', required=True)

    args = parser.parse_args()

    jlink = pylink.JLink()
    jlink.open()
    if args.iface.upper() == 'SWD':
        jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
    elif args.iface.upper() == 'JTAG':
        jlink.set_tif(pylink.enums.JLinkInterfaces.JTAG)
    else:
        print('Error: Unsupported interface {}'.format(args.iface))
        exit(-1)

    if(args.idcode != None):
        jlink.exec_command("SetCPUConnectIDCODE = {}".format(args.idcode.upper()))
    try:
        jlink.connect(args.device)
    except JLinkException as e:
        print('Error while connecting to the target. {}'.format(e))
        exit(-1)
    jlink.set_reset_strategy(pylink.enums.JLinkResetStrategyCortexM3.CONNECT_UNDER_RESET)
    jlink.reset()

    if(args.erase):
        jlink.erase()

    jlink.flash_file(args.file, args.address)
    jlink.reset()
    jlink.close()
    exit(0)
