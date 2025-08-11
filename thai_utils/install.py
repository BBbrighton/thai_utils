# -*- coding: utf-8 -*-
# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
import subprocess
import sys


def after_install():
    """Install pythainlp after app installation"""
    frappe.log("Installing pythainlp library...")
    
    try:
        # Try to import pythainlp to check if it's already installed
        import pythainlp
        frappe.log("pythainlp is already installed")
    except ImportError:
        # Install pythainlp using pip
        frappe.log("pythainlp not found, installing...")
        
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "pythainlp>=4.0.0"
            ])
            frappe.log("Successfully installed pythainlp")
            
            # Import to verify installation
            import pythainlp
            frappe.log(f"pythainlp version {pythainlp.__version__} installed successfully")
            
        except subprocess.CalledProcessError as e:
            frappe.log(f"Failed to install pythainlp: {str(e)}")
            frappe.throw(
                "Failed to install pythainlp library. "
                "Please install manually: ./env/bin/pip install pythainlp"
            )
