---
nav_title: 기본값 설정
article_title: 기본 액체 값 설정
page_order: 5
description: "이 참조 문서에서는 메시지에서 사용하는 개인화 속성에 대한 기본 대체 값을 설정하는 방법에 대해 설명합니다."

---

# 기본값 설정

{% raw %}

> 메시지에서 사용하는 모든 개인화 속성에 대해 기본 대체 값을 설정할 수 있습니다. 

기본값은 "default"라는 이름의 [액체 필터][3] (그림과 같이 필터를 인라인으로 구분하려면 `|` 사용)를 지정하여 추가할 수 있습니다.

```
| default: 'Insert Your Desired Default Here'
```

기본값이 제공되지 않고 필드가 누락되었거나 사용자에게 설정되지 않은 경우 메시지에서 필드가 비워집니다.

다음 예는 기본값을 추가하는 올바른 구문을 보여줍니다. 이 경우 사용자의 `first_name` 필드가 비어 있거나 사용할 수 없는 경우 "Valued User"라는 단어가 `{{ ${first_name} }}` 속성을 대체합니다.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

신원 미상이라는 사용자에게는 이 메시지가 다음과 같이 표시됩니다:

```
Hi Janet, thanks for using the App!
```

아니면...

```
Hi Valued User, thanks for using the App!
```

{% endraw %}

[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#null 속성 값에 대한 회계 처리
