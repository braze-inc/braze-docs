## 중첩된 속성 정보

중첩 고객 속성을 사용하면 단일 커스텀 속성 오브젝트의 데이터로 더욱 풍부한 세그먼트를 구축하고 메시지를 개인화할 수 있습니다.

다음 예제에서 커스텀 속성 `favorite_book` 에는 중첩된 고객 속성 `title`, `author`, `publishing_date` 이 포함되어 있습니다. 이 개체를 사용하여 저자별로 사용자를 타겟팅하거나, 게시 날짜별로 필터링하거나, 책 제목을 메시지에 직접 삽입할 수 있습니다:

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```