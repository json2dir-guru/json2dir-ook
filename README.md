# json2dir-ook

json2dir in Ook!: `json2dir.ook` (transliterated by `tools/bf2ook.py` from json2dir-brainfuck's pure 8-command `json2dir.bf`) checks UTF-8, parses and validates the JSON document and prints a shell script, which the POSIX sh launcher `json2dir` runs; the launcher only frames stdin as decimal byte values (`od -An -v -tu1`). Interpreter: `ook -ook -r` built from `extras/ook.l` of rdebath/Brainfuck (8-bit wrapping cells).

    python3 tools/bf2ook.py ../json2dir-brainfuck/json2dir.bf > json2dir.ook
    JSON2DIR_OOK="/path/to/ook -ook -r" ./json2dir < tree.json
