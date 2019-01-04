from conans import ConanFile, CMake, tools

class JuceConan(ConanFile):
    name = "juce"
    url = "https://github.com/biewers/conan-juce"
    description = "JUCE Conan Recipe"
    license = "Apache-2.0"
    version = "5.3.2"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = ["CMakeLists.txt", "*.cmake", "JuceLibraryCode/*"]
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/WeAreROLI/JUCE.git")
        self.run("cd JUCE && git checkout {0}".format(self.version))

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake . %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy(pattern="*.h", dst="include", src="JUCE/modules")
        self.copy(pattern="*.h", dst="include", src="JuceLibraryCode", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.dylib", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Macos":
            self.cpp_info.exelinkflags.append("-framework CoreFoundation")
            self.cpp_info.sharedlinkflags.append("-framework CoreFoundation")
            self.cpp_info.exelinkflags.append("-framework CoreServices")
            self.cpp_info.sharedlinkflags.append("-framework CoreServices")
            self.cpp_info.exelinkflags.append("-framework AppleScriptObjC")
            self.cpp_info.sharedlinkflags.append("-framework AppleScriptObjC")
            self.cpp_info.exelinkflags.append("-framework Cocoa")
            self.cpp_info.sharedlinkflags.append("-framework Cocoa")

