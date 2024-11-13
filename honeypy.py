# Libraries
import argparse
from ssh_honeypot import *
from web_honeypot import *

# Parse Arguments

if __name__ == "__main__":
    parser = argparse.ArgumentParser() 

    parser.add_argument('-a','--address', type=str, required=True)
    parser.add_argument('-p','--port', type=int, required=True)
    parser.add_argument('-u', '--username', type=str)
    parser.add_argument('-w', '--password', type=str)

    parser.add_argument('-s', '--ssh', action="store_true")
    parser.add_argument('-wh', '--http', action="store_true")
    
    args = parser.parse_args()
    
    try:
        if args.ssh:
            print("[-] Running SSH Honeypot...")
            honeypot(args.address, args.port, args.username, args.password)

            if not args.username:
                username = None
            if not args.password:
                password = None
        elif args.http:
            print("[-] Running HTTP WordPress Honeypot...")

            if not args.username:
                args.username = "admin"
            if not args.password:
                args.password = "password"

            print(f"Port: {args.port} Username: {args.username} Password {args.password}")
            run_web_honeypot(args.port, args.username, args.password)
            pass
        else:
            print("[!] Choose a honeypot type (SSH --ssh) or (HTTP --http).")

    except:
        print("\n Exiting HONEYPY...\n")