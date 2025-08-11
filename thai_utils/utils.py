# -*- coding: utf-8 -*-
# Thai Utilities for Frappe/ERPNext
# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

# Try to import pythainlp
try:
    from pythainlp.util import bahttext, thai_strftime
    PYTHAINLP_AVAILABLE = True
except ImportError:
    PYTHAINLP_AVAILABLE = False
    # Show error message in frappe UI
    import subprocess
    import sys
    
    def install_pythainlp():
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pythainlp>=4.0.0"])
            return True
        except:
            return False
    
    if not install_pythainlp():
        frappe.log("pythainlp is not installed. Installing it now...")


@frappe.whitelist()
def currency_to_thai_words(amount):
    """
    Convert currency amount to Thai words using pythainlp
    
    Examples:
    - 1111.11 → หนึ่งพันหนึ่งร้อยสิบเอ็ดบาทสิบเอ็ดสตางค์
    - 1000000 → หนึ่งล้านบาทถ้วน
    """
    if not PYTHAINLP_AVAILABLE:
        # Try to import again after installation attempt
        try:
            from pythainlp.util import bahttext
        except ImportError:
            frappe.throw("pythainlp library is not installed. Please run: bench --site your-site install-app thai_utils")
    
    if amount is None:
        return ''
    
    try:
        amount = float(amount)
    except (ValueError, TypeError):
        return ''
    
    return bahttext(amount)


# Shorter alias for use in print formats
def thai_baht(amount):
    """Alias for currency_to_thai_words for shorter syntax in print formats"""
    return currency_to_thai_words(amount)


@frappe.whitelist()
def format_thai_date(date, fmt='%-d %B %Y'):
    """
    Format date in Thai using pythainlp
    
    Args:
        date: Date to format
        fmt: Format string (default: '%-d %B %Y' = 1 มกราคม 2568)
             Common formats:
             - '%-d %B %Y' → 1 มกราคม 2568
             - '%-d %b %Y' → 1 ม.ค. 2568
             - '%A %-d %B %Y' → วันจันทร์ 1 มกราคม 2568
             - '%-d/%m/%Y' → 1/1/2568
    
    Returns:
        Thai formatted date string
    """
    if not PYTHAINLP_AVAILABLE:
        # Try to import again after installation attempt
        try:
            from pythainlp.util import thai_strftime
        except ImportError:
            frappe.throw("pythainlp library is not installed. Please run: bench --site your-site install-app thai_utils")
    
    if date is None:
        return ''
    
    # Convert string to datetime if needed
    if isinstance(date, str):
        date = frappe.utils.getdate(date)
    
    # thai_strftime automatically converts to Buddhist Era (พ.ศ.)
    return thai_strftime(date, fmt)


# Shorter alias
def thai_date(date, fmt='%-d %B %Y'):
    """Alias for format_thai_date for shorter syntax in print formats"""
    return format_thai_date(date, fmt)
