#!/usr/bin/env python3
"""
Final fix for concatenated table rows.
"""

import re
from pathlib import Path

def split_table_rows(line):
    """Split a line that contains multiple table rows."""
    # Pattern: | Control | Guidance |
    # We need to find all table row patterns and split them
    
    # Find all table row matches
    pattern = r'\| ([^|]+) \| ([^|]+) \|'
    matches = list(re.finditer(pattern, line))
    
    if len(matches) <= 1:
        return [line]
    
    # Split the line at table row boundaries
    result = []
    last_end = 0
    
    for i, match in enumerate(matches):
        start = match.start()
        end = match.end()
        
        # Get text before this match
        if start > last_end:
            before = line[last_end:start].strip()
            if before:
                result.append(before)
        
        # Add the table row
        result.append(match.group(0))
        last_end = end
    
    # Add remaining text
    if last_end < len(line):
        remaining = line[last_end:].strip()
        if remaining:
            result.append(remaining)
    
    return result

def process_file(file_path):
    """Process file to fix concatenated rows."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    result_lines = []
    i = 0
    fixed = 0
    
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Check if line has multiple table rows (more than 3 | characters suggests multiple rows)
        if line.count('|') >= 6 and '|' in line:
            # Try to split
            parts = split_table_rows(line)
            if len(parts) > 1:
                fixed += 1
                for part in parts:
                    result_lines.append(part)
            else:
                result_lines.append(line)
        else:
            result_lines.append(line)
        
        i += 1
    
    if fixed > 0:
        print(f"Split {fixed} concatenated line(s) in {file_path.name}")
    
    return '\n'.join(result_lines) + '\n'

def main():
    workspace_dir = Path('/workspace/mirror_asd-acsc/e8_workspace')
    file_path = workspace_dir / 'E8 assessment process guide ML1.md'
    
    if file_path.exists():
        new_content = process_file(file_path)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # Now run fix_all_remaining again
        import subprocess
        subprocess.run(['python3', '/workspace/fix_all_remaining.py'])

if __name__ == '__main__':
    main()
