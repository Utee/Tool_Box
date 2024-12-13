from scanner import scan_single_target, scan_multiple_targets
from report_generator import save_results_to_file

def main_menu():
    print("\nNetwork Vulnerability Scanner")
    print("1. Single Target Scan")
    print("2. Range of IPs Scan")
    print("3. Export Results to JSON")
    print("4. Exit")
    choice = input("Choose an option: ")
    return choice

if __name__ == "__main__":
    scan_results = {}

    while True:
        choice = main_menu()
        
        if choice == "1":
            ip = input("Enter target IP address: ")
            port_range = input("Enter port range (e.g., 1-1024): ")
            scan_results = scan_single_target(ip, port_range)
        
        elif choice == "2":
            ip_range = input("Enter target IP range (e.g., 192.168.1.1-192.168.1.10): ")
            port_range = input("Enter port range (e.g., 1-1024): ")
            scan_results = scan_multiple_targets(ip_range, port_range)
        
        elif choice == "3":
            filename = input("Enter the filename to save results (e.g., results.json): ")
            save_results_to_file(scan_results, filename)
        
        elif choice == "4":
            print("Exiting the scanner. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
