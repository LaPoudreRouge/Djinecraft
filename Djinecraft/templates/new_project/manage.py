#!/usr/bin/env python3

import sys
import os
from Djinecraft.core.start_app import start_app

def main():
    if len(sys.argv) < 2:
        print("Usage: manage.py [command] [name]")
        return

    command = sys.argv[1]
    if command == "startapp":
        if len(sys.argv) != 3:
            print("Usage: manage.py startapp <appname>")
            return
        app_name = sys.argv[2]
        start_app(app_name)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
