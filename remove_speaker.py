import os

PATH_DIR = './'

fileList = os.listdir(PATH_DIR)


def parse_lines(lines):
    # 각 라인들의 ':' 문자를 찾아서 이전 문자들과 다음 여백까지 제거
    # ex) Heena Bawazir: Hello everybody, good evening.
    # -> "Heena Bawazir: " 제거
    # -> Hello everybody, good evening.
    new_lines = []
    for line in lines:
        foundIdx = line.find(': ')
        if (foundIdx > -1):
            new_line = line[foundIdx + 2:]
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    return new_lines


for fileName in fileList:
    # splitext()의 [0] = 파일 이름, [1] = 확장자
    validExtentions = ['.txt', '.srt']
    if (os.path.splitext(fileName)[1] not in validExtentions):
        continue

    rf = open(PATH_DIR + fileName, 'r', encoding='utf-8')
    newLines = parse_lines(rf.readlines())
    rf.close()

    wf = open(PATH_DIR + '변환_' + fileName, 'w', encoding='utf-8')
    wf.writelines(newLines)
    wf.close()
