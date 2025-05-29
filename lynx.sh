#!/bin/bash
# Lynx IP Scanner - Let's hack the network, bro!

# Colors
black="\033[1;30m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
nc="\033[0m"

# Output snippets (Metasploit vibes)
info="[${cyan}*${nc}] "
success="[${green}+${nc}] "
error="[${red}-${nc}] "
prompt="[${yellow}#${nc}] "

# URLs (split to deter edits)
gh_base="https://github"
gh_user="Resonex"
tg_base="https://t"
tg_chan="me/cyber_snipper"
wa_base="https://wa"
wa_num="+2348158848771/"
github="${gh_base}.com/${gh_user}"
telegram="${tg_base}.${tg_chan}"
website="${wa_base}.me/${wa_num}"

# Spinner
spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='🔥🌟⚡💥'
    while ps -p $pid > /dev/null; do
        local temp=${spinstr#?}
        printf " ${purple}[%c]${nc} " "$spinstr"
        spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b"
    done
    printf "   \b\b\b"
}

# Banner (bold LYNX, colorful, fun)
banner() {
    clear
    echo -e "${cyan}
    ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗
    ██╔══██╗╚██╗ ██╔╝████╗  ██║╚██╗██╔╝
    ██████╔╝ ╚████╔╝ ██╔██╗ ██║ ╚███╔╝ 
    ██╔═══╝   ╚██╔╝  ██║╚██╗██║  ██╔██╗ 
    ██║        ██║   ██║ ╚████║ ██╔╝ ██╗
    ╚═╝        ╚═╝   ╚═╝  ╚═══╝ ╚═╝  ╚═╝
${green}    IP Scanner v1.0 - Let’s Scan, Bro!${nc}"
    echo -e "${red}============================================================${nc}"
    echo -e "${yellow}       Lynx IP Scanner - Powered by Nmap Magic       ${nc}"
    echo -e "${red}============================================================${nc}"
    echo -e "${blue}       Created by: [Your Name] | Resonex Crew${nc}"
    echo -e "${green}       Github: ${cyan}${github}${nc}"
    echo -e "${green}       Telegram: ${cyan}${telegram}${nc}"
    echo -e "${purple}       Ready to rock? Let’s do this LEGALLY! 😎${nc}"
    sleep 5
    clear
}

# Notice
notice() {
    echo -e "${error}Yo, this tool’s for learnin’ only. Don’t be a bad guy!"
    echo
    read -p "${prompt}Cool with that? (y/n): " opt
    if [[ $opt =~ [Nn] ]]; then
        echo -e "${error}Peace out! Gotta agree to play nice."
        exit 0
    fi
    echo -e "${success}Sweet, let’s roll!"
    clear
}

# Video (GitHub repo)
video() {
    echo -e "${purple}============================================================${nc}"
    echo -e "${green}       Get Started with Lynx IP Scanner       ${nc}"
    echo -e "${purple}============================================================${nc}"
    echo
    echo -e "${info}Check our GitHub for the setup lowdown"
    echo -e "${success}Repo: ${cyan}${github}${nc}"
    xdg-open "${github}" &> /dev/null &
    read -p "${prompt}Done checkin’ the repo? (y/n): " opt
    if [[ $opt =~ [Nn] ]]; then
        echo -e "${error}Gotta peek at the repo first, bro!"
        exit 0
    fi
    echo -e "${success}Nice one, you’re ready!"
    clear
}

# Website
website() {
    echo -e "${blue}============================================================${nc}"
    echo -e "${green}       Hit Up Lynx Contact       ${nc}"
    echo -e "${blue}============================================================${nc}"
    echo
    echo -e "${info}Zappin’ to contact page..."
    xdg-open "${website}" &> /dev/null &
    sleep 3
    echo -e "${success}Contact page fired up!"
    clear
}

# Dependencies
deps() {
    echo -e "${red}============================================================${nc}"
    echo -e "${green}       Rockin’ the Install!       ${nc}"
    echo -e "${red}============================================================${nc}"
    echo
    echo -e "${info}Scannin’ for tools..."
    sleep 1
    if [ -d "/data/data/com.termux" ]; then
        echo -e "${success}Termux mode activated!"
        if ! command -v nmap &> /dev/null; then
            echo -e "${info}Grabbin’ Nmap..."
            pkg install nmap -y & spinner $!
        fi
        if ! command -v python &> /dev/null; then
            echo -e "${info}Snaggin’ Python..."
            pkg install python -y & spinner $!
        fi
        if ! python -c "import flask" &> /dev/null; then
            echo -e "${info}Poppin’ in Flask..."
            pip install flask & spinner $!
        fi
    else
        echo -e "${success}Linux mode, let’s go!"
        if [ "$EUID" -ne 0 ]; then
            echo -e "${error}Need sudo powers, bro!"
            exit 1
        fi
        if ! command -v nmap &> /dev/null; then
            echo -e "${info}Installin’ Nmap..."
            apt update &> /dev/null
            apt install nmap -y & spinner $!
        fi
        if ! command -v python3 &> /dev/null; then
            echo -e "${info}Gettin’ Python3..."
            apt install python3 python3-pip -y & spinner $!
        fi
        if ! python3 -c "import flask" &> /dev/null; then
            echo -e "${info}Addin’ Flask..."
            pip3 install flask & spinner $!
        fi
    fi
    echo -e "${success}All set, time to scan!"
    sleep 2
    clear
}

# Menu
menu() {
    clear
    echo -e "${cyan}
    ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗
    ██╔══██╗╚██╗ ██╔╝████╗  ██║╚██╗██╔╝
    ██████╔╝ ╚████╔╝ ██╔██╗ ██║ ╚███╔╝ 
    ██╔═══╝   ╚██╔╝  ██║╚██╗██║  ██╔██╗ 
    ██║        ██║   ██║ ╚████║ ██╔╝ ██╗
    ╚═╝        ╚═╝   ╚═╝  ╚═══╝ ╚═╝  ╚═╝
${green}    IP Scanner v1.0${nc}"
    echo -e "${yellow}============================================================${nc}"
    echo -e "${green}       Lynx IP Scanner - Let’s Hack the Network!       ${nc}"
    echo -e "${yellow}============================================================${nc}"
    echo
    echo -e "${cyan}=== Scan Options ===${nc}"
    echo -e "${white}1)${nc} Quick Scan 🚀"
    echo -e "${white}2)${nc} Detailed Scan 🔍"
    echo
    echo -e "${cyan}=== Settings ===${nc}"
    echo -e "${white}i)${nc} Change Output Dir (${yellow}$HOME/lynx_output${nc})"
    echo -e "${white}x)${nc} About Lynx 😎"
    echo -e "${white}m)${nc} More Tools 🛠️"
    echo -e "${white}0)${nc} Exit 👋"
    echo
    printf "${cyan}lynx${nc} > "
    read opt
}

# Start
start() {
    echo -e "${info}Firing up Lynx IP Scanner..."
    python3 app.py &> lynx.log &
    local pid=$!
    sleep 2
    if ps -p $pid > /dev/null; then
        echo -e "${success}Lynx is live at http://localhost:5000"
        echo -e "${info}Hit Ctrl+C to chill"
        echo -e "${info}Restart: bash lynx.sh"
        wait $pid
    else
        echo -e "${error}Oops, Lynx tripped! Check lynx.log"
        exit 1
    fi
}

# Main
stty -echoctl
trap "echo -e '\n${success}Catch ya later! Hit us up: ${telegram}'; exit" INT
export OUTPUT_DIR="$HOME/lynx_output"
mkdir -p "$OUTPUT_DIR"
banner
notice
video
website
deps
while true; do
    menu
    case $opt in
        1)
            echo -e "${info}Zappin’ off a Quick Scan..."
            start
            break
            ;;
        2)
            echo -e "${info}Diving deep with Detailed Scan..."
            start
            break
            ;;
        i)
            echo -e "${prompt}Where to save scans? "
            printf "${cyan}lynx${nc} > "
            read dir
            if [[ ! -d "$dir" ]]; then
                echo -e "${error}Bad dir, try again!"
                sleep 1
            else
                export OUTPUT_DIR="$dir"
                mkdir -p "$OUTPUT_DIR"
                echo -e "${success}Saves now goin’ to $dir"
                sleep 1
            fi
            ;;
        x)
            clear
            echo -e "${cyan}
    ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗
    ██╔══██╗╚██╗ ██╔╝████╗  ██║╚██╗██╔╝
    ██████╔╝ ╚████╔╝ ██╔██╗ ██║ ╚███╔╝ 
    ██╔═══╝   ╚██╔╝  ██║╚██╗██║  ██╔██╗ 
    ██║        ██║   ██║ ╚████║ ██╔╝ ██╗
    ╚═╝        ╚═╝   ╚═╝  ╚═══╝ ╚═╝  ╚═╝
${green}    IP Scanner v1.0${nc}"
            echo -e "${cyan}=== About Lynx IP Scanner ===${nc}"
            echo -e "${white}Tool: ${cyan}Lynx IP Scanner${nc}"
            echo -e "${white}Version: ${cyan}1.0${nc}"
            echo -e "${white}Description: ${cyan}IP Scanner powered by Nmap${nc}"
            echo -e "${white}Author: ${cyan}[Your Name]${nc}"
            echo -e "${white}Github: ${cyan}${github}${nc}"
            echo -e "${white}Website: ${cyan}${website}${nc}"
            echo -e "${white}Telegram: ${cyan}${telegram}${nc}"
            printf "${cyan}lynx${nc} > "
            read _
            ;;
        m)
            xdg-open "${telegram}" &> /dev/null &
            echo -e "${info}Checkin’ out more tools!"
            sleep 1
            ;;
        0)
            echo -e "${success}Lynx out! Stay awesome!"
            exit 0
            ;;
        *)
            echo -e "${error}Huh? Pick a real option!"
            sleep 1
            ;;
    esac
done
