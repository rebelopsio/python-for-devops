# What I want to do is look for a config YAML file. That file location can be defined in 
# one of three places; environmental variable, current directory, or user's directory.
# In the config file we will have a list of directories to start. Those directories will 
# be the directories that we list the contents of. 
import os
from pprint import pprint
import yaml


def find_config_file(config_file="config.yml"):
    '''
    Function returns the path of the config file. It first checks for the path set in
    an environmental variable, then checks for the file in the current directory, then
    checks the user's home directory for a file called config.yml.
    '''
    # env variable named PYSCRIPTCONFIG
    env_var = "PYSCRIPTCONFIG"
    if env_var in os.environ:
        var_path = os.path.join(f"${env_var}", config_file)
        path = os.path.expandvars(var_path)
        print(f"Checking {path}")
        if os.path.exists(path):
            return path

    path = os.path.join(os.getcwd(), config_file)
    print(f"Checking {path}")
    if os.path.exists(path):
        return path

    user_dir = os.path.expanduser("~/")
    path = os.path.join(user_dir, config_file)
    if os.path.exists(path):
        return path

    print("Config file not found.")

def get_dirs_from_config(config_file):
    dirs_list = []
    with open(config_file, 'r') as cf:
        cf_loaded = yaml.safe_load(cf)
    for d in cf_loaded['directories']:
        dirs_list.append(d)
    return dirs_list

def main():
    get_dirs_from_config(find_config_file())

if __name__ == "__main__":
    print("Let's get started.")
    main()