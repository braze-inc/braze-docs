---
nav_title: "사용자 별칭 개체"
article_title: API 사용자 별칭 개체
page_order: 11
page_type: reference
description: "이 참조 문서에서는 사용자 별칭 객체의 다양한 구성 요소에 대해 설명합니다."

---

# 사용자 별칭 개체

> 별칭은 대체 고유 사용자 식별자 역할을 합니다. 사용자 별칭 개체를 사용하면 모바일 앱이나 웹사이트에 로그인하기 전과 후에 특정 사용자를 추적하는 분석에 일관된 식별자를 설정할 수 있습니다. 또한 이 개체를 사용하여 타사 공급업체에서 사용하는 식별자를 Braze 사용자에게 추가하여 외부에서 데이터를 보다 쉽게 조정할 수 있습니다.

사용자 별칭 객체는 식별자 자체에 대한 `alias_name` 및 별칭 유형을 나타내는 `alias_label` 의 두 부분으로 구성됩니다. 사용자는 레이블이 다른 여러 개의 별칭을 가질 수 있지만 `alias_label` 당 `alias_name` 하나만 사용할 수 있습니다.

이 오브젝트는 모든 엔드포인트에서 자주 사용되며, 다른 오브젝트 내에서도 자주 사용됩니다.

## 개체 본문

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

### 예시

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "email_id"
  },
  "external_id": "user_456"
}
```