#this is for building the stack walker

# SRC = https://github.com/ivn/google-breakpad/tree/mydebugid/src/
set(SRC ..)

include_directories(${SRC})
add_definitions( -DNO_STABS_SUPPORT -D_POSIX -D__USE_MINGW_ANSI_STDIO )


add_library(libdisasm STATIC ${SRC}/third_party/libdisasm/ia32_implicit.c
    ${SRC}/third_party/libdisasm/ia32_implicit.h
    ${SRC}/third_party/libdisasm/ia32_insn.c
    ${SRC}/third_party/libdisasm/ia32_insn.h
    ${SRC}/third_party/libdisasm/ia32_invariant.c
    ${SRC}/third_party/libdisasm/ia32_invariant.h
    ${SRC}/third_party/libdisasm/ia32_modrm.c
    ${SRC}/third_party/libdisasm/ia32_modrm.h
    ${SRC}/third_party/libdisasm/ia32_opcode_tables.c
    ${SRC}/third_party/libdisasm/ia32_opcode_tables.h
    ${SRC}/third_party/libdisasm/ia32_operand.c
    ${SRC}/third_party/libdisasm/ia32_operand.h
    ${SRC}/third_party/libdisasm/ia32_reg.c
    ${SRC}/third_party/libdisasm/ia32_reg.h
    ${SRC}/third_party/libdisasm/ia32_settings.c
    ${SRC}/third_party/libdisasm/ia32_settings.h
    ${SRC}/third_party/libdisasm/libdis.h
    ${SRC}/third_party/libdisasm/qword.h
    ${SRC}/third_party/libdisasm/x86_disasm.c
    ${SRC}/third_party/libdisasm/x86_format.c
    ${SRC}/third_party/libdisasm/x86_imm.c
    ${SRC}/third_party/libdisasm/x86_imm.h
    ${SRC}/third_party/libdisasm/x86_insn.c
    ${SRC}/third_party/libdisasm/x86_misc.c
    ${SRC}/third_party/libdisasm/x86_operand_list.c
    ${SRC}/third_party/libdisasm/x86_operand_list.h
)

add_executable(minidump_stackwalk
    ${SRC}/processor/minidump_stackwalk.cc
    ${SRC}/processor/basic_code_modules.cc
    ${SRC}/processor/basic_source_line_resolver.cc
    ${SRC}/processor/binarystream.cc
    ${SRC}/processor/call_stack.cc
    ${SRC}/processor/cfi_frame_info.cc
    ${SRC}/processor/disassembler_x86.cc
    ${SRC}/processor/exploitability.cc
    ${SRC}/processor/exploitability_linux.cc
    ${SRC}/processor/exploitability_win.cc
    ${SRC}/processor/logging.cc
    ${SRC}/processor/minidump.cc
    ${SRC}/processor/minidump_processor.cc
    ${SRC}/processor/pathname_stripper.cc
    ${SRC}/processor/process_state.cc
    ${SRC}/processor/simple_symbol_supplier.cc
    ${SRC}/processor/source_line_resolver_base.cc
    ${SRC}/processor/stack_frame_cpu.cc
    ${SRC}/processor/stack_frame_symbolizer.cc
    ${SRC}/processor/stackwalker.cc
    ${SRC}/processor/stackwalker_amd64.cc
    ${SRC}/processor/stackwalker_arm.cc
    ${SRC}/processor/stackwalker_arm64.cc
    ${SRC}/processor/stackwalker_address_list.cc
    ${SRC}/processor/stackwalker_mips.cc
    ${SRC}/processor/stackwalker_ppc.cc
    ${SRC}/processor/stackwalker_ppc64.cc
    ${SRC}/processor/stackwalker_sparc.cc
    ${SRC}/processor/stackwalker_x86.cc
    ${SRC}/processor/tokenize.cc
)
target_link_libraries(minidump_stackwalk libdisasm ws2_32)
