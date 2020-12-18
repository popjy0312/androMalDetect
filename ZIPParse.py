import zipfile
class ZIPParse():
    def __init__(self):
        self.feature = [0,0,0,0,0] # tot_size, res, lib, AndroidManifest.xml, classes*.dex
    def getFeature(self,filename):
        try:
            zp = zipfile.ZipFile(filename)
        except:
            return [0,0,0,0,0]
        self.feature = [0,0,0,0,0]
        for fp in zp.filelist:
            this_name = fp.filename
            this_size = fp.file_size
            self.feature[0] += this_size
            if this_name[:4] == 'res/':
                self.feature[1] += fp.file_size
            elif this_name[:4] == 'lib/':
                self.feature[2] += fp.file_size
            elif this_name == 'AndroidManifest.xml':
                self.feature[3] += fp.file_size
            elif this_name[:7] == 'classes':
                self.feature[4] += fp.file_size
        self.feature[1] /= self.feature[0]
        self.feature[2] /= self.feature[0]
        self.feature[3] /= self.feature[0]
        self.feature[4] /= self.feature[0]
        return self.feature