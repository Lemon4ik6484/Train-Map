import xml.etree.ElementTree as ET
import pathlib
import os

def change_svg_path_color(input_svg, output_svg, old_color, new_color):
    tree = ET.parse(input_svg)
    root = tree.getroot()
    
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    for path in root.findall('.//svg:path', ns):
        style = path.get('style')
        if style and f'fill:{old_color}' in style:
            new_style = style.replace(f'fill:{old_color}', f'fill:{new_color}')
            path.set('style', new_style)
        elif path.get('fill') == old_color:
            path.set('fill', new_color)
    
    tree.write(output_svg)

def change_stroke_color(svg_file, original_color, new_color, new_svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    for rect in root.iter('{http://www.w3.org/2000/svg}rect'):
        if rect.get('stroke') == original_color:
            rect.set('stroke', new_color)
    
    tree.write(new_svg_file)

def change_rect_fill_color(svg_file, original_color, new_color, new_svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    for rect in root.iter('{http://www.w3.org/2000/svg}rect'):
        if rect.get('fill') == original_color:
            rect.set('fill', new_color)
    
    tree.write(new_svg_file)

def change_path_stroke_color(input_file, old_color, new_color, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    for path in root.findall('.//svg:path', ns):
        style = path.get('style')
        if style and old_color in style:
            new_style = style.replace(old_color, new_color)
            path.set('style', new_style)
        
        fill = path.get('fill')
        if fill == old_color:
            path.set('fill', new_color)
        
        stroke = path.get('stroke')
        if stroke == old_color:
            path.set('stroke', new_color)

    tree.write(output_file)

input_one = './current/map.svg'
old_color = '#FCFAF3'
new_color = '#000000'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'

change_stroke_color(input_one, old_color, new_color, result_one)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = '#FCFAF3'
new_color = '#080E1E'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'

change_path_stroke_color(input_one, old_color, new_color, result_one)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = 'white'
new_color = '#000000'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'

change_stroke_color(input_one, old_color, new_color, result_one)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = '#56544D'
new_color = '#FFFFFF'

change_svg_path_color(input_one, result_one, old_color, new_color)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = '#6D6B65'
new_color = '#FFFFFF'

change_svg_path_color(input_one, result_one, old_color, new_color)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = 'white'
new_color = '#161F37'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'

change_rect_fill_color(input_one, old_color, new_color, result_one)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = '#FCFAF3'
new_color = '#080E1E'
result_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'

change_rect_fill_color(input_one, old_color, new_color, result_one)

input_one = f'{pathlib.Path(__file__).parent.resolve()}\\output.svg'
old_color = '#E0DDD0'
new_color = '#55648E'
result_one = './current/dark_map.svg'

change_stroke_color(input_one, old_color, new_color, result_one)

os.remove(f"{pathlib.Path(__file__).parent.resolve()}\\output.svg")