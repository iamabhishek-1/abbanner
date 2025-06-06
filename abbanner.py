#!/usr/bin/env python3
# AbhiByte Terminal Banner - Cross-Platform (Windows, Linux, Termux)
# Now with user customization!

import os
import sys
import platform
import time
import random
import json
import argparse
from datetime import datetime, timedelta
import subprocess


class AbhiByteBanner:
    def __init__(self, name=None):
        self.platform = self.detect_platform()
        self.config = self.load_config()

        # Override name if provided
        if name:
            self.config['name'] = name

        self.colors = self.setup_colors()
        self.width = self.get_terminal_width()

    def detect_platform(self):
        if 'termux' in os.environ.get('PREFIX', ''):
            return 'termux'
        return platform.system().lower()

    def load_config(self):
        config_dir = os.path.expanduser('~/.config/abbanner')
        config_path = os.path.join(config_dir, 'config.json')

        default_config = {
            'name': 'AbhiByte',
            'style': 'modern',
            'show_animation': True,
            'color_scheme': 'auto'
        }

        try:
            os.makedirs(config_dir, exist_ok=True)
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    return json.load(f)
            else:
                with open(config_path, 'w') as f:
                    json.dump(default_config, f, indent=4)
                return default_config
        except Exception as e:
            print(f"Config error: {e}, using defaults")
            return default_config

    def setup_colors(self):
        schemes = {
            'day': {'primary': '38;5;27', 'secondary': '38;5;39', 'text': '38;5;255'},
            'night': {'primary': '38;5;54', 'secondary': '38;5;93', 'text': '38;5;253'},
            'matrix': {'primary': '38;5;40', 'secondary': '38;5;28', 'text': '38;5;46'},
            'abhibyte': {'primary': '38;5;208', 'secondary': '38;5;202', 'text': '38;5;229'}
        }

        if self.config['color_scheme'] == 'auto':
            hour = datetime.now().hour
            return schemes['night'] if 18 <= hour < 6 else schemes['day']
        return schemes.get(self.config['color_scheme'], schemes['day'])

    def get_terminal_width(self):
        try:
            return os.get_terminal_size().columns
        except:
            return 80

    def generate_ascii_art(self):
        arts = [
            r"""
  ___  _     _     _       ____        _      
 / _ \| |__ (_)___| |__   | __ ) _   _| |_ __ 
| | | | '_ \| / __| '_ \  |  _ \| | | | | '__|
| |_| | |_) | \__ \ | | | | |_) | |_| | | |   
 \___/|_.__// |___/_| |_| |____/ \__,_|_|_|  
          |__/                                
            """,
            r"""
    _    _       _     _       _____     _   
   / \  | |__   (_)___| |__   |_ _|_ _ | |_ 
  / _ \ | '_ \  | / __| '_ \   | || ' \| __|
 / ___ \| |_) | | \__ \ | | |  | || | || |_ 
/_/   \_\_.__/  |_|___/_| |_| |___|_||_|\__|
            """,
            r"""
 █████╗ ██████╗ ██╗  ██╗██╗██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗██║  ██║██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
███████║██████╔╝███████║██║██████╔╝ ╚████╔╝    ██║   █████╗  
██╔══██║██╔══██╗██╔══██║██║██╔══██╗  ╚██╔╝     ██║   ██╔══╝  
██║  ██║██║  ██║██║  ██║██║██████╔╝   ██║      ██║   ███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝
            """
        ]
        return random.choice(arts)

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
            try:
                import android
                info['android_version'] = android.get_device().release
            except:
                info['android_version'] = 'unknown'
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
        except Exception as e:
            print(f"Uptime error: {e}", file=sys.stderr)
            return "unknown"

    def display(self):
        try:
            ascii_art = self.generate_ascii_art()
            sys_info = self.get_system_info()

            print(f"\033[{self.colors['primary']}m{ascii_art}\033[0m")
            print(f"\033[{self.colors['secondary']}m{'=' * self.width}\033[0m")

            info_text = [
                f"\033[{self.colors['text']}mWelcome \033[1m{self.config['name']}\033[0m",
                f"\033[{self.colors['text']}mPlatform: \033[1m{sys_info['platform']}\033[0m",
                f"\033[{self.colors['text']}mKernel: \033[1m{sys_info['kernel']}\033[0m",
                f"\033[{self.colors['text']}mUptime: \033[1m{sys_info['uptime']}\033[0m",
                f"\033[{self.colors['text']}mShell: \033[1m{sys_info['shell']}\033[0m",
                f"\033[{self.colors['text']}mTerminal: \033[1m{sys_info['term']}\033[0m"
            ]

            for line in info_text:
                print(line.center(self.width))

            print(f"\033[{self.colors['secondary']}m{'=' * self.width}\033[0m")
            print(f"\033[{self.colors['primary']}mhttps://github.com/abhibyte\033[0m".center(self.width))

        except Exception as e:
            print(f"Display error: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description='AbhiByte Terminal Banner')
    parser.add_argument('--name', help='Set custom display name')
    parser.add_argument('--color', help='Color scheme (day/night/matrix/abhibyte)')
    args = parser.parse_args()

    banner = AbhiByteBanner(name=args.name)
    if args.color:
        banner.config['color_scheme'] = args.color
    banner.display()


if __name__ == "__main__":
    main()