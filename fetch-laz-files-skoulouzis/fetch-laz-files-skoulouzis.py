import pathlib
from laserfarm.remote_utils import list_remote
from laserfarm.remote_utils import get_wdclient

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()

id = args.id



conf_wd_opts = { 'webdav_hostname':  'https://lfw-ds001-i022.lifewatch.dev:32443/', 'webdav_login':  '20BNXDdL8mg24OaD', 'webdav_password':  'zDoy0hNKkcnsdsQ@OYAVd'}
conf_remote_path_ahn =  '/webdav/LAZ'

conf_wd_opts = { 'webdav_hostname':  'https://lfw-ds001-i022.lifewatch.dev:32443/', 'webdav_login':  '20BNXDdL8mg24OaD', 'webdav_password':  'zDoy0hNKkcnsdsQ@OYAVd'}
conf_remote_path_ahn =  '/webdav/LAZ'
print(conf_remote_path_ahn)
laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), pathlib.Path(conf_remote_path_ahn).as_posix())
             if f.lower().endswith('.laz')]
print(laz_files)

import json
filename = "/tmp/laz_files_" + id + ".json"
file_laz_files = open(filename, "w")
file_laz_files.write(json.dumps(laz_files))
file_laz_files.close()
