#!/usr/bin/env python3
"""
Script to fix remaining table rows that weren't converted.
"""

import re
from pathlib import Path

def clean_html_tags(text):
    """Clean HTML tags from text, converting <br> to newlines."""
    text = text.replace('<br>', '\n')
    return text

def extract_code_block(text):
    """Extract and format code blocks from HTML."""
    if '<pre><code>' not in text or '</code></pre>' not in text:
        return None, text
    
    code_match = re.search(r'<pre><code>(.*?)</code></pre>', text, re.DOTALL)
    if not code_match:
        return None, text
    
    code_content = code_match.group(1)
    code_content = code_content.replace('<br>', '\n').strip()
    
    lang = ''
    if 'powershell' in code_content.lower() or 'Get-' in code_content or '$' in code_content or 'function' in code_content.lower():
        lang = 'powershell'
    elif 'winver' in code_content.lower() or 'cat /etc/os-release' in code_content.lower():
        lang = 'bash'
    
    before = text[:code_match.start()].strip()
    after = text[code_match.end():].strip()
    
    return (code_content, lang, before, after), None

def convert_table_row_to_bullet(control, guidance_list):
    """Convert a control and its guidance list to bullet format."""
    result = []
    result.append(f"- **{control}**")
    
    for g in guidance_list:
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
    
    return '\n'.join(result)

def process_file(file_path):
    """Process file to convert remaining table rows."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    result_lines = []
    i = 0
    converted_count = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a table row (starts with | and has multiple |)
        if line.strip().startswith('|') and line.count('|') >= 3:
            # Collect all consecutive table rows
            table_rows = []
            start_i = i
            
            while i < len(lines) and lines[i].strip().startswith('|') and lines[i].count('|') >= 3:
                table_rows.append(lines[i].rstrip())
                i += 1
            
            # Parse table rows
            controls = []
            current_control = None
            current_guidance = []
            
            for row in table_rows:
                parts = [p.strip() for p in row.split('|')]
                if len(parts) < 3:
                    continue
                
                control = parts[1].strip()
                guidance = parts[2].strip()
                
                if not control:
                    # Continuation
                    if guidance:
                        current_guidance.append(guidance)
                else:
                    # New control
                    if current_control is not None:
                        controls.append((current_control, current_guidance))
                    current_control = control
                    current_guidance = [guidance] if guidance else []
            
            if current_control is not None:
                controls.append((current_control, current_guidance))
            
            # Convert to bullets
            if controls:
                converted_count += len(controls)
                for control, guidance_list in controls:
                    bullet_text = convert_table_row_to_bullet(control, guidance_list)
                    result_lines.append(bullet_text)
                    result_lines.append("")
            else:
                # Keep original if we couldn't parse
                result_lines.extend([r + '\n' for r in table_rows])
        else:
            result_lines.append(line.rstrip() + '\n')
            i += 1
    
    if converted_count > 0:
        print(f"Converted {converted_count} remaining table row(s) in {file_path.name}")
    
    return ''.join(result_lines).rstrip() + '\n'

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
