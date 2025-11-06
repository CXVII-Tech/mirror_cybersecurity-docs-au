#!/usr/bin/env python3
"""
Script to fix ALL remaining table rows, including isolated ones.
"""

import re
from pathlib import Path

def clean_html_tags(text):
    """Clean HTML tags from text."""
    text = text.replace('<br>', '\n')
    return text

def extract_code_block(text):
    """Extract and format code blocks from HTML."""
    if '<pre><code>' not in text or '</code></pre>' not in text:
        return None, text
    
    code_match = re.search(r'<pre><code>(.*?)</code></pre>', text, re.DOTALL)
    if not code_match:
        return None, text
    
    code_content = code_match.group(1).replace('<br>', '\n').strip()
    
    lang = ''
    if 'powershell' in code_content.lower() or 'Get-' in code_content or '$' in code_content or 'function' in code_content.lower():
        lang = 'powershell'
    elif 'winver' in code_content.lower() or 'cat /etc/os-release' in code_content.lower():
        lang = 'bash'
    
    before = text[:code_match.start()].strip()
    after = text[code_match.end():].strip()
    
    return (code_content, lang, before, after), None

def format_guidance(g):
    """Format a single guidance item."""
    result = []
    code_info, remaining = extract_code_block(g)
    
    if code_info:
        code_content, lang, before, after = code_info
        if before:
            result.append(f"  - {before}")
        result.append("")
        result.append(f"    ```{lang}")
        for code_line in code_content.split('\n'):
            if code_line.strip():
                result.append(f"    {code_line}")
        result.append(f"    ```")
        result.append("")
        if after:
            result.append(f"  - {after}")
    else:
        g_clean = clean_html_tags(remaining or g)
        for g_line in g_clean.split('\n'):
            if g_line.strip():
                result.append(f"  - {g_line.strip()}")
    
    return result

def process_file(file_path):
    """Process file to convert ALL remaining table rows."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    result_lines = []
    i = 0
    converted_count = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a table row
        if line.strip().startswith('|') and line.count('|') >= 3:
            # Parse the row
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3:
                control = parts[1].strip()
                guidance = parts[2].strip()
                
                # Collect continuation rows
                guidance_list = [guidance] if guidance else []
                i += 1
                
                while i < len(lines) and lines[i].strip().startswith('|') and lines[i].count('|') >= 3:
                    cont_parts = [p.strip() for p in lines[i].split('|')]
                    if len(cont_parts) >= 3:
                        cont_control = cont_parts[1].strip()
                        cont_guidance = cont_parts[2].strip()
                        
                        if not cont_control:
                            # Continuation
                            if cont_guidance:
                                guidance_list.append(cont_guidance)
                            i += 1
                        else:
                            # New control - output current and start new
                            break
                
                # Output the control
                if control:
                    converted_count += 1
                    result_lines.append(f"- **{control}**")
                    for g in guidance_list:
                        result_lines.extend(format_guidance(g))
                    result_lines.append("")
                else:
                    # Just continuation rows without a control - shouldn't happen, but handle it
                    for g in guidance_list:
                        result_lines.extend(format_guidance(g))
                    result_lines.append("")
            else:
                result_lines.append(line)
                i += 1
        else:
            result_lines.append(line)
            i += 1
    
    if converted_count > 0:
        print(f"Converted {converted_count} remaining table row(s) in {file_path.name}")
    
    return ''.join(result_lines)

def main():
    workspace_dir = Path('/workspace/mirror_asd-acsc/e8_workspace')
    
    files_to_process = [
        'E8 assessment process guide ML1.md',
        'E8 assessment process guide ML2.md',
        'E8 assessment process guide ML3.md',
    ]
    
    for filename in files_to_process:
        file_path = workspace_dir / filename
        if not file_path.exists():
            continue
        
        print(f"\nProcessing {filename}...")
        try:
            new_content = process_file(file_path)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Completed {filename}")
        except Exception as e:
            print(f"✗ Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()
