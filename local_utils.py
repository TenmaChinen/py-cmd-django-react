import shutil, os, re

def get_args_dict(l_args):

    # d_params = {'scope':'global', 'pkg_mgr':'pnp'}
    d_params = {'scope':'global', 'pkg_mgr':'pnpm'}
    d_options = {'scope':['global','local'], 'pkg_mgr':['npm','pnpm']}

    if len(l_args) == 1:
        print(f'\n    Default params : --scope={d_params["scope"]} --pkg_mgr={d_params["pkg_mgr"]}')
        return d_params

    for arg in l_args[1:]:
        if arg.__contains__('--') and arg.__contains__('='):
            arg = arg.strip('--')
            key, value = arg.split('=')
            if key in d_params and value in d_options[key]:
                d_params[key] = value
                continue

        print(f'\n    Arg : {arg} is not valid\n\n    Params must be:')
        for key in d_params.keys():
            values = ' or '.join(d_options[key])
            print(f'        --{key}={values}')
        print()
        return None
    return d_params

def copy_project_files(src_dir, dst_dir):
    files_dir = src_dir / 'files'

    # [ app ]
    for file_name in ['urls.py', 'settings.py']:
        src_file_path = files_dir / 'app' / file_name
        dst_file_path = dst_dir / 'app' / file_name
        shutil.copy(src=src_file_path, dst=dst_file_path)

    # [ api ]
    for file_name in ['urls.py', 'views.py']:
        src_file_path = files_dir / 'api' / file_name
        dst_file_path = dst_dir / 'api' / file_name
        shutil.copy(src=src_file_path, dst=dst_file_path)

    # [ frontend ]
    for file_name in ['urls.py', '.babelrc','webpack.config.js', 'views.py', 'src', 'static', 'templates']:
        src_file_path = files_dir / 'frontend' / file_name
        dst_file_path = dst_dir / 'frontend' / file_name
        
        if os.path.isfile(src_file_path):
            shutil.copy(src=src_file_path, dst=dst_file_path)
        elif os.path.isdir(src_file_path):
            shutil.copytree(src=src_file_path, dst=dst_file_path)


def settings_modificator(settings_path):

    string = load_file(file_path=settings_path)

    l_apps = ['frontend', 'api']
    str_apps = '\n'.join( [ f"\t'{app}'," for app in l_apps ] )
    
    string = re.sub(
        pattern=r"(INSTALLED_APPS = \[[^\]]*?)(\])",
        repl=rf'\1{str_apps}\n]', string=string
    )

    save_file(file_path=settings_path, string=string)


def load_file(file_path):
    file = open(file_path,'r')
    string = file.read()
    file.close()
    return string

def save_file(file_path, string):
    file = open(file_path,'w')
    file.write(string)
    file.close()