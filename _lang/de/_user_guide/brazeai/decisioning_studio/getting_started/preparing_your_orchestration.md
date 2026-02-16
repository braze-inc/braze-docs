---
nav_title: Vorbereiten Ihrer Orchestrierung
article_title: Vorbereiten Ihrer Orchestrierung
page_order: 3
page_type: reference
description: "Dieser referenzierte Artikel erklärt, was Sie vorbereiten müssen, bevor Sie die Orchestrierung für BrazeAI Decisioning Studio einrichten. Dazu gehören die Auswahl Ihrer CEP und das Sammeln der erforderlichen Zugangsdaten und Assets."
---

# Vorbereiten Ihrer Orchestrierung

> Dieser referenzierte Artikel erklärt, was Sie vor der Einrichtung der Orchestrierung für BrazeAI Decisioning Studio™ vorbereiten müssen, einschließlich der Auswahl Ihrer Customer-Engagement-Plattform (CEP) und der Zusammenstellung der erforderlichen Zugangsdaten und Assets.

## Was ist Orchestrierung?

Die Orchestrierung ist die Verbindung zwischen Decisioning Studio und Ihrer Customer-Engagement-Plattform (CEP). Sobald Ihr Entscheidungsagent die optimale Aktion für jeden Kunden:in ermittelt hat, führt die Orchestrierung diese Entscheidungen aus, indem sie personalisierte Kommunikation über Ihre CEP auslöst.

Stellen Sie es sich so vor:

- **Decisioning Studio** entscheidet, *was* gesendet wird und *wann* es gesendet wird
- **Ihr CEP** kümmert sich darum *, wie* es gesendet wird

## Wählen Sie Ihr CEP

Der erste Schritt besteht darin, die Customer-Engagement-Plattform zu bestimmen, die Sie mit Decisioning Studio verwenden werden. Ihre Wahl beeinflusst die Komplexität der Einrichtung und die verfügbaren Features.

### Unterstützte CEPs

| CEP | Entscheidungsfindung Studio Go | Decisioning Studio Pro | Art der Integration |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Native API-Integration (empfohlen) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | API-Ereignisse + Journey Builder |
| **Klaviyo** | ✓ | ✓ | API-Ereignisse + Abläufe |
| **Andere CEPs** | - | ✓ | Angepasst (Empfehlungsdatei) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
Wenn Sie bereits Braze als CEP verwenden, empfehlen wir Ihnen, die native Integration von Braze zu verwenden, um die Einrichtung so reibungslos wie möglich zu gestalten.
{% endalert %}

## Was Sie für die Vorbereitung benötigen

Bevor Sie die Orchestrierung einrichten, sollten Sie die folgenden Artikel auf der Grundlage der von Ihnen gewählten CEP sammeln.

{% tabs %}
{% tab Braze %}

| Artikel | Beschreibung |
|------|-------------|
| **REST-API-Schlüssel** | Ein neuer API-Schlüssel mit Berechtigungen für Nutzerdaten, Nachrichten, Kampagnen, Canvas, Segmente und Templates. |
| **Braze-Dashboard URL** | Die URL Ihrer Braze-Instanz (z.B. `https://dashboard-01.braze.com`). |
| **App ID** | Der API-Schlüssel für die App, die Sie tracken möchten (zu finden unter **Einstellungen** > **App-Einstellungen**). |
| **Name und Adresse der E-Mail-Anzeige** | Die Absenderinformationen, die Sie für Ihre Kampagnen verwenden möchten (zu finden unter **Einstellungen** > **E-Mail-Voreinstellungen**). |
| **Basis-Templates** | Die Templates für Nachrichten, die Ihr Agent für die Orchestrierung verwendet. Sie werden API-getriggerte Kampagnen für jedes Template erstellen. |
| **Testnutzer:in ID** | Eine Nutzer:innen-ID zum Testen der Integration vor dem Start. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Artikel | Beschreibung |
|------|-------------|
| **Zugangsdaten für App-Pakete** | Client-ID, Client-Geheimnis, Authentifizierungs-Basis-URI, REST-Basis-URI und SOAP-Basis-URI von einem installierten Paket mit Server-zu-Server API Integration. |
| **API-Berechtigungen** | Bereiche für Kanäle, Assets, Automatisierungen, Journeys, Kontakte, Datenerweiterungen und Tracking-Ereignisse. |
| **Daten Erweiterungen** | Sie benötigen Datenerweiterungen für Abonnent:in-Daten, Engagement-Daten und Empfehlungen. |
| **E-Mail-Templates** | Die Templates, die Sie in Decisioning Studio verwenden möchten, mit den jeweiligen Template IDs. |
| **Zugang zum Journey Builder** | Zugang zur Erstellung und Aktivierung von mehrstufigen Reisen mit API-Eingangsquellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Artikel | Beschreibung |
|------|-------------|
| **Private API-Schlüssel** | Ein neuer API-Schlüssel mit Vollzugriffsrechten für Ereignisse, Abläufe, Listen, Metriken, Profile und Templates. |
| **E-Mail-Templates** | Die Templates, die Sie in Decisioning Studio verwenden möchten. Templates müssen mit einer Bewegung verknüpft sein (Sie können zu diesem Zweck eine Platzhalterbewegung erstellen). |
| **Informationen zum Absender** | Der Name des Absenders und die E-Mail Adresse, die Sie für Ihre Kampagnen verwenden möchten. |
| **Flow Zugang** | Zugang zum Erstellen und Aktivieren von Bewegungen mit metrischen Triggern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
Angepasste CEP-Integrationen sind nur mit Decisioning Studio Pro möglich.
{% endalert %}

Wenn Sie eine andere CEP als Braze, SFMC oder Klaviyo verwenden, kann Decisioning Studio Pro über einen Empfehlungsdateiansatz integriert werden:

| Artikel | Beschreibung |
|------|-------------|
| **Fähigkeit zur Datenaufnahme** | Ihr CEP muss in der Lage sein, Empfehlungsdateien (in der Regel CSV oder JSON) mit personalisierten Entscheidungen für jede Kund:in aufzunehmen. |
| **Unterstützung dynamischer Inhalte** | Ihre Kampagnen müssen das dynamische Auffüllen von Feldern auf der Grundlage von Empfehlungsdaten unterstützen. |
| **Angepasste technische Ressourcen** | Ihr Team muss die Integration erstellen, um Empfehlungsdateien zu lesen und Mitteilungen zu triggern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planung Ihrer Kampagnen

Bevor Sie die Orchestrierung einrichten, sollten Sie die folgenden Details beachten:

### Basis-Templates

Eine Basis-Vorlage ist eine beliebige Nachrichten-Vorlage, die Ihr Entscheidungs-Agent verwenden kann. Bedenken Sie:

- **Wie viele Templates?** Ihr Agent kann mit einer oder mehreren Templates arbeiten. Wenn es mehrere sind, kann der Agent anpassen, welches Template jeder Kund:in erhält.
- **Welche Kanäle?** E-Mail, Push, SMS oder eine Kombination davon. Für jeden Kanal sind möglicherweise eigene Templates und Kampagnen erforderlich.
- **Welche dynamischen Elemente?** Legen Sie fest, welche Teile Ihrer Nachricht der Agent personalisieren soll (Betreffzeilen, CTAs, Angebote, Timing usw.). Diese werden dann zu API triggernden Eigenschaften oder dynamischen Platzhaltern.

### Einstellungen für die Wiedererwählbarkeit

Ihre Kampagnen sollten es Nutzern:innen erlauben, Nachrichten mehrfach zu empfangen:

- Zum Testen sollten Sie dieselbe Kampagne wiederholt an dieselben Nutzer:innen senden.
- In der Produktion kann der Agent feststellen, dass dieselbe Kampagne für einen Nutzer:innen an aufeinanderfolgenden Tagen optimal ist.

{% alert note %}
Die Agenten von Decisioning Studio sind so konzipiert, dass sie bei der Einrichtung der Wiederzulassung zu Testzwecken Häufigkeitsobergrenzen beachten und dieselbe Kampagne in der Produktion nicht mehr als einmal pro Tag an einen Nutzer:innen senden.
{% endalert %}

### API triggernde Eigenschaften

Planen Sie bei Braze-Integrationen, welche Dimensionen Ihr Agent optimieren soll. Diese werden zu API triggernden Eigenschaften, die dynamische Werte an Ihre Kampagnen weitergeben:

| Beispiel Dimension | API triggernde Eigenschaft |
|-------------------|---------------------|
| Betreffzeile | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Aufruf zum Handeln | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Angebot | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Rabattbetrag | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Bewährte Praktiken

Behalten Sie bei der Vorbereitung der Orchestrierung diese bewährten Verfahren im Hinterkopf:

1. **Fangen Sie einfach an.** Beginnen Sie mit einem Kanal und einer oder zwei Templates. Sie können später erweitern, wenn Sie lernen, was funktioniert.
2. **Testen Sie gründlich.** Testen Sie Ihre Integration vor dem Start mit einer kleinen Gruppe von Nutzer:innen, um zu überprüfen, ob dynamischer Content korrekt aufgefüllt wird.
3. **Dokumentieren Sie Ihre Einrichtung.** Behalten Sie den Überblick über Kampagnen IDs, Template IDs, API-Schlüssel und andere Bezeichner. Diese müssen Sie im Decisioning Studio Portal referenzieren.
4. **Stimmen Sie sich mit Ihrem Team ab.** An der Einrichtung der Orchestrierung können Marketing-, Entwickler- und Daten-Teams beteiligt sein. Stellen Sie sicher, dass jeder seine Rolle in diesem Prozess versteht.
5. **Planen Sie Daten für das Feedback.** Bei der Orchestrierung geht es nicht nur um das Versenden von Nachrichten, sondern auch um das Sammeln von Daten zum Engagement und zur Konversion, aus denen Ihr Agent lernen kann. Weitere Informationen finden Sie unter [Vorbereiten Ihrer Datenquellen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/preparing_your_data_sources/).

## Nächste Schritte

Sobald Sie Ihre Zugangsdaten gesammelt und Ihre Kampagnen geplant haben, können Sie die Orchestrierung einrichten:

- [Decisioning Studio Go: Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro: Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

