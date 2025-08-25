#!/bin/sh
set -e
python check_db.py
exec python -u run.py
