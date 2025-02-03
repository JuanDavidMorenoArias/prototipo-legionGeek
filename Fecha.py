class Fecha:
    def __init__(self, dd=0, mm=0, aa=0):
        if dd==0 and mm==0 and aa==0:
          return None
        else:
          self._dd = dd
          self._mm = mm
          self._aa = aa

    def getD(self):
        return self._dd

    def setD(self, dd):
        self._dd = dd

    def getD(self):
        return self.mm

    def setM(self, mm):
        self.mm = mm

    def getA(self):
        return self._aa

    def setA(self, aa):
        self._aa = aa

    def __str__(self):
      return (f"{self._dd} {self._mm} {self._aa}")