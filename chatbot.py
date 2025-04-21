from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np
from groq import Groq
import os

client = Groq(api_key="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")


def get_answer_from_context(question: str, context_chunks: list[str]) -> str:
    context = "\n".join(context_chunks)
    prompt = f"""Question: {question}
                 Context: {context}
                 Answer:"""
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "Câu trả lời phải luôn là Tiếng Việt. Bạn là trợ lý tư vấn điểm chuẩn đại học năm 2024. Hãy trả lời ngắn gọn, súc tích và chính xác."},
            {"role": "user", "content": question},
            {"role": "assistant", "content": prompt}
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False
    )
    return response.choices[0].message.content


embedding_model = None
context_data = None
context_keys = None
faiss_index = None


def initialize_chatbot():
    global embedding_model, context_data, context_keys, faiss_index

    if not os.path.exists("./data/dataset.json") or not os.path.exists("./data/vector_db.faiss"):
        return False

    try:
        embedding_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

        with open("./data/dataset.json", "r", encoding="utf-8") as file:
            context_data = json.load(file)

        context_keys = list(context_data.keys())

        faiss_index = faiss.read_index("./data/vector_db.faiss")

        return True
    except Exception as e:
        print(f"Lỗi khi khởi tạo chatbot: {e}")
        return False


def process_question(question: str) -> str:
    if embedding_model is None or context_data is None or context_keys is None or faiss_index is None:
        return "Chatbot chưa được khởi tạo. Vui lòng thử lại sau."

    try:
        query_vector = np.array(embedding_model.encode([question], show_progress_bar=False)).astype("float32")

        _, top_indices = faiss_index.search(query_vector, k=3)

        matched_keys = [context_keys[i] for i in top_indices[0]]
        matched_contexts = [context_data[key] for key in matched_keys]

        answer = get_answer_from_context(question, matched_contexts)

        return answer
    except Exception as e:
        print(f"Lỗi khi xử lý câu hỏi: {e}")
        return "Đã xảy ra lỗi khi xử lý câu hỏi của bạn. Vui lòng thử lại sau."


def fallback_answer(question: str) -> str:
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "Bạn là trợ lý tư vấn điểm chuẩn đại học năm 2024. Hãy trả lời ngắn gọn, súc tích và chính xác bằng Tiếng Việt."},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        stream=False
    )
    return response.choices[0].message.content


def get_chatbot_response(question: str) -> str:
    global embedding_model, context_data, context_keys, faiss_index

    if embedding_model is None:
        success = initialize_chatbot()
        if not success:
            return fallback_answer(question)

    try:
        query_vector = np.array(embedding_model.encode([question], show_progress_bar=False)).astype("float32")

        _, top_indices = faiss_index.search(query_vector, k=3)

        matched_keys = [context_keys[i] for i in top_indices[0]]
        matched_contexts = [context_data[key] for key in matched_keys]

        answer = get_answer_from_context(question, matched_contexts)

        return answer
    except Exception as e:
        print(f"Lỗi khi xử lý câu hỏi: {e}")
        return "Đã xảy ra lỗi khi xử lý câu hỏi của bạn. Vui lòng thử lại sau."
