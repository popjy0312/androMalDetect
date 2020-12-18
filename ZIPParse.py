import zipfile
from consts import featureDIM

class ZIPParse():
    def __init__(self):
        # tot_size, res, lib, AndroidManifest.xml, classes*.dex
        # file cnt, res file cnt, lib file cnt
        self.feature = [0] * featureDIM 
    def getFeature1(self,filename):
        try:
            zp = zipfile.ZipFile(filename)
        except:
            return [0] * 5
        self.feature = [0] * 5
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
        return self.feature[:5]
    
    def getFeature2(self,filename):
        try:
            zp = zipfile.ZipFile(filename)
        except:
            return [0] * featureDIM
        self.feature = [0] * featureDIM
        for fp in zp.filelist:
            this_name = fp.filename
            this_size = fp.file_size
            self.feature[0] += this_size
            if this_name[:4] == 'res/':
                self.feature[1] += fp.file_size
                self.feature[6] += 1
            elif this_name[:4] == 'lib/':
                self.feature[2] += fp.file_size
                self.feature[7] += 1
            elif this_name == 'AndroidManifest.xml':
                self.feature[3] += fp.file_size
            elif this_name[:7] == 'classes':
                self.feature[4] += fp.file_size
            self.feature[5] += 1
        self.feature[1] /= self.feature[0]
        self.feature[2] /= self.feature[0]
        self.feature[3] /= self.feature[0]
        self.feature[4] /= self.feature[0]
        self.feature[6] /= self.feature[5]
        self.feature[7] /= self.feature[5]
        return self.feature