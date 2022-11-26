
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR RL78)

if(MINGW OR CYGWIN OR WIN32)
	set(EXECUTABLE_FILE_EXTESION .exe)
endif()

find_path(RL78_TOOLCHAIN_DIR rl78-elf-gcc${EXECUTABLE_FILE_EXTESION})


set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
set(CMAKE_C_COMPILER_WORKS 1)
set(CMAKE_ASM_COMPILER_WORKS 1)


set(CMAKE_C_COMPILER ${RL78_TOOLCHAIN_DIR}/rl78-elf-gcc${EXECUTABLE_FILE_EXTESION})
set(CMAKE_ASM_COMPILER ${RL78_TOOLCHAIN_DIR}/rl78-elf-gcc${EXECUTABLE_FILE_EXTESION})
set(CMAKE_C_LINKER ${RL78_TOOLCHAIN_DIR}/rl78-elf-gcc${EXECUTABLE_FILE_EXTESION})
set(CMAKE_OBJCOPY ${RL78_TOOLCHAIN_DIR}/rl78-elf-objcopy${EXECUTABLE_FILE_EXTESION})

SET(ASM_OPTIONS "-x assembler-with-cpp -Wa,--gdwarf2")
SET(CMAKE_ASM_FLAGS "${CFLAGS} ${ASM_OPTIONS}" )

set(CMAKE_SIZE_UTIL ${RL78_TOOLCHAIN_DIR}/rl78-elf-size${EXECUTABLE_FILE_EXTESION})


