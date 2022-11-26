add_library(cobs src/cobs.c)
target_include_directories(cobs PUBLIC include)
target_compile_options(cobs PRIVATE -std=c11)
