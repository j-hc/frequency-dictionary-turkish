import csv
import re
import os


RE_WORD = re.compile(
    r"^([0-9]+) ([a-zçğıöşü]+) ((?:(?:adv|adj|v|n|posp|det|conj|posp)(?:, )?){1,2}).+?\n([0-9]+) (0\.[0-9]+)",  flags=re.DOTALL | re.MULTILINE)
TXTS_DIR = r"./txts" # OCR'd book pages
CSV_DIR = r"./turkish-words-freq.csv"


with open(CSV_DIR, "w+", newline='') as parsed_f:
    csv_writer = csv.writer(parsed_f)
    csv_writer.writerow(
        ["rank", "headword", "part of speech", "frequency", "dispersion"])
    for f in sorted(os.listdir(TXTS_DIR)):
        fpath = os.path.join(TXTS_DIR, f)
        with open(fpath, "r") as txt:
            def rep(w: tuple):
                w = list(w)
                t = w[2]
                if ',' in t:
                    w[2] = t.replace(', ', '/')
                    return tuple(w)
                else:
                    return tuple(w)
            parsed_row = list(map(rep, RE_WORD.findall(txt.read())))
            assert all(len(r) == 5 for r in parsed_row), parsed_row
            csv_writer.writerows(parsed_row)

print("completed")
