---
nav_title: Kopieren zwischen Arbeitsbereichen
article_title: Kopieren über Arbeitsbereiche hinweg
page_order: 4.5
alias: "/copying_to_workspaces/"
page_type: reference
description: "Dieser referenzierte Artikel bietet eine Übersicht darüber, wie Sie Kampagnen und Canvase in verschiedene Workspaces kopieren können."
tool:
    - Campaigns
    - Canvas
---

# Kopieren von Kampagnen und Canvase zwischen Workspaces

> Durch das Kopieren von Kampagnen über verschiedene Arbeitsbereiche hinweg können Sie mit einer Kopie einer Kampagne in einem anderen Arbeitsbereich beginnen und so die Erstellung Ihrer Nachrichten beschleunigen. Auf dieser Seite erfahren Sie, wie Sie Kampagnen in verschiedene Arbeitsbereiche kopieren können und was kopiert wird und was nicht.

Wenn Sie eine Kampagne oder ein Canvas in einen anderen Workspace kopieren, bleibt die Kopie als Entwurf erhalten, bis Sie sie bearbeiten und einführen. So können Sie Ihre erfolgreichen Messaging-Strategien beibehalten und weiter ausbauen.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
Das Kopieren von Kampagnen über Workspaces hinweg ist allgemein verfügbar. Kanal-Unterstützung für Content-Cards ist derzeit nicht verfügbar.
{% endalert %}

Sie können Kampagnen für diese unterstützten Kanäle in verschiedene Workspaces kopieren: SMS, In-App-Nachrichten, Push-Benachrichtigungen, E-Mail und Webhooks. Sie können auch über E-Mail Templates, Feature-Flags und Content-Blöcke hinweg kopieren. Beachten Sie, dass Multichannel-Kampagnen mit nicht unterstützten Kanälen nicht in andere Arbeitsbereiche kopiert werden können.

So kopieren Sie eine Kampagne in einen anderen Workspace:

1. Wählen Sie das Zahnradsymbol <i class="fas fa-cog"></i> neben der ausgewählten Kampagne aus.
2. Wählen Sie **In Workspace kopieren**. 
3. Prüfen und testen Sie Ihre Kampagne nach dem Kopieren, um sicherzustellen, dass alle Felder korrekt funktionieren.

{% endtab %}
{% tab canvas %}

{% alert important %}
Das Kopieren von Canvase über mehrere Workspaces hinweg ist allgemein verfügbar. Die folgenden Kanäle werden derzeit nicht unterstützt: LINE, Content-Cards, und WhatsApp.
{% endalert %}

Sie können Canvase für diese unterstützten Kanäle in verschiedene Workspaces kopieren: E-Mail, In-App-Nachrichten, Push, Webhooks und SMS.

So kopieren Sie ein Canvas in einen anderen Workspace:

1. Wählen Sie das Menü <i class="fa-solid fa-ellipsis-vertical"></i> neben dem ausgewählten Canvas aus.
2. Wählen Sie **In Workspace kopieren**. 
3. Prüfen und testen Sie nach dem Kopieren Ihr Canvas, um sicherzustellen, dass alle Felder korrekt funktionieren.

Beim Kopieren eines Canvas mit Audience Sync-Schritten werden die Einstellungen nicht in den Workspace des Ziels kopiert, wohl aber die Schritte auf dem Weg dorthin.

{% endtab %}
{% endtabs %}

## Was über Arbeitsbereiche hinweg kopiert wird

Beachten Sie, dass die folgende Liste nicht vollständig ist, was in die Workspaces kopiert wird und was nicht. Überprüfen Sie am besten die Details der Kampagne und des Canvas und testen Sie, ob Ihre Nachricht wie erwartet funktioniert.

### Details

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Beschreibung | Territorien | 
| Typ | Tags | 
| Aktionen (verschachtelt) | Segmente | 
| Konvertierungsverhalten (verschachtelt) | Genehmigungen | 
| Konfigurationen für die stille Zeit | Auslösezeitplan | 
| Frequency-Capping | Kampagnen-Zusammenfassungen | 
| Abonnementstatus |  | 
| Wiederholungen |  | 
| Ist transaktional |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Beschreibung | Territorien | 
| Typ | Tags | 
| Aktionen (verschachtelt) | Segmente | 
| Konvertierungsverhalten (verschachtelt) | Genehmigungen | 
| Konfigurationen für die stille Zeit | Auslösezeitplan | 
| Frequency-Capping | Canvas-Zusammenfassungen | 
| Abonnementstatus |  | 
| Wiederholungen |  | 
| Ist transaktional |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Verhalten bei Konversion

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Verhalten | Arbeitsbereich-IDs |
| Interaktion im Rahmen der Kampagne |  Kampagnen-ID | 
| Name des angepassten Events |  | 
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Verhalten | Arbeitsbereich-IDs |
| Canvas-Interaktion |  Canvas-ID | 
| Name des angepassten Events |  | 
| Produktname |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Aktionen

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Verhalten | Arbeitsbereich-IDs |
| Interaktion im Rahmen der Kampagne |  Kampagnen-ID | 
| Name des angepassten Events |  | 
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Verhalten | Arbeitsbereich-IDs |
| Canvas-Interaktion |  Canvas-ID | 
| Name des angepassten Events |  | 
| Produktname |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Nachrichtenvarianten

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Prozentsatz senden | API-ID |
| Typ |  Seedgruppen-IDs | 
|  |  Linkvorlagen-IDs | 
|  |  Interne Benutzergruppen-IDs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Prozentsatz senden | API-ID |
| Typ |  Seedgruppen-IDs | 
|  |  Linkvorlagen-IDs | 
|  |  Interne Benutzergruppen-IDs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}


### E-Mail Nachricht Variation

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Textkörper | Absender |
| Nachrichtenzusätze |  Antwort an | 
| Titel |  BCC | 
| Betreff |  Link-Template | 
|  |  Link-Aliasing |
|  | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Textkörper | Absender |
| Nachrichtenzusätze |  Antwort an | 
| Titel |  BCC | 
| Betreff |  Link-Template | 
|  |  Link-Aliasing |
|  | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### E-Mail-Textkörper

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Klartext | Link-Aliasing |
| HTML und Drag-and-Drop-Inhalte | Übersetzungen | 
| Preheader |  | 
| Inline-CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Klartext | Link-Aliasing |
| HTML und Drag-and-Drop-Inhalte | Übersetzungen | 
| Preheader |  | 
| Inline-CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### E-Mail-Templates

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Textkörper | API-IDs |
| Beschreibung | Bild-IDs | 
| Betreff | Territorien | 
| Kopfzeilen | Tags | 
| | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Textkörper | API-IDs |
| Beschreibung | Bild-IDs | 
| Betreff | Territorien | 
| Kopfzeilen | Tags | 
| | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Content-Blöcke

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Name | Link-Aliasing |
| Beschreibung | API-Schlüssel | 
| Content | Territorien | 
| HTML und Drag-and-Drop-Inhalte | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Name | Link-Aliasing |
| Beschreibung | API-Schlüssel | 
| Content | Territorien | 
| HTML und Drag-and-Drop-Inhalte | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### SMS Nachrichten Variation

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Textkörper | Messenger |
| Link-Verkürzung | VCF-Medienobjekte | 
| Klick-Tracking |  | 
| Medien |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Textkörper | Messenger |
| Link-Verkürzung | VCF-Medienobjekte | 
| Klick-Tracking |  | 
| Medien |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Kopieren von Nachrichten, die Liquid enthalten

Liquid-Referenzen in Nachrichten werden in den Workspace des Ziels kopiert, aber die Referenzen funktionieren möglicherweise nicht wie erwartet. Das bedeutet, wenn ein Canvas aus Workspace A in Workspace B kopiert wird, kann Workspace B nicht auf die Details von Workspace A referenzieren, auch nicht auf Liquid-Referenzen. So werden u. a. keine Felder wie Auslöseaktionen und Zielgruppenfilter übernommen.

Behalten Sie beim Kopieren von Kampagnen und Canvase über Workspaces hinweg die folgenden Liquid-Referenzen mit Abhängigkeiten im Auge:

- Katalogartikel-Tags
- Connected-Content-Tags
- Content-Blöcke
- Angepasste Attribute
- Einstellungszentren
- Produkt-Empfehlungen
- Abonnementstatus-Tags
- Gutschein- und Aktionstags

## Kopieren von Nachrichten mit Feature-Flags

Um eine Feature-Flag-Kampagne und ein Canvas mit einem Feature-Flag-Schritt zwischen Workspaces zu kopieren, vergewissern Sie sich, dass im Ziel-Workspace ein [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments) mit einer ID konfiguriert ist, die entweder mit dem Feature-Flag übereinstimmt, das in der ursprünglichen Kampagne referenziert wurde, oder mit dem Feature-Flag-Schritt, der im ursprünglichen Canvas referenziert wurde.

Wenn Sie eine Kampagne oder ein Canvas kopieren, das einen Feature-Flag-Schritt mit einer Feature-Flag ID enthält, die im Ziel-Workspace nicht vorhanden ist, wird der Feature-Flag-Schritt kopiert, nicht aber sein Inhalt.

## Kopieren von Nachrichten mit Content-Blöcken

Wenn Sie eine Kampagne in andere Arbeitsbereiche kopieren, werden die Content-Blöcke nicht mitkopiert. Sie können jedoch im Zielarbeitsbereich referenziert werden, wenn ein Block mit demselben Namen existiert. Alternativ können Sie ihn (oder entsprechende Liquid-Verweise) auch im Zielarbeitsbereich erstellen und so Fehler beim Kampagnenstart vermeiden.

Bei Canvase, die auf einen Content-Block referenzieren, muss der Content-Block zunächst in den Ziel-Workspace kopiert werden.
