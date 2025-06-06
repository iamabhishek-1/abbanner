#!/usr/bin/env python3
# Tech Byte Terminal Banner with Interactive Username Setup
# Inspired by T-Header (https://github.com/remo7777/T-Header)

import os
import sys
import platform
import random
import json
import argparse
from datetime import datetime, timedelta
import subprocess


class TechByteBanner:
    def __init__(self):
        self.platform = self.detect_platform()
        self.config = self.load_config()
        self.colors = self.setup_colors()
        self.width = self.get_terminal_width()
        self.show_welcome()

    def show_welcome(self):
        """Display Tech Byte welcome banner"""
        tech_byte_art = r"""
  _______          _    _        ____        _      
 |__   __|        | |  | |      |  _ \      | |     
    | | ___   ___ | |_ | |__    | |_) |_   _| |_ __ 
    | |/ _ \ / _ \| __|| '_ \   |  _ <| | | | | '__|
    | | (_) |  __/| |_ | | | |  | |_) | |_| | | |   
    |_|\___/ \___| \__||_| |_|  |____/ \__,_|_|_|   
        """
        print(f"\033[38;5;208m{tech_byte_art}\033[0m")
        print(f"\033[38;5;39m{'=' * self.width}\033[0m")
        print("\033[1mWelcome to Tech Byte Terminal Customizer!\033[0m".center(self.width))
        print(f"\033[38;5;39m{'=' * self.width}\033[0m\n")

    def detect_platform(self):
        if 'termux' in os.environ.get('PREFIX', ''):
            return 'termux'
        return platform.system().lower()

    def load_config(self):
        config_dir = os.path.expanduser('~/.config/techbyte')
        config_path = os.path.join(config_dir, 'config.json')

        default_config = {
            'username': 'TechByteUser',
            'style': 'modern',
            'color_scheme': 'techbyte'
        }

        try:
            os.makedirs(config_dir, exist_ok=True)
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    return json.load(f)
            else:
                self.prompt_username(default_config)
                with open(config_path, 'w') as f:
                    json.dump(default_config, f, indent=4)
                return default_config
        except Exception as e:
            print(f"Config error: {e}, using defaults")
            return default_config

    def prompt_username(self, config):
        """Interactive username prompt"""
        print("\n\033[1mLet's personalize your terminal!\033[0m")
        print("(Press Enter to keep default: TechByteUser)")
        new_name = input("\033[38;5;208mEnter your username: \033[0m").strip()
        if new_name:
            config['username'] = new_name
            print(f"\033[32mUsername set to: {new_name}\033[0m")
        else:
            print("\033[33mUsing default username\033[0m")

    def setup_colors(self):
        schemes = {
            'techbyte': {'primary': '38;5;208', 'secondary': '38;5;202', 'text': '38;5;229'},
            'matrix': {'primary': '38;5;40', 'secondary': '38;5;28', 'text': '38;5;46'},
            'ocean': {'primary': '38;5;27', 'secondary': '38;5;39', 'text': '38;5;255'}
        }
        return schemes.get(self.config.get('color_scheme', 'techbyte'), schemes['techbyte'])

    def get_terminal_width(self):
        try:
            return os.get_terminal_size().columns
        except:
            return 80

    def get_system_info(self):
        info = {
            'os': platform.system(),
            'hostname': platform.node(),
            'kernel': platform.release(),
            'uptime': self.get_uptime(),
            'shell': os.path.basename(os.getenv('SHELL', 'unknown')),
            'term': os.getenv('TERM', 'unknown')
        }

        if self.platform == 'termux':
            info['platform'] = 'Termux (Android)'
        elif self.platform == 'windows':
            info['platform'] = f"Windows {platform.version()}"
        else:
            info['platform'] = f"{info['os']} {platform.machine()}"

        return info

    def get_uptime(self):
        try:
            if self.platform == 'windows':
                cmd = 'wmic os get lastbootuptime'
                uptime_sec = int(subprocess.check_output(cmd).decode().split()[1])
                boot_time = datetime.strptime(str(uptime_sec), '%Y%m%d%H%M%S')
                return str(datetime.now() - boot_time).split('.')[0]
            else:
                with open('/proc/uptime', 'r') as f:
                    uptime_sec = float(f.readline().split()[0])
                    return str(timedelta(seconds=uptime_sec)).split('.')[0]
        except:
            return "unknown"

    def display_banner(self):
        """Main banner display"""
        sys_info = self.get_system_info()

        print(f"\n\033[{self.colors['primary']}m{' Tech Byte Terminal ':=^{self.width}}\033[0m")
        print(f"\033[{self.colors['text']}mUser: \033[1m{self.config['username']}\033[0m".center(self.width))
        print(f"\033[{self.colors['secondary']}m{'-' * self.width}\033[0m")

        info_lines = [
            f"Platform: {sys_info['platform']}",
            f"Hostname: {sys_info['hostname']}",
            f"OS: {sys_info['os']} {sys_info['kernel']}",
            f"Uptime: {sys_info['uptime']}",
            f"Shell: {sys_info['shell']}",
            f"Terminal: {sys_info['term']}"
        ]

        for line in info_lines:
            print(f"\033[{self.colors['text']}m{line.center(self.width)}\033[0m")

        print(f"\033[{self.colors['primary']}m{'=' * self.width}\033[0m")
        print("\033[38;5;208mhttps://github.com/yourusername/techbyte\033[0m".center(self.width))


def main():
    parser = argparse.ArgumentParser(description='Tech Byte Terminal Banner')
    parser.add_argument('--change-name', action='store_true', help='Change username')
    args = parser.parse_args()

    banner = TechByteBanner()
    if args.change_name:
        banner.prompt_username(banner.config)
        # Save new config
        config_path = os.path.expanduser('~/.config/techbyte/config.json')
        with open(config_path, 'w') as f:
            json.dump(banner.config, f, indent=4)
    banner.display_banner()


if __name__ == "__main__":
    main()