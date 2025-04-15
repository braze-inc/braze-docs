---
nav_title: FAQ
article_title: 지능 FAQ
page_order: 191
description: "이 문서에서는 인텔리전트 채널, 지능형 선택 및 Intelligent Timing에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
---

# 자주 묻는 질문

> 이 문서에서는 Intelligence Suite에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 지능형 선택

### 지능형 선택과 함께 사용할 때 24시간 이내에 재적격성을 부여할 수 없는 이유는 무엇인가요?

지능형 선택 캠페인이 너무 짧은 기간 내에 다시 자격을 부여하는 것은 제어 배리언트의 무결성에 영향을 미칠 수 있으므로 허용되지 않습니다. 24시간의 간격을 두어 알고리즘이 통계적으로 유효한 데이터 세트를 확보할 수 있도록 돕습니다.

일반적으로 재자격이 있는 캠페인은 사용자가 이전에 받은 것과 동일한 배리언트를 다시 입력하게 합니다. 지능형 선택을 사용하면 이 기능의 최적 할당 측면으로 인해 배리언트 배포가 변경될 수 있으므로 Braze는 사용자에게 동일한 캠페인 배리언트를 제공한다고 보장할 수 없습니다. 지능형 선택이 배리언트 성능을 재검토하기 전에 사용자가 다시 입력하도록 허용하면 재입력한 사용자로 인해 데이터가 왜곡될 수 있습니다.

예를 들어 캠페인에서 이러한 배리언트를 사용하는 경우입니다.

- 배리언트 A: 20%
- 배리언트 B: 20%
- 제어: 60%

그러면 두 번째 라운드의 배리언트 분포는 다음과 같을 수 있습니다.

- 배리언트 A: 15%
- 배리언트 B: 25%
- 제어: 60%

### 캠페인 초기 단계에서 내 지능형 선택 배리언트가 동일한 전송을 표시하는 이유는 무엇인가요?

지능형 선택은 캠페인 전환의 현재 상태에 따라 전송할 배리언트를 할당합니다. 전송이 여러 배리언트에 골고루 전송되는 훈련 기간이 지난 후에야 최종 배리언트 할당이 결정됩니다. 캠페인 초기 단계에서 지능형 선택이 균등하게 전송되지 않도록 하려면 기존 A/B 테스트에 고정 배리언트를 사용하세요.

### 지능형 선택은 명확한 승자를 선택하지 않고 최적화를 중단하나요?

지능형 선택은 실험을 계속해도 전환율이 현재 전환율의 1% 이상 개선되지 않는다는 확신이 95% 이상이면 최적화를 중단합니다.

### 내 캔버스 또는 캠페인에서 지능형 선택을 활성화할 수 없는 이유는 무엇인가요(회색으로 표시됨)?

다음과 같은 경우 지능형 선택을 사용할 수 없습니다.

- 캠페인 또는 캔버스에 전환 이벤트를 추가하지 않았습니다.
- 단일 전송 캠페인을 만들고 있습니다.
- 24시간 이내에 다시 자격을 부여할 수 있습니다.
- 캔버스는 추가 배리언트나 대조군이 추가되지 않은 단일 배리언트으로 구성됩니다.
- 캔버스는 배리언트가 추가되지 않은 단일 대조군으로 구성됩니다.

---

## Intelligent Timing

### General

#### What does Intelligent Timing predict?

Intelligent Timing focuses on predicting when a user is most likely to open or click your messages to ensure your messages reach users at optimal engagement times.

#### Is Intelligent Timing calculated separately for each day of the week?

No, Intelligent Timing isn’t tied to specific days. Instead, it personalizes send times based on each user’s unique engagement patterns and the channel you’re using, such as email or push notifications. This ensures your messages reach users when they’re most receptive.

### Calculations

#### What data is used to calculate the optimal time for each user?

To calculate the optimal time, Intelligent Timing:

1. Analyzes the interaction data for each user recorded by the Braze SDK. This includes:
  - Session times
  - Push direct opens
  - Push influenced opens
  - Email clicks
  - Email opens (excluding machine opens)
2. Groups these events by time, identifying the optimal send time for each user.

#### Are Machine Opens included when calculating optimal time?

No, [Machine Opens]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens) are excluded from calculations for optimal time. This means that send times are based solely on genuine user engagement, providing more accurate timing for your campaigns.

#### How precise is the optimal time?

Intelligent Timing schedules messages during each user’s “most engaged hour” based on their session starts and message open events. Within that hour, the message timing is rounded to the nearest five minutes. For example, if a user’s optimal time is calculated as 4:58 PM, the message will be scheduled for 5:00 PM. There may be slight delays in delivery due to system activity during busy periods.

#### What are the fallback calculations if there is not enough data?

If there are fewer than five relevant events for a user, Intelligent Timing uses the [fallback time][1] in your message settings. 

### Campaign management

#### 모든 시간대의 모든 사용자에게 성공적으로 전달하려면 Intelligent Timing 캠페인을 얼마나 미리 시작해야 하나요?

Braze는 세계에서 가장 이른 시간대 중 하나인 사모아 시간 자정을 기준으로 최적의 시간을 계산합니다. 하루 동안 약 48시간에 걸쳐 진행됩니다. 예를 들어, 최적의 시간이 오전 12시 1분이고 호주에 거주하는 사람은 이미 최적의 시간이 지났기 때문에 보내기에는 '너무 늦었습니다'. For these reasons, you need to schedule 48 hours in advance to successfully deliver to everyone in the world who uses your app.

#### Intelligent Timing 캠페인의 전송이 거의 또는 전혀 표시되지 않는 이유는 무엇인가요?

Braze는 정확한 예측을 위해 기준이 되는 데이터 포인트 수가 필요합니다. 세션 데이터가 충분하지 않거나 대상 사용자의 이메일 클릭 또는 열기 횟수가 거의 없거나 전혀 없는 경우(예: 신규 사용자), Intelligent Timing은 기본적으로 해당 요일에 워크스페이스에서 가장 인기 있는 시간으로 설정될 수 있습니다. 워크스페이스에 대한 정보가 충분하지 않으면 기본 시간인 오후 5시로 돌아갑니다. 특정 대체 [시간]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options)을 설정하도록 선택할 수도 있습니다.

#### Intelligent Timing 캠페인이 예정된 날짜보다 늦게 전송되는 이유는 무엇인가요?

A/B 테스트를 활용하고 있기 때문에 Intelligent Timing 캠페인이 예정된 날짜보다 늦게 전송될 수 있습니다. A/B 테스트를 사용하는 캠페인은 A/B 테스트가 종료된 후 자동으로 위닝 배리언트를 전송하여 캠페인 전송 기간을 늘릴 수 있습니다. 기본적으로 Intelligent Timing 캠페인은 다음 날 나머지 사용자에게 위닝 배리언트를 발송하도록 예약되어 있지만, 이 발송 날짜를 변경할 수 있습니다.

Intelligent Timing 캠페인이 있는 경우 A/B 테스트가 완료될 때까지 시간을 더 두고 위닝 배리언트를 하루가 아닌 이틀 동안 전송하도록 예약하는 것이 좋습니다. 

### Technical considerations

#### Braze는 세그먼트 및 오디언스 필터의 자격 기준을 언제 확인하나요?

Braze는 캠페인이 시작될 때 두 가지 검사를 수행합니다.

1. **Initial check:** At midnight in the first timezone on the day of send.
2. **Scheduled time check:** Just before sending at the time Intelligent Timing selected for the user.

Be careful when filtering based on other campaign sends to avoid targeting ineligible segments. For example, if you were to send out two campaigns on the same day for different times, and add a filter that only allows users to receive the second campaign if they’ve received the first, users won’t receive the second campaign. 이는 캠페인이 처음 만들어지고 세그먼트가 형성되었을 때 자격을 갖춘 사람이 없었기 때문입니다.

#### Intelligent Timing 캠페인에서 방해금지 시간을 사용할 수 있나요?

Quiet Hours can be used on a campaign that uses Intelligent Timing. The Intelligent Timing algorithm will avoid Quiet Hours so that it still sends the message to all eligible users. That said, we recommend turning Quiet Hours off unless there are policy, compliance, or other legal implications to when messages can and can't be sent.

#### What happens if the optimal time for a user is within the Quiet Hours? 

If the determined optimal time falls within Quiet Hours, Braze finds the nearest edge of the Quiet Hours and schedules the message for the next allowable hour before or after Quiet Hours. The message is enqueued to send at the closest boundary of Quiet Hours relative to the optimal time.

#### Intelligent Timing 및 사요양 제한조치를 사용할 수 있나요?

Rate limiting can be used on a campaign that uses Intelligent Timing. However, the nature of rate limiting means that some users may receive their message at a less-than-optimal time, particularly if a large number of users relative to the rate limit size are scheduled at the fallback time because of insufficient data. 

We recommend using rate limiting on an Intelligent Timing campaign only when there are technical requirements that must be met using rate limiting.

#### IP 워밍업 중에 Intelligent Timing을 사용할 수 있나요?

Braze doesn’t recommend using Intelligent Timing when users are first IP warming, as some of its behaviors can cause difficulties hitting daily volumes. 이는 Intelligent Timing이 캠페인 세그먼트를 두 번 평가하기 때문에 발생합니다. 캠페인을 처음 만들 때 한 번, 사용자에게 보내기 전에 두 번째로 사용자가 여전히 해당 세그먼트에 있어야 하는지 확인합니다.

이로 인해 세그먼트가 이동하고 변경되어 일부 사용자가 두 번째 평가에서 세그먼트에서 탈락하는 경우가 종종 있습니다. These users don’t get replaced, impacting how close to the maximum user cap you can achieve.

#### 가장 인기 있는 앱 시간은 어떻게 결정되나요?

가장 인기 있는 앱 시간은 워크스페이스의 평균 세션 시작 시간(현지 시간 기준)에 따라 결정됩니다. 이 측정지표는 캠페인의 시간을 미리 볼 때 대시보드에서 빨간색으로 표시되어 있습니다.

#### Intelligent Timing이 기계 열람 수를 설명하나요?

예, 기계 열람 수는 Intelligent Timing에 의해 필터링되므로 출력에 영향을 미치지 않습니다.

#### Intelligent Timing이 최대한 잘 작동하도록 하려면 어떻게 해야 하나요?

Intelligent Timing uses each user’s individual history of message engagement at whatever times they received messages. Intelligent Timing을 사용하기 전에 하루 중 다른 시간대에 사용자에게 메시지를 보냈는지 확인하세요. That way, you can “sample” when might be the best time for each user. 하루 중 다른 시간대를 부적절하게 샘플링하면 Intelligent Timing이 사용자에게 최적의 전송 시간을 선택하지 못할 수 있습니다.


[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing#fallback-time
