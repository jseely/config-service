#!/usr/bin/env python3
import os

from azure.cli.core.application import APPLICATION, Configuration
from azure.cli.core._session import ACCOUNT, CONFIG, SESSION
from azure.cli.core._environment import get_config_dir

def initialize_client():
    azure_folder = get_config_dir()
    if not os.path.exists(azure_folder):
        os.makedirs(azure_folder)
    ACCOUNT.load(os.path.join(azure_folder, 'azureProfile.json'))
    CONFIG.load(os.path.join(azure_folder, 'az.json'))
    SESSION.load(os.path.join(azure_folder, 'az.sess'), max_age=3600)

    APPLICATION.initialize(Configuration())

def execute_cli_command(command):
    try:
        cmd_result = APPLICATION.execute(command)
        return cmd_result.result
    except:
        return None

initialize_client()
