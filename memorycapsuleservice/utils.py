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
        if len(str) == 0 or str.isspace():
            return True
        else:
            return False
