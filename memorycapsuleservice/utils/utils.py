import hashlib
from functools import partial

class utils:
    # 判断两个字符串是否完全相等
    @staticmethod
    def checkTwoString(str1, str2):
        if str1 == str2:
            return True
        else:
            return False

    # 判断字符串是否为空
    @staticmethod
    def checkStringEmpty(str):
        if str.isspace() or len(str) == 0:
            return True
        else:
            return False

    @staticmethod
    def md5(filename):
        md5 = hashlib.md5()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(128 * md5.block_size), b''):
                md5.update(chunk)
        return md5.hexdigest()

