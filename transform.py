import os
 
PATH_DIR = './'
 
fileList = os.listdir(PATH_DIR)

def get_newline_replaced_from_linefeed_to_empty(line):
    # 줄바꿈 문자 존재여부, 위치에 따라 변환된 텍스트를 반환
    LINE_FEED = '\n'
    
    # 문장이 '.'으로 끝나는 경우는 줄바꿈 추가
    if line.find('.' + LINE_FEED) >= 0: return line + LINE_FEED
    
    # 불필요한 줄바꿈 제거
    if line == LINE_FEED and len(line) == 1: return ''
    
    # 계속 이어지는 문장으로 판단하여 띄어쓰기로 교체
    return line.replace(LINE_FEED, ' ')


def parse_lines(lines):
    # 각 라인들의 줄바꿈 텍스트를 재배치하여 읽기 좋게 변환한 새로운 텍스트 라인들을 반환
    newLines = []
    for line in lines:
        newLines.append(get_newline_replaced_from_linefeed_to_empty(line))
    return newLines


for fileName in fileList:
    # splitext()의 [0] = 파일 이름, [1] = 확장자
    if os.path.splitext(fileName)[1] != '.txt': continue

    rf = open(PATH_DIR + fileName, 'r', encoding='utf-8')
    newLines = parse_lines(rf.readlines())
    rf.close()

    wf = open(PATH_DIR + '변환_' + fileName, 'w', encoding='utf-8')
    wf.writelines(newLines)
    wf.close()
