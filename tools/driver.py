
import os
import sys
CXXC="g++"
CC="gcc"
def str_to_bool( str_v):
    """
       Converts 'something' to boolean. Raises exception for invalid formats
           Possible True  values: 1, True, "1", "TRue", "yes", "y", "t"
           Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
    """
    if str(value).lower() in ("yes", "y", "true",  "t", "1"): return True
    if str(value).lower() in ("no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))

class Dragon (self):
    def __init__(self):
        self._colorful = str_to_bool(os.environ['DRAGONCOLOR'])
        self._run_phase_c2i = True
        self._run_phase_i2s = True
        self._run_phase_i2ll = False
        self._run_phase_s2o = True
        self._run_phase_o2exe = True

        self._preprocessor_opt = ""
        self._compiler_opt = ""
        self._assembler_opt = ""
        self._linker_opt=""
        self._compile_cpp = False

    def initCPPCompile(self):
        self._preprocessor = CC
        self._compiler = CC
        self._assembler = CC
        self._linker = CC
    def initCCompile(self):
        self._preprocessor = CXXC
        self._compiler = CXXC
        self._assembler = CXXC
        self._linker= CXXC
        self._compile_cpp = False

    def prepareOptions (self, argv):
        self.add_additional_c2i_opt()
        self.add_additional_o2exe_opt()
        self.prepare_c2i_opt(argv)
        self.prepare_i2s_opt(argv)
        self.prepare_s2o_opt(argv)
        self.prepare_o2exe_opt(argv)


    def run(self):
        if self._run_phase_c2i:
            self.run_preprocessor()
        if self._run_phase_i2s:
            self.run_compiler()
        if self._run_phase_i2ll:
            self.run_compiler_to_llvmIR()
        if self._run_phase_s2o:
            self.run_assembler()
        if self._run_phase_o2exe:
            self.run_linker()

    def run_preprocessor(self):


    def run_compiler (self):

    def run_compiler_to_llvmIR(self):


    def run_assembler(self):

    def run_linker (self):



def main(argv):
    Dragon dragonobj = Dragon()
    if '-E' in argv:
        dragonobj._run_phase_i2s = False
        dragonobj._run_phase_s2o = False
        dragonobj._run_phase_o2exe = False
    elif '-S' in argv:
        if '-emit-llvm' in argv:
            dragonobj._run_phase_i2ll = True
            dragonobj._run_phase_i2s = False
        dragonobj._run_phase_s2o = False
        dragonobj._run_phase_o2exe=False
    elif '-c' in argv:
        dragonobj._run_phase_o2exe=False

    if '++' in argv[0]:
        dragonobj._compile_cpp = True
        dragonobj.initCPPCompile()
    else:
        dragonobj.initCCompile()

    dragonobj.prepareOptions(argv[1:])
    dragonobj.run()




if __name__ == "__main__":
    main (sys.argv)
