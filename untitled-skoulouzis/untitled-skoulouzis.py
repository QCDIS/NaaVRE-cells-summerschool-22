import pathlib
import os

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--conf_hostname', action='store', type=str, required='True', dest='conf_hostname')
arg_parser.add_argument('--conf_login', action='store', type=str, required='True', dest='conf_login')
arg_parser.add_argument('--conf_password', action='store', type=str, required='True', dest='conf_password')


args = arg_parser.parse_args()

id = args.id

conf_hostname = args.conf_hostname
conf_login = args.conf_login
conf_password = args.conf_password



                    

if 'JUPYTERHUB_USER' in os.environ:
    param_username = os.environ['JUPYTERHUB_USER']
    
conf_remote_path_root = '/webdav/LAZ'
conf_remote_path_split = pathlib.Path(conf_remote_path_root + '/split_'+param_username)
conf_remote_path_retiled = pathlib.Path(conf_remote_path_root + '/retiled_'+param_username)
conf_remote_path_norm = pathlib.Path(conf_remote_path_root + '/norm_'+param_username)
conf_remote_path_targets = pathlib.Path(conf_remote_path_root + '/targets_'+param_username)
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_ahn = conf_remote_path_root



conf_feature_name = 'perc_95_normalized_height'
conf_validate_precision = '0.001'
conf_tile_mesh_size = '10.'
conf_filter_type= 'select_equal'
conf_attribute = 'raw_classification'
conf_min_x = '-113107.81'
conf_max_x = '398892.19'
conf_min_y = '214783.87'
conf_max_y = '726783.87'
conf_n_tiles_side = '512'
conf_apply_filter_value = '1'
conf_laz_compression_factor = '7'
conf_max_filesize = '262144000'  # desired max file size (in bytes)

conf_wd_opts = { 'webdav_hostname': conf_hostname, 'webdav_login': conf_login, 'webdav_password': conf_password}

