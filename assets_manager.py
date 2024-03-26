import os

folder_path = "assets"

asset_fodlers = os.listdir(folder_path)

for folder in asset_fodlers:
    sub_dir = f'{folder_path}/{folder}'
    
    if folder.split('_')[0] == 'ignore':
        continue

    assets = ''

    for asset in os.listdir(sub_dir):
        asset_var_name = ''
        for n in range(len(asset.split('.')[0].split('_'))):
            name_segs = asset.split('.')[0].split('_')
            if n == 0:
                asset_var_name += name_segs[0]
            else:
                asset_var_name += name_segs[n].capitalize()

        code = f"\n\tstatic const String {asset_var_name} = '$_root/{asset}';"
        assets += code
        pass
    


    code = 'class '+f'{folder.capitalize()}Assets'+' {\n'+ '\tstatic const String _root = \''+ sub_dir+'\';\n'+assets+'\n}'

    with open (f'lib/shared/data/{folder}_assets.dart', 'w') as f:
        f.write(code)
