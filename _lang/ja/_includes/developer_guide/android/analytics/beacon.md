# ビーコンの統合

> この記事では、特定の種類のビーコンを Braze と統合して、セグメンテーションとメッセージングを可能にする方法について説明します。

## Infillion ビーコン

インフィリオン・ビーコンを設定し、アプリに統合すれば、訪問の設定や終了、ビーコンの目撃などのカスタムイベントを記録できる。これらのイベントのプロパティ (場所の名前、滞在時間など) をログに記録することもできます。

ユーザーが場所に入ったときにカスタムイベントをログに記録するには、次のコードを`onVisitStart`メソッドに含めます。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```

{% endtab %}
{% endtabs %}

`requestImmediateDataFlush`は、アプリがバックグラウンドで実行されている場合でもイベントが必ずログに記録されることを確認します。これと同じプロセスを、場所から離れる行動についても実装できます。作業中のアクティビティとコンテキストによって、`logCustomEvent`行と`requestImmediateDataFlush`行の連携方法が変更される可能性があることに注意してください。また、このコードについては、ユーザーが新しい場所を入力するたびに固有のカスタムイベントが作成され、増分されることに注意してください。そのため、50個を超える場所を作成する予定の場合は、一般的な「入力された場所」カスタムイベントを1つ作成し、イベントプロパティとして場所名を含めることをお勧めします。
