
def get_args_dict(l_args):

    d_params = {'scope':'global', 'pkg_mgr':'pnpm'}
    d_options = {'scope':['global','local'], 'pkg_mgr':['npm','pnpm']}

    if len(l_args) == 1:
        print(f'\n    Default params : --scope={d_params["scope"]} --pkg_mgr={d_params["pkg_mgr"]}')
        return d_params

    for arg in l_args:
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