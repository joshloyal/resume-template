import os
import jinja2
import yaml
import plac


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
    render_template = template.render(**options)

    #options = OptionsParser.from_yaml('resume.yaml')
    #render_template = template.render(**options.to_dict())

    if not os.path.exists('build'):
        os.makedirs('build')

    with open(os.path.join('build', 'resume.{}'.format(output_type)), 'w') as f:
        f.write(render_template)


if __name__ == '__main__':
    plac.call(main)

