#!/usr/bin/env python3
"""Byte-level mojibake repair: UTF-8 read as Latin-1/CP1252 then re-encoded."""
import os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# (mojibake bytes, correct bytes)
REPLACEMENTS = [
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', '—'.encode('utf-8')),  # â€" -> —
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9c', '–'.encode('utf-8')),  # â€" -> –
    (b'\xc3\xa2\xe2\x82\xac\xe2\x84\xa2', '’'.encode('utf-8')),  # â€™ -> '
    (b'\xc3\xa2\xe2\x82\xac\xcb\x9c',     '‘'.encode('utf-8')),  # â€˜ -> '
    (b'\xc3\xa2\xe2\x82\xac\xc5\x93',     '“'.encode('utf-8')),  # â€œ -> "
    (b'\xc3\xa2\xe2\x82\xac\xc2\x9d',     '”'.encode('utf-8')),  # alt right quote
    (b'\xc3\xa2\xe2\x82\xac\xc2\x9c',     '“'.encode('utf-8')),  # alt left quote
    (b'\xc3\xa2\xe2\x80\xa0\xe2\x80\x99', '→'.encode('utf-8')),  # â†' -> →
    (b'\xc3\xa2\xe2\x80\xa0\xe2\x80\x90', '←'.encode('utf-8')),  # â†� -> ←
    (b'\xc3\xa2\xe2\x82\xac\xe2\x80\xa2', '•'.encode('utf-8')),  # â€¢ -> •
    (b'\xc3\x82\xc2\xb7',                 '·'.encode('utf-8')),  # Â· -> ·
    (b'\xc3\x82\xc2\xa0',                 b' '),                       # Â  -> space
    (b'\xc3\xa2\xe2\x80\x9e\xe2\x80\xa2', '™'.encode('utf-8')),  # â„¢ trademark
    (b'\xc3\xa2\xe2\x80\x9e\xe2\x80\xa6', '…'.encode('utf-8')),  # â€¦ ellipsis
    # Fallback bare 'â€' often left after partial fix:
    (b'\xc3\xa2\xe2\x82\xac',             '—'.encode('utf-8')),  # bare â€ -> em (safest default)
]

ROOT = r'C:\Users\HP\benjisaiempire-site'
EXCLUDE_DIRS = {'_design', '_qa', 'node_modules', '.git'}
EXTENSIONS = {'.html', '.css', '.txt', '.xml'}

total_files = 0
total_subs = 0
files_changed = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for fn in filenames:
        ext = os.path.splitext(fn)[1].lower()
        if ext not in EXTENSIONS:
            continue
        full = os.path.join(dirpath, fn)
        with open(full, 'rb') as fh:
            data = fh.read()
        orig = data
        n = 0
        for src, dst in REPLACEMENTS:
            count = data.count(src)
            if count:
                data = data.replace(src, dst)
                n += count
        if data != orig:
            with open(full, 'wb') as fh:
                fh.write(data)
            files_changed.append((os.path.relpath(full, ROOT), n))
            total_subs += n
        total_files += 1

print(f'Scanned: {total_files}')
print(f'Files changed: {len(files_changed)}')
print(f'Total substitutions: {total_subs}')
for rel, n in files_changed[:30]:
    print(f'  {n:4d}  {rel}')
