import shelve
from classModelInterface import ModelInterface

class ChatSupport:
    def __init__(self):
        self.__MInterface = ModelInterface()
        self.__usersDialogs = shelve.open("UsersDialogData")

    def __getUserdialog(self, userid):
        if userid in self.__usersDialogs:
            return self.__usersDialogs[userid]
        return ""

    def __setUserdialog(self, userid, dialog):
        self.__usersDialogs[userid] = dialog

    def getAnswer(self,userid,text):

        dig = self.__getUserdialog(userid) + " @@ПЕРВЫЙ@@ " + text
        ans = self.__MInterface.generate(dig)

        self.__setUserdialog(userid, ans)
        return ans.split("@@ВТОРОЙ@@")[-1]
