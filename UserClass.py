

class School:
    #getter

    def SetSchoolName(self,schoolName):
        self._SchoolName = schoolName

    def GetSchoolName(self):
        return self._SchoolName





def main():
    sch = School()
    sch.SetSchoolName("nalambayi")
    print(sch.GetSchoolName())

    sch2 = School()
    sch2.SetSchoolName("kabisa")
    print(sch2.GetSchoolName())

if __name__ == '__main__':main()