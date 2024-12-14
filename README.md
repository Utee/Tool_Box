# Tool_Box (Network Vulnerability Scanner)

A Python-based Network Vulnerability Scanner designed to identify open ports and running services on target hosts within a network. This tool is useful for understanding the security posture of a network by detecting potential vulnerabilities.

## Features

1. **Single Target Scan**: Scan a specific IP address for open ports and services.
2. **IP Range Scan**: Scan multiple IP addresses in a given range.
3. **Export Results**: Save scan results to a JSON file for analysis.
4. **Real-Time Progress Updates**: See the scanning progress for large target ranges.
5. **Extensible Architecture**: Ready for integration with vulnerability databases (e.g., CVE).

## Installation

### Prerequisites
- Python 3.7+
- `nmap` installed on your system.

To install Nmap on macOS, run:
```bash
brew install nmap
```

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/utee/tool_box.git
   cd tool_box
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scanner using the following command:
```bash
python main.py
```

### Menu Options
1. **Single Target Scan**: Enter a single IP address and a port range (e.g., `1-1024`).
2. **Range of IPs Scan**: Provide an IP range (e.g., `192.168.1.1-192.168.1.10`) and a port range.
3. **Export Results**: Save scan results to a JSON file for further analysis.
4. **Exit**: Exit the application.

### Example
**Single Target Scan**:
```
Enter target IP address: 192.168.1.1
Enter port range (e.g., 1-1024): 1-1024
Scanning 192.168.1.1 on ports 1-1024...
Results:
{
    "192.168.1.1": {
        "state": "up",
        "protocols": {
            "tcp": {
                "22": {
                    "state": "open",
                    "name": "ssh"
                },
                "80": {
                    "state": "open",
                    "name": "http"
                }
            }
        }
    }
}
```

**Save Results to JSON**:
```
Enter the filename to save results (e.g., results.json): scan_results.json
Results successfully saved to scan_results.json
```

## File Structure
```
tool_box/
├── venv/                  
├── main.py                
├── scanner.py             
├── report_generator.py    
├── requirements.txt       
└── README.md              
```

## Disclaimer
This tool is for **educational purposes only**. Use it only on networks you own or have explicit permission to scan. Unauthorized scanning of networks is illegal and unethical.

## Future Improvements
1. Integrate CVE databases for mapping detected services to known vulnerabilities.
2. Add real-time alerts for critical vulnerabilities.
3. Develop a web interface for easier usage.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.
