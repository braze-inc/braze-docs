---
nav_title: Konversions-Events
article_title: Konversions-Events
page_order: 5
page_type: tutorial
description: "In diesem Artikel erfahren Sie, was Conversion-Ereignisse sind, wie Sie sie nutzen und Ihre Erfolgsmetriken in Braze definieren können und wie Sie diese Tools nutzen können, um zu sehen, wie engagiert Ihre Benutzer sind."
tool: Campaigns

---
# Konversionsereignisse

> Mit Konversionsereignissen können Sie sicherstellen, dass Sie relevante, nützliche Daten sammeln, die Sie später nutzen können, um Insights für Ihre Kampagne zu gewinnen. 

Um Engagementzahlen und die notwendigen Daten zur Wirksamkeit Ihres Messaging für die KPIs zu erfassen, können Sie mit Braze Konversionsereignisse für Ihre Kampagnen und Canvases festlegen.

Ein Konversionsereignis ist eine Kennzahl, die zeigt, ob auf Ihre Nachricht innerhalb eines bestimmten Zeitraums nach dem Erhalt eine hochwertige Aktion folgt. Auf diese Weise können diese wertvollen Aktionen den verschiedenen Etappen der Interaktion zuordnen. 

Wenn Sie z.B. eine personalisierte Kampagne für aktive Benutzer erstellen, eignet sich das Konversionsereignis **Sitzung starten** innerhalb von zwei oder drei Tagen, da Sie so ein Gefühl für das Nutzerengagement nach dem Erhalt Ihrer Nachricht bekommen. Weitere Ereignisse wie **Kauf tätigen**, **App aktualisieren** oder benutzerdefinierte Ereignisse können ebenfalls als Konversionsereignisse ausgewählt werden.

Wenn Sie mehr über das Thema Konversion erfahren möchten, schauen Sie sich den [Braze-Onlinekurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Einrichtung von Kampagnen an.

## Primäres Konversionsereignis

Das primäre Konversionsereignis  ist das erste Ereignis, das bei der Erstellung einer Kampagne oder eines Canvas hinzugefügt wird. Es hat den größten Einfluss auf Engagement und Berichterstattung. Das können Sie mit primären Konversionsereignissen tun:

- Berechnen Sie die siegreiche Nachrichtenvariation in [multivariaten][4] Kampagnen oder Canvases.
- Legen Sie das Zeitfenster fest, in dem die Einnahmen für die Kampagne oder das Canvas berechnet werden.
- Passen Sie die Nachrichtenverteilung für Kampagnen und Canvases per [Intelligenter Auswahl][5] an.

{% alert note %}
Wenn Nachrichten mit dem Liquid-Tag `abort` abgebrochen werden, werden nur die Benutzer, die die Varianten durchgehen, potenziell abgebrochen. Das bedeutet, dass die Nachrichten an Benutzer, die die Kontrollgruppe durchlaufen, nicht abgebrochen werden, was zu verzerrten Konvertierungsprozentsätzen zwischen Varianten und Kontrollgruppen führen kann. Als Abhilfe verwenden Sie die [Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment), um Ihre Benutzer bei der Eingabe von Kampagnen und Canvas anzusprechen.
{% endalert %}

## Schritt 1: Kampagne mit Conversion-Tracking erstellen

[Erstellen Sie eine Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) für Ihren gewünschten Nachrichtenkanal. Wenn Sie die Nachrichten und den Zeitplan für Ihre Kampagne festgelegt haben, können Sie bis zu vier Konvertierungsereignisse verfolgen.

Wir empfehlen Ihnen, so viele Konversionsereignisse zu verwenden, wie Sie für notwendig halten, denn die Ergänzung eines zweiten (oder dritten) Konversionsereignisses kann die Berichterstattung erheblich bereichern. Angenommen, Sie haben eine Kampagne, die auf passive Nutzer abzielt. In diesem Fall können Sie durch Hinzufügen eines sekundären Conversion-Ereignisses und des primären Conversion-Ereignisses **"Starts Session"** besser verstehen, wie effektiv Ihre Kampagne Ihre Benutzer zurück in Ihre Anwendung bringt. 

## Schritt 2: Konvertierungsereignisse hinzufügen

Wählen Sie für jedes Konversionsereignis, das Sie verfolgen möchten, das Ereignis und die Konversionsfrist aus.

1. Wählen Sie den allgemeinen Ereignistyp, den Sie verwenden möchten:
  - **Sitzung starten** Ein Benutzer zählt als Konversion, wenn er eine der von Ihnen angegebenen Apps öffnet (standardmäßig sind das alle Apps im Workspace).
  - **Kauf tätigen**: Ein Benutzer zählt als Konversion, wenn er das von Ihnen angegebene Produkt kauft (standardmäßig sind das alle Produkte).
  - **Benutzerdefiniertes Ereignis ausführen**: Ein Benutzer zählt als Konversion, wenn er eines Ihrer benutzerdefinierten Ereignisse ausführt (keine Standardeinstellung, Sie müssen das Ereignis angeben).
  - **App upgraden**: Ein Benutzer zählt als Konversion, wenn er die eine der von Ihnen angegebenen Apps aktualisiert (standardmäßig sind das alle Apps im Workspace). Braze führt nach bestem Wissen und Gewissen einen numerischen Vergleich durch, um festzustellen, ob es sich bei der Versionsänderung um ein Upgrade handelt. Das ist z. B. der Fall, wenn er ein Upgrade von Version 1.2.3 auf 1.3.0 vornimmt. Braze erkennt aber keine Konversion, wenn jemand ein Downgrade von 1.2.3 auf 1.2.2 vornimmt. Wenn der Versionsname der App jedoch Zeichenfolgen wie z.B. "1.2.3-beta2" enthält, kann Braze nicht feststellen, ob es sich bei einer Versionsänderung um ein Upgrade handelt. In diesem Fall zählt Braze es als Umwandlung, wenn sich die letzte App-Version des Benutzers ändert.
  - **E-Mail öffnen**: Ein Benutzer zählt als Konversion, wenn er die E-Mail öffnet (nur bei E-Mail-Kampagnen).
  - **E-Mail anklicken**: Ein Benutzer zählt als Konversion, wenn er auf einen Link in der E-Mail klickt (nur bei E-Mail-Kampagnen).<br><br>
2. Setzen Sie sich eine Konversionsfrist. Das ist die maximale Zeitspanne, die bis zur Konversion vergehen darf. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen einzuräumen, in dem es als Konversion zählt, wenn der Benutzer die angegebene Aktion durchführt.  

![Der Ereignistyp "Kauf tätigen" erfasst z. B. Benutzer als Konversion, die einen Kauf tätigen. Die Frist beträgt 12 Stunden.][2]

Sobald Sie Ihre Konversionsereignisse ausgewählt haben, fahren Sie mit der Kampagnenerstellung und dem Versand fort.

## Schritt 3: Ergebnisse anzeigen

Gehen Sie auf die Seite **Details**, um die Details für jedes Conversion-Ereignis anzuzeigen, das mit der soeben erstellten Kampagne verbunden ist. Unabhängig von den von Ihnen ausgewählten Konversionsereignissen können Sie auch die Gesamteinnahmen sehen, die dieser spezifischen Kampagne sowie bestimmten Varianten während des Zeitfensters des primären Konversionsereignisses zugeschrieben werden können.

{% alert note %}
Wenn bei der Erstellung der Kampagne keine Konversionsereignisse ausgewählt werden, wird die Zeit auf drei Tage voreingestellt.
{% endalert %}

Bei Nachrichten mit mehreren Varianten können Sie außerdem die Anzahl und relative Häufigkeit der Konversionsereignisse für Ihre Kontrollgruppe und die einzelnen Varianten einsehen.

![][3]

## Regeln zum Konversionstracking

Konversionsereignisse ermöglichen es, Nutzeraktionen auf einen bestimmten Punkt der Interaktion zurückzuführen. Allerdings gibt es ein paar Dinge zu beachten, wenn es darum geht, wie Braze mit Mehrfachkonvertierungen umgeht. In den folgenden Beispielen wird gezeigt, wie Braze diese Konversionen verfolgt:

- Die Konversion erfolgt pro Benutzer, nicht pro Gerät. Das bedeutet, dass ein Benutzer nur einmal als Konversionsereignis gezählt wird, auch wenn eine Nachricht an mehrere Geräte gesendet wird. Ein weiteres Beispiel: Nehmen wir an, eine Kampagne hat nur ein Conversion-Ereignis, nämlich "Tätigt einen Kauf". Wenn ein Nutzer, der diese Kampagne erhält, innerhalb der Umwandlungsfrist zwei separate Käufe tätigt, wird nur eine Umwandlung gezählt.
- Wenn ein Benutzer ein Konversionsereignis innerhalb der Frist für zwei separate Kampagnen oder Canvases durchführt, wird diese Konversion bei beiden registriert.
- Eine Konversion wird auch dann festgestellt, wenn ein Benutzer das jeweilige Konversionsereignis im Fenster durchführt, auch wenn er die Nachricht nicht geöffnet oder angeklickt hat.

[2]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[3]: {% image_buster /assets/img_archive/conversion_event_details.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing
[5]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
