import pathlib

from pydo import *

this_dir = pathlib.Path(__file__).parent

services = ['keybow.service']

package = {

    'requires': [],

    'sysroot_debs': [],

    'root_debs': [

    ],

    'target': this_dir / 'keybow.tar.gz',
    'install': [f'{{chroot}} {{stage}} /bin/systemctl reenable {service}' for service in services],

}

from ... import sysroot

env = sysroot.env.copy()

stage = this_dir / 'stage'
start = this_dir / 'start.sh'
service_files = [this_dir / s for s in services]

@command(produces=[package['target']], consumes=service_files + [start, sysroot.toolchain, sysroot.sysroot])
def build():
    call([
        f'rm -rf --one-file-system {stage}',
        f'mkdir -p {stage}',
        f'cp {start} {stage}',
        f'mkdir -p {stage}/etc/systemd/system',
        f'cp {" ".join(str(s) for s in service_files)} {stage}/etc/systemd/system/',
        f'tar -C {stage} -czf {package["target"]} .',
    ], env=env, shell=True)


@command()
def clean():
    call([
        f'rm -rf --one-file-system {stage} {package["target"]}',
    ])
