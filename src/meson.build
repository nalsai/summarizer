pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'summarizer')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('NLTK_DATA', join_paths(get_option('prefix'), get_option('datadir'), 'ntlk_data'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
    input: 'summarizer.in',
    output: 'summarizer',
    configuration: conf,
    install: true,
    install_dir: get_option('bindir')
)

sources = [
    '__init__.py',
    'main.py',
    'text_summarize.py',
    'ui.py',
]

install_data(sources, install_dir: moduledir)
