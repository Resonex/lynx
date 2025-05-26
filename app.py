lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll = __name__, bool, Exception, print, str

from socket import socket as lllllllllIIllI, SOCK_STREAM as lIlIllllIlIIll, AF_INET as IIIIIlIlIIlIIl
from psutil import AccessDenied as IIlllIlIIllIlI, NoSuchProcess as IlIllIIllIllIl, process_iter as llIlIllIlIlIlI
from sys import exit as IIlIlllIlllIlI
from shutil import which as llIIlllllIIllI
from signal import signal as lIlIllIIIIIlIl, SIGINT as lIIllIIlIIIlll
from subprocess import run as IlllllIllllIll, CalledProcessError as llllIIlIIIlllI
from flask import Flask as lIlIlIIIIIlIll, render_template as IIlllIIIlIIIll, request as lIIIIlllIIIIll, jsonify as IIIlllllIlIIII
lIIIIlllIllIlllllI = lIlIlIIIIIlIll(lllllllllllllll)

def llIllIllIlIlIlllII(IIIllIlllIIllIlllI=5000):
    try:
        IIIIllllllIlIIIIII = lllllllllIIllI(IIIIIlIlIIlIIl, lIlIllllIlIIll)
        IIIIllllllIlIIIIII.settimeout(2)
        IIIlIlIlIIIllllIIl = IIIIllllllIlIIIIII.connect_ex(('localhost', IIIllIlllIIllIlllI))
        IIIIllllllIlIIIIII.close()
        if IIIlIlIlIIIllllIIl == 0:
            lllllllllllllII(f'Port {IIIllIlllIIllIlllI} is in use. Attempting to free it...')
            lIIIIIIlIIIIlIlIII = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
            for IlIlIllIIllllIlIIl in llIlIllIlIlIlI(['pid', 'name']):
                try:
                    for IIllIlllIIIllIlllI in IlIlIllIIllllIlIIl.connections():
                        if IIllIlllIIIllIlllI.laddr.IIIllIlllIIllIlllI == IIIllIlllIIllIlllI:
                            lllllllllllllII(f"Found process {IlIlIllIIllllIlIIl.info['name']} (PID: {IlIlIllIIllllIlIIl.info['pid']}) using port {IIIllIlllIIllIlllI}")
                            IlIlIllIIllllIlIIl.kill()
                            lllllllllllllII(f"Killed process {IlIlIllIIllllIlIIl.info['pid']}")
                            lIIIIIIlIIIIlIlIII = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
                            break
                except (IlIllIIllIllIl, IIlllIlIIllIlI):
                    continue
            if not lIIIIIIlIIIIlIlIII:
                lllllllllllllII(f'Could not free port {IIIllIlllIIllIlllI}. Try running with sudo or closing the process manually.')
                IIlIlllIlllIlI(1)
        return llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
    except lllllllllllllIl as llllIlIIIIIIIIIIlI:
        lllllllllllllII(f'Error checking port: {llllIlIIIIIIIIIIlI}')
        IIlIlllIlllIlI(1)

def lIlIIIlIlIlIIlIIll():
    return llIIlllllIIllI('nmap') is not None

def IIIlIIlIIIllIlllIl(IlIIllIIllIIIlIlIl, lIlIlIIlllIIIlIIll):
    lllllllllllllII('Shutting down Lynx server...')
    IIlIlllIlllIlI(0)
lIlIllIIIIIlIl(lIIllIIlIIIlll, IIIlIIlIIIllIlllIl)

@lIIIIlllIllIlllllI.route('/')
def IIIlIllIIlllIlllll():
    return IIlllIIIlIIIll('index.html')

@lIIIIlllIllIlllllI.route('/scan', methods=['POST'])
def IlIIlllIIIllIlllII():
    if not lIlIIIlIlIlIIlIIll():
        return (IIIlllllIlIIII({'error': 'nmap is not installed. Install it with: pkg install nmap'}), 500)
    IllIIIlIIllIIlllII = lIIIIlllIIIIll.json
    IIIIlIIlIlIlIIlllI = IllIIIlIIllIIlllII.get('target')
    lllIIIlllIIIIlIIll = IllIIIlIIllIIlllII.get('options', {})
    if not IIIIlIIlIlIlIIlllI:
        return (IIIlllllIlIIII({'error': 'No target specified.'}), 400)
    IlllIIIIlIlIllllII = IllIIIlIlIlIIlIIII(IIIIlIIlIlIlIIlllI, lllIIIlllIIIIlIIll)
    try:
        IIIlIlIlIIIllllIIl = IlllllIllllIll(IlllIIIIlIlIllllII, capture_output=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1), text=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1), check=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
        return IIIlllllIlIIII({'output': IIIlIlIlIIIllllIIl.stdout})
    except llllIIlIIIlllI as llllIlIIIIIIIIIIlI:
        IllIIlIIlIIlIlIlIl = llllIlIIIIIIIIIIlI.stderr
        if 'root' in IllIIlIIlIIlIlIlIl.lower() or 'permission' in IllIIlIIlIIlIlIlIl.lower():
            IllIIlIIlIIlIlIlIl = 'Some Nmap options require root access. Try running Termux with sudo.'
        return (IIIlllllIlIIII({'error': IllIIlIIlIIlIlIlIl}), 500)
    except lllllllllllllIl as llllIlIIIIIIIIIIlI:
        return (IIIlllllIlIIII({'error': f'Unexpected error: {llllllllllllIll(llllIlIIIIIIIIIIlI)}'}), 500)

def IllIIIlIlIlIIlIIII(IIIIlIIlIlIlIIlllI, lllIIIlllIIIIlIIll):
    IlllIIIIlIlIllllII = ['nmap']
    if 'scan_type' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['scan_type']:
        IlllIIIIlIlIllllII.append(lllIIIlllIIIIlIIll['scan_type'])
    if 'ports' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['ports']:
        IlllIIIIlIlIllllII.extend(['-p', lllIIIlllIIIIlIIll['ports']])
    if lllIIIlllIIIIlIIll.get('fast_scan'):
        IlllIIIIlIlIllllII.append('-F')
    if 'top_ports' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['top_ports']:
        IlllIIIIlIlIllllII.extend(['--top-ports', lllIIIlllIIIIlIIll['top_ports']])
    if lllIIIlllIIIIlIIll.get('port_ratio') and 'port_ratio_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['port_ratio_value']:
        IlllIIIIlIlIllllII.extend(['--port-ratio', lllIIIlllIIIIlIIll['port_ratio_value']])
    if lllIIIlllIIIIlIIll.get('exclude_ports') and 'exclude_ports_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['exclude_ports_value']:
        IlllIIIIlIlIllllII.extend(['--exclude-ports', lllIIIlllIIIIlIIll['exclude_ports_value']])
    if lllIIIlllIIIIlIIll.get('all_ports'):
        IlllIIIIlIlIllllII.append('--allports')
    if lllIIIlllIIIIlIIll.get('random_ports'):
        IlllIIIIlIlIllllII.append('--rport')
    if lllIIIlllIIIIlIIll.get('os_detection'):
        IlllIIIIlIlIllllII.append('-O')
    if lllIIIlllIIIIlIIll.get('version_detection'):
        IlllIIIIlIlIllllII.append('-sV')
    if 'version_intensity' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['version_intensity']:
        IlllIIIIlIlIllllII.extend(['--version-intensity', lllIIIlllIIIIlIIll['version_intensity']])
    if lllIIIlllIIIIlIIll.get('version_light'):
        IlllIIIIlIlIllllII.append('--version-light')
    if lllIIIlllIIIIlIIll.get('version_all'):
        IlllIIIIlIlIllllII.append('--version-all')
    if lllIIIlllIIIIlIIll.get('traceroute'):
        IlllIIIIlIlIllllII.append('--traceroute')
    if lllIIIlllIIIIlIIll.get('service_info'):
        IlllIIIIlIlIllllII.append('-sR')
    if lllIIIlllIIIIlIIll.get('dns_resolution'):
        IlllIIIIlIlIllllII.append('--dns-resolution')
    if 'timing' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['timing']:
        IlllIIIIlIlIllllII.append(lllIIIlllIIIIlIIll['timing'])
    if 'min_rate' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['min_rate']:
        IlllIIIIlIlIllllII.extend(['--min-rate', lllIIIlllIIIIlIIll['min_rate']])
    if 'max_rate' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['max_rate']:
        IlllIIIIlIlIllllII.extend(['--max-rate', lllIIIlllIIIIlIIll['max_rate']])
    if 'min_parallelism' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['min_parallelism']:
        IlllIIIIlIlIllllII.extend(['--min-parallelism', lllIIIlllIIIIlIIll['min_parallelism']])
    if 'max_parallelism' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['max_parallelism']:
        IlllIIIIlIlIllllII.extend(['--max-parallelism', lllIIIlllIIIIlIIll['max_parallelism']])
    if 'min_rtt_timeout' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['min_rtt_timeout']:
        IlllIIIIlIlIllllII.extend(['--min-rtt-timeout', lllIIIlllIIIIlIIll['min_rtt_timeout']])
    if 'max_rtt_timeout' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['max_rtt_timeout']:
        IlllIIIIlIlIllllII.extend(['--max-rtt-timeout', lllIIIlllIIIIlIIll['max_rtt_timeout']])
    if 'initial_rtt_timeout' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['initial_rtt_timeout']:
        IlllIIIIlIlIllllII.extend(['--initial-rtt-timeout', lllIIIlllIIIIlIIll['initial_rtt_timeout']])
    if 'scan_delay' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['scan_delay']:
        IlllIIIIlIlIllllII.extend(['--scan-delay', lllIIIlllIIIIlIIll['scan_delay']])
    if 'host_timeout' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['host_timeout']:
        IlllIIIIlIlIllllII.extend(['--host-timeout', lllIIIlllIIIIlIIll['host_timeout']])
    if 'min_hostgroup' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['min_hostgroup']:
        IlllIIIIlIlIllllII.extend(['--min-hostgroup', lllIIIlllIIIIlIIll['min_hostgroup']])
    if 'max_hostgroup' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['max_hostgroup']:
        IlllIIIIlIlIllllII.extend(['--max-hostgroup', lllIIIlllIIIIlIIll['max_hostgroup']])
    if 'spoof_mac' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['spoof_mac']:
        IlllIIIIlIlIllllII.extend(['--spoof-mac', lllIIIlllIIIIlIIll['spoof_mac']])
    if 'data_length' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['data_length']:
        IlllIIIIlIlIllllII.extend(['--data-length', lllIIIlllIIIIlIIll['data_length']])
    if lllIIIlllIIIIlIIll.get('badsum'):
        IlllIIIIlIlIllllII.append('--badsum')
    if 'ttl' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['ttl']:
        IlllIIIIlIlIllllII.extend(['--ttl', lllIIIlllIIIIlIIll['ttl']])
    if lllIIIlllIIIIlIIll.get('decoys') and 'decoys_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['decoys_value']:
        IlllIIIIlIlIllllII.extend(['-D', lllIIIlllIIIIlIIll['decoys_value']])
    if lllIIIlllIIIIlIIll.get('fragment'):
        IlllIIIIlIlIllllII.append('-f')
    if 'source_port' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['source_port']:
        IlllIIIIlIlIllllII.extend(['--source-port', lllIIIlllIIIIlIIll['source_port']])
    if lllIIIlllIIIIlIIll.get('ip_options') and 'ip_options_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['ip_options_value']:
        IlllIIIIlIlIllllII.extend(['--ip-options', lllIIIlllIIIIlIIll['ip_options_value']])
    if lllIIIlllIIIIlIIll.get('randomize_hosts'):
        IlllIIIIlIlIllllII.append('--randomize-hosts')
    if lllIIIlllIIIIlIIll.get('spoof_source') and 'spoof_source_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['spoof_source_value']:
        IlllIIIIlIlIllllII.extend(['-S', lllIIIlllIIIIlIIll['spoof_source_value']])
    if lllIIIlllIIIIlIIll.get('script') and 'script_args' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['script_args']:
        IlllIIIIlIlIllllII.extend(['--script', lllIIIlllIIIIlIIll['script_args']])
    if lllIIIlllIIIIlIIll.get('script_trace'):
        IlllIIIIlIlIllllII.append('--script-trace')
    if lllIIIlllIIIIlIIll.get('script_default'):
        IlllIIIIlIlIllllII.append('--script=default')
    if lllIIIlllIIIIlIIll.get('script_safe'):
        IlllIIIIlIlIllllII.append('--script=safe')
    if 'script_categories' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['script_categories']:
        IlllIIIIlIlIllllII.extend(['--script', lllIIIlllIIIIlIIll['script_categories']])
    if lllIIIlllIIIIlIIll.get('verbose'):
        IlllIIIIlIlIllllII.append('-v')
    if lllIIIlllIIIIlIIll.get('reason'):
        IlllIIIIlIlIllllII.append('--reason')
    if lllIIIlllIIIIlIIll.get('open'):
        IlllIIIIlIlIllllII.append('--open')
    if lllIIIlllIIIIlIIll.get('packet_trace'):
        IlllIIIIlIlIllllII.append('--packet-trace')
    if lllIIIlllIIIIlIIll.get('no_stylesheet'):
        IlllIIIIlIlIllllII.append('--no-stylesheet')
    if lllIIIlllIIIIlIIll.get('resolve_all'):
        IlllIIIIlIlIllllII.append('--resolve-all')
    if lllIIIlllIIIIlIIll.get('append_output'):
        IlllIIIIlIlIllllII.append('--append-output')
    if lllIIIlllIIIIlIIll.get('stats_every') and 'stats_interval' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['stats_interval']:
        IlllIIIIlIlIllllII.extend(['--stats-every', lllIIIlllIIIIlIIll['stats_interval']])
    if lllIIIlllIIIIlIIll.get('xml_output'):
        IlllIIIIlIlIllllII.extend(['-oX', '-'])
    if lllIIIlllIIIIlIIll.get('grep_output'):
        IlllIIIIlIlIllllII.extend(['-oG', '-'])
    if lllIIIlllIIIIlIIll.get('sn'):
        IlllIIIIlIlIllllII.append('-sn')
    if lllIIIlllIIIIlIIll.get('pe'):
        IlllIIIIlIlIllllII.append('-PE')
    if lllIIIlllIIIIlIIll.get('pp'):
        IlllIIIIlIlIllllII.append('-PP')
    if lllIIIlllIIIIlIIll.get('pm'):
        IlllIIIIlIlIllllII.append('-PM')
    if lllIIIlllIIIIlIIll.get('ps') and 'ps_ports' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['ps_ports']:
        IlllIIIIlIlIllllII.extend(['-PS', lllIIIlllIIIIlIIll['ps_ports']])
    if lllIIIlllIIIIlIIll.get('pa') and 'pa_ports' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['pa_ports']:
        IlllIIIIlIlIllllII.extend(['-PA', lllIIIlllIIIIlIIll['pa_ports']])
    if lllIIIlllIIIIlIIll.get('pu') and 'pu_ports' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['pu_ports']:
        IlllIIIIlIlIllllII.extend(['-PU', lllIIIlllIIIIlIIll['pu_ports']])
    if lllIIIlllIIIIlIIll.get('no_ping'):
        IlllIIIIlIlIllllII.append('-Pn')
    if lllIIIlllIIIIlIIll.get('disable_arp_ping'):
        IlllIIIIlIlIllllII.append('--disable-arp-ping')
    if lllIIIlllIIIIlIIll.get('privileged'):
        IlllIIIIlIlIllllII.append('--privileged')
    if lllIIIlllIIIIlIIll.get('unprivileged'):
        IlllIIIIlIlIllllII.append('--unprivileged')
    if lllIIIlllIIIIlIIll.get('send_eth'):
        IlllIIIIlIlIllllII.append('--send-eth')
    if lllIIIlllIIIIlIIll.get('send_ip'):
        IlllIIIIlIlIllllII.append('--send-ip')
    if lllIIIlllIIIIlIIll.get('iflist'):
        IlllIIIIlIlIllllII.append('-e')
    if lllIIIlllIIIIlIIll.get('6'):
        IlllIIIIlIlIllllII.append('-6')
    if lllIIIlllIIIIlIIll.get('system_dns'):
        IlllIIIIlIlIllllII.append('--system-dns')
    if lllIIIlllIIIIlIIll.get('dns_servers') and 'dns_servers_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['dns_servers_value']:
        IlllIIIIlIlIllllII.extend(['--dns-servers', lllIIIlllIIIIlIIll['dns_servers_value']])
    if lllIIIlllIIIIlIIll.get('mtu') and 'mtu_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['mtu_value']:
        IlllIIIIlIlIllllII.extend(['--mtu', lllIIIlllIIIIlIIll['mtu_value']])
    if lllIIIlllIIIIlIIll.get('data') and 'data_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['data_value']:
        IlllIIIIlIlIllllII.extend(['--data', lllIIIlllIIIIlIIll['data_value']])
    if lllIIIlllIIIIlIIll.get('data_string') and 'data_string_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['data_string_value']:
        IlllIIIIlIlIllllII.extend(['--data-string', lllIIIlllIIIIlIIll['data_string_value']])
    if lllIIIlllIIIIlIIll.get('proxies') and 'proxies_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['proxies_value']:
        IlllIIIIlIlIllllII.extend(['--proxies', lllIIIlllIIIIlIIll['proxies_value']])
    if lllIIIlllIIIIlIIll.get('spoof_idle') and 'spoof_idle_value' in lllIIIlllIIIIlIIll and lllIIIlllIIIIlIIll['spoof_idle_value']:
        IlllIIIIlIlIllllII.extend(['-sI', lllIIIlllIIIIlIIll['spoof_idle_value']])
    if lllIIIlllIIIIlIIll.get('dry_run'):
        IlllIIIIlIlIllllII.append('--dry-run')
    if lllIIIlllIIIIlIIll.get('skip_host_discovery'):
        IlllIIIIlIlIllllII.append('--skip-host-discovery')
    IlllIIIIlIlIllllII.append(IIIIlIIlIlIlIIlllI)
    return IlllIIIIlIlIllllII
if lllllllllllllll == '__main__':
    llIllIllIlIlIlllII(5000)
    lllllllllllllII('Starting Lynx server on http://localhost:5000')
    lIIIIlllIllIlllllI.run(host='0.0.0.0', port=5000, debug=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0))
