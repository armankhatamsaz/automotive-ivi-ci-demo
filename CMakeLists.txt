cmake_minimum_required(VERSION 3.14)
project(AutomotiveIVIVolume C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 14)

add_library(ivi_volume STATIC src/volume.c)
target_include_directories(ivi_volume PUBLIC src)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()
add_executable(test_volume tests/test_volume.cpp)
target_link_libraries(test_volume PRIVATE ivi_volume GTest::gtest_main)

add_test(NAME VolumeUnitTests COMMAND test_volume)
