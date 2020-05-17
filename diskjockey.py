#!/usr/bin/env python

import argparse
import os
from pathlib import Path
import subprocess


def imagize(device, archive_dir, diskid):
    diskid = str(diskid)
    target_dir = archive_dir / diskid
    target_file = Path(diskid + '.img')
    target_path = target_dir / target_file
    os.mkdir(target_dir)
    try:
        subprocess.check_call(["pv", f"<{device}", f">{target_path}"])
    except subprocess.CalledProcessError as image_exc:
        err = (f"ERROR - return code {image_exc.errcode}" +
                f"while running {image_exc.cmd}\n" +
                f"Output: {image_exc.output}")
        print(err)
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--device',
                        help='block device to read from. default: /dev/fd0')
    parser.add_argument('-s', '--start',
                        help='starting disk ID number. default: 1')
    parser.add_argument('-d', '--dir',
                        help='archive directory. default: current directory')
    args = parser.parse_args()
    device = args.device if args.device else '/dev/fd0'
    archive_dir = Path(args.dir) if args.dir else Path('.')
    diskid = args.start if args.start else 1

    if not archive_dir.is_dir():
        raise NotADirectoryError
    imagize(device, archive_dir, diskid)

if __name__ == '__main__':
    main()
