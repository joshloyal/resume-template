import copy
import os
import re
import jinja2
import yaml
import plac
import datetime


def add_tag(string, tag):
    return ('<{}>' + string + '</{}>').format(tag, tag)


def html(content):
    """Take content and format it with paragraph breaks."""
    new_content = ''
    for p in content.split('\n'):
        if p:
            new_content += add_tag(p, 'p')

    return new_content


def do_replacement(yaml_data, replacements):
    yaml_data = copy.deepcopy(yaml_data)

    if isinstance(yaml_data, str):
        for org_str, rep_str in replacements:
            yaml_data = re.sub(org_str, rep_str, yaml_data)
    elif isinstance(yaml_data, dict):
        for k, v in yaml_data.items():
            yaml_data[k] = do_replacement(v, replacements)
    elif isinstance(yaml_data, list):
        for idx, item in enumerate(yaml_data):
            yaml_data[idx] = do_replacement(item, replacements)

    return yaml_data


@plac.annotations(
    output_type=('Type of output to generate.')
)
def main(output_type):
    latex_env = jinja2.Environment(
        block_start_string='\BLOCK{',
        block_end_string='}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.abspath('./templates/latex')))


    markdown_env = jinja2.Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        loader=jinja2.FileSystemLoader(os.path.abspath('./templates/markdown')))

    html_env = jinja2.Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        loader=jinja2.FileSystemLoader(os.path.abspath('./templates/html')))


    if output_type == 'tex':
        template = latex_env.get_template('section.{}'.format(output_type))
    elif output_type == 'md':
        template = markdown_env.get_template('section.{}'.format(output_type))
    else:
        template = html_env.get_template('section.{}'.format(output_type))

    options = yaml.load(open('./data/resume.yaml', 'r'))
    options['date'] = datetime.datetime.now().strftime("%Y-%m-%d")

    if output_type == 'html':
        options['summary'] = html(options['summary'])

        # Taken from https://github.com/bamos/cv/blob/master/generate.py
        REPLACEMENTS = [
            (r'\\\\\[[^\]]*]', '\n'),  # newlines
            (r'\\ ', ' '),  # spaces
            (r'\\&', '&'),  # unescape &
            (r'\\\$', '$'),  # unescape $
            (r'\\%', '%'),  # unescape %
            (r'\\textbf{([^}]*)}', r'**\1**'),  # bold text
            (r'\{ *\\bf *([^}]*)\}', r'**\1**'),
            (r'\\textit{([^}]*)}', r'*\1*'),  # italic text
            (r'\{ *\\it *([^}]*)\}', r'*\1*'),
            (r'\\LaTeX', 'LaTeX'),  # \LaTeX to boring old LaTeX
            (r'\\TeX', 'TeX'),  # \TeX to boring old TeX
            ('---', '-'),  # em dash
            ('--', '-'),  # en dash
            (r'``([^\']*)\'\'', r'"\1"'),  # quotes
            (r'\\url{([^}]*)}', r'[\1](\1)'),  # urls
            (r'\\href{([^}]*)}{([^}]*)}', r'[\2](\1)'),  # urls
            (r'\{([^}]*)\}', r'\1'),  # Brackets.
        ]
        options = do_replacement(options, REPLACEMENTS)

    render_template = template.render(**options)

    #options = OptionsParser.from_yaml('resume.yaml')
    #render_template = template.render(**options.to_dict())

    if not os.path.exists('build'):
        os.makedirs('build')

    with open(os.path.join('build', 'resume.{}'.format(output_type)), 'w') as f:
        f.write(render_template)

    if output_type == 'html':
        template = html_env.get_template('code.{}'.format(output_type))
        render_template = template.render(**options)
        with open(os.path.join('build', 'code.{}'.format(output_type)), 'w') as f:
            f.write(render_template)



if __name__ == '__main__':
    plac.call(main)

