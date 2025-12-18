{% if include.section == "Variant distribution" %}

Die Verteilung zwischen den Varianten ist nicht immer gleichmäßig. So funktioniert die Verteilung von Varianten.

Jedes Mal, wenn eine Nachricht in einer multivariaten Kampagne versendet wird, wählt das System unabhängig eine zufällige Option gemäß den von Ihnen festgelegten Prozentsätzen aus und weist auf der Grundlage des Ergebnisses eine Variante zu. Es ist wie das Werfen einer Münze - Anomalien sind möglich. Wenn Sie schon einmal 100 Mal eine Münze geworfen haben, wissen Sie, dass Sie wahrscheinlich nicht jedes Mal eine exakte 50:50-Aufteilung zwischen Kopf und Zahl erhalten werden, auch wenn Sie nur zwei Möglichkeiten haben. Sie könnten 52 Kopf und 48 Zahl erhalten.

Wenn Sie mehrere Varianten haben, die Sie gleichmäßig aufteilen möchten, müssen Sie auch sicherstellen, dass die Anzahl der Varianten ein Vielfaches von 100 ist. Andernfalls wird bei einigen Varianten ein höherer Prozentsatz der Nutzer auf diese Variante verteilt sein als bei anderen. Wenn Ihre Kampagne zum Beispiel 7 Varianten hat, kann es keine gleichmäßige Verteilung der Varianten geben, da 7 als ganze Zahl nicht gleichmäßig durch 100 teilbar ist. In diesem Fall hätten Sie 2 Varianten von 15 % und 5 Varianten von 14 %.

#### Hinweis zu In-App-Nachrichten

Wenn Sie einen A/B-Test für In-App-Nachrichten durchführen, kann es sein, dass Ihre Analytics eine höhere Verteilung zwischen einer Variante und einer anderen anzeigen, auch wenn die prozentuale Aufteilung gleich ist. Betrachten Sie zum Beispiel das folgende Diagramm der *eindeutigen Empfänger* für Variante A und Variante C.

![Grafik der eindeutigen Empfänger:innen für zwei Varianten mit einer ähnlichen Form zwischen Variante A und Variante C, wobei Variante A eine höhere Anzahl von eindeutigen Empfänger:innen pro Tag aufweist]({% image_buster /assets/img/variant_distribution_iam.png %})

Variante A hat eine durchgängig höhere Anzahl von *Unique Recipients* als Variante C. Das liegt nicht an der Verteilung der Varianten, sondern daran, wie *Unique Recipients* für In-App-Nachrichten berechnet werden. Bei In-App-Nachrichten sind *Unique Recipients* eigentlich *Unique Impressions*, also die Gesamtzahl der Personen, die die In-App-Nachricht erhalten und angesehen haben. Das bedeutet, dass ein Benutzer, der die Nachricht aus irgendeinem Grund nicht erhält oder sich entscheidet, sie nicht anzusehen, nicht in die Zählung der *eindeutigen Empfänger* einbezogen wird und die Variantenverteilung verzerrt erscheinen kann.

{% endif %}