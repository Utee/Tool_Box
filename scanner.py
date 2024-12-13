import nmap

def scan_single_target(ip, port_range):
    scanner = nmap.PortScanner()
    print(f"Scanning {ip} on ports {port_range}...")
    scanner.scan(ip, port_range, '-v')
    
    results = {}
    for host in scanner.all_hosts():
        results[host] = {
            'state': scanner[host].state(),
            'protocols': {}
        }
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            results[host]['protocols'][proto] = {
                port: scanner[host][proto][port] for port in ports
            }
    return results

def scan_multiple_targets(ip_range, port_range):
    scanner = nmap.PortScanner()
    print(f"Scanning IP range {ip_range} on ports {port_range}...")
    
    results = {}
    for ip in ip_range.split('-'):  
        print(f"Scanning {ip}...")
        scanner.scan(ip, port_range, '-v')
        results[ip] = {
            'state': scanner[ip].state(),
            'protocols': {}
        }
        for proto in scanner[ip].all_protocols():
            ports = scanner[ip][proto].keys()
            results[ip]['protocols'][proto] = {
                port: scanner[ip][proto][port] for port in ports
            }
    return results
