# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "thai_utils"
app_title = "Thai Utils"
app_publisher = "Your Name"
app_description = "Thai language utilities for Frappe/ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "your@email.com"
app_license = "MIT"

# Installation
# ------------
after_install = "thai_utils.install.after_install"

# Add Jinja filters
jinja = {
    "filters": [
        "thai_utils.utils.currency_to_thai_words",
        "thai_utils.utils.thai_baht",
        "thai_utils.utils.format_thai_date",
        "thai_utils.utils.thai_date"
    ]
}
