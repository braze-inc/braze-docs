---
nav_title: Vorbereitung Ihrer Orchestrierung
article_title: Vorbereitung Ihrer Orchestrierung
page_order: 3
page_type: reference
description: "Dieser Referenzartikel erläutert, was Sie vorbereiten müssen, bevor Sie die Orchestrierung für BrazeAI Decisioning Studio einrichten, einschließlich der Auswahl Ihres CEP und der Zusammenstellung der erforderlichen Zugangsdaten und Ressourcen."
---

# Vorbereitung Ihrer Orchestrierung

> Dieser Referenzartikel erläutert, was Sie vor der Einrichtung der Orchestrierung für BrazeAI Decisioning Studio™ vorbereiten müssen, einschließlich der Auswahl Ihrer Customer-Engagement-Plattform (CEP) und der Beschaffung der erforderlichen Zugangsdaten und Ressourcen.

## Was ist Orchestrierung?

Orchestrierung bezeichnet die Verbindung zwischen Decisioning Studio und Ihrer Customer-Engagement-Plattform (CEP). Sobald Ihr Entscheidungsagent die optimale Maßnahme für jeden Kunden ermittelt hat, setzt die Orchestrierung diese Entscheidungen um, indem sie personalisierte Kommunikationen über Ihr CEP triggert.

Betrachten Sie es einmal so:

- **Das Decisioning Studio** entscheidet, *welche Inhalte* *wann* versendet werden sollen.
- **Ihr CEP** regelt*, wie* es versendet wird.

## Auswahl Ihres CEP

Der erste Schritt besteht darin, zu bestimmen, welche Customer-Engagement-Plattform Sie mit Decisioning Studio verwenden möchten. Ihre Entscheidung beeinflusst die Komplexität der Einrichtung und die verfügbaren Features.

### Unterstützte CEPs

| CEP | Entscheidungsstudio Go | Entscheidungsstudio Pro | Art der Integration |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Native API-Integration (empfohlen) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | API-Ereignisse + Journey Builder |
| **Klaviyo** | ✓ | ✓ | API-Ereignisse + Abläufe |
| **Andere CEPs** | — | ✓ | Angepasst (Empfehlungsdatei) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
Sollten Sie bereits Braze als CEP verwenden, empfehlen wir Ihnen die native Braze-Integration, um eine reibungslose Einrichtung zu gewährleisten.
{% endalert %}

## Was Sie vorbereiten müssen

Bevor Sie die Orchestrierung einrichten, stellen Sie bitte die folgenden Artikel basierend auf dem von Ihnen gewählten CEP zusammen.

{% tabs %}
{% tab Braze %}

| Artikel | Beschreibung |
|------|-------------|
| **REST-API-Schlüssel** | Ein neuer API-Schlüssel mit Berechtigungen für Nutzerdaten, Nachrichten, Kampagnen, Canvas, Segmente und Templates. |
| **URL des Braze-Dashboards** | Die URL Ihrer Braze-Instanz (zum Beispiel )`https://dashboard-01.braze.com`. |
| **App-ID** | Der API-Schlüssel, der mit der App verknüpft ist, die Sie verfolgen möchten (zu finden unter **„Einstellungen“** > **„App-Einstellungen“**). |
| **Anzeigename und E-Mail-Adresse** | Die Informationen zum Absender, die für Ihre Kampagnen verwendet werden sollen (zu finden unter **„Einstellungen“** > **„E-Mail-Einstellungen“**). |
| **Basis-Templates** | Die Templates für die Orchestrierung, die Ihr Agent verwenden wird. Sie erstellen API-gesteuerte Kampagnen für jedes Template. |
| **Testnutzer:in-ID** | Eine Benutzer-ID zum Testen der Integration vor der Einführung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Artikel | Beschreibung |
|------|-------------|
| **Zugangsdaten für die App-Pakete** | Client-ID, Client-Geheimnis, Authentifizierungs-Basis-URI, REST-Basis-URI und SOAP-Basis-URI aus einem installierten Paket mit Server-zu-Server-API-Integration. |
| **API-Berechtigungen** | Bereiche für Kanäle, Assets, Automatisierungen, Journeys, Kontakte, Daten-Erweiterungen und Tracking-Ereignisse. |
| **Datenerweiterungen** | Sie benötigen Datenerweiterungen für Daten über Abonnent:innen, Engagement-Daten und Empfehlungen. |
| **E-Mail-Templates** | Die Templates, die Decisioning Studio verwenden soll, mit den jeweiligen Templates-IDs. |
| **Zugang zum Journey Builder** | Zugriff zum Erstellen und Aktivieren mehrstufiger Journeys mit API-Ereignis-Eingängen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Artikel | Beschreibung |
|------|-------------|
| **Privater API-Schlüssel** | Ein neuer API-Schlüssel mit Vollzugriff auf Ereignisse, Abläufe, Listen, Metriken, Profile und Templates. |
| **E-Mail-Templates** | Die Templates, die Decisioning Studio verwenden soll. Templates müssen mit einem Ablauf verknüpft sein (zu diesem Zweck können Sie einen Platzhalterablauf erstellen). |
| **Informationen zum Absender** | Der Name und die E-Mail-Adresse des Absenders, die für Ihre Kampagnen verwendet werden sollen. |
| **Zugang zum Fluss** | Zugriff zum Erstellen und Aktivieren von Flows mit Metriken, die Triggern auslösen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
Angepasste CEP-Integrationen sind ausschließlich mit Decisioning Studio Pro verfügbar.
{% endalert %}

Wenn Sie ein anderes CEP als Braze, SFMC oder Klaviyo verwenden, kann Decisioning Studio Pro über einen Empfehlungsdatei-Ansatz integriert werden:

| Artikel | Beschreibung |
|------|-------------|
| **Datenaufnahme** | Ihr CEP muss in der Lage sein, Empfehlungsdateien (in der Regel CSV oder JSON) zu verarbeiten, die personalisierte Entscheidungen für jeden Kunden enthalten. |
| **Unterstützung dynamischen Contents** | Ihre Kampagnen müssen die dynamische Befüllung von Feldern auf der Grundlage von Empfehlungsdaten unterstützen. |
| **Angepasste technische Ressourcen** | Ihr Team muss die Integration erstellen, um Empfehlungsdateien zu lesen und Kommunikationen zu triggern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planung Ihrer Kampagnen

Bevor Sie die Orchestrierung einrichten, sollten Sie die folgenden Details berücksichtigen:

### Basis-Templates

Eine Basisvorlage ist jedes Template für Nachrichten, das Ihr Entscheidungsagent verwenden könnte. Bitte beachten Sie:

- **Wie viele Templates?** Ihr Agent kann mit einem Template oder mehreren Templates arbeiten. Bei mehreren Kund:innen kann der Mitarbeiter die Personalisierung der Templates individuell festlegen, sodass jede Kund:in ein anderes Template erhält.
- **Welche Kanäle?** E-Mail, Push-Benachrichtigung, SMS oder eine Kombination daraus. Für jeden Kanal können separate Templates und Kampagnen erforderlich sein.
- **Welche dynamischen Elemente?** Identifizieren Sie, welche Teile Ihrer Nachricht der Agent personalisieren wird (Betreffzeilen, CTAs, Angebote, Zeitplanung usw.). Diese werden zu API-Trigger-Eigenschaften oder dynamischen Platzhaltern.

### Einstellungen zur Wiederwahlberechtigung

Ihre Kampagnen sollten es den Nutzern:innen ermöglichen, Nachrichten mehrfach zu empfangen:

- Für Testzwecke sollten Sie dieselbe Kampagne wiederholt an denselben Nutzer:in senden.
- In der Produktion kann der Agent feststellen, dass dieselbe Kampagne für eine Nutzer:in an aufeinanderfolgenden Tagen optimal ist.

{% alert note %}
Bei der Einrichtung der erneuten Testberechtigung sind die Agenten von Decisioning Studio so konzipiert, dass sie Frequency-Capping einhalten und dieselbe Kampagne nicht mehr als einmal pro Tag an eine Nutzer:in senden.
{% endalert %}

### API-Trigger-Eigenschaften

Für Braze-Integrationen planen Sie bitte, welche Dimensionen Ihr Agent optimieren soll. Diese werden zu API-Trigger-Eigenschaften, die dynamische Werte an Ihre Kampagnen übergeben:

| Beispiel-Dimension | API-Trigger-Eigenschaft |
|-------------------|---------------------|
| Betreffzeile | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Aufruf zum Handeln | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Angebot | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Rabattbetrag | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Bewährte Praktiken

Beachten Sie bei der Vorbereitung der Orchestrierung die folgenden bewährten Verfahren:

1. **Fangen Sie einfach an.** Beginnen Sie mit einem Kanal und ein oder zwei Templates. Sie können später erweitern, wenn Sie erfahren, was funktioniert.
2. **Bitte führen Sie gründliche Tests durch.** Bitte überprüfen Sie Ihre Integration vor der Einführung mit einer kleinen Gruppe von Nutzer:innen, um sicherzustellen, dass dynamischer Content korrekt angezeigt wird.
3. **Bitte erstellen Sie die Dokumentation Ihrer Konfiguration.** Bitte verfolgen Sie Kampagnen-IDs, Template-IDs, API-Schlüssel und andere Bezeichner. Bitte beachten Sie, dass Sie diese im Decisioning Studio-Portal referenzieren müssen.
4. **Bitte stimmen Sie sich mit Ihrem Team ab.** Die Einrichtung der Orchestrierung kann Marketing-, Entwicklerteams und Teams für Daten umfassen. Bitte stellen Sie sicher, dass alle Beteiligten ihre Rolle in diesem Prozess verstehen.
5. **Planen Sie Daten zur Rückmeldung ein.** Bei der Orchestrierung geht es nicht nur um das Versenden von Nachrichten, sondern auch um das Sammeln von Engagement- und Konversionsdaten, die Ihren Mitarbeitern beim Lernen helfen. Weitere Informationen finden Sie unter [Vorbereiten Ihrer Datenquellen.]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/preparing_your_data_sources/)

## Nächste Schritte

Nachdem Sie Ihre Zugangsdaten zusammengestellt und Ihre Kampagnen geplant haben, können Sie mit der Einrichtung der Orchestrierung fortfahren:

- [Entscheidungsstudio Go: Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Entscheidungsstudio Pro: Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

