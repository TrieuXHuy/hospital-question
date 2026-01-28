#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converter for Medical Quiz Questions to Azota Format
Converts tab-separated medical quiz data to standardized Azota format
"""

import sys
import re


def parse_questions(file_path):
    """Parse questions from the input file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    questions = []
    i = 0
    
    # Skip header lines
    while i < len(lines) and not lines[i].strip().startswith('1\t'):
        i += 1
    
    # Parse each question
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Try to parse as question header (STT, Mã, Nội dung)
        parts = line.split('\t')
        if len(parts) >= 3 and parts[0].isdigit():
            stt = parts[0]
            code = parts[1]
            content = parts[2]
            
            # Read the next 4 lines for options A, B, C, D
            options = []
            answer = None
            
            for j in range(4):
                i += 1
                if i >= len(lines):
                    break
                    
                option_line = lines[i].strip()
                
                # Check if this is option D (which contains the answer)
                if option_line.startswith('D.'):
                    # Split by tab to extract answer
                    option_parts = option_line.split('\t')
                    option_text = option_parts[0]
                    if len(option_parts) > 1 and option_parts[1].strip():
                        answer = option_parts[1].strip()
                    options.append(option_text)
                else:
                    options.append(option_line)
            
            if len(options) == 4 and answer:
                questions.append({
                    'stt': stt,
                    'code': code,
                    'content': content,
                    'options': options,
                    'answer': answer
                })
        
        i += 1
    
    return questions


def format_to_azota(questions):
    """Format questions to Azota standard format"""
    output_lines = []
    
    for q in questions:
        # Format: Câu [STT] ([Mã câu]): [Nội dung câu hỏi]
        title = f"Câu {q['stt']} ({q['code']}): {q['content']}"
        output_lines.append(title)
        
        # Add each option on a new line
        for option in q['options']:
            output_lines.append(option)
        
        # Add answer line
        output_lines.append(f"Đáp án: {q['answer']}")
        
        # Add blank line between questions
        output_lines.append("")
    
    return '\n'.join(output_lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_to_azota.py <input_file>")
        print("Example: python convert_to_azota.py 'PHẦN NHỚ.ini'")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        questions = parse_questions(input_file)
        azota_format = format_to_azota(questions)
        
        # Output in a code block for easy copying
        print("```")
        print(azota_format)
        print("```")
        
        print(f"\n✓ Successfully converted {len(questions)} questions to Azota format", file=sys.stderr)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
