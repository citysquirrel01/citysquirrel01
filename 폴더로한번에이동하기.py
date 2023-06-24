import os
import shutil

source_folder = "/Users/parkdahye/Downloads/myUL-Reports-Procedures-Date_2023. 6. 24. 오후undefined 23149"
destination_folder = "/Users/parkdahye/Desktop/ul"

# 폴더 "가" 안의 모든 폴더를 확인
for foldername in os.listdir(source_folder):
    folder_path = os.path.join(source_folder, foldername)
    # 폴더인 경우에만 처리
    if os.path.isdir(folder_path):
        # 폴더 내의 모든 파일을 확인
        for filename in os.listdir(folder_path):
            if filename.endswith(".docx"):
                # 원본 파일의 전체 경로
                source_file = os.path.join(folder_path, filename)
                # 이동할 파일의 전체 경로
                destination_file = os.path.join(destination_folder, filename)
                # 파일 이동
                shutil.move(source_file, destination_file)
                print(f"{filename}을(를) 이동했습니다.")
