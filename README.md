# LYNX Network scanner Gui

A sleek, web-based GUI for Nmap, Featuring 100+ Nmap commands, glassmorphism design, and a responsive interface optimized for Linux and Termux. Scan networks with ease.

<img src="https://i.ibb.co/xq57zQ7L/Picsart-25-05-26-04-56-36-071.png" alt="Logo" width="30%"/>

## Features
- 100+ Nmap commands with customizable options.
- Glassmorphism UI with light purple, cyan, and teal-green colors.
- Responsive design for desktop, mobile, and Termux.
- Save and copy scan configurations.
- Real-time scan animations and results display.
- Help modal with detailed usage instructions.

## Installation

### For Linux
1. Clone the repository:
   ```bash
   git clone https://github.com/resonex/lynx.git
   cd nmap-web-gui
   ```

2. Install dependencies:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip nmap -y
   pip3 install flask
   ```

3. Run the application:
   ```bash
   python3 app.py
   ```

4. Open in browser:
   ```bash
   xdg-open http://localhost:5000
   ```

### For Termux
1. Clone the repository:
   ```bash
   pkg install git -y
   git clone https://github.com/resonex/lynx.git
   cd nmap-web-gui
   ```

2. Install dependencies:
   ```bash
   pkg update && pkg upgrade -y
   pkg install python nmap -y
   pip install flask
   pip install psutil
   ```

3. Run the application:
   ```bash
   chmod +x lynx.py
   bash lynx.py
   ```

4. Open in browser:
   ```bash
   termux-open-url http://localhost:5000
   ```

## Usage
1. After installation, the tool will run on `http://localhost:5000`.
2. Enter your target (IP or domain) in the input field.
3. Select scan options from the dropdowns and checkboxes.
4. Click **Scan** to start the scan.
5. View results in the results section, with options to save or copy the command.

## Nmap Commands

Below is a comprehensive list of all 100+ Nmap commands supported by this tool, grouped by category with brief explanations.

### Host Discovery
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-sn`                   | Ping scan (no port scan).                        |
| `-Pn`                   | Treat all hosts as online (skip discovery).      |
| `-PS<ports>`            | TCP SYN ping (e.g., `-PS22,80`).                |
| `-PA<ports>`            | TCP ACK ping (e.g., `-PA22,80`).                |
| `-PU<ports>`            | UDP ping (e.g., `-PU53`).                       |
| `-PE`                   | ICMP echo request ping.                          |
| `-PP`                   | ICMP timestamp ping.                             |
| `-PM`                   | ICMP netmask request ping.                       |
| `-PO<protocol>`         | IP protocol ping (e.g., `-PO1,2`).              |
| `--disable-arp-ping`    | Disable ARP ping for host discovery.             |

### Port Scanning
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-sS`                   | TCP SYN scan (stealth scan).                     |
| `-sT`                   | TCP connect scan (full handshake).               |
| `-sU`                   | UDP scan.                                        |
| `-sA`                   | TCP ACK scan (for firewall rules).               |
| `-sW`                   | TCP Window scan (similar to ACK scan).           |
| `-sM`                   | TCP Maimon scan (FIN/ACK probe).                 |
| `-sN`                   | TCP Null scan (no flags set).                    |
| `-sF`                   | TCP FIN scan (FIN flag set).                     |
| `-sX`                   | TCP Xmas scan (FIN, PSH, URG flags set).         |
| `-p<ports>`             | Specify ports (e.g., `-p22,80` or `-p1-1000`).   |
| `-F`                    | Fast scan (top 100 ports).                       |
| `--top-ports <n>`       | Scan top `n` ports (e.g., `--top-ports 50`).     |

### Service and Version Detection
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-sV`                   | Version detection for services.                  |
| `--version-intensity <n>` | Set version scan intensity (0-9, e.g., `--version-intensity 5`). |
| `--version-light`       | Light version scan (intensity 2).                |
| `--version-all`         | Try all probes (intensity 9).                    |
| `--version-trace`       | Show version scan activity (debugging).          |

### OS Detection
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-O`                    | Enable OS detection.                             |
| `--osscan-limit`        | Limit OS detection to promising targets.         |
| `--osscan-guess`        | Guess OS more aggressively.                      |

### Timing and Performance
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-T<0-5>`               | Timing template (0=paranoid, 5=insane, e.g., `-T4`). |
| `--min-hostgroup <n>`   | Min parallel hosts (e.g., `--min-hostgroup 50`). |
| `--max-hostgroup <n>`   | Max parallel hosts (e.g., `--max-hostgroup 100`).|
| `--min-parallelism <n>` | Min parallel probes (e.g., `--min-parallelism 10`). |
| `--max-parallelism <n>` | Max parallel probes (e.g., `--max-parallelism 50`). |
| `--min-rtt-timeout <time>` | Min RTT timeout (e.g., `--min-rtt-timeout 100ms`). |
| `--max-rtt-timeout <time>` | Max RTT timeout (e.g., `--max-rtt-timeout 500ms`). |
| `--initial-rtt-timeout <time>` | Initial RTT timeout (e.g., `--initial-rtt-timeout 300ms`). |
| `--max-retries <n>`     | Max retries (e.g., `--max-retries 3`).           |
| `--host-timeout <time>` | Host timeout (e.g., `--host-timeout 30m`).       |
| `--scan-delay <time>`   | Delay between probes (e.g., `--scan-delay 50ms`).|

### Firewall/IDS Evasion
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-f`                    | Fragment packets (evade firewalls).              |
| `--mtu <n>`             | Set MTU for fragmentation (e.g., `--mtu 24`).    |
| `-D <decoy1,decoy2,...>` | Use decoys (e.g., `-D 1.1.1.1,2.2.2.2`).        |
| `-S <IP>`               | Spoof source IP (e.g., `-S 1.1.1.1`).           |
| `--source-port <port>`  | Spoof source port (e.g., `--source-port 53`).    |
| `--data-length <n>`     | Append random data (e.g., `--data-length 50`).   |
| `--ttl <n>`             | Set TTL (e.g., `--ttl 64`).                      |
| `--randomize-hosts`     | Randomize target host order.                     |
| `--spoof-mac <MAC>`     | Spoof MAC address (e.g., `--spoof-mac 00:11:22:33:44:55`). |
| `--badsum`              | Send packets with bad checksums.                 |

### Output Options
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-oN <file>`            | Normal output to file (e.g., `-oN scan.txt`).    |
| `-oX <file>`            | XML output to file (e.g., `-oX scan.xml`).       |
| `-oG <file>`            | Grepable output to file (e.g., `-oG scan.grep`). |
| `-oA <basename>`        | Output in all formats (e.g., `-oA scan`).        |
| `-v`                    | Increase verbosity (can repeat, e.g., `-vv`).    |
| `-d`                    | Increase debugging (can repeat, e.g., `-dd`).    |
| `--reason`              | Show reason for port states.                     |
| `--open`                | Show only open ports.                            |
| `--packet-trace`        | Show all packets sent/received.                  |
| `--iflist`              | List interfaces and routes.                      |

### Scripting (NSE)
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-sC`                   | Run default NSE scripts.                         |
| `--script <script>`     | Run specific script (e.g., `--script http-title`). |
| `--script-args <args>`  | Pass script arguments (e.g., `--script-args user=admin`). |
| `--script-trace`        | Show script activity (debugging).                |
| `--script-updatedb`     | Update NSE script database.                      |

### Miscellaneous
| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `-6`                    | Enable IPv6 scanning.                            |
| `-A`                    | Aggressive scan (OS, version, scripts, traceroute). |
| `--datadir <dir>`       | Custom data file location (e.g., `--datadir /path`). |
| `--send-eth`            | Send using raw Ethernet frames.                  |
| `--privileged`          | Assume user has full privileges.                 |
| `--unprivileged`        | Assume user lacks raw socket privileges.         |
| `-V`                    | Show Nmap version.                               |
| `-h`                    | Show help.                                       |
| `--dns-servers <servers>` | Custom DNS servers (e.g., `--dns-servers 8.8.8.8`). |
| `--system-dns`          | Use system DNS resolver.                         |
| `--traceroute`          | Run traceroute to target.                        |

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
