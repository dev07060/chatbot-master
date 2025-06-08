import pandas as pd               # 데이터프레임 형태로 CSV 파일을 다루기 위한 라이브러리
import Levenshtein               # 레벤슈타인 거리 계산을 위한 라이브러리

# ChatbotData.csv 파일 불러오기
# 질문(Q), 답변(A), 라벨(label) 컬럼이 포함되어 있음
chatbot_data = pd.read_csv('ChatbotData.csv')

# 질문과 답변만 리스트로 추출
questions = chatbot_data['Q'].tolist()  # 질문(Q) 리스트
answers = chatbot_data['A'].tolist()    # 답변(A) 리스트

def get_most_similar_answer(user_input):
    """
    사용자 입력과 가장 유사한 질문을 찾아 해당하는 답변을 반환하는 함수
    
    Parameters:
        user_input (str): 사용자가 입력한 질문
        
    Returns:
        tuple: (가장 유사한 질문, 해당 질문에 대한 챗봇의 답변)
    """
    # 각 질문과 사용자 입력 간의 레벤슈타인 거리 계산
    distances = [Levenshtein.distance(user_input, q) for q in questions]
    
    # 최소 거리를 가지는 질문의 인덱스를 구함 (가장 유사한 질문)
    min_index = distances.index(min(distances))
    
    # 가장 유사한 질문과 해당 답변 반환
    return questions[min_index], answers[min_index]

# 챗봇 인터페이스 실행 부분 (콘솔 입력 기반)
if __name__ == '__main__':
    print("안녕하세요! 무엇을 도와드릴까요? (종료하려면 '종료'라고 입력하세요)")
    
    while True:
        # 사용자로부터 질문 입력 받기
        user_input = input(">> ")
        
        # '종료' 입력 시 챗봇 종료
        if user_input.lower() == '종료':
            print("안녕히 가세요!")
            break
        
        # 가장 유사한 질문과 챗봇의 응답 구하기
        question, response = get_most_similar_answer(user_input)
        
        # 결과 출력
        print(f"가장 유사한 질문: {question}")
        print(f"챗봇: {response}")