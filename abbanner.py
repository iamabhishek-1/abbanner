#!/usr/bin/env python3
# Tech Byte Terminal Banner - Clean Version

import os
import platform
from datetime import datetime, timedelta


def get_username():
    """Ask user for their name"""
    print("\n\033[1;36mTECH BYTE TERMINAL CUSTOMIZER\033[0m")
    print("\033[33mEnter your name to personalize:\033[0m")
    username = input("> ").strip()
    return username if username else "TechByteUser"


def display_banner(username):
    """Show the customized banner"""
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get system info
    hostname = platform.node()
    os_info = f"{platform.system()} {platform.release()}"

    # Terminal width
    try:
        width = os.get_terminal_size().columns
    except:
        width = 60

    # BIG BOLD USERNAME
    print(f"\n\033[1;34m{username.center(width)}\033[0m")
    print("\033[38;5;208m" + "=" * width + "\033[0m")

    # Tech Byte branding (smaller)
    print(f"\033[33m{'Tech Byte'.center(width)}\033[0m")
    print("\033[38;5;208m" + "-" * width + "\033[0m")

    # System info
    print(f"Host: {hostname}".center(width))
    print(f"OS: {os_info}".center(width))
    print("\033[38;5;208m" + "=" * width + "\033[0m")


if __name__ == "__main__":
    username = get_username()
    display_banner(username)