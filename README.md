# Thai Utils

Simple Thai language utilities for Frappe/ERPNext using pythainlp library

## Features

- Convert numbers/currency to Thai words using pythainlp's bahttext function
- Format dates in Thai with Buddhist Era (พ.ศ.) using pythainlp's thai_strftime
- **Automatic installation of pythainlp library** - no manual installation needed!

## Installation

```bash
cd ~/frappe-bench

# Get the app - pythainlp will be installed automatically
bench get-app thai_utils /path/to/thai_utils

# Install the app to your site
bench --site your-site install-app thai_utils
```

That's it! The pythainlp library will be installed automatically during app installation.

## Usage in Print Formats

### Currency to Thai Words
```jinja
<!-- Convert currency to Thai words -->
<p>จำนวนเงิน: {{ doc.grand_total }}</p>
<p>ตัวอักษร: {{ doc.grand_total | currency_to_thai_words }}</p>

<!-- Or use shorter alias -->
<p>ตัวอักษร: {{ doc.grand_total | thai_baht }}</p>
```

Example:
- Input: `1111.11`
- Output: `หนึ่งพันหนึ่งร้อยสิบเอ็ดบาทสิบเอ็ดสตางค์`

### Thai Date Formatting
```jinja
<!-- Default format: 1 มกราคม 2568 -->
<p>วันที่: {{ doc.posting_date | thai_date }}</p>

<!-- Short month: 1 ม.ค. 2568 -->
<p>วันที่: {{ doc.posting_date | thai_date('%-d %b %Y') }}</p>

<!-- With day name: วันจันทร์ 1 มกราคม 2568 -->
<p>วันที่: {{ doc.posting_date | thai_date('%A %-d %B %Y') }}</p>

<!-- Numeric format: 1/1/2568 -->
<p>วันที่: {{ doc.posting_date | thai_date('%-d/%m/%Y') }}</p>
```

## Usage in Python

```python
from thai_utils.utils import currency_to_thai_words, format_thai_date

# Convert amount to Thai words
thai_text = currency_to_thai_words(1111.11)
# Result: หนึ่งพันหนึ่งร้อยสิบเอ็ดบาทสิบเอ็ดสตางค์

# Format date in Thai
thai_date = format_thai_date('2025-01-15')
# Result: 15 มกราคม 2568

# With custom format
thai_date = format_thai_date('2025-01-15', '%A %-d %B %Y')
# Result: วันพุธ 15 มกราคม 2568
```

## Usage in Client Scripts

```javascript
// Convert currency
frappe.call({
    method: 'thai_utils.utils.currency_to_thai_words',
    args: {
        amount: 1111.11
    },
    callback: function(r) {
        console.log(r.message);
        // หนึ่งพันหนึ่งร้อยสิบเอ็ดบาทสิบเอ็ดสตางค์
    }
});

// Format date
frappe.call({
    method: 'thai_utils.utils.format_thai_date',
    args: {
        date: '2025-01-15',
        fmt: '%-d %B %Y'
    },
    callback: function(r) {
        console.log(r.message);
        // 15 มกราคม 2568
    }
});
```

## Format String Reference

Common format codes for `thai_date`:
- `%A` - Full weekday name (วันจันทร์, วันอังคาร, etc.)
- `%a` - Abbreviated weekday name (จ., อ., etc.)
- `%B` - Full month name (มกราคม, กุมภาพันธ์, etc.)
- `%b` - Abbreviated month name (ม.ค., ก.พ., etc.)
- `%d` - Day of month with leading zero (01-31)
- `%-d` - Day of month without leading zero (1-31)
- `%m` - Month number with leading zero (01-12)
- `%Y` - Year in Buddhist Era (2568)
- `%y` - Year without century (68)

## Troubleshooting

If you encounter any issues with pythainlp installation, you can manually install it:

```bash
cd ~/frappe-bench
./env/bin/pip install pythainlp>=4.0.0
```

## License

MIT
