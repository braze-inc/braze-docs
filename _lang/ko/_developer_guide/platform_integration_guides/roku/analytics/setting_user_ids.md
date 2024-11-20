---
nav_title: 사용자 ID 설정
article_title: Roku에 사용자 ID 설정
platform: Roku
page_order: 0
page_type: reference
description: "이 참조 문서에서는 Roku 사용자 ID를 식별하고 설정하는 방법, 모범 사례 및 중요한 고려사항을 다룹니다."
 
---

# 사용자 ID 설정

> 이 참조 문서에서는 Roku 사용자 ID를 식별하고 설정하는 방법, 모범 사례 및 중요한 고려사항을 다룹니다.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

사용자가 식별되는 즉시(일반적으로 로그인 후) 다음 호출을 수행하여 사용자 ID를 설정해야 합니다.

```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## 제안된 사용자 ID 명명 규칙

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## 사용자 ID 통합 모범 사례 및 참고 사항

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

