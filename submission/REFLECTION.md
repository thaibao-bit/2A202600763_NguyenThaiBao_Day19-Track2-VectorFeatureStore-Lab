# Reflection — Lab 19

**Tên:** Nguyễn Thái Bảo
**Cohort:** A20
**Path đã chạy:** lite

---

## Câu hỏi (≤ 200 chữ)

> Trên golden set 50 queries, mode nào thắng ở loại query nào (`exact` /
> `paraphrase` / `mixed`), và tại sao? Khi nào bạn **không** dùng hybrid
> (i.e. khi nào pure BM25 hoặc pure vector là lựa chọn đúng)?

Trên golden set, hybrid thắng trung bình: 78.6%, cao hơn BM25 77.8% và vector
73.2%. Với `exact`, BM25 và hybrid cùng đạt 96.7% vì query chứa đúng thuật ngữ
kỹ thuật như Kubernetes, OAuth, PostgreSQL nên lexical match rất mạnh. Với
`mixed`, hybrid tốt nhất (100.0%) vì RRF kết hợp được tín hiệu keyword rõ ràng
và ngữ nghĩa của phần mô tả tiếng Việt. Với `paraphrase`, kết quả lần chạy này
BM25 hơi nhỉnh hơn hybrid/vector; lý do có thể là corpus synthetic vẫn còn nhiều
từ chủ đề trùng nhau, còn model `bge-small-en` không tối ưu hoàn toàn cho tiếng
Việt. Tôi không dùng hybrid khi query là mã lỗi, ID, tên API chính xác hoặc cần
latency/cost thấp nhất; khi đó BM25 đủ tốt. Ngược lại, nếu query dài, mơ hồ,
nhiều diễn đạt đồng nghĩa hoặc code-switch vi/en, pure vector có thể phù hợp hơn.

---

## Điều ngạc nhiên nhất khi làm lab này

Điều ngạc nhiên nhất là hybrid thắng không phải vì vector luôn tốt hơn, mà vì nó
giảm rủi ro khi mỗi retriever mạnh ở một kiểu query khác nhau.

---

## Bonus challenge

- [ ] Đã làm bonus (xem `bonus/`)
- [ ] Pair work với: N/A
