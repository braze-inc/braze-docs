---
nav_title: 사용자 ID 설정
article_title: 웹용 사용자 ID 설정
platform: Web
page_order: 1
page_type: reference
description: "이 도움말에서는 각 사용자에 대한 사용자 ID를 설정하는 방법과 변경하기 전에 고려해야 할 모범 사례 및 중요 사항을 설명합니다."
 
---

# 사용자 ID 설정

> 이 도움말에서는 각 사용자에 대한 사용자 ID를 설정하는 방법과 변경하기 전에 고려해야 할 모범 사례 및 중요 사항을 설명합니다.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

사용자가 식별되면 일반적으로 로그인 후 사용자 ID를 설정하기 위해 다음 호출을 즉시 수행해야 합니다.

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**사용자가 로그아웃할 때 `changeUser()` 으로 전화하지 마세요.** `changeUser()`를 정적 기본값으로 설정하면 사용자가 다시 로그인할 때까지 모든 사용자 활동이 해당 기본 '사용자'와 연결됩니다.
{% endalert %}

사용자가 로그아웃할 때 사용자 ID를 변경하면 이전에 로그인한 사용자를 리인게이지먼트 캠페인으로 타겟팅할 수 없게 되므로 사용자 ID를 변경하지 않는 것이 좋습니다. 여러 사용자가 동일한 기기를 사용할 것으로 예상되지만 앱에서 로그아웃한 상태일 때 사용자 중 한 명만을 타겟팅하려는 경우, 로그아웃 상태에서 타겟팅하려는 사용자 ID를 별도로 추적하고 앱의 로그아웃 프로세스의 일환으로 해당 사용자 ID로 전환하는 방법을 권장합니다.

자세한 내용은 [`changeUser()` 문서 ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser "자바독스를") 참조하세요.

## 추천 사용자 ID 명명 규칙

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## 사용자 ID 통합 모범 사례 및 참고 사항

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## 사용자 별칭 지정

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Web" %}

