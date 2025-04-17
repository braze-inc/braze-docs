# Dashboard zur Nachrichtenverwendung

> Das Message Usage Dashboard bietet Ihnen einen Self-Service-Einblick in die Nutzung Ihres SMS- und WhatsApp-Guthabens und gibt Ihnen einen umfassenden Überblick über die historische und aktuelle Nutzung im Vergleich zu den vertraglich festgelegten Kontingenten. Diese Insights können Unklarheiten ausräumen und Ihnen helfen, Anpassungen vorzunehmen, um Überschussrisiken zu vermeiden.

Das Dashboard **Nachrichtenverwendung** ist in drei Bereiche unterteilt:
- [Übersicht über die Credit-Nutzung](#credit-usage-overview)
- [SMS/MMS](#smsmms) 
- [WhatsApp](#whatsapp)

Rufen Sie das Dashboard auf, indem Sie zu **Einstellungen** > **Abrechnung** > **Nachrichtennutzung** gehen.

## Übersicht über die Verwendung von Nachrichtenguthaben

**Die Übersicht über die Nutzung von Nachrichten-Credits** bietet einen Überblick über die Nutzung aller Kanäle, die Credits verwenden. Sie können sehen, wie es um Ihre Credit-Gesamtmenge bestellt ist, und finden Details zu Ihrem aktiven Vertrag und Ihrer Vertragslaufzeit.

Auf dieser Seite wird angezeigt, ob Sie einen Vertrag über Nachrichtenguthaben haben oder ob Sie WhatsApp gekauft haben. Die Kanäle, die Nachrichtenguthaben verwenden, werden in der **Übersicht über die Credit-Vereinbarung** angezeigt.

{% alert note %}
Wenn Sie WhatsApp gekauft haben, aber keinen Vertrag über Nachrichtenguthaben abgeschlossen haben, sehen Sie trotzdem den Guthabenverbrauch für WhatsApp, da dies die Art und Weise ist, wie ältere WhatsApp-Verträge abgerechnet werden. Dies unterscheidet sich von herkömmlichen SMS, die nur dann Guthaben verbrauchen, wenn Sie einen Vertrag über Nachrichtenguthaben abgeschlossen haben.
{% endalert %}

Die Daten der **Übersicht über die Nutzung von Nachrichtenguthaben** beschränken sich auf die Vertragslaufzeit, die in der **Übersicht über den Credits-Vertrag** angezeigt wird. Sie können nicht nach einem Datumsbereich außerhalb des **Kreditzeitraums** filtern.

### Nutzung von Nachrichten-Credits über Vertrag

Das Diagramm **Nutzung des Nachrichtenguthabens über den Vertrag** zeigt Ihre Nutzung über den ausgewählten Zeitraum an. Die Granularität dieses Charts hängt von dem von Ihnen gewählten Zeitrahmen ab. Exportieren Sie die Exportoptionen, indem Sie das Menü in der oberen rechten Ecke des Charts auswählen.

![Dashboard „Übersicht über die Credits-Nutzung für Nachrichten“ mit Abschnitten für die Nutzung von Credits, die Übersicht über den Credit-Vertrag und den Credit-Verbrauch über den Vertrag.][1]{: style="max-width:80%;"}

## SMS und MMS

**SMS/MMS-Credit-Verbrauch** zeigt die Aufschlüsselung der Nutzung für den SMS/MMS-Kanal. Die Spalten in der Datentabelle variieren je nachdem, ob es sich bei SMS/MMS um einen Kreditkanal handelt. Wenn es sich bei SMS/MMS um einen Guthaben-Kanal handelt, werden zusätzliche Spalten **Guthabenquote** und **Guthaben** angezeigt, die den jeweiligen Ländersatz und das verbrauchte Guthaben angeben. Zusätzlich zeigen Kacheln auf hoher Ebene den gesamten SMS- und ggf. MMS-Verbrauch im ausgewählten Datumsbereich an.

Es sind Filter verfügbar, mit denen Sie nach **Land** oder **SMS-Typ** filtern können.

![SMS-/MSS-Credit-Verbrauch mit Kacheln für übergeordnete Daten und einem Abschnitt für den Verbrauch nach Konto.][2]{: style="max-width:80%;"}

Anders als die **Übersicht über die Nutzung von Nachrichtenguthaben** enthält dieser Abschnitt historische Daten aus früheren Vertragszeiträumen. 

{% alert note %}
Es ist möglich, einen Datumsbereich auszuwählen, der sowohl die Verwendung von Nicht-Credits als auch von Nachrichten-Credits enthält. In diesem Fall wird der Verbrauch, der außerhalb des Nachrichtenguthabens stattgefunden hat, in den Spalten **Guthabenquote** und **Guthaben** mit `—` (Null) angezeigt.
{% endalert %}

![SMS/MMS-Guthaben-Nutzungstabelle mit Nullwerten.][3]{: style="max-width:80%;"}

## WhatsApp

**WhatsApp-Credits-Verbrauch** zeigt die Aufschlüsselung der Nutzung für den WhatsApp-Kanal. Die Kacheln zeigen die Gesamtnutzung des WhatsApp-Guthabens an, die im Abschnitt **Nutzung nach Konto** aufgeschlüsselt werden kann, indem Sie Filter anwenden, um die Ergebnisse der Datentabelle auf einen bestimmten Arbeitsbereich zu beschränken.

### Filter

Sie können Ihre Daten filtern nach:
- Land
- WhatsApp-Business-Konto
- Braze-Workspace
- Gesprächskategorie-Typ
- Region

![WhatsApp-Credits-Verbrauch mit einer Kachel für insgesamt verbrauchte Credits und einer Verbrauchstabelle nach Konto.][4]{: style="max-width:80%;"}

## Was Sie wissen sollten

{% alert important %}
Die im Dashboard **Nachrichtenverwendung** angezeigten Daten beziehen sich auf die Vertragsebene und sind nicht auf ein einzelnes Dashboard-Unternehmen oder einen Arbeitsbereich beschränkt. Diese Daten spiegeln die Nutzung aller Arbeitsbereiche innerhalb Ihres Dashboards wider und möglicherweise auch aller Dashboards (wenn Sie mehrere haben).
{% endalert %}

- Die zugrundeliegenden Daten werden täglich zur Verfügung gestellt, wobei die Datentabellen um 3 Uhr, 9 Uhr, 12 Uhr und 18 Uhr EST aktualisiert werden. 
- Braze folgt der üblichen Rundungsmethodik: Zahlen werden auf das nächste Zehntel aufgerundet.

[1]: {% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}
[2]: {% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}
[3]: {% image_buster /assets/img/app_settings/sms_table_null3.png %}
[4]: {% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}