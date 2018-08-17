"""
Hook specifications that pluggy plugins can override
"""
import pluggy

hookspec = pluggy.HookspecMarker('tljh')
hookimpl = pluggy.HookimplMarker('tljh')


@hookspec
def tljh_extra_user_conda_packages():
    """
    Return list of extra conda packages to install in user environment.
    """
    pass


@hookspec
def tljh_extra_user_pip_packages():
    """
    Return list of extra pip packages to install in user environment.
    """
    pass


@hookspec
def tljh_extra_apt_packages():
    """
    Return list of extra apt packages to install in the user environment.

    These will be installed before additional pip or conda packages.
    """
    pass


@hookspec
def tljh_config_post_install(config):
    """
    Modify on-disk tljh-config after installation.

    config is a dict-like object that should be modified
    in-place. The contents of the on-disk config.yaml will
    be the serialized contents of config, so try to not
    overwrite anything the user might have explicitly set.
    """
    pass