cmake_minimum_required(VERSION 3.4)
project(juce)

include(common.cmake)
include(options.cmake)
include(modules.cmake)

message(STATUS "CMAKE_CXX_FLAGS=${CMAKE_CXX_FLAGS}")
message(STATUS "CMAKE_CXX_FLAGS_DEBUG=${CMAKE_CXX_FLAGS_DEBUG}")
message(STATUS "CMAKE_CXX_FLAGS_RELEASE=${CMAKE_CXX_FLAGS_RELEASE}")

include_directories(${PROJECT_SOURCE_DIR}/JUCE/modules)
add_library(juce STATIC ${juce_SOURCES})

