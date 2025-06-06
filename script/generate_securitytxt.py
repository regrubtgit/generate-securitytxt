# generate_securitytxt.py

import argparse
from datetime import datetime, timedelta
import os

def prompt_or_default(prompt_text, default=""):
    value = input(f"{prompt_text} [{default}]: ").strip()
    return value if value else default

def generate_securitytxt(contact, expires, encryption="", acknowledgment="", policy="", hiring="", preferred_languages="en"):
    lines = []

    if contact:
        lines.append(f"Contact: {contact}")
    if expires:
        lines.append(f"Expires: {expires}")
    if encryption:
        lines.append(f"Encryption: {encryption}")
    if acknowledgment:
        lines.append(f"Acknowledgments: {acknowledgment}")
    if policy:
        lines.append(f"Policy: {policy}")
    if hiring:
        lines.append(f"Hiring: {hiring}")
    if preferred_languages:
        lines.append(f"Preferred-Languages: {preferred_languages}")

    return "\n".join(lines) + "\n"

def main():
    parser = argparse.ArgumentParser(description="Generate a security.txt file (RFC 9116)")
    parser.add_argument("--contact", help="Contact email or URL", default="")
    parser.add_argument("--expires", help="Expiration date (RFC3339)", default="")
    parser.add_argument("--encryption", help="Link to PGP key", default="")
    parser.add_argument("--ack", help="Acknowledgments page", default="")
    parser.add_argument("--policy", help="Security policy URL", default="")
    parser.add_argument("--hiring", help="Security hiring page", default="")
    parser.add_argument("--languages", help="Preferred languages", default="en")
    parser.add_argument("--output", help="Output file", default="security.txt")
    parser.add_argument("--interactive", help="Run in interactive mode", action="store_true")

    args = parser.parse_args()

    if args.interactive:
        print("Running in interactive mode...\n")
        contact = prompt_or_default("Contact (email or URL)", args.contact)
        default_exp = (datetime.utcnow() + timedelta(days=365)).isoformat() + "Z"
        expires = prompt_or_default("Expires (RFC3339)", args.expires or default_exp)
        encryption = prompt_or_default("Encryption key URL", args.encryption)
        ack = prompt_or_default("Acknowledgments URL", args.ack)
        policy = prompt_or_default("Policy URL", args.policy)
        hiring = prompt_or_default("Hiring URL", args.hiring)
        languages = prompt_or_default("Preferred Languages", args.languages)
    else:
        contact = args.contact
        expires = args.expires or (datetime.utcnow() + timedelta(days=365)).isoformat() + "Z"
        encryption = args.encryption
        ack = args.ack
        policy = args.policy
        hiring = args.hiring
        languages = args.languages

    output = generate_securitytxt(contact, expires, encryption, ack, policy, hiring, languages)
    with open(args.output, "w") as f:
        f.write(output)
    print(f"\n✅ security.txt generated and saved to {args.output}")

if __name__ == "__main__":
    main()
