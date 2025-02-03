class Date:
    def __init__(self, dd=0, mm=0, yy=0):
        if dd==0 and mm==0 and yy==0:
          return None
        else:
          self._dd = dd
          self._mm = mm
          self._yy = yy

    def getD(self):
        return self._dd

    def setD(self, dd):
        self._dd = dd

    def getM(self):
        return self.mm

    def setM(self, mm):
        self.mm = mm

    def getY(self):
        return self._yy

    def setY(self, yy):
        self._yy = yy

    def __str__(self):
      return (f"{self._dd} {self._mm} {self._yy}")