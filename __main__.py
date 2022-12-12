import os, sys, shutil, json, webbrowser
from pathlib import Path
from . import local_utils

d_params = local_utils.get_args_dict(l_args=sys.argv)

if d_params is None:
    sys.exit()

SRC_DIR = Path(__file__).resolve().parent
DST_DIR = Path(os.getcwd()).resolve()

#######################
###   D J A N G O   ###
#######################

os.system('django-admin startproject app .')
os.system('python manage.py startapp frontend')

# Add [ frontend ] app to Django [ settings.py ]

with open(DST_DIR / 'app' / 'settings.py' , 'r+' ) as file:
  l_lines = file.readlines()
  for idx,line in enumerate(l_lines):
    if line.__contains__('django.contrib.staticfiles'):
      l_lines.insert(idx+1, '    \'frontend\',\n')
      file.seek(0)
      file.write(''.join(l_lines))
      break

# Copy urls.py from [ app ]
src_file_path = SRC_DIR / 'files' / 'urls_a.py'
dst_file_path = DST_DIR/ 'app' / 'urls.py'
shutil.copy(src=src_file_path, dst=dst_file_path)

# Copy urls.py from [ frontend ]
src_file_path = SRC_DIR / 'files' / 'urls_f.py'
dst_file_path = DST_DIR/ 'frontend' / 'urls.py'
shutil.copy(src=src_file_path, dst=dst_file_path)

# Copy needed files
for file_name in ['.babelrc','webpack.config.js', 'views.py', 'src', 'static', 'templates']:
    src_file_path = SRC_DIR / 'files' / file_name
    dst_file_path = DST_DIR / 'frontend' / file_name
    if os.path.isfile(src_file_path):
        shutil.copy(src=src_file_path, dst=dst_file_path)
    elif os.path.isdir(src_file_path):
        shutil.copytree(src=src_file_path, dst=dst_file_path)

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
        'start': 'webpack-dev-server --config webpack.config.js',
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

webbrowser.open('http://localhost:8080')
os.system(f'{pkg_mgr} run start')