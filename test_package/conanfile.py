import os

from conans import ConanFile, CMake, tools

class OUIBlendishTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "NanoVG/master@qno/testing"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".{}ouiblendishtest".format(os.sep))
