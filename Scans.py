import os
import shutil

class Worck:
    def __init__(self):
        self.outfil = "/home/wandors/out.pdf"
        self.nametemp = "temps"
        self.tempfile = "/temp"
        self.tempfiled = "/tempd"
        self.pathtemp = "./{0}".format(self.nametemp)
        if not os.path.exists(self.pathtemp):
            os.mkdir(self.pathtemp)
            with open(self.pathtemp + self.tempfile, "w") as f:
                f.close()
            with open(self.pathtemp + self.tempfiled, "w") as f:
                f.close()
    def CrPeopl(self):
        self.nampepd = raw_input("\xd0\x92\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb8 \xd0\xb8\xd0\xbc\xd1\x8f \xd0\x97\xd0\x9a: ")
        if self.nampepd == "":
            self.Crdocsfil()
        else:
            with open(self.pathtemp + self.tempfile, "w") as f:
                f.write("./{0}/".format(self.nampepd))
                f.close()
            if not os.path.exists("./{0}".format(self.nampepd)):
                os.mkdir("./{0}/".format(self.nampepd))
            self.Crdocsfil()

    def Crdocsfil(self):
        self.namdocd = raw_input('\xd0\xb2\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb8 \xd0\xb4\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82: ')
        if self.namdocd == "":
            pass
        else:
            with open(self.pathtemp + self.tempfile, "r") as f:
                self.texp = f.read()
                f.close()
            self.dirdoc = str(self.texp + self.namdocd)
            os.mkdir(self.dirdoc)
            shutil.copy(self.outfil, self.dirdoc)






w = Worck()
w.CrPeopl()
#w.Crdocsfil()