function(cxx_define FLAG VALUE)
    if(WIN32)
        set(${FLAG} "${${FLAG}} /D${VALUE}" PARENT_SCOPE)
    else()
        set(${FLAG} "${${FLAG}} -D${VALUE}" PARENT_SCOPE)
    endif()
endfunction(cxx_define)

if(UNIX AND !APPLE)
    cxx_define(CMAKE_CXX_FLAGS "LINUX")
endif(UNIX AND !APPLE)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
cxx_define(CMAKE_CXX_FLAGS_DEBUG "DEBUG")
cxx_define(CMAKE_CXX_FLAGS_RELEASE "NDEBUG")

