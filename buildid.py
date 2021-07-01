import sys
import zipfile

from elftools.elf.elffile import ELFFile
from elftools.elf.sections import NoteSection

def GetElfBuildId(elf):
    for section in elf.iter_sections():
        if not isinstance(section, NoteSection):
            continue
        for note in section.iter_notes():
            if note['n_type'] == 'NT_GNU_BUILD_ID':
                # Idiotic byte-swapping procedure from FileId::ConvertIdentifierToString
                # in breakpad/src/common/linux/file_id.cc
                bytes = (3,2,1,0, 5,4, 7,6, 8,9,10,11,12,13,14,15)
                return ''.join(note['n_desc'][2*i: 2*i + 2] for i in bytes).upper() + '0'

_, file = sys.argv
if file.endswith('.dpk'):
    z = zipfile.ZipFile(file)
    for bin in z.namelist():
        if not bin.endswith('.nexe'):
            continue
        id = GetElfBuildId(ELFFile(z.open(bin)))
        print(bin, id)
