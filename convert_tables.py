#!/usr/bin/env python3
"""
Script to convert Markdown tables to bullet point format.
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
    
    # Find code block
    code_match = re.search(r'<pre><code>(.*?)</code></pre>', text, re.DOTALL)
    if not code_match:
        return None, text
    
    code_content = code_match.group(1)
    code_content = code_content.replace('<br>', '\n').strip()
    
    # Determine language
    lang = ''
    if 'powershell' in code_content.lower() or 'Get-' in code_content or '$' in code_content or 'function' in code_content.lower():
        lang = 'powershell'
    elif 'winver' in code_content.lower() or 'cat /etc/os-release' in code_content.lower():
        lang = 'bash'
    
    before = text[:code_match.start()].strip()
    after = text[code_match.end():].strip()
    
    return (code_content, lang, before, after), None

def convert_table_to_bullets(table_lines):
    """Convert table lines to bullet point format."""
    if len(table_lines) < 3:
        return '\n'.join(table_lines)
    
    # Skip header and separator
    data_lines = table_lines[2:]
    
    result = []
    result.append("**Assessment Guidance (ordered by effectiveness):**")
    result.append("")
    
    current_control = None
    current_guidance = []
    
    for line in data_lines:
        if not line.strip() or not line.strip().startswith('|'):
            continue
        
        # Parse: | Control | Guidance |
        parts = [p.strip() for p in line.split('|')]
        if len(parts) < 3:
            continue
        
        control = parts[1].strip()
        guidance = parts[2].strip()
        
        # Empty control means continuation
        if not control:
            if guidance:
                current_guidance.append(guidance)
            continue
        
        # Output previous control
        if current_control is not None:
            result.append(f"- **{current_control}**")
            for g in current_guidance:
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
                    # Split on newlines if any
                    for g_line in g_clean.split('\n'):
                        if g_line.strip():
                            result.append(f"  - {g_line.strip()}")
            result.append("")
        
        # Start new control
        current_control = control
        current_guidance = [guidance] if guidance else []
    
    # Output last control
    if current_control is not None:
        result.append(f"- **{current_control}**")
        for g in current_guidance:
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
        result.append("")
    
    return '\n'.join(result)

def process_file(file_path):
    """Process a single file, converting all tables to bullet points."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    result_lines = []
    i = 0
    table_count = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a table header
        if '| Control | Assessment Guidance (ordered by effectiveness) |' in line:
            table_count += 1
            # Collect all table lines
            table_lines = []
            table_lines.append(line.rstrip())
            
            # Next line should be separator
            if i + 1 < len(lines):
                i += 1
                table_lines.append(lines[i].rstrip())
            
            # Collect data rows until we hit a non-table line or section header
            i += 1
            while i < len(lines):
                next_line = lines[i]
                # Stop if we hit a section header (###) or blank line followed by section header
                if next_line.strip().startswith('###'):
                    break
                # Stop if we hit a blank line and next non-blank is a section header
                if not next_line.strip() and i + 1 < len(lines):
                    if lines[i + 1].strip().startswith('###'):
                        break
                # Continue if it's a table row
                if next_line.strip().startswith('|') and '|' in next_line:
                    table_lines.append(next_line.rstrip())
                    i += 1
                elif not next_line.strip():
                    # Blank line within table - might be end, but check next line
                    if i + 1 < len(lines) and lines[i + 1].strip().startswith('|'):
                        table_lines.append(next_line.rstrip())
                        i += 1
                    else:
                        break
                else:
                    # Not a table line
                    break
            
            # Convert table to bullets
            bullet_text = convert_table_to_bullets(table_lines)
            result_lines.append(bullet_text)
            result_lines.append("")
        else:
            result_lines.append(line.rstrip())
            i += 1
    
    print(f"Found {table_count} table(s) in {file_path.name}")
    
    return '\n'.join(result_lines)

def main():
    workspace_dir = Path('/workspace/mirror_asd-acsc/e8_workspace')
    
    files_to_process = [
        'E8 assessment process guide ML1.md',
        'E8 assessment process guide ML2.md',
        'E8 assessment process guide ML3.md',
        'Essential Eight assessment process guide WORKING.md'
    ]
    
    for filename in files_to_process:
        file_path = workspace_dir / filename
        if not file_path.exists():
            print(f"File not found: {file_path}")
            continue
        
        print(f"\nProcessing {filename}...")
        try:
            new_content = process_file(file_path)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Completed {filename}")
        except Exception as e:
            print(f"✗ Error processing {filename}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()
