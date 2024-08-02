#%%
import argparse

parser = argparse.ArgumentParser(
    description='Generate publications.html.')
parser.add_argument('-i', '--input', help='Input filename', default='../data/publications.xlsx')
parser.add_argument('-o', '--output', help='Output filename', default='../src/publications.html')

args = parser.parse_known_args()[0]

import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
env = Environment(loader=FileSystemLoader(Path(__file__).parent / './templates', encoding='utf8'))
template = env.get_template('publication_section.jinja')

SHEET_NAMES = ['英文原著・総説・教科書', '和文原著・総説・教科書', '国際学会・海外講演', '国内学会・講演', '受賞', '科学研究費補助金交付・奨学金']
IDS = ['english', 'japanese', 'international', 'domestic', 'award', 'grant']

xl = pd.ExcelFile(args.input)
assert set(xl.sheet_names) == set(SHEET_NAMES), f'Invalid sheet names: {xl.sheet_names}'
sections = []
for sheet, sheet_id in zip(SHEET_NAMES, IDS):
    df = xl.parse(sheet, names=['no','data'], header=None)
    section = template.render(id=sheet_id, section=sheet, publications=df['data'].to_list())
    sections.append(section)
# %%
jumps = [f'<li class="column"><a href="#{id}">{section}</a></li>' for section, id in zip(SHEET_NAMES, IDS)]
with open(args.output, 'w', encoding='utf8') as f:
    f.write('<ul class="columns has-text-centered is-vcentered is-centered is-multiline is-size-7">' + '\n'.join(jumps) + '</ul>')
    f.write('\n'.join(sections))

# %%
