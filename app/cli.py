"""
Command-line interface for user handling
"""

import argparse
import sys
from typing import List, Optional

def create_parser() -> argparse.ArgumentParser:
    """
    Create the argument parser for the CLI
    
    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description='Find and store the user created',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    # Input source options
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument('--input', '-i', type=str,
                           help='Input user')
    input_group.add_argument('--file', '-f', type=str,
                           help='Input file containing users')

    
    # Output options
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Show detailed information')
    
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Only output the user (useful for scripting)')
    
    parser.add_argument('--format', '-F', choices=['text', 'json'], 
                       default='text', help='Output format (default: text)')
    
    parser.add_argument('--stats', '-s', action='store_true',
                       help='Show additional statistics')
    
    parser.add_argument('--version', action='version', 
                       version='User locator 1.0.0')
    
    return parser

def main():
    """Main entry point for the CLI application"""
    parser = create_parser()
    args = parser.parse_args()
    
    # Select and run 
    try:
        content = "Hello world"
        print(content)
    except Exception as e:
        print(f"Error processing input: {e}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
