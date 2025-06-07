#!/bin/bash

# Termux/Linux Banner Script by Tech Byte
# Features:
# 1. Displays a big bold "TECH BYTE" banner
# 2. Shows social media credits (Instagram and YouTube)
# 3. Prompts user to enter their username
# 4. Displays the username banner
# 5. Shows "Created by tech byte" credits in small size

# === Styling codes ===
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Check if figlet is installed, required for banners
if ! command -v figlet &> /dev/null
then
    echo -e "${RED}Error:${NC} figlet is required but not installed."
    echo "Please install figlet first."
    echo "On Termux: pkg install figlet"
    echo "On Debian/Ubuntu: sudo apt-get install figlet"
    exit 1
fi

# Clear screen
clear

# Display main "TECH BYTE" banner in green bold
echo -e "${GREEN}${BOLD}"
figlet -f big "TECH BYTE"
echo -e "${NC}"

# Show social media credits in bold
echo -e "${BOLD}Instagram:${NC} @tech_byte    ${BOLD}YouTube:${NC} @bytewithabhi"
echo ""

# Prompt user to enter username
read -p "Enter your username: " username

# Validate input: username cannot be empty
if [ -z "$username" ]; then
    echo -e "${RED}Error:${NC} Username cannot be empty. Exiting."
    exit 1
fi

# Clear screen before showing username banner
clear

# Show username banner in cyan bold
echo -e "${CYAN}${BOLD}"
figlet "$username"
echo -e "${NC}"

# Display created by tech byte credit in small size
echo -e "${BOLD}Created by tech byte${NC}"
echo "Instagram: @tech_byte"
echo "YouTube: @bytewithabhi"
