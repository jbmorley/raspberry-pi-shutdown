#!/usr/bin/env python3

import argparse
import atexit
import os
import subprocess

import RPi.GPIO as GPIO


GPIO_PIN = 21

def exit_handler():
    RPi.GPIO.cleanup()    


def main():
    parser = argparse.ArgumentParser(description="Raspberry Pi shutdown utility.")
    parser.add_argument("--dry-run", action="store_true", default=False, help="dry run only")
    options = parser.parse_args()
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.wait_for_edge(GPIO_PIN, GPIO.FALLING)

    print("Shutting down...")
    if not options.dry_run:
        subprocess.check_call(["sync"])
        subprocess.check_call(["/sbin/shutdown", "-h", "now"])
    

if __name__ == "__main__":
    main()