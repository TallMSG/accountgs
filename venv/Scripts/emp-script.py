#!"D:\Studies\Python\Advanced Python\Accounts\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'emp==0.1.5','console_scripts','emp'
__requires__ = 'emp==0.1.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('emp==0.1.5', 'console_scripts', 'emp')()
    )
