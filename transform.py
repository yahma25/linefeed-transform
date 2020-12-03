import os

PATH_DIR = './'

fileList = os.listdir(PATH_DIR)


def get_newline_replaced_from_linefeed_to_empty(line):
    # 줄바꿈 문자 존재여부, 위치에 따라 변환된 텍스트를 반환
    LINE_FEED = '\n'

    # 띄어쓰기와 줄바꿈을 다시 정의하기 위해 문자만 남겨둠
    new_line = line.strip()

    # 불필요한 줄바꿈 제거
    if len(new_line) <= 1:
        return ''

    last_char = new_line[len(new_line) - 1]
    sentence_end_char_list = ['.', '!', '?']

    # 종료 문자면 줄바꿈, 문장 간의 한줄 여백을 두기 위해 줄바꿈 1개 추가
    if (last_char in sentence_end_char_list):
        return new_line + LINE_FEED + LINE_FEED

    # 이 외의 경우는 이어지는 문장으로 간주하고 띄어쓰기
    return new_line + ' '


def parse_lines(lines):
    # 각 라인들의 줄바꿈 텍스트를 재배치하여 읽기 좋게 변환한 새로운 텍스트 라인들을 반환
    new_lines = []
    for line in lines:
        replaced_line = get_newline_replaced_from_linefeed_to_empty(line)
        new_lines.append(replaced_line)
    return new_lines


for fileName in fileList:
    # splitext()의 [0] = 파일 이름, [1] = 확장자
    if os.path.splitext(fileName)[1] != '.txt':
        continue

    rf = open(PATH_DIR + fileName, 'r', encoding='utf-8')
    newLines = parse_lines(rf.readlines())
    rf.close()

    wf = open(PATH_DIR + '변환_' + fileName, 'w', encoding='utf-8')
    wf.writelines(newLines)
    wf.close()
