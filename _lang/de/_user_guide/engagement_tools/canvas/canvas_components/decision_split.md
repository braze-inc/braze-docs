---
nav_title: Decision-Split 
article_title: Decision-Split 
alias: /decision_split/
page_order: 2
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Decision-Splits in Ihrem Canvas erstellen und verwenden."
tool: Canvas

---

# Decision-Split 

> Die Komponente Decision-Split in Canvas erlaubt es Ihnen, Ihren Nutzer:innen personalisierte Erlebnisse in Echtzeit zuzustellen. 

Mit dieser Komponente können Sie Canvas-Verzweigungen erstellen, je nachdem, ob ein:e Nutzer:in einer Abfrage entspricht.

![][1]{: style="float:right;max-width:20%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

## Decision-Split erstellen 

Um einen Decision-Split in Ihrem Workflow zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente aus der Seitenleiste oder klicken Sie auf die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> am unteren Rand eines Schritts und wählen Sie **Entscheidung teilen**.

### Split definieren

Wie wollen Sie Ihre Benutzer aufteilen? Sie können [Segmente][5] und Filter verwenden, um die Linie zu zeichnen. Im Wesentlichen erstellen Sie eine `true` oder `false` Abfrage, die Ihre Nutzer:innen auswertet und sie dann zu einem oder mehreren Schritten weiterleitet. Sie müssen mindestens ein Segment oder einen Filter verwenden. Sie müssen nicht sowohl ein Segment als auch einen Filter verwenden.

![][2]{: style="max-width:90%;"}

{% alert note %}
Standardmäßig werden Segmente und Filter für eine Decision-Split-Komponente direkt nach dem Empfang eines vorherigen Schritts geprüft, es sei denn, Sie fügen einen Delay hinzu.
{% endalert %} 

## Split verwenden

Mit einem Decision-Split können Sie die Pfade Ihrer Nutzer:innen auf der Grundlage ihres Segments oder ihrer Attribute unterscheiden, sogar danach, ob sie bestimmte Messaging-Kanäle nutzen, um Ihre Nachrichten zu erhalten!

Nehmen wir an, Sie erstellen einen Onboarding-Ablauf. Sie könnten mit einer Willkommens-E-Mail bei der Anmeldung beginnen. Dann, zwei Tage später, möchten Sie eine Push Nachricht versenden, aber nur an Nutzer:innen, die Push Enablement haben. Danach erhalten alle Nutzer:innen drei Tage nach ihrer Registrierung eine weitere E-Mail. Sie könnten Ihren Decision-Split auch nutzen, um eine In-App-Nachricht an Nutzer:innen zu senden, die Push nicht aktiviert haben, um sie zu ermutigen, Push zu aktivieren.

![][3]{: style="max-width:60%;"}

Wenn es keinen Schritt gibt, der einem der Pfade folgt, verlassen Nutzer:innen, die diesen Pfad beschreiten, den Canvas. 

{% alert important %}
Ein Decision-Split kann keine kann keine vollständigen Stufenschritte enthalten. Mit anderen Worten: Sie können keinen vollständigen Schritt erstellen, der in einen Filterschritt und einen vollständigen Schritt verzweigt. Diese Einschränkung besteht, denn wenn es einen Branch mit einem Filterschritt und einem Vollschritt gäbe, wäre nicht klar, welchen Branch die Nutzer:innen nehmen würden.
<br>
Ein Filterschritt kann nur mit einem nächsten Schritt verbunden werden.
{% endalert %}

## Analytics

In der folgenden Tabelle finden Sie Beschreibungen der Analysefunktionen für diesen Schritt:

| Metrisch | Beschreibung |
|---|---|
| Eingetreten | Die Gesamtzahl, wie oft der Schritt eingegeben wurde. Wenn Ihr Canvas eine Wiederholungsberechtigung hat und ein Nutzer:innen einen Decision-Split-Schritt zweimal eingibt, werden zwei Eingänge aufgezeichnet. |
| Ja | Die Anzahl der Entrys, die die angegebenen Kriterien erfüllten und den „Ja“-Pfad durchliefen. |
| Kein:e | Die Anzahl der Entrys, die die festgelegten Kriterien nicht erfüllten und den „Nein“-Pfad durchliefen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[1]: {% image_buster /assets/img/decision-split-1.png %}
[2]: {% image_buster /assets/img/define-split-2.png %}
[3]: {% image_buster /assets/img/use-split-onboarding-3.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/
