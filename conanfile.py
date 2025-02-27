from conans import ConanFile, tools


class Bzip2Conan(ConanFile):
    name = "bzip2"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    description = "<Description of Bzip2 here>"
    url = "None"
    license = "None"
    author = "None"
    topics = None

    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
