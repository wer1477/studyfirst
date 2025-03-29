class fish:
    def __init__(self,fid,fname):
        self.fid=fid
        self.fname=fname
    def live(self):
        if self.fname=="草鱼":
            print("分布于我国，栖息于江河湖泊中。")
        else:
            print("no date")
class freshwaterfish(fish):
    def __init__(self, fid, fname,fhabit):
       self.fid=fid
       self.fname=fname
       self.fhabit=fhabit
    def live(self):
       if self.fname=="草鱼":
            print("分布于我国，栖息于江河湖泊中。属食草性鱼类")
       else:
            print("no date")
w=freshwaterfish(1,"草鱼","weyyw")
w.live()

        
            
            
            
            
