from PlayblastBot.Controller import PlayblastBotSlaveController

class PlayblastBotSlaveLauncher(object):
    @staticmethod
    def Exec(mode='Desktop'):
        if mode == 'Desktop':
            PlayblastBotSlaveLauncher.Desktop()
        elif mode == 'Maya':
            PlayblastBotSlaveLauncher.Desktop()

    @staticmethod
    def Desktop():
        from PlayblastBot.Lib import PlayblastBotSlaveLib

        PlayblastBotSlaveLib.SetValue(234234)
        dialog = PlayblastBotSlaveController()
        dialog.Initialize()
        dialog.Show()

    @staticmethod
    def Maya():
        from PlayblastBot.Lib import PlayblastBotSlaveLib

        PlayblastBotSlaveLib.SetValue(234234)
        dialog = PlayblastBotSlaveController()
        dialog.Initialize()
        dialog.Show()