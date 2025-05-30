# 읽음 및 읽지 않음 표시기

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Braze를 사용하면 뉴스피드 카드에서 읽지 않음 및 읽음 표시기를 선택적으로 켤 수 있습니다.

![텍스트와 함께 시계 이미지가 표시된 뉴스피드 카드입니다. 텍스트 상단 모서리에는 카드가 읽혔는지 여부를 나타내는 파란색 또는 회색 삼각형이 있습니다. 파란색 삼각형은 카드를 읽었음을 나타냅니다.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## 표시기 활성화

이 기능을 사용하려면 `braze.xml` 파일에 다음 줄을 추가하세요:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## 표시기 사용자 지정하기

이러한 표시기는 `icon_read` 및 `icon_unread` 드로어블을 변경하여 사용자 지정할 수 있습니다.

