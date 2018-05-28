from PlayblastBot.Controller import PlayblastBotManagerController

class PlayblastBotManagerLauncher(object):
    @staticmethod
    def Exec(mode='Desktop'):
        if mode == 'Desktop':
            PlayblastBotManagerLauncher.Desktop()
        elif mode == 'Maya':
            PlayblastBotManagerLauncher.Maya()

    @staticmethod
    def Desktop():
        from PlayblastBot.Lib import PlayblastBotManagerLib

        PlayblastBotManagerLib.SetValue(234234)
        dialog = PlayblastBotManagerController()
        dialog.Initialize()
        dialog.Show()

    @staticmethod
    def Maya():
        from PlayblastBot.Lib import PlayblastBotManagerLib

        PlayblastBotManagerLib.SetValue(234234)
        dialog = PlayblastBotManagerController()
        dialog.Initialize()
        dialog.Show()