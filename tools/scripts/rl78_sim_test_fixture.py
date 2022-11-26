#!/usr/bin/env python3

'''
File: jlink_test_fixture.py

Copyright (c) 2019 Diego Asanza <f.asanza@gmail.com>

SPDX-License-Identifier: Apache-2.0
'''

import subprocess
import argparse
import os
import re
import sys
import threading
from shutil import which
import time

rl78_elf_gdb = 'rl78-elf-gdb'

def startGdbClient(name, gdbinit, executable):

  gdbargs = [rl78_elf_gdb,
    '-q', '-batch',
    '-ex', 'target sim',
    '-ex', 'file {}'.format(executable),
    '-ex', 'load',
    '-ex', 'run',
    '-ex', 'quit',
    ]

  if gdbinit != None:
    gdbargs.append('-x')
    gdbargs.append(gdbinit)

  try:
    gdbClient = subprocess.Popen(gdbargs, stdout=subprocess.PIPE , stderr=fnull )
  except FileNotFoundError:
    print('Error: ' + rl78_elf_gdb + ' not found')
    print('Check that arm gnu tools are installed and available in your path\n')
    print_failure()
    exit(1)

  buf = gdbClient.stdout.read()
  buf = buf.decode('ascii', 'ignore')

  if re.search(r'Connection timed out', buf):
    return -1

  lines = buf.split('\n')

  for line in lines:
    line = line.replace('\x00', '')
    line = line.replace('\r', '')
    line = line.replace('`', '')
    if re.search(r'^Loading section.*$', line):
        continue
    if re.search(r'^Connected to the simulator.*$', line):
        continue
    if re.search(r'^.*(Semihosting|Semi-hosting|SYSRESETREQ).*$', line):
      continue
    print(line)
    if re.search(r'^OK', line):
      return 0
  return 0

def print_failure():
    print('-----------------------')
    print('0 Tests 0 Failures 0 Ignored')
    print('FAIL')

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='RL78 Test Fixture')

  parser.add_argument('-gdbpath', default=None, help='Path to gdb')
  parser.add_argument('-gdbinit', help='gdb init script file path')
  parser.add_argument('executable', help='executable file path')

  args = parser.parse_args()

  fnull = open(os.devnull, 'w')

  if args.gdbpath == None:
    if os.name == 'nt':
      rl78_elf_gdb = rl78_elf_gdb + '.exe'

  # start the client
  rval = startGdbClient(rl78_elf_gdb, args.gdbinit, args.executable)

  exit( rval )
