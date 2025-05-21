#!/bin/bash

# Version: 1.0
# Author: Thomas Burger
# Author e-mail: regrubt@gmail.com
# Name of the script: generate-securitytxt.sh
# License: MIT License

# Function to show help message
show_help() {
  cat << EOF
Usage: ./generate_securitytxt.sh [--help]

This script generates a valid security.txt file which you can place in the .well-known directory of your site.

Options:
  --help      Show this help message and exit

The script will prompt for all required and optional fields interactively.

For more information on the security.txt standard, see: https://www.rfc-editor.org/rfc/rfc9116
EOF
  exit 0
}

# Show help if --help is passed
if [[ "$1" == "--help" ]]; then
  show_help
fi

echo "=== Security.txt Generator ==="
echo "This script will generate a security.txt"
echo ""

# Create .well-known directory if it doesn't exist
mkdir -p .well-known
chmod 755 .well-known

# Required fields
read -p "Contact (e.g. mailto:security@example.com): " contact
read -p "Expires (e.g. 2025-12-31T23:59:00Z): " expires

# Optional fields
read -p "Encryption URL (optional): " encryption
read -p "Acknowledgments URL (optional): " acknowledgments
read -p "Preferred Languages (e.g. en, nl) (optional): " preferred_languages
read -p "Canonical URL (e.g. https://example.com/.well-known/security.txt) (optional): " canonical
read -p "Policy URL (optional): " policy
read -p "Hiring URL (optional): " hiring

# Output file
file=".well-known/security.txt"

# Start writing to file
{
  echo "# security.txt"
  echo "# This file contains contact information for reporting security issues."
  echo ""
  echo "Contact: $contact"
  echo "Expires: $expires"

  [[ -n "$encryption" ]] && echo "Encryption: $encryption"
  [[ -n "$acknowledgments" ]] && echo "Acknowledgments: $acknowledgments"
  [[ -n "$preferred_languages" ]] && echo "Preferred-Languages: $preferred_languages"
  [[ -n "$canonical" ]] && echo "Canonical: $canonical"
  [[ -n "$policy" ]] && echo "Policy: $policy"
  [[ -n "$hiring" ]] && echo "Hiring: $hiring"

  echo ""
  echo "# Dutch:"
  echo "# We waarderen het als beveiligingsonderzoekers kwetsbaarheden op een"
  echo "# verantwoorde manier melden. Neem contact met ons op via de bovenstaande"
  echo "# contactinformatie."
  echo ""
  echo "# English:"
  echo "# We appreciate responsible disclosure of security vulnerabilities."
  echo "# Please contact us using the information provided above."
} > "$file"

# Set permissions
chmod 644 "$file"

echo ""
echo "security.txt has been generated at .well-known/security.txt"

