---
nav_title: Zwischen Workspaces kopieren
article_title: Zwischen Workspaces kopieren
page_order: 4
alias: "/copying_to_workspaces/"
page_type: reference
description: "Dieser Referenzartikel bietet eine Übersicht darüber, wie Sie Kampagnen und Canvase in verschiedene Workspaces kopieren können."
tool:
    - Campaigns
    - Canvas
---

# Kampagnen und Canvase über Workspaces hinweg kopieren

> Durch das Kopieren von Kampagnen über verschiedene Workspaces hinweg können Sie mit einer Kopie einer Kampagne in einem anderen Workspace beginnen und so die Erstellung Ihrer Nachrichten beschleunigen. Auf dieser Seite erfahren Sie, wie Sie Kampagnen in verschiedene Workspaces kopieren können und was dabei kopiert wird und was nicht.

Wenn Sie eine Kampagne oder ein Canvas in einen anderen Workspace kopieren, bleibt die Kopie als Entwurf erhalten, bis Sie sie bearbeiten und starten. So können Sie Ihre erfolgreichen Messaging-Strategien beibehalten und weiter ausbauen.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
Das Kopieren von Kampagnen über Workspaces hinweg ist allgemein verfügbar. Kanal-Unterstützung für Content-Cards ist derzeit nicht verfügbar.
{% endalert %}

Sie können Kampagnen für die folgenden unterstützten Kanäle in verschiedene Workspaces kopieren: SMS, In-App-Nachrichten, Push-Benachrichtigungen, E-Mail und Webhooks. Sie können auch E-Mail-Templates, Feature-Flags und Content-Blöcke kopieren. Beachten Sie, dass Multichannel-Kampagnen mit nicht unterstützten Kanälen nicht in andere Workspaces kopiert werden können.

So kopieren Sie eine Kampagne in einen anderen Workspace:

1. Wählen Sie das <i class="fas fa-cog"></i> Zahnradsymbol neben der ausgewählten Kampagne aus.
2. Wählen Sie **In Workspace kopieren**. 
3. Prüfen und testen Sie Ihre Kampagne nach dem Kopieren, um sicherzustellen, dass alle Felder korrekt funktionieren.

{% endtab %}
{% tab canvas %}

{% alert important %}
Das Kopieren von Canvases über Workspaces hinweg ist allgemein verfügbar. Die folgenden Kanäle werden derzeit nicht unterstützt: LINE, Content-Cards und WhatsApp.
{% endalert %}

Sie können Canvase für die folgenden unterstützten Kanäle in verschiedene Workspaces kopieren: E-Mail, In-App-Nachrichten, Push, Webhooks und SMS.

So kopieren Sie ein Canvas in einen anderen Workspace:

1. Wählen Sie das Menü <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;neben dem ausgewählten Canvas aus.
2. Wählen Sie **In Workspace kopieren**. 
3. Prüfen und testen Sie nach dem Kopieren Ihr Canvas, um sicherzustellen, dass alle Felder korrekt funktionieren.

Beim Kopieren eines Canvas mit Audience-Sync-Schritten werden die Einstellungen nicht in den Ziel-Workspace kopiert, wohl aber die Schritte im Verlauf.

{% endtab %}
{% endtabs %}

## Was über Workspaces hinweg kopiert wird

Beachten Sie, dass die folgende Liste nicht vollständig ist, was über Workspaces hinweg kopiert wird und was nicht. Überprüfen Sie am besten die Details der Kampagne und des Canvas und testen Sie, ob Ihre Nachricht wie erwartet funktioniert.

### Details

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Beschreibung | Territorien | 
| Typ | Tags | 
| Aktionen (verschachtelt) | Segmente | 
| Konversionsverhalten (verschachtelt) | Genehmigungen | 
| Konfigurationen für die stille Zeit | Auslösezeitplan | 
| Frequency-Capping-Konfigurationen | Kampagnen-Zusammenfassungen | 
| Abo-Status der Empfänger:innen | Filter | 
| Wiederkehrender Zeitplan |  | 
| Ist transaktional |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Beschreibung | Territorien | 
| Typ | Tags | 
| Aktionen (verschachtelt) | Segmente | 
| Konversionsverhalten (verschachtelt) | Genehmigungen | 
| Konfigurationen für die stille Zeit | Auslösezeitplan | 
| Frequency-Capping-Konfigurationen | Canvas-Zusammenfassungen | 
| Abo-Status der Empfänger:innen | Filter | 
| Wiederkehrender Zeitplan | Ausstiegskriterien | 
| Ist transaktional |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Konversionsverhalten

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
| Kampagnen-Interaktion |  Kampagnen-ID | 
| Name des angepassten Events |  | 
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
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
| Verhaltenstyp | Workspace-IDs |
| Kampagnen-Interaktion |  Kampagnen-ID | 
| Name des angepassten Events |  | 
| Produktname |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Verhaltenstyp | Workspace-IDs |
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
| Sendeprozentsatz | API-ID |
| Typ |  Seed-Gruppen-IDs | 
|  |  Link-Template-IDs | 
|  |  Interne Nutzergruppen-IDs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Sendeprozentsatz | API-ID |
| Typ |  Seed-Gruppen-IDs | 
|  |  Link-Template-IDs | 
|  |  Interne Nutzergruppen-IDs | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}


### E-Mail-Nachrichtenvariante

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Textkörper | Absenderadresse |
| Nachrichtenzusätze |  Antwort an | 
| Titel |  BCC | 
| Betreff |  Link-Template | 
|  |  Link Aliasing |
|  | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| E-Mail-Textkörper | Absenderadresse |
| Nachrichtenzusätze |  Antwort an | 
| Titel |  BCC | 
| Betreff |  Link-Template | 
|  |  Link Aliasing |
|  | Übersetzungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### E-Mail-Textkörper

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Klartext | Link Aliasing |
| HTML und Drag-and-Drop-Inhalte | Übersetzungen | 
| Preheader |  | 
| Inline-CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Klartext | Link Aliasing |
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
| Name | Link Aliasing |
| Beschreibung | API-Schlüssel | 
| Inhalt | Territorien | 
| HTML und Drag-and-Drop-Inhalte | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Name | Link Aliasing |
| Beschreibung | API-Schlüssel | 
| Inhalt | Territorien | 
| HTML und Drag-and-Drop-Inhalte | Tags | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### SMS-Nachrichtenvariante

{% tabs local %}
{% tab campaigns %}

| Kopiert | Ausgelassen |
|---|---|
| Textkörper | Messaging-Dienst |
| Link-Verkürzung | VCF-Medienobjekte | 
| Klick-Tracking |  | 
| Medienobjekte |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Kopiert | Ausgelassen |
|---|---|
| Textkörper | Messaging-Dienst |
| Link-Verkürzung | VCF-Medienobjekte | 
| Klick-Tracking |  | 
| Medienobjekte |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Kopieren von Nachrichten, die Liquid enthalten

Liquid-Referenzen in Nachrichtentexten werden in den Ziel-Workspace kopiert, funktionieren dort aber möglicherweise nicht wie erwartet. Das bedeutet: Wenn ein Canvas aus Workspace A in Workspace B kopiert wird, kann Workspace B nicht auf die Details von Workspace A zugreifen – einschließlich Liquid-Referenzen. So werden beispielsweise Felder wie Auslöseaktionen und Zielgruppen-Filter nicht übernommen.

Behalten Sie beim Kopieren von Kampagnen und Canvases über Workspaces hinweg die folgenden Liquid-Referenzen mit Abhängigkeiten im Auge:

- Katalogartikel-Tags
- Connected-Content-Tags
- Content-Blöcke
- Angepasste Attribute
- Einstellungszentren
- Produktempfehlungen
- Abo-Status-Tags
- Gutschein- und Aktions-Tags

## Kopieren von Nachrichten mit Feature-Flags

Um eine Feature-Flag-Kampagne und ein Canvas mit einem Feature-Flag-Schritt zwischen Workspaces zu kopieren, stellen Sie sicher, dass im Ziel-Workspace ein [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments) mit einer ID konfiguriert ist, die entweder mit dem Feature-Flag übereinstimmt, auf das in der ursprünglichen Kampagne verwiesen wird, oder mit dem Feature-Flag-Schritt, auf den im ursprünglichen Canvas verwiesen wird.

Wenn Sie eine Kampagne oder ein Canvas kopieren, das einen Feature-Flag-Schritt mit einer Feature-Flag-ID enthält, die im Ziel-Workspace nicht vorhanden ist, wird der Feature-Flag-Schritt zwar kopiert, nicht aber sein Inhalt.

## Kopieren von Nachrichten mit Content-Blöcken

Wenn Sie eine Kampagne über Workspaces hinweg kopieren, werden die Content-Blöcke nicht mitkopiert. Ein Content-Block kann jedoch im Ziel-Workspace referenziert werden, wenn dort ein Block mit demselben Namen existiert. Alternativ können Sie den Content-Block (oder die entsprechenden Liquid-Referenzen) im Ziel-Workspace erstellen, um Fehler beim Starten einer Kampagne zu vermeiden.

Bei Canvases, die auf einen Content-Block verweisen, muss der Content-Block zunächst in den Ziel-Workspace kopiert werden.