import json
import os
import argparse

def generate_config(ip, port, user_id, password, realm='', ip2='', port2='', domain1='', domain2=''):
    config = {
        "ip": ip,
        "port": str(port),
        "id": user_id,
        "password": password,
        "realm": realm,
        "ip2": ip2,
        "port2": str(port2) if port2 else "",
        "domain1": domain1,
        "domain2": domain2,
        "data": []
    }
    
    file_name = "HyteraIP.json"
    with open(file_name, 'w') as f:
        json.dump(config, f, indent=4)
    
    print(f"Successfully generated {file_name}")
    print("\nTo push this file to your device, run the following command:")
    print(f"adb push {file_name} /sdcard/{file_name}")
    print("\nAfter pushing, please restart the application.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate HyteraIP.json configuration file.")
    parser.add_argument("--ip", required=True, help="Server IP address")
    parser.add_argument("--port", required=True, help="Server Port")
    parser.add_argument("--id", required=True, help="User ID (without @domain)")
    parser.add_argument("--pwd", required=True, help="Password")
    parser.add_argument("--realm", default="", help="Business ID / Realm (optional)")
    parser.add_argument("--ip2", default="", help="Backup Server IP (optional)")
    parser.add_argument("--port2", default="", help="Backup Server Port (optional)")
    parser.add_argument("--domain1", default="", help="Server Domain 1 (optional)")
    parser.add_argument("--domain2", default="", help="Server Domain 2 (optional)")

    args = parser.parse_args()
    
    generate_config(
        args.ip, args.port, args.id, args.pwd, 
        args.realm, args.ip2, args.port2, 
        args.domain1, args.domain2
    )
