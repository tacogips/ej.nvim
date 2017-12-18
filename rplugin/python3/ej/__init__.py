import neovim

@neovim.plugin
class Ej(object):
    def __init__(self,nvim):
        self.nvim = nvim

    @neovim.function("TestFunction")
    def testfunction(self,args):
        print(args)
