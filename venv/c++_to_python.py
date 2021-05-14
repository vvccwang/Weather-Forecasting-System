class etGridCrd():
    # 初始化
    def __init__(self, iLine=0, iCmp=0):
        self.line = iLine
        self.cmp = iCmp

    # 重载==
    def __eq__(self, crd):
        return self.line == crd.line and self.cmp == crd.cmp
    # 重载！=
    def __ne__(self, crd):
        return self.line != crd.line or self.cmp != crd.cmp
    # 重载<
    def __lt__(self, crd):
        return self.line < crd.line or (self.line == crd.line and self.cmp < crd.cmp)
    # 重载<=
    def __le__(self, crd):
        return self.line < crd.line or (self.line == crd.line and self.cmp <= crd.cmp)
    # 重载>
    def __gt__(self, crd):
        return self.line > crd.line or (self.line == crd.line and self.cmp > crd.cmp)
    # 重载>=
    def __ge__(self, crd):
        return self.line > crd.line or (self.line == crd.line and self.cmp >= crd.cmp)

    # 函数模板
    # 重载=  不会 ?????????????????????
    def dengyu(self,pt):
        self.line = int(pt._y + 0.5)
        self.cmp = int(pt._x + 0.5)
        return self

    # 重载+=
    def __iadd__(self, r):
        self.line += r.line
        self.cmp += r.cmp
        return self
    # 重载-=
    def __isub__(self, r):
        self.line -= r.line
        self.cmp -= r.cmp
        return self

    # 重载+
    def __add__(self, r):
        return etGridCrd(self.line + r.line, self.cmp + r.cmp)
    # 重载-
    def __sub__(self, r):
        return etGridCrd(self.line - r.line, self.cmp - r.cmp)
# e1 = etGridCrd(3,3)
# e2 = etGridCrd(1,2)
# e3 = etGridCrd(3,3)
# print(e1.cmp,e2.cmp,e3.cmp)
#
# print(e3==e2)
# print(e3==e1)
#
# print(e3.line,e3.cmp)
#
# e=e3-e2
#
# print(e.line,e.cmp)

class etLinearRange():
    def __init__(self, start = 0 , nCount = 0 , step = 0):
        self._start = start
        self._nCount = nCount
        self._step = step

    def IsValidRange(self):
        return self._nCount > 0 and self._step > 0

    def SetRange(self, start, nCount, step):
        _start = start
        _nCount = nCount
        _step = step

    def SetStart(self,start):
        self._start = start
    def SetCount(self,nCount):
        self._nCount = nCount
    def SetStep(self,step):
        self._step = step

    def GetStart(self):
        return self._start
    def GetCount(self):
        return self._nCount
    def GetStep(self):
        return self._step
    def GetEnd(self):
        return self._start + self._step * (self._nCount-1)

    def ValueToIndex(self, v, pOk = False):
        if self._step == 0:
            return False
        idx = round((v - self._start) / self._step)
        if pOk :
            pOk = (idx >= 0 and idx < self._nCount)
            return idx

    def ValueToIndexEx(self, v, pOk = False):
        if self._step == 0:
            return False
        idx = (v - self._start) / self._step
        if pOk :
            #Type()类型 ???????????
            pOk = (idx >= Type(0) and idx < Type(self._nCount))
            return idx

    def IndexToValue(self, i, pOk = False):
        if self._step == 0: return False
        if pOk :
            pOk = IsValidIndex(i)
        return self._start + i * self._step

    def IndexToValueEx(self, i):
        assert(self._step != 0)
        return self._start + i * self._step

    def IsValidIndex(self, i):
        return i >= 0 and i < self._nCount

    def IsValidValue(self, v):
        ok = False
        self.ValueToIndex(v, ok)
        return ok

    def __and__(self, a):
        if not self.IsValidRange() and not a.IsValidRange():
            return etLinearRange()
        s = max(self._start, a._start)
        end0 = self.GetEnd()
        end1 = a.GetEnd()
        e = min(end0,end1)
        if s > e:
            return etLinearRange()
        step = max(self._step, a._step)
        return etLinearRange(s, (e - s) / step + 1, step)

    #重写&=   ???????????
    def weiyu(self,a):
        return self & a

    def __or__(self, a):
        if not self.IsValidRange():
            return a
        if not a.IsValidRange():
            return self
        s = min(self._start,a._start)
        end0 = GetEnd()
        end1 = a.GetEnd()
        e = max(end0, end1)
        step = min(self._step, a._step)
        return etLinearRange(s, (e - s) / step + 1, step)

    # 重写|=   ???????????
    def weihuo(self,a):
        return self | a

    # 重载==
    def __eq__(self, a):
        return self._start == a._start and self._step == a._step and self._nCount == a._nCount
    # 重载！=
    def __ne__(self, a):
        return not(self == a)

    def Contains(self,a,bIncludeEqual = True):
        if self._step != a._step:
            return False
        if bIncludeEqual:
            return self._start <= a._start and self.GetEnd() >= a.GetEnd()

    def SerializeJson(self, obj, bSave, sPrefix):
        if bSave:
            obj[sPrefix + "_start"] = self._start
            obj[sPrefix + "_count"] = self._nCount
            obj[sPrefix + "_step"] = self._step
        else:
            self._nCount = obj.value(sPrefix + "_count").toInt(self._nCount)
            self._start = obj.value(sPrefix + "_start").toDouble()
            self._step = obj.value(sPrefix + "_step").toDouble()


# t=etLinearRange()
# print(t.IsValidRange())