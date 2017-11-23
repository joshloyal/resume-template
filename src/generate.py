import os
import jinja2
import yaml
import plac
import datetime


DATA_PATH = './data/'

def add_tag(string, tag):
    return ('<{}>' + string + '</{}>').format(tag, tag)


def html(content):
    """Take content and format it with paragraph breaks."""
    new_content = ''
    for p in content.split('\n'):
        if p:
            new_content += add_tag(p, 'p')

    return new_content


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

    options = yaml.load(open(os.path.join(DATA_PATH, 'resume.yaml'), 'r'))
    for section in options['section_order']:
        content_path = os.path.join(DATA_PATH, section + '.yaml')
        if os.path.exists(content_path):
            options[section] = yaml.load(open(content_path, 'r'))

    options['date'] = datetime.datetime.now().strftime("%Y-%m-%d")

    if output_type == 'html':
        options['summary'] = html(options['summary'])

    render_template = template.render(**options)

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

