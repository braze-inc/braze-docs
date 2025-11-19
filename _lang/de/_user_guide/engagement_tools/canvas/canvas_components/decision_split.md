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

![Ein Decision-Split-Schritt mit dem Namen "Push enabled?" für Nutzer:innen, die nicht über Push Enablement verfügen, und Nutzer:innen, die über Push Enablement verfügen.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Mit dieser Komponente können Sie Canvas-Verzweigungen erstellen, je nachdem, ob ein:e Nutzer:in einer Abfrage entspricht.

## Decision-Split erstellen 

Um einen Decision-Split in Ihrem Arbeitsablauf zu erstellen, fügen Sie einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie dann die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> plus Button am unteren Ende eines Schritts und wählen Sie **Decision-Split**.

### Split definieren

Wie wollen Sie Ihre Benutzer aufteilen? Sie können [Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments/) und Filter verwenden, um die Linie zu zeichnen. Im Wesentlichen erstellen Sie eine `true` oder `false` Abfrage, die Ihre Nutzer:innen auswertet und sie dann zu einem oder mehreren Schritten weiterleitet. Sie müssen mindestens ein Segment oder einen Filter verwenden. Sie müssen nicht sowohl ein Segment als auch einen Filter verwenden.

![Ein Decision-Split-Schritt, bei dem der Filter "Foreground Push Enabled is true" ausgewählt ist.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
Standardmäßig werden Segmente und Filter für einen Decision-Split-Schritt direkt nach dem Empfang eines vorherigen Schritts überprüft, es sei denn, Sie fügen eine Verzögerung hinzu.
{% endalert %} 

## Split verwenden

Mit einem Decision-Split können Sie die Pfade Ihrer Nutzer:innen auf der Grundlage ihres Segments oder ihrer Attribute unterscheiden, sogar danach, ob sie bestimmte Messaging-Kanäle nutzen, um Ihre Nachrichten zu erhalten!

Nehmen wir an, Sie erstellen einen Onboarding-Ablauf. Sie könnten mit einer Willkommens-E-Mail bei der Anmeldung beginnen. Dann, zwei Tage später, möchten Sie eine Push Nachricht versenden, aber nur an Nutzer:innen, die Push Enablement haben. Danach erhalten alle Nutzer:innen drei Tage nach ihrer Registrierung eine weitere E-Mail. Sie könnten Ihren Decision-Split auch nutzen, um eine In-App-Nachricht an Nutzer:innen zu senden, die Push nicht aktiviert haben, um sie zu ermutigen, Push zu aktivieren.

Wenn es keinen Schritt gibt, der einem der Pfade folgt, verlassen Nutzer:innen, die diesen Pfad beschreiten, den Canvas. 

![Ein Decision-Split-Schritt mit dem Namen "Push enabled?" für Nutzer:innen, die kein Enablement haben, und solche, die es haben. Nutzer:innen, die kein Push Enablement haben, erhalten mit einer Verzögerung von 3 Tagen eine Nachricht per E-Mail. Nutzer:innen mit Push-Enablement erhalten mit 1-tägiger Verzögerung eine Push-Benachrichtigung, gefolgt von einer 2-tägigen Verzögerung. Danach erhalten sie die gleiche Nachricht per E-Mail wie Nutzer:innen ohne Push-Enablement.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Analytics

In der folgenden Tabelle finden Sie Beschreibungen der Analysefunktionen für diesen Schritt:

| Metrisch | Beschreibung |
|---|---|
| _Eingetreten_ | Die Gesamtzahl, wie oft der Schritt eingegeben wurde. Wenn Ihr Canvas eine Wiederholungsberechtigung hat und ein Nutzer:innen einen Decision-Split-Schritt zweimal eingibt, werden zwei Eingänge aufgezeichnet. |
| _Ja_ | Die Anzahl der Entrys, die die angegebenen Kriterien erfüllten und den „Ja“-Pfad durchliefen. |
| _Kein:e_ | Die Anzahl der Entrys, die die festgelegten Kriterien nicht erfüllten und den „Nein“-Pfad durchliefen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

