---
page_order: 2.0
nav_title: Rate limits
article_title: Braze SDK 사용량 제한
description: "Braze SDK의 지능형 클라이언트 측 사용량 제한 기능에 대해 알아보세요. 이 기능은 배터리 수명을 최적화하고, 대역폭 사용량을 줄이며, 안정적인 데이터 전달을 보장합니다."
---

# Braze SDK 사용량 제한

> Braze SDK의 지능형 클라이언트 측 사용량 제한 기능에 대해 알아보세요. 이 기능은 배터리 수명을 최적화하고, 대역폭 사용량을 줄이며, 안정적인 데이터 전달을 보장합니다.

## SDK 사용량 제한 이해하기

Braze SDK 사용량 제한은 성능 최적화, 배터리 소모 최소화, 데이터 사용량 감소 및 안정적인 데이터 전달을 보장하기 위해 다음과 같은 기능을 사용합니다:

### 비동기 처리

Braze SDK는 사용량 제한을 위해 토큰 버킷 알고리즘을 사용합니다. 이 접근법은 장기적인 속도 제어를 유지하면서 활동의 급증을 허용합니다. 엄격한 대기줄에서 요청을 처리하는 대신, 토큰 버킷은 비동기적으로 작동합니다:

- **토큰 생성**: 토큰은 버킷에 일정한 속도로 보충됩니다.
- **요청 처리**: 토큰이 사용 가능한 상태에서 도착한 모든 SDK 호출은 다른 호출의 도착 시점과 무관하게 즉시 진행됩니다.
- **엄격한 순서 없음**: 요청은 줄을 서서 기다리지 않습니다. 여러 호출이 다음 사용 가능한 토큰을 놓고 경쟁할 수 있습니다.
- **버스트 처리**: 요청 시점에 충분한 토큰이 사용 가능한 경우, 짧은 활동 폭발이 허용됩니다.
- **속도 제어**: 장기적인 처리량은 꾸준한 토큰 보충 속도에 의해 제한됩니다.

이 비동기적 흐름은 SDK가 예측 가능한 전체 트래픽 수준을 유지하면서 사용 가능한 네트워크 용량에 신속하게 대응할 수 있도록 도와줍니다.

### 적응형 사용량 제한

Braze SDK는 네트워크 인프라를 보호하고 최적의 성능을 유지하기 위해 실시간으로 사용량 제한을 조정할 수 있습니다. 이 접근법은:

- **과부하를 방지합니다**: 네트워크 혼잡을 방지하기 위해 제한을 조정합니다.
- **성능을 최적화합니다**: 다양한 조건에서도 SDK의 원활한 작동을 유지합니다.
- **조건에 반응합니다**: 현재 네트워크 및 사용 패턴에 따라 적응합니다.

{% alert note %}
제한은 실시간으로 조정되므로 정확한 버킷 크기와 정적 값은 제공되지 않습니다. 네트워크 상태 및 사용량에 따라 변경될 수 있습니다.
{% endalert %}

### 네트워킹 최적화

Braze SDK에는 효율성 향상, 배터리 사용량 감소, 다양한 네트워크 환경 처리를 위한 여러 내장 동작이 포함되어 있습니다:

- **자동 배치**: 이벤트를 대기줄에 넣고 효율적인 배치 단위로 전송합니다.
- **네트워크 인식 동작**: 연결 품질에 따라 플러시 속도를 조정합니다.
- **배터리 최적화**: 라디오 웨이크업 및 네트워크 호출을 최소화합니다.
- **점진적 성능 저하**: 네트워크 상태가 좋지 않은 환경에서도 기능을 유지합니다.
- **백그라운드/포그라운드 인식**: 앱의 라이프사이클 변화에 따라 동작을 최적화합니다.

## 모범 사례

다음 모범 사례를 따라 사용량 제한 문제를 방지하세요:

| 이렇게 하세요 | 이렇게 하지 마세요 |
| --- | --- |
| 의미 있는 사용자 동작과 마일스톤을 추적하세요 | 모든 사소한 상호작용이나 UI 이벤트를 추적하지 마세요 |
| 필요한 경우에만 콘텐츠를 새로고침하세요 | 사용자 동작(스크롤 이벤트 등)마다 콘텐츠를 새로고침하지 마세요 |
| SDK가 자동으로 배치 처리를 수행하도록 하세요 | 절대적으로 필요한 경우가 아니면 즉시 데이터 전송을 강제하지 마세요 |
| 분석에 가치를 더하는 이벤트에 집중하세요 | 빈도를 고려하지 않고 SDK 메서드를 빠르게 연속 호출하지 마세요 |
{: .reset-td-br_1 .reset-td-br-2 role="presentation"}

## 도움 받기

SDK 사용량 제한 문제를 겪고 있다면 다음 네트워킹 메서드를 검토하세요:

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

[Braze 고객지원]({{site.baseurl}}/user_guide/administrative/access_braze/support)에 문의할 때는 사용 중인 각 네트워킹 SDK 메서드에 대해 다음 세부 정보를 포함해 주세요:

```plaintext
Method name:

Frequency:
[Describe how often this is called, e.g., at every app launch, once per session]

Trigger/context:
[Describe what causes it to be called, e.g., button click, scroll event]

Code snippet:  
[Paste the exact code where this method is called, one snippet for each time it is called]

Patterns in user flow that may cause bursts or excessive calls:
[Describe here]
```
