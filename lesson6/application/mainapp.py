from lesson6.application.pupol import Pupol


class MainApp:

    def __init__(self):
        pass
        self._is_run = False

        self.__pupol = Pupol("nick", 32, [], "self")

    def __readconfig(self):
        pass

    def __init_loger(self):
        pass

    def __read_pupol_list(self):
        pass
        self.__pupol_list = []

    def run(self):
        self._is_run = True
        try:
            # self.__readconfig()
            # self.__init_loger()
            # self.__pupol_list()
            mypupol = Pupol("nick", 32, [], "self")
            print(str(mypupol))

        except Exception as e:
            pass
        finally:
            self._is_run =False

    def exit(self):
        self._is_run = False

    def exec(self):
        pass
        while self._is_run:
            pass





