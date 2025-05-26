import subprocess
import signal
import sys
import socket
import os
import psutil
from flask import Flask, render_template, request, jsonify
import shutil

app = Flask(__name__)

def check_and_free_port(port=5000):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex(('localhost', port))
        sock.close()

        if result == 0:
            print(f"Port {port} is in use. Attempting to free it...")
            freed = False
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    for conn in proc.connections():
                        if conn.laddr.port == port:
                            print(f"Found process {proc.info['name']} (PID: {proc.info['pid']}) using port {port}")
                            proc.kill()
                            print(f"Killed process {proc.info['pid']}")
                            freed = True
                            break
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            if not freed:
                print(f"Could not free port {port}. Try running with sudo or closing the process manually.")
                sys.exit(1)
        return True
    except Exception as e:
        print(f"Error checking port: {e}")
        sys.exit(1)

# Check if nmap is installed
def check_nmap():
    return shutil.which('nmap') is not None

# Handle Ctrl+C for clean shutdown
def signal_handler(sig, frame):
    print("Shutting down Lynx server...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    if not check_nmap():
        return jsonify({'error': 'nmap is not installed. Install it with: pkg install nmap'}), 500

    data = request.json
    target = data.get('target')
    options = data.get('options', {})

    if not target:
        return jsonify({'error': 'No target specified.'}), 400

    cmd = build_nmap_command(target, options)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return jsonify({'output': result.stdout})
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr
        if 'root' in error_msg.lower() or 'permission' in error_msg.lower():
            error_msg = 'Some Nmap options require root access. Try running Termux with sudo.'
        return jsonify({'error': error_msg}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

def build_nmap_command(target, options):
    cmd = ['nmap']
    
    # Scan Type
    if 'scan_type' in options and options['scan_type']:
        cmd.append(options['scan_type'])
    
    # Port Specifications
    if 'ports' in options and options['ports']:
        cmd.extend(['-p', options['ports']])
    if options.get('fast_scan'):
        cmd.append('-F')
    if 'top_ports' in options and options['top_ports']:
        cmd.extend(['--top-ports', options['top_ports']])
    if options.get('port_ratio') and 'port_ratio_value' in options and options['port_ratio_value']:
        cmd.extend(['--port-ratio', options['port_ratio_value']])
    if options.get('exclude_ports') and 'exclude_ports_value' in options and options['exclude_ports_value']:
        cmd.extend(['--exclude-ports', options['exclude_ports_value']])
    if options.get('all_ports'):
        cmd.append('--allports')
    if options.get('random_ports'):
        cmd.append('--rport')
    
    # Detection
    if options.get('os_detection'):
        cmd.append('-O')
    if options.get('version_detection'):
        cmd.append('-sV')
    if 'version_intensity' in options and options['version_intensity']:
        cmd.extend(['--version-intensity', options['version_intensity']])
    if options.get('version_light'):
        cmd.append('--version-light')
    if options.get('version_all'):
        cmd.append('--version-all')
    if options.get('traceroute'):
        cmd.append('--traceroute')
    if options.get('service_info'):
        cmd.append('-sR')
    if options.get('dns_resolution'):
        cmd.append('--dns-resolution')
    
    # Timing
    if 'timing' in options and options['timing']:
        cmd.append(options['timing'])
    if 'min_rate' in options and options['min_rate']:
        cmd.extend(['--min-rate', options['min_rate']])
    if 'max_rate' in options and options['max_rate']:
        cmd.extend(['--max-rate', options['max_rate']])
    if 'min_parallelism' in options and options['min_parallelism']:
        cmd.extend(['--min-parallelism', options['min_parallelism']])
    if 'max_parallelism' in options and options['max_parallelism']:
        cmd.extend(['--max-parallelism', options['max_parallelism']])
    if 'min_rtt_timeout' in options and options['min_rtt_timeout']:
        cmd.extend(['--min-rtt-timeout', options['min_rtt_timeout']])
    if 'max_rtt_timeout' in options and options['max_rtt_timeout']:
        cmd.extend(['--max-rtt-timeout', options['max_rtt_timeout']])
    if 'initial_rtt_timeout' in options and options['initial_rtt_timeout']:
        cmd.extend(['--initial-rtt-timeout', options['initial_rtt_timeout']])
    if 'scan_delay' in options and options['scan_delay']:
        cmd.extend(['--scan-delay', options['scan_delay']])
    if 'host_timeout' in options and options['host_timeout']:
        cmd.extend(['--host-timeout', options['host_timeout']])
    if 'min_hostgroup' in options and options['min_hostgroup']:
        cmd.extend(['--min-hostgroup', options['min_hostgroup']])
    if 'max_hostgroup' in options and options['max_hostgroup']:
        cmd.extend(['--max-hostgroup', options['max_hostgroup']])
    
    # Evasion
    if 'spoof_mac' in options and options['spoof_mac']:
        cmd.extend(['--spoof-mac', options['spoof_mac']])
    if 'data_length' in options and options['data_length']:
        cmd.extend(['--data-length', options['data_length']])
    if options.get('badsum'):
        cmd.append('--badsum')
    if 'ttl' in options and options['ttl']:
        cmd.extend(['--ttl', options['ttl']])
    if options.get('decoys') and 'decoys_value' in options and options['decoys_value']:
        cmd.extend(['-D', options['decoys_value']])
    if options.get('fragment'):
        cmd.append('-f')
    if 'source_port' in options and options['source_port']:
        cmd.extend(['--source-port', options['source_port']])
    if options.get('ip_options') and 'ip_options_value' in options and options['ip_options_value']:
        cmd.extend(['--ip-options', options['ip_options_value']])
    if options.get('randomize_hosts'):
        cmd.append('--randomize-hosts')
    if options.get('spoof_source') and 'spoof_source_value' in options and options['spoof_source_value']:
        cmd.extend(['-S', options['spoof_source_value']])
    
    # Scripting
    if options.get('script') and 'script_args' in options and options['script_args']:
        cmd.extend(['--script', options['script_args']])
    if options.get('script_trace'):
        cmd.append('--script-trace')
    if options.get('script_default'):
        cmd.append('--script=default')
    if options.get('script_safe'):
        cmd.append('--script=safe')
    if 'script_categories' in options and options['script_categories']:
        cmd.extend(['--script', options['script_categories']])
    
    # Output
    if options.get('verbose'):
        cmd.append('-v')
    if options.get('reason'):
        cmd.append('--reason')
    if options.get('open'):
        cmd.append('--open')
    if options.get('packet_trace'):
        cmd.append('--packet-trace')
    if options.get('no_stylesheet'):
        cmd.append('--no-stylesheet')
    if options.get('resolve_all'):
        cmd.append('--resolve-all')
    if options.get('append_output'):
        cmd.append('--append-output')
    if options.get('stats_every') and 'stats_interval' in options and options['stats_interval']:
        cmd.extend(['--stats-every', options['stats_interval']])
    if options.get('xml_output'):
        cmd.extend(['-oX', '-'])
    if options.get('grep_output'):
        cmd.extend(['-oG', '-'])
    
    # Host Discovery
    if options.get('sn'):
        cmd.append('-sn')
    if options.get('pe'):
        cmd.append('-PE')
    if options.get('pp'):
        cmd.append('-PP')
    if options.get('pm'):
        cmd.append('-PM')
    if options.get('ps') and 'ps_ports' in options and options['ps_ports']:
        cmd.extend(['-PS', options['ps_ports']])
    if options.get('pa') and 'pa_ports' in options and options['pa_ports']:
        cmd.extend(['-PA', options['pa_ports']])
    if options.get('pu') and 'pu_ports' in options and options['pu_ports']:
        cmd.extend(['-PU', options['pu_ports']])
    if options.get('no_ping'):
        cmd.append('-Pn')
    if options.get('disable_arp_ping'):
        cmd.append('--disable-arp-ping')
    
    # Miscellaneous
    if options.get('privileged'):
        cmd.append('--privileged')
    if options.get('unprivileged'):
        cmd.append('--unprivileged')
    if options.get('send_eth'):
        cmd.append('--send-eth')
    if options.get('send_ip'):
        cmd.append('--send-ip')
    if options.get('iflist'):
        cmd.append('-e')
    if options.get('6'):
        cmd.append('-6')
    if options.get('system_dns'):
        cmd.append('--system-dns')
    if options.get('dns_servers') and 'dns_servers_value' in options and options['dns_servers_value']:
        cmd.extend(['--dns-servers', options['dns_servers_value']])
    if options.get('mtu') and 'mtu_value' in options and options['mtu_value']:
        cmd.extend(['--mtu', options['mtu_value']])
    if options.get('data') and 'data_value' in options and options['data_value']:
        cmd.extend(['--data', options['data_value']])
    if options.get('data_string') and 'data_string_value' in options and options['data_string_value']:
        cmd.extend(['--data-string', options['data_string_value']])
    if options.get('proxies') and 'proxies_value' in options and options['proxies_value']:
        cmd.extend(['--proxies', options['proxies_value']])
    if options.get('spoof_idle') and 'spoof_idle_value' in options and options['spoof_idle_value']:
        cmd.extend(['-sI', options['spoof_idle_value']])
    if options.get('dry_run'):
        cmd.append('--dry-run')
    if options.get('skip_host_discovery'):
        cmd.append('--skip-host-discovery')
    
    cmd.append(target)
    return cmd

if __name__ == '__main__':
    check_and_free_port(5000)
    print("Starting Lynx server on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
