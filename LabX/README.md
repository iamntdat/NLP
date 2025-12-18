# Báo cáo tổng quan: Text-To-Speech (TTS)

## 1. Mục tiêu bài tập
Tổng hợp, phân tích và trình bày có hệ thống về:
- Bối cảnh nghiên cứu Text-To-Speech (TTS)
- Các hướng tiếp cận chính trong TTS
- Ưu / nhược điểm của từng hướng
- Cách các nghiên cứu hiện đại kết hợp các thành phần để giảm nhược điểm và tăng ưu điểm

---

## 2. Bức tranh toàn cảnh (Overview)

Sự phát triển của TTS có thể chia thành 3 **level chính**:

### 🔹 Level 1 — Rule-based / Concatenative
- Dựa trên luật hoặc ghép các đoạn âm thanh có sẵn
- Nhanh, dễ triển khai, ít tài nguyên
- Chất lượng tự nhiên và biểu cảm thấp

### 🔹 Level 2 — Deep Learning Acoustic Models + Neural Vocoders
- Ví dụ: Tacotron, Tacotron2 + WaveNet / HiFi-GAN
- Chất lượng tự nhiên cao, giọng mượt
- Yêu cầu nhiều dữ liệu và tài nguyên tính toán

### 🔹 Level 3 — Few-shot / Zero-shot Voice Cloning
- Tạo giọng nói giống người tham chiếu chỉ với vài giây audio
- Kỹ thuật phức tạp, chi phí cao
- Tiềm ẩn rủi ro lạm dụng (deepfake)

---

## 3. Các phương pháp chính và ví dụ tiêu biểu

### 3.1. Concatenative & Parametric TTS (truyền thống)
**Ý tưởng:**
- Ghép các đơn vị âm thanh (phoneme, syllable)
- Hoặc dự đoán tham số rồi tổng hợp lại waveform

**Hạn chế:**
- Thiếu linh hoạt
- Khó biểu cảm, ngữ điệu kém tự nhiên

---

### 3.2. Neural TTS (End-to-End)

#### 🔸 Tacotron / Tacotron 2
- Chuyển `text → mel-spectrogram`
- Cần vocoder để sinh waveform
- Tacotron 2 là cột mốc lớn về chất lượng tự nhiên

#### 🔸 FastSpeech / FastSpeech 2
- Kiến trúc **non-autoregressive**
- Sinh nhanh, ổn định, phù hợp triển khai thực tế
- FastSpeech2 học trực tiếp:
  - duration
  - pitch
  - energy

#### 🔸 VITS (Variational Inference + GAN)
- End-to-end, một giai đoạn
- Kết hợp VAE + GAN
- Sinh trực tiếp waveform chất lượng cao

---

### 3.3. Neural Vocoders
| Vocoder | Đặc điểm |
|-------|--------|
| WaveNet | Chất lượng rất cao, nhưng chậm |
| WaveGlow | Song song, nhanh hơn |
| HiFi-GAN | Rất nhanh, chất lượng cao, phổ biến |
| Parallel WaveGAN | Tốc độ tốt, ổn định |

---

## 4. Few-shot & Zero-shot Voice Cloning

**Nguyên lý chung:**
- Tách riêng **speaker encoder**
- Dùng embedding giọng nói để điều kiện hóa mô hình TTS

### 🔹 Zero-shot
- Chỉ cần vài giây audio
- Không fine-tune
- Linh hoạt nhưng độ giống giọng có thể thấp

### 🔹 Few-shot
- Fine-tune hoặc adapter
- Fidelity cao hơn
- Tốn thêm dữ liệu & thời gian huấn luyện

---

## 5. Ưu điểm và nhược điểm theo level

### Level 1 — Rule / Concatenative
**Ưu điểm**
- Nhanh
- Ít yêu cầu dữ liệu

**Nhược điểm**
- Giọng không tự nhiên
- Khó biểu cảm

### Level 2 — Deep Learning + Vocoder
**Ưu điểm**
- Chất lượng tự nhiên cao
- Biểu cảm tốt

**Nhược điểm**
- Cần nhiều dữ liệu
- Vocoder autoregressive có thể chậm

### Level 3 — Few/Zero-shot
**Ưu điểm**
- Cá nhân hóa giọng nói nhanh
- Ứng dụng đa dạng

**Nhược điểm**
- Rủi ro deepfake
- Chất lượng giảm khi dữ liệu quá ít

---

## 6. Các thách thức và hướng giải quyết hiện tại

### ⚡ Hiệu suất & độ trễ
- FastSpeech2 (non-autoregressive)
- HiFi-GAN cho inference nhanh

### 🌍 Đa ngôn ngữ & low-resource
- Self-supervised learning (wav2vec, XLS-R)
- Transfer learning
- Hierarchical / multilingual models

### 🎵 Biểu cảm & Prosody
- Dự đoán pitch / energy / duration
- Style tokens
- Expressive TTS models

### 🔐 An ninh & đạo đức
- Watermarking
- Deepfake detection
- Metadata & chính sách sử dụng

---

## 7. Pipeline TTS tham khảo

1. **Data collection & preprocessing**
   - Chuẩn hóa transcript
   - Tách câu
   - Chuẩn hóa ký tự
   - Chuyển text → phoneme (nếu cần)

2. **Speaker / Style extractor**
   - Dùng pre-trained speaker encoder
   - Phục vụ multi-speaker hoặc voice cloning

3. **Acoustic model**
   - FastSpeech2 (ưu tiên tốc độ)
   - VITS (ưu tiên chất lượng)

4. **Neural vocoder**
   - HiFi-GAN
   - Parallel WaveGAN

5. **Fine-tuning / Adaptation**
   - Few-shot adaptation nếu cần

6. **Watermarking & Detection**
   - Phục vụ yêu cầu đạo đức và an toàn

7. **Evaluation**
   - MOS (subjective)
   - MCD
   - CER / WER
   - Speaker similarity (x-vector, EER)
   - Prosody metrics

---

## 📌 Kết luận
TTS hiện đại là sự kết hợp chặt chẽ giữa:
- Mô hình học sâu
- Kiến trúc sinh nhanh
- Kỹ thuật cá nhân hóa giọng nói
- Các biện pháp đảm bảo an toàn và đạo đức

Xu hướng tương lai tập trung vào **chất lượng cao + tốc độ nhanh + ít dữ liệu + an toàn**.
