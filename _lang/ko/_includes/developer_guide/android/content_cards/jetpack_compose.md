# Jetpack Compose를 사용하는 콘텐츠 카드

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션용 Jetpack Compose를 사용한 콘텐츠 카드 통합을 다룹니다.

Android에서는 `ContentCardsList()`를 사용하여 콘텐츠 카드 피드를 Compose 애플리케이션에 추가할 수 있습니다. For example:

```kotlin
setContent {
    ContentCardsList()
}
```

## 카드 클릭 처리

카드 클릭을 처리하려면 `Card`를 가져와 `Boolean`을 `onCardClicked`로 반환하는 함수를 전달합니다. `true`가 반환되면 Braze는 분석을 위해 기록하는 작업 외에 클릭에 대한 어떠한 처리도 하지 않습니다. `false` 이 반환되면 Braze가 클릭을 처리합니다.

```kotlin
ContentCardsList(
    onCardClicked = { card ->
        if (card.extras.containsKey("mySpecialKey")) {
            // handle the click here
            true
        } else {
            // Let Braze handle the click
            false
        }
    }
)
```

## 해제에 대한 알림 활성화

카드가 해제될 때 알림을 받으려면 `onCardDismissed` 함수로 함수를 전달합니다.

```kotlin
ContentCardsList(
    onCardDismissed = { card ->
        // Do what you need with the card
    }
)
```
