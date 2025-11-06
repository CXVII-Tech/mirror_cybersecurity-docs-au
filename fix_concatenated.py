#!/usr/bin/env python3
"""
Fix concatenated table rows.
"""

from pathlib import Path
import re

def process_file(file_path):
    """Fix concatenated table rows."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    result_lines = []
    i = 0
    fixed_count = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if line contains multiple table rows (multiple | Control | patterns)
        if '|' in line and line.count('|') >= 6:  # At least 2 table rows
            # Split by table row pattern: | Control | Guidance |
            # Look for pattern: | [text] | [text] |
            parts = re.split(r'(\|[^|]+\|[^|]+\|)', line)
            
            # Reconstruct properly
            new_lines = []
            for part in parts:
                part = part.strip()
                if part.startswith('|') and part.count('|') >= 3:
                    new_lines.append(part)
                elif part and not part.startswith('|'):
                    # This might be continuation content, check if it's bullet points
                    if part.startswith('- '):
                        new_lines.append(part)
                    else:
                        # Might be concatenated guidance
                        if new_lines:
                            new_lines[-1] += ' ' + part
                        else:
                            new_lines.append(part)
            
            if len(new_lines) > 1:
                fixed_count += 1
                result_lines.extend(new_lines)
            else:
                result_lines.append(line)
        else:
            result_lines.append(line)
        
        i += 1
    
    if fixed_count > 0:
        print(f"Fixed {fixed_count} concatenated line(s) in {file_path.name}")
    
    return '\n'.join(result_lines)

# Actually, let me take a simpler approach - just find and replace the specific problematic patterns
def fix_specific_issues(file_path):
    """Fix specific concatenated patterns."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern: | Control | Guidance |  - bullet | Control | Guidance |
    # We need to split these properly
    
    # Find lines with multiple table rows
    pattern = r'(\| [^|]+\| [^|]+\|)\s+(- [^|]+)\s+(\| [^|]+\| [^|]+\|)'
    
    def split_match(m):
        row1 = m.group(1)
        bullet = m.group(2)
        row2 = m.group(3)
        return f"{row1}\n{bullet}\n{row2}"
    
    new_content = re.sub(pattern, split_match, content)
    
    # Also handle cases where multiple table rows are on same line
    # Pattern: | Control | Guidance || Control | Guidance |
    pattern2 = r'(\| [^|]+\| [^|]+\|)\s*(\| [^|]+\| [^|]+\|)'
    
    def split_match2(m):
        return f"{m.group(1)}\n{m.group(2)}"
    
    new_content = re.sub(pattern2, split_match2, new_content)
    
    if new_content != content:
        print(f"Fixed concatenated table rows in {file_path.name}")
    
    return new_content

def main():
    workspace_dir = Path('/workspace/mirror_asd-acsc/e8_workspace')
    file_path = workspace_dir / 'E8 assessment process guide ML1.md'
    
    if file_path.exists():
        new_content = fix_specific_issues(file_path)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✓ Fixed ML1.md")
    
    # Now run the fix_all_remaining script again
    import subprocess
    result = subprocess.run(['python3', '/workspace/fix_all_remaining.py'], 
                          capture_output=True, text=True)
    print(result.stdout)

if __name__ == '__main__':
    main()
