#!/bin/bash

# Colors
GREEN="\033[1;32m"
RED="\033[1;31m"
BLUE="\033[1;34m"
NC="\033[0m"

# Spinner function for loading animation
spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " ${BLUE}[%c]${NC}  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

# Display LYNX banner
display_banner() {
    clear
    echo -e "${GREEN}"
    cat << "EOF"
 _     _   _   _   _  
| |   | | | \ | | | | 
| |   | | |  \| | | | 
| |   | | | . ` | | | 
| |___| | | |\  | |_| 
|_____/  |_| \_| (_)  
EOF
    echo -e "   IP Scanning Tool v1.0${NC}"
    echo -e "${BLUE}   Powered by Nmap${NC}"
    sleep 1
}

# Install dependencies based on OS
install_dependencies() {
    echo -e "${BLUE}Checking dependencies...${NC}"
    sleep 1

    if [ -d "/data/data/com.termux" ]; then
        # Termux environment
        echo -e "${GREEN}Detected Termux environment${NC}"
        if ! command -v nmap &> /dev/null; then
            echo "Installing Nmap..."
            pkg install nmap -y & spinner $!
        fi
        if ! command -v python &> /dev/null; then
            echo "Installing Python..."
            pkg install python -y & spinner $!
        fi
        if ! python -c "import flask" &> /dev/null; then
            echo "Installing Flask..."
            pip install flask & spinner $!
        fi
    else
        # Linux environment
        echo -e "${GREEN}Detected Linux environment${NC}"
        if [ "$EUID" -ne 0 ]; then
            echo -e "${RED}Please run as root or use sudo on Linux${NC}"
            exit 1
        fi
        if ! command -v nmap &> /dev/null; then
            echo "Installing Nmap..."
            apt update &> /dev/null
            apt install nmap -y & spinner $!
        fi
        if ! command -v python3 &> /dev/null; then
            echo "Installing Python3..."
            apt install python3 python3-pip -y & spinner $!
        fi
        if ! python3 -c "import flask" &> /dev/null; then
            echo "Installing Flask..."
            pip3 install flask & spinner $!
        fi
    fi
    echo -e "${GREEN}All dependencies installed successfully!${NC}"
    sleep 1
}

# Start the Flask app
start_app() {
    echo -e "${BLUE}Starting Lynx...${NC}"
    python3 app.py &> lynx.log &
    local pid=$!
    sleep 2
    if ps -p $pid > /dev/null; then
        echo -e "${GREEN}Lynx is running at http://localhost:5000${NC}"
        echo -e "${BLUE}Press Ctrl+C to stop${NC}"
        wait $pid
    else
        echo -e "${RED}Failed to start Lynx. Check lynx.log for details.${NC}"
        exit 1
    fi
}

# Main execution
display_banner
install_dependencies
start_app