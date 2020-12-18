import pickle
import ZIPParse
from consts import featureDIM,DATASET_CNT

class featureSet():
    def __init__(self, featureDim):
        self.data = list()
        self.ans = list()
        self.featureDim = featureDim
    
    def addFeature(self, newFeature: list, ans: int):
        self.data.append(newFeature)
        self.ans.append(ans)

    def dump(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self,f)

if __name__ == '__main__':
    fs = featureSet(featureDIM)
    zp = ZIPParse.ZIPParse()

    dataList = open('lists.csv','rb')
    dataList.readline()
#b'sha256,sha1,md5,dex_date,apk_size,pkg_name,vercode,vt_detection,vt_scan_date,dex_size,markets\n'

    for i in range(DATASET_CNT):
        print(i)
        l = dataList.readline()
        l = str(l).split(',')
        apkName = str(l[0])[2:] + '.apk'
        vt_detection = str(l[-4])
        newFeature = zp.getFeature('../apks/'+apkName)

        if newFeature == [0] * featureDIM or vt_detection == '':
            continue

        if(int(vt_detection) >= 1):
            is_mal = 1
        else:
            is_mal = 0
        assert is_mal == 1 or is_mal == 0 , (l, vt_detection)
        fs.addFeature(newFeature, int(vt_detection))

    fs.dump('featureSet')

    dataList.close()