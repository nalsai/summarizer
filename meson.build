project('summarizer',
          version: '0.1.0',
    meson_version: '>= 0.50.0',
)

subdir('data')
subdir('src')
install_subdir('tokenizers', install_dir : join_paths(get_option('prefix'), get_option('datadir'), 'ntlk_data'))
