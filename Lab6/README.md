# 🧠 Lab 6: Giới thiệu về Transformers

## 1. Mục tiêu
- Ôn tập kiến thức cơ bản về kiến trúc Transformer.
- Sử dụng các mô hình Transformer tiền huấn luyện cho các tác vụ NLP cơ bản.
- Làm quen với thư viện **Hugging Face Transformers**.

---

## 2. Kiến thức cơ bản về Transformers

### 2.1 Kiến trúc Transformer
Transformer gồm hai thành phần chính:

- **Encoder**: Mã hóa văn bản đầu vào thành các vector ngữ cảnh.
- **Decoder**: Sinh văn bản đầu ra dựa trên biểu diễn của Encoder và các token trước đó.
- **Self-Attention**: Cho phép mô hình đánh giá mức độ quan trọng của các từ trong câu.

### 2.2 Các loại mô hình Transformer
- **Encoder-only**: BERT, RoBERTa → hiểu ngữ cảnh, phân loại, NER, MLM.
- **Decoder-only**: GPT → sinh văn bản, dự đoán token tiếp theo.
- **Encoder–Decoder**: T5, BART → dịch máy, tóm tắt.

---

## 3. Cài đặt môi trường

```bash
pip install transformers torch
```

---

## 4. Bài tập thực hành

### Bài 1: Masked Language Modeling (MLM)

**Code:**
```python
from transformers import pipeline

mask_filler = pipeline("fill-mask")

input_sentence = "Hanoi is the [MASK] of Vietnam."
predictions = mask_filler(input_sentence, top_k=5)

print(f"Câu gốc: {input_sentence}")
for pred in predictions:
    print(f"Dự đoán: '{pred['token_str']}' | score={pred['score']:.4f}")
    print(f" -> {pred['sequence']}")
```

**Câu hỏi & trả lời:**

1. **Mô hình có dự đoán đúng từ *capital* không?**  
→ Có. Trong hầu hết các lần chạy, từ *capital* xuất hiện ở vị trí đầu hoặc trong top-5 với độ tin cậy cao.

2. **Vì sao Encoder-only (BERT) phù hợp cho tác vụ này?**  
→ Vì BERT có khả năng nhìn ngữ cảnh **hai chiều**, cho phép tận dụng cả từ trước và sau token bị che để dự đoán chính xác.

---

### Bài 2: Next Token Prediction (Text Generation)

**Code:**
```python
from transformers import pipeline

generator = pipeline("text-generation")

prompt = "The best thing about learning NLP is"
outputs = generator(prompt, max_length=50, num_return_sequences=1)

print(f"Câu mồi: {prompt}")
print(outputs[0]['generated_text'])
```

**Câu hỏi & trả lời:**

1. **Kết quả sinh ra có hợp lý không?**  
→ Có. Văn bản sinh ra thường mạch lạc và liên quan đến học NLP.

2. **Vì sao Decoder-only (GPT) phù hợp?**  
→ GPT được huấn luyện để dự đoán **token tiếp theo** theo hướng một chiều, rất phù hợp cho sinh văn bản liên tục.

---

### Bài 3: Vector biểu diễn câu (Sentence Representation)

**Code (Mean Pooling):**
```python
import torch
from transformers import AutoTokenizer, AutoModel

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

sentences = ["This is a sample sentence."]
inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

with torch.no_grad():
    outputs = model(**inputs)

last_hidden_state = outputs.last_hidden_state
attention_mask = inputs['attention_mask']

mask_expanded = attention_mask.unsqueeze(-1).expand(last_hidden_state.size()).float()
sum_embeddings = torch.sum(last_hidden_state * mask_expanded, 1)
sum_mask = torch.clamp(mask_expanded.sum(1), min=1e-9)
sentence_embedding = sum_embeddings / sum_mask

print(sentence_embedding)
print("Kích thước vector:", sentence_embedding.shape)
```

**Câu hỏi & trả lời:**

1. **Kích thước vector là bao nhiêu? Tương ứng tham số nào?**  
→ Vector có kích thước **(1, 768)**.  
→ 768 là **hidden_size** của mô hình `bert-base-uncased`.

2. **Vì sao cần attention_mask khi Mean Pooling?**  
→ Để **loại bỏ ảnh hưởng của các token padding**, đảm bảo chỉ tính trung bình trên các token thật.

---

## 5. Tổng kết

- BERT rất mạnh cho các tác vụ **hiểu ngữ cảnh** (MLM, embedding).
- GPT phù hợp cho **sinh văn bản** và dự đoán token tiếp theo.
- Mean Pooling tạo sentence embedding ổn định và hiệu quả.
- Transformer là nền tảng cho các mô hình NLP hiện đại như BERT, GPT, T5.

---

## 6. Kết luận

Lab này giúp làm quen với:
- Kiến trúc Transformer
- Hugging Face pipelines
- Ứng dụng thực tế của Encoder-only và Decoder-only models

Đây là nền tảng quan trọng để tiếp cận các mô hình NLP nâng cao.

