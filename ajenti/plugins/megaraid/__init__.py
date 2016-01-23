from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='RAID',
    description='LSI MegaRAID status display',
    icon='hdd',
    dependencies=[
        PluginDependency('main'),
        FileDependency('/usr/sbin/megacli'),
    ],
)


def init():
    import api
    import main
    import widget
