import subprocess, dotbot

class Flatpak(dotbot.Plugin):
    _directive = 'flatpak'


    def can_handle(self, directive):
        return self._directive == directive

    def handle(self, directive, data):
        if directive != self._directive:
            raise ValueError('flatpak cannot handle directive %s' %
                directive)

        success = True

        for app in data:
            try:
                subprocess.run(
                        ['flatpak install --noninteractive --assumeyes flathub '+app],
                        shell=True,
                        check=True)
            except subprocess.CalledProcessError:
                success = False

        if success:
            self._log.info('All packages have been installed')
        else:
            self._log.error('Some packages were not successfully installed')
        return success
