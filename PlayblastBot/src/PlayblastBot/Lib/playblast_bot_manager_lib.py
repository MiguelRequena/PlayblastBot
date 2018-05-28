from PowerRing.Purple.Lib.Model import RowTableModel, CellTableModel

class PlayblastBotManagerLib(object):
    _value = 0

    @staticmethod
    def MakePlayblast():
        pass

    @classmethod
    def GetValue(cls):
        return cls._value

    @classmethod
    def SetValue(cls, value):
        cls._value = value


    @staticmethod
    def GetJobsData():
        lista = [
            'asdfs'
        ]
        rows = []

        for st in lista:
            row = RowTableModel(name='%s' % st, data=st)
            row.Cells.append(PlayblastBotManagerLib.MakeCellName(st))
            rows.append(row)
        return rows

    @staticmethod
    def MakeCellName(st):
        cell = CellTableModel()
        cell.Name = st
        cell.Data = st
        cell.Label = st
        return cell

    @staticmethod
    def LaunchSlave():
        py.run('/usr/')