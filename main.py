import os
import shlex

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_tree(path, indent=""):
    files = os.listdir(path)
    for idx, name in enumerate(sorted(files)):
        full_path = os.path.join(path, name)
        is_last = idx == len(files) - 1
        prefix = "└── " if is_last else "├── "
        print(indent + prefix + name)
        if os.path.isdir(full_path):
            next_indent = indent + ("    " if is_last else "│   ")
            print_tree(full_path, next_indent)

def indexDel(cmd, start, end):
    return cmd[:start] + cmd[end:]
clear()

while True:
    name = input("컴퓨터 이름를 입력하세요: ")
    if not os.path.exists(f"C:\\Users\\{name}"):
        print("컴퓨터 이름으로 올바르지 않습니다.")
    else:
        break

highPath = os.path.join("C:\\")
nowPath = os.path.join("C:\\Users", name)
clear()
print("Welcome to Conminal!")
while True:
    cmd = input(f"#{name}/ {nowPath} $ ")
    if cmd == "exit":
        break
    elif cmd == "clean":
        clear()
    elif cmd == "tree":
        print_tree(nowPath)
    elif cmd.startswith("cd"):
        cmd = indexDel(cmd, 0, 3)
        if cmd.startswith('"') and cmd.endswith('"'):
            cmd = cmd[1:-1]
        elif cmd.startswith('"'):
            cmd = cmd[1:]
        elif cmd.endswith('"'):
            cmd = cmd[:-1]
        if cmd.startswith("C:\\") or cmd.startswith("D:\\"):
            cmd = cmd
        elif cmd == "~":
            cmd = highPath
        else:
            cmd = nowPath + "\\" + cmd
        if not os.path.exists(cmd):
            print(f"\"{cmd}\"이 경로는 존재하지 않는 경로입니다.")
        else:
            nowPath = cmd
    
    elif cmd.startswith("makfile"):
        cmd = indexDel(cmd, 0, len("makfile"))
        nameAndContent = shlex.split(cmd)
        filename = nameAndContent[0]
        content = nameAndContent[1]
        filepath =  nowPath + "\\" + filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    elif cmd.startswith("makfolder"):
        cmd = indexDel(cmd, 0, len("makfolder"))
        cmd = cmd.strip()
        cmd = cmd[1:-1]
        os.mkdir(nowPath + "\\" + cmd)

    elif cmd == "help":
        print("""
        Conminal v0.1 사용법:
        - exit: 종료
        - clean: 화면 지우기
        - tree: 현재 디렉토리 트리 출력
        - cd [경로]: 디렉토리 이동 (절대경로나 상대경로 가능)
        - makfile "파일명" "내용": 파일 생성 및 내용 쓰기
        - makfolder "폴더명": 폴더 생성
        - help: 이 도움말 출력
        """)
    
    elif cmd == "ls":
        folders = [f for f in os.listdir(nowPath) if os.path.isdir(os.path.join(nowPath, f))]
        for folder in folders:
            print(folder + " ")
        
    else:
        print(f"{cmd}은(는) 실행할 수 있는 프로그램 또는 등록 되어 있는 명령어, 내부 또는 외부 배치파일이 아닙니다.")