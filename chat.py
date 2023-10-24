import json
from difflib import get_close_matches

def load_kb(path):
    with open(path,'r') as file:
        data = json.load(file)
    return data
def save_kb(path,data):
    with open(path,'w') as file:
        json.dump(data, file, indent=2)
def find_b_match(uquestion, questions):
    matches = get_close_matches(uquestion,questions,n=1,cutoff=0.7)
    return matches[0] if matches else None
def get_ans(question,kb):
    for q in kb["questions"]:
        if q["question"]== question:
            return q["answer"]
def chatbot():
    kb=load_kb("knowledge_base.json")
    while True:
        user_input=input("you: ")
        if(user_input=="quit"):
            break
        best_match = find_b_match(user_input, [q["question"] for q in kb["questions"]])
        if best_match:
            answer=get_ans(best_match,kb)
            print(f'bot: {answer}')
        else:
            print("bot: I don't know the answer. can you teach me ? ")
            new_answer = input("type new ans or skip to skip: ")
            if new_answer.lower()!= 'skip':
                kb["questions"].append({"question":user_input,"answer":new_answer})
                save_kb('knowledge_base.json',kb)
                print("thank you I learned a new response!")
chatbot()


