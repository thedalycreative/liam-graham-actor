import sys

def convert_to_light_mode(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Update CSS Variables
    content = content.replace('--black: #050505;', '--black: #FAF9F6;')
    content = content.replace('--charcoal: #0E0E0E;', '--charcoal: #F2F0EB;')
    content = content.replace('--surface: #161616;', '--surface: #FFFFFF;')
    content = content.replace('--surface-hover: #1E1E1E;', '--surface-hover: #F8F6F0;')
    content = content.replace('--border: #222222;', '--border: #E0DCD5;')
    content = content.replace('--border-light: #2A2A2A;', '--border-light: #D1CCC4;')
    content = content.replace('--text-primary: #F0EDE8;', '--text-primary: #1A1A1A;')
    content = content.replace('--text-secondary: #8A8680;', '--text-secondary: #5C5A55;')
    content = content.replace('--text-muted: #5A5752;', '--text-muted: #827F78;')
    # Gold colors adjusted slightly for light background contrast
    content = content.replace('--gold: #C9A96E;', '--gold: #A88645;')
    content = content.replace('--gold-dim: #A68B4B;', '--gold-dim: #C2A56C;')
    content = content.replace('--gold-bright: #DCC088;', '--gold-bright: #8C6D32;')
    content = content.replace('--gold-glow: rgba(201, 169, 110, 0.15);', '--gold-glow: rgba(168, 134, 69, 0.15);')

    # 2. Update RGBA hardcoded values for dark colors
    content = content.replace('rgba(5, 5, 5,', 'rgba(250, 249, 246,')
    content = content.replace('rgba(5,5,5,', 'rgba(250,249,246,')
    content = content.replace('rgba(22,22,22,', 'rgba(240,240,240,')
    
    # 3. Reduce shadow opacity for light mode
    content = content.replace('rgba(0,0,0,0.45)', 'rgba(0,0,0,0.15)')
    content = content.replace('rgba(0,0,0,0.3)', 'rgba(0,0,0,0.1)')
    
    # 4. Hero image filter: make it lighter
    content = content.replace('filter: brightness(0.4) contrast(1.15) saturate(0.9);', 'filter: brightness(0.9) contrast(1.05) saturate(0.9);')
    
    # 5. Film grain (svg inline) - make it darker so it shows up on light bg
    content = content.replace("filter='url(%23noise)' opacity='0.03'", "filter='url(%23noise)' opacity='0.06'")
    
    with open(file_path, 'w') as f:
        f.write(content)
        
if __name__ == "__main__":
    convert_to_light_mode('/Users/thetimdaly/Desktop/VS Code/liam-graham-actor/liam-graham-actor-website/css/style.css')
    print("Done")
