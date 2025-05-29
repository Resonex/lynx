#!/bin/bash
# Lynx IP Scanner

# Colors
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
cyan="\033[1;36m"
white="\033[1;37m"
magenta="\033[1;35m"
nc="\033[0m"

# Output snippets (Metasploit-style)
info="${cyan}[*]${nc} "
success="${green}[+]${nc} "
error="${red}[-]${nc} "
prompt="${yellow}[#]${nc} "

# URLs
github="https://github.com/Resonex"
telegram="https://t.me/cyber_snipper"
website="https://wa.me/+2348158848771/"

# Spinner
spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\'
    while ps -p $pid > /dev/null; do
        local temp=${spinstr#?}
        printf "${cyan}[%c]${nc} " "$spinstr"
        spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b"
    done
    printf "   \b\b\b"
}

# Banner
banner() {
    clear
    echo -e "${cyan}
 ██▓   ▓██   ██▓ ███▄    █ ▒██   ██▒
▓██▒    ▒██  ██▒ ██ ▀█   █ ▒▒ █ █ ▒░
▒██░     ▒██ ██░▓██  ▀█ ██▒░░  █   ░
▒██░     ░ ▐██▓░▓██▒  ▐▌██▒ ░ █ █ ▒ 
░██████▒ ░ ██▒▓░▒██░   ▓██░▒██▒ ▒██▒
░ ▒░▓  ░  ██▒▒▒ ░ ▒░   ▒ ▒ ▒▒ ░ ░▓ ░
░ ░ ▒  ░▓██ ░▒░ ░ ░░   ░ ▒░░░   ░▒ ░
  ░ ░   ▒ ▒ ░░     ░   ░ ░  ░    ░  
    ░  ░░ ░              ░  ░    ░  
        ░ ░                         
${white}    IP Scanner v1.0${nc}"
    echo -e "${red}============================================================${nc}"
    echo -e "${green}       Lynx IP Scanner - Network Analysis with Nmap       ${nc}"
    echo -e "${red}============================================================${nc}"
    echo -e "${white}       Developed by: Resonex | Resonex Cybersecurity${nc}"
    echo -e "${yellow}       Github: ${cyan}${github}${nc}"
    echo -e "${yellow}       Telegram: ${cyan}${telegram}${nc}"
    echo -e "${magenta}       For educational purposes only.${nc}"
    sleep 5
    clear
}

# Notice
notice() {
    echo -e "${error}This tool is intended for educational purposes only. Unauthorized use is prohibited.${nc}"
    echo
    echo -e "${prompt}${yellow}Accept terms? (y/n):${nc} "
    read opt
    if [[ $opt =~ [Nn] ]]; then
        echo -e "${error}Exiting. Terms not accepted.${nc}"
        exit 0
    fi
    echo -e "${success}Terms accepted.${nc}"
    clear
}

# Video (GitHub repo)
video() {
    echo -e "${red}============================================================${nc}"
    echo -e "${green}       Lynx IP Scanner Setup Instructions       ${nc}"
    echo -e "${red}============================================================${nc}"
    echo
    echo -e "${info}${cyan}Opening setup guide: ${github}${nc}"
    xdg-open "${github}" > /dev/null 2>&1 &
    echo -e "${prompt}${yellow}Reviewed setup guide? (y/n):${nc} "
    read opt
    if [[ $opt =~ [Nn] ]]; then
        echo -e "${error}Exiting. Please review the setup guide.${nc}"
        exit 0
    fi
    echo -e "${success}Setup guide reviewed.${nc}"
    clear
}

# Website
website() {
    echo -e "${red}============================================================${nc}"
    echo -e "${green}       Lynx Contact Page       ${nc}"
    echo -e "${red}============================================================${nc}"
    echo
    echo -e "${info}${cyan}Opening contact page: ${website}${nc}"
    xdg-open "${website}" > /dev/null 2>&1 &
    sleep 1
    echo -e "${success}Contact page opened.${nc}"
    clear
}

# Dependencies
deps() {
    echo -e "${red}============================================================${nc}"
    echo -e "${green}       Installing Dependencies       ${nc}"
    echo -e "${red}============================================================${nc}"
    echo
    echo -e "${info}${cyan}Verifying dependencies...${nc}"
    sleep 1
    if [ -d "/data/data/com.termux" ]; then
        echo -e "${success}${green}Termux environment detected.${nc}"
        if ! command -v nmap > /dev/null 2>&1; then
            echo -e "${info}${cyan}Installing Nmap...${nc}"
            pkg install nmap -y & spinner $!
        fi
        if ! command -v python > /dev/null 2>&1; then
            echo -e "${info}${cyan}Installing Python...${nc}"
            pkg install python -y & spinner $!
        fi
        if ! python -c "import flask" > /dev/null 2>&1; then
            echo -e "${info}${cyan}Installing Flask...${nc}"
            pip install flask & spinner $!
        fi
    else
        echo -e "${success}${green}Linux environment detected.${nc}"
        if [ "$EUID" -ne 0 ]; then
            echo -e "${error}Please run with sudo.${nc}"
            exit 1
        fi
        if ! command -v nmap > /dev/null 2>&1; then
            echo -e "${info}${cyan}Installing Nmap...${nc}"
            apt update > /dev/null 2>&1
            apt install nmap -y & spinner $!
        fi
        if ! command -v python3 > /dev/null 2>&1; then
            echo -e "${info}${cyan}Installing Python3...${nc}"
            apt install python3 python3-pip -y & spinner $!
        fi
        if ! python3 -c "import flask" > /dev/null 2>&1; then
            echo -e "${info}${cyan}Installing Flask...${nc}"
            pip3 install flask & spinner $!
        fi
    fi
    echo -e "${success}${green}Dependencies installed.${nc}"
    sleep 1
    clear
}

# Menu
menu() {
    clear
    echo -e "${cyan}
 ██▓   ▓██   ██▓ ███▄    █ ▒██   ██▒
▓██▒    ▒██  ██▒ ██ ▀█   █ ▒▒ █ █ ▒░
▒██░     ▒██ ██░▓██  ▀█ ██▒░░  █   ░
▒██░     ░ ▐██▓░▓██▒  ▐▌██▒ ░ █ █ ▒ 
░██████▒ ░ ██▒▓░▒██░   ▓██░▒██▒ ▒██▒
░ ▒░▓  ░  ██▒▒▒ ░ ▒░   ▒ ▒ ▒▒ ░ ░▓ ░
░ ░ ▒  ░▓██ ░▒░ ░ ░░   ░ ▒░░░   ░▒ ░
  ░ ░   ▒ ▒ ░░     ░   ░ ░  ░    ░  
    ░  ░░ ░              ░  ░    ░  
        ░ ░                         
${white}    IP Scanner v1.0${nc}"
    echo -e "${red}============================================================${nc}"
    echo -e "${green}       Lynx IP Scanner       ${nc}"
    echo -e "${red}============================================================${nc}"
    echo
    echo -e "${cyan}=== Options ===${nc}"
    echo -e "${white}i)${nc} ${yellow}Change Output Directory (${HOME}/lynx_output)${nc}"
    echo -e "${white}x)${nc} ${yellow}About${nc}"
    echo -e "${white}m)${nc} ${yellow}More Tools${nc}"
    echo -e "${white}0)${nc} ${yellow}Exit${nc}"
    echo
    echo -e "${prompt}${cyan}lynx >${nc} "
    read opt
}

# Start
start() {
    echo -e "${info}${cyan}Starting Lynx IP Scanner...${nc}"
    python3 app.py > lynx.log 2>&1 &
    local pid=$!
    sleep 2
    if ps -p $pid > /dev/null; then
        echo -e "${success}${green}Running at http://localhost:5000${nc}"
        echo -e "${info}${cyan}Press Ctrl+C to stop${nc}"
        echo -e "${info}${cyan}Restart: bash lynx.sh${nc}"
        wait $pid
    else
        echo -e "${error}Failed to start. Check lynx.log${nc}"
        exit 1
    fi
}

# Main
stty -echoctl
trap "echo -e '\n${success}${green}Terminated. Contact: ${telegram}${nc}'; exit" INT
export OUTPUT_DIR="$HOME/lynx_output"
mkdir -p "$OUTPUT_DIR" 2>/dev/null
banner
notice
video
website
deps
while true; do
    menu
    case $opt in
        i)
            echo -e "${prompt}${yellow}Enter Output Directory:${nc} "
            echo -e "${prompt}${cyan}lynx >${nc} "
            read dir
            if [[ ! -d "$dir" ]]; then
                echo -e "${error}Invalid directory.${nc}"
                sleep 1
            else
                export OUTPUT_DIR="$dir"
                mkdir -p "$OUTPUT_DIR" 2>/dev/null
                echo -e "${success}${green}Output directory set to $dir${nc}"
                sleep 1
            fi
            ;;
        x)
            clear
            echo -e "${cyan}
 ██▓   ▓██   ██▓ ███▄    █ ▒██   ██▒
▓██▒    ▒██  ██▒ ██ ▀█   █ ▒▒ █ █ ▒░
▒██░     ▒██ ██░▓██  ▀█ ██▒░░  █   ░
▒██░     ░ ▐██▓░▓██▒  ▐▌██▒ ░ █ █ ▒ 
░██████▒ ░ ██▒▓░▒██░   ▓██░▒██▒ ▒██▒
░ ▒░▓  ░  ██▒▒▒ ░ ▒░   ▒ ▒ ▒▒ ░ ░▓ ░
░ ░ ▒  ░▓██ ░▒░ ░ ░░   ░ ▒░░░   ░▒ ░
  ░ ░   ▒ ▒ ░░     ░   ░ ░  ░    ░  
    ░  ░░ ░              ░  ░    ░  
        ░ ░                         
${white}    IP Scanner v1.0${nc}"
            echo -e "${cyan}=== About Lynx IP Scanner ===${nc}"
            echo -e "${white}Tool:${nc} ${cyan}Lynx IP Scanner${nc}"
            echo -e "${white}Version:${nc} ${cyan}1.0${nc}"
            echo -e "${white}Description:${nc} ${cyan}Network scanner powered by Nmap${nc}"
            echo -e "${white}Author:${nc} ${cyan}Resonex${nc}"
            echo -e "${white}Github:${nc} ${cyan}${github}${nc}"
            echo -e "${white}Website:${nc} ${cyan}${website}${nc}"
            echo -e "${white}Telegram:${nc} ${cyan}${telegram}${nc}"
            echo -e "${prompt}${cyan}lynx >${nc} "
            read _
            ;;
        m)
            echo -e "${info}${cyan}Opening more tools: ${telegram}${nc}"
            xdg-open "${telegram}" > /dev/null 2>&1 &
            sleep 1
            ;;
        0)
            echo -e "${success}${green}Exiting Lynx IP Scanner.${nc}"
            exit 0
            ;;
        *)
            echo -e "${error}Invalid option.${nc}"
            sleep 1
            ;;
    esac
done
start
