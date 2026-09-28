#!/usr/bin/env python3
import pathlib,runpy
R=pathlib.Path(__file__).resolve().parents[1]
v=(R/'VERSION').read_text().strip()
major=v.split('.')[0]
p=R/'scripts'/f'validate_{major}_0.py'
if not p.exists():
 raise SystemExit(f'No current major-release validator: {p.name}')
runpy.run_path(str(p),run_name='__main__')
