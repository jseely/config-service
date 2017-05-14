#!/usr/bin/env python3
import json

from fabric.api import *

from azure_cli_wrapper import execute_cli_command

def get_cluster_hosts():
    vmss_vms = execute_cli_command(['vmss', 'list-instances', '--resource-group', 'config-service', '--name', 'cephcluster'])
    return [ vm['osProfile']['computerName'] for vm in vmss_vms ]

def get_jumpbox_ip():
    jumpbox_ip = execute_cli_command(['network', 'public-ip', 'show', '--resource-group', 'config-service', '--name', 'jumpbox-ip'])
    return jumpbox_ip['ipAddress']

def target_ceph_machines():
    env.user = 'justin'
    env.hosts = get_cluster_hosts()
    env.gateway = get_jumpbox_ip()
    env.forward_agent = True
    print("Targetting: {}".format(json.dumps(env.hosts)))
    print("Using jumpbox: {}".format(env.gateway))

def target_jumpbox():
    env.user = 'justin'
    env.hosts = [get_jumpbox_ip()]
    env.forward_agent = True
    print("Targetting: {}".format(json.dumps(env.hosts)))

def install_ceph():
    cluster_hosts = get_cluster_hosts()
    run('ceph-deploy new {}'.format(" ".join(cluster_hosts)))

def update_apt_repository():
    sudo('apt-get update')