#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )

    # This allows easy placement of apps within the interior
    # website_v2 directory.
    current_path = Path(__file__).parent.resolve()
    sys.path.append(str(current_path / "website_v2"))

    print(sys.argv)
    execute_from_command_line(sys.argv)
