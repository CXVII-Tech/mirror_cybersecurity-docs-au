#!/usr/bin/env python3
"""
Fix concatenated table rows by properly parsing and converting them.
"""

import re
from pathlib import Path

def parse_and_convert_table_rows(content):
    """Parse and convert all table rows in content."""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if line contains table row pattern: | Control | Guidance |
        if '|' in line and re.search(r'\| [^|]+\| [^|]+\|', line):
            # This line might have multiple table rows concatenated
            # Split by table row pattern
            parts = re.split(r'(\| [^|]+\| [^|]+\|)', line)
            
            current_control = None
            current_guidance = []
            
            for part in parts:
                part = part.strip()
                
                # Check if it's a table row
                if re.match(r'^\| [^|]+\| [^|]+\|$', part):
                    # Parse the row
                    match = re.match(r'^\| ([^|]+) \| ([^|]+) \|$', part)
                    if match:
                        control = match.group(1).strip()
                        guidance = match.group(2).strip()
                        
                        # Output previous control
                        if current_control:
                            result.append(f"- **{current_control}**")
                            for g in current_guidance:
                                # Split concatenated bullet points
                                if '  - ' in g:
                                    bullets = re.split(r'  - ', g)
                                    for bullet in bullets:
                                        if bullet.strip():
                                            result.append(f"  - {bullet.strip()}")
                                else:
                                    result.append(f"  - {g}")
                            result.append("")
                        
                        # Start new control
                        current_control = control
                        current_guidance = [guidance] if guidance else []
                elif part:
                    # This is continuation content (bullets or text)
                    if part.startswith('- ') or part.startswith('  - '):
                        # It's already a bullet, add as is
                        if current_guidance:
                            current_guidance.append(part)
                        else:
                            # No current control, just add as regular line
                            result.append(part)
                    elif '  - ' in part:
                        # Contains concatenated bullets
                        bullets = re.split(r'  - ', part)
                        for bullet in bullets:
                            if bullet.strip():
                                if current_guidance:
                                    current_guidance.append(f"  - {bullet.strip()}")
                                else:
                                    result.append(f"  - {bullet.strip()}")
                    else:
                        # Regular text - append to current guidance or add as line
                        if current_guidance:
                            current_guidance[-1] += ' ' + part
                        else:
                            result.append(part)
            
            # Output last control
            if current_control:
                result.append(f"- **{current_control}**")
                for g in current_guidance:
                    if '  - ' in g:
                        bullets = re.split(r'  - ', g)
                        for bullet in bullets:
                            if bullet.strip():
                                result.append(f"  - {bullet.strip()}")
                    else:
                        result.append(f"  - {g}")
                result.append("")
        else:
            result.append(line)
        
        i += 1
    
    return '\n'.join(result)

def main():
    workspace_dir = Path('/workspace/mirror_asd-acsc/e8_workspace')
    file_path = workspace_dir / 'E8 assessment process guide ML1.md'
    
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = parse_and_convert_table_rows(content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓ Fixed ML1.md")

if __name__ == '__main__':
    main()
