import pathlib

from pydo import *

this_dir = pathlib.Path(__file__).parent

package = {

    'requires': [],

    'sysroot_debs': [],

    'root_debs': [
        'openssh-server',
    ],

    'target': this_dir / 'ssh.tar.gz',
    'install': [
        # enable SSH services
        '{chroot} {stage} /bin/systemctl reenable ssh',
    ],

}

stage = this_dir / 'stage'


@command(produces=[package['target']])
def build():
    call([
        f'rm -rf --one-file-system {stage}',

        f'mkdir -p {stage}/etc/systemd/system',

        f'tar -C {stage} -czf {package["target"]} .'
    ])


@command()
def clean():
    call([f'rm -rf --one-file-system {stage} {package["target"]}'])
