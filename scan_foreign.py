import os, sys, re

path = r"D:/AIDownloadFiles/国学json/百家号带货视频/baijiadaihuo/input/视频文案/引导文案"
foreign = re.compile(r'[а-яА-ЯёЁ\u3040-\u30ff\uac00-\ud7af]|[a-zA-Z]{4,}')

for fname in sorted(os.listdir(path)):
    if not fname.endswith('.txt'):
        continue
    fpath = os.path.join(path, fname)
    with open(fpath, encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f, 1):
            m = foreign.search(line)
            if m:
                print(f"{fname}:{i}: {line.strip()[:80]}")
