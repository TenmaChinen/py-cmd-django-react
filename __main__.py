from . import local_utils as utils
import os, sys, json, webbrowser
from subprocess import Popen
from pathlib import Path

d_params = utils.get_args_dict(l_args=sys.argv)

if d_params is None:
    sys.exit()

SRC_DIR = Path(__file__).resolve().parent
DST_DIR = Path(os.getcwd()).resolve()

#######################
###   D J A N G O   ###
#######################

os.system('django-admin startproject app .')
os.system('python manage.py startapp api')
os.system('python manage.py startapp frontend')
os.system('python manage.py migrate')

# copy [ app ] [ frontend ] [ api ] files
utils.copy_project_files(src_dir=SRC_DIR, dst_dir=DST_DIR)
utils.settings_modificator(settings_path=DST_DIR / 'app' / 'settings.py')

#######################
####   R E A C T   ####
#######################

scope = d_params['scope']
pkg_mgr = d_params['pkg_mgr']

os.chdir('frontend')

if pkg_mgr == 'npm':
    os.system('npm init -y')
else:
    os.system('pnpm init')


with open('package.json','r+') as file:
    data = json.load(file)
    # dev just allows to see changes on manual refresh
    data['scripts'] = {
        'dev': 'webpack-dev-server --config webpack.config.js --host 127.0.0.1 --port 8080',
        # 'dev': 'webpack-dev-server --config webpack.config.js',
        'build': 'webpack --mode production',
        }
    file.seek(0)
    json.dump(data, file, indent=4)

str_react_libs = 'react react-dom react-router-dom'
str_babel_libs = '@babel/core @babel/preset-env @babel/preset-react'
str_webpack_libs = 'webpack webpack-cli webpack-dev-server html-webpack-plugin'
str_loaders_libs = 'babel-loader css-loader style-loader file-loader sass sass-loader '

if d_params['scope'] == 'local':
    os.system(f'{pkg_mgr} i {str_react_libs} --S')
    os.system(f'{pkg_mgr} i {str_babel_libs} {str_webpack_libs} {str_loaders_libs} --D')
else:
    if pkg_mgr == 'npm':
        os.system(f'npm link {str_react_libs} {str_babel_libs} {str_webpack_libs} {str_loaders_libs}')
    else:
        os.system(f'pnpm link -g {str_react_libs} {str_babel_libs} {str_webpack_libs} {str_loaders_libs}')



# seeking frontend dir
Popen(['start', 'cmd', '/k', 'py manage.py runserver'], cwd='..', shell=True)
# Popen(['start', 'cmd', '/k', f'{pkg_mgr} run dev'], shell=True)

# webbrowser.open('http://localhost:8080')
webbrowser.open('http://127.0.0.1:8080/foo')

os.system('cls')
os.system(f'{pkg_mgr} run dev')

