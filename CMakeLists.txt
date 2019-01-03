cmake_minimum_required(VERSION 3.4)
project(juce)

if(UNIX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -DNDEBUG")
endif(UNIX)

include_directories(${PROJECT_SOURCE_DIR}/JUCE/modules)

set(juce_SOURCES
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/AppConfig.h
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/JuceHeader.h
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_analytics.cpp
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_audio_basics.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_audio_devices.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_audio_formats.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_audio_processors.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_audio_utils.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_blocks_basics.cpp
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_box2d.cpp
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_core.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_cryptography.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_data_structures.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_dsp.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_events.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_gui_basics.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_graphics.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_gui_extra.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_opengl.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_osc.cpp
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_product_unlocking.mm
    ${CMAKE_CURRENT_LIST_DIR}/JuceLibraryCode/include_juce_video.mm
)

add_library(juce STATIC ${juce_SOURCES})

