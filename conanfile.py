from conans import ConanFile, tools
import os

class OUIBlendishConan(ConanFile):
    name = "OUIBlendish"
    version = "latest"
    license = "MIT"
    author = "Leonard Ritter"
    url = "https://github.com/qno/conan-oui-blendish"
    homepage = "https://bitbucket.org/duangle/oui-blendish"
    description = "Blendish - Blender 2.5 UI based theming functions for NanoVG."

    no_copy_source = True

    _pkg_name = "oui-blendish"

    def requirements(self):
        self.requires.add("NanoVG/master@qno/testing")

    def source(self):
        url = "https://bitbucket.org/duangle/oui-blendish/get/eb226e17ec5b.zip"
        self.output.info("Downloading {}".format(url))
        tools.get(url, sha256="b26fd14046ca3e93cb6ea0ad3538028b0e2e2679ffe2e2f655b4c14862621dbf")
        os.rename("duangle-oui-blendish-eb226e17ec5b", self._pkg_name)

    def package(self):
        self.copy("*.h", dst="include", src=self._pkg_name)

    def package_id(self):
        self.info.header_only()
