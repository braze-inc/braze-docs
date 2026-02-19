---
nav_title: Jaspis
article_title: Jaspis
description: "In diesem referenzierten Artikel wird die Integration zwischen Braze und Jasper beschrieben."
alias: /partners/jasper/
page_type: partner
search_tag: Partner
---

# Jaspis 

> [Jasper](https://www.jasper.ai/) ist eine KI-gestützte Content-Plattform, die Ihre Marke in die Lage versetzt, qualitativ hochwertige, markengerechte Inhalte über verschiedene Kanäle, einschließlich Blogs, Anzeigen und Social Media, zu erstellen, zu verwalten und zu skalieren.

_Diese Integration wird von Jasper gepflegt._

## Übersicht

Die Integration von Jasper und Braze ermöglicht es Ihnen, die Erstellung von Inhalten und die Durchführung von Kampagnen zu optimieren. Mit Jasper können Ihre Marketing Teams in wenigen Minuten hochwertige, markengerechte Texte erstellen. Braze wird dann die Zustellung dieser Nachrichten an die richtige Zielgruppe zum optimalen Zeitpunkt erleichtern. Diese Integration fördert nahtlose Arbeitsabläufe, reduziert den manuellen Aufwand und sorgt für bessere Ergebnisse beim Engagement.

Die Vorteile dieser Integration sind unter anderem:

- **Schnelle Durchführung von Kampagnen:** Starten Sie Kampagnen in Minuten, nicht in Wochen.
- **Konsistente Markensprache:** Verwenden Sie Jasper Templates, um sicherzustellen, dass die erstellten Texte den Markenrichtlinien genau entsprechen.
- **Gezielte Generierung von Inhalten:** Erstellen Sie hochgradig angepasstes Messaging mit Segmenten der Zielgruppe, Style Guides und proprietären Artikeln.
- **Dynamische Personalisierung:** Verwenden Sie Liquid Platzhalter, wie {% raw %}```{{${first_name}}}```{% endraw %}, für eine skalierbare Personalisierung innerhalb von Braze.
- **Fehlerreduzierung:** Automatisierte Arbeitsabläufe minimieren Copy-Paste-Fehler und reduzieren manuelle Schritte.

## Voraussetzungen

| Anforderung   | Beschreibung  |
| ------------------- | ---------------- |
| Jaspis-Konto      | Sie benötigen ein Jasper-Konto, um diese Partnerschaft nutzen zu können. |
| Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen. <br>  <br>`templates.email.create` <br> `templates.email.update` <br>`content_blocks.create` <br>`content_blocks.update` <br><br>Dieser Schlüssel kann im Braze-Dashboard generiert werden, indem Sie zu **Einstellungen > API-Schlüssel** navigieren.  |
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr spezifischer Endpunkt hängt von der Braze-URL für Ihre Instanz ab. Referenzieren Sie die [Braze API Basics: Endpunkte]({{site.baseurl}}/api/basics#endpoints) Dokumentation für weitere Einzelheiten. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

## Integrationsmethoden

Es gibt zwei Methoden zur Erstellung von Inhalten in Jasper und zum Update von Braze Templates:

1. Verwenden Sie die Jasper API direkt
2. Verwenden Sie Jasper Studio, um eine angepasste App zu erstellen, die für Braze geeignet ist.

{% tabs %}
{% tab Jasper API %}

## Methode: Verwenden Sie die Jasper API direkt

Diese Methode ist ideal für die programmgesteuerte Erstellung und Aktualisierung von E-Mail HTML-Templates in Braze und umgeht die manuelle Einrichtung in Jasper und Braze.

### Schritt 1: Jasper einrichten

1. Folgen Sie den Anweisungen unter [Erste Schritte](https://developers.jasper.ai/docs/getting-started-1), um Ihren Jasper API-Schlüssel zu generieren.
2. Verwenden Sie das vorgefertigte Template von Jasper, das für die Erstellung von HTML-E-Mail-Vorlagen von Braze optimiert ist und die Template ID `skl_BC53D8AC5B4B47E8BE557EBB706E9B47` hat.
3. Erfassen Sie die Werte für die folgenden Felder, die für eine Anfrage zur Generierung von Inhalten für eine Braze HTML E-Mail-Vorlage erforderlich sind.

| Feld | Beschreibung |
| --- | --- |
| `emailObjective`| Definieren Sie das Ziel der E-Mail klar und deutlich. |
| `ctaLink`| Die URL für Ihren Call-to-Action. |
| `unsubscribeLink`| Erforderlich für Marketing E-Mails. |
| `brandColor`| Die Primärfarbe Ihrer Marke im Hexadezimalformat (zum Beispiel `#4dfa8a`). |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

**Optionale Felder**

| Feld | Beschreibung |
| --- | --- |
|`toneId` | Sprachstil der Marke |
| `audienceId`| Zielgruppen-Segmentierung |
| `styleId`| Style guide |
| `knowledgeIds` | Erweiterter Inhaltskontext. Sie können bis zu drei IDs hinzufügen. |
{: .reset-td-br-1 .rest-td-br-2 role=“presentation” }

{: start="4"}
4\. Generieren Sie Ihre Ausgabe, indem Sie die Vorlage über die Jasper API ausführen. Dies erzeugt eine JSON-Nutzlast, die die `subject`, `preheader` und `body` (HTML-Inhalte) enthält.

{% subtabs %}
{% subtab Sample request %}

### Anfrage für Muster

{% raw %}
```bash
curl --location 'https://api.jasper.ai/v1/templates/skl_BC53D8AC5B4B47E8BE557EBB706E9B47/run?toneId=ton_811696974b3c4db4b3ac0041685c3b7c&knowledgeIds=kno_0a62fc17529e4fe69a71f30b6f0e88a7&audienceId=aud_0199117a690a7cc98481f8700916e2a6' \
--header 'Content-Type: application/json' \
--header 'x-api-key: ••••••' \
--data '{
  "inputs": {
    "emailObjective": "Announce a webinar and highlight Jasper + Braze integration benefits. Use {{${firstname}}} in the subject and body. Body length ~400 words. Include CTA buttons for registration and footer with unsubscribe link. Apply brand color to buttons and links.",
    "ctaLink": "https://yourbrand.com/register",
    "unsubscribeLink": "{{${unsubscribe_link}}}",
    "brandColor":"#4dfa8a"
  },
  "options": {
    "outputCount": 1,
    "outputLanguage": "English",
    "inputLanguage": "English",
    "languageFormality": "less"
  }
}'
```
{% endraw %}

{% endsubtab %}
{% subtab Sample output %}

### Beispielhafte Ausgabe
```
{
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}
```
{% endsubtab %}
{% endsubtabs %}

### Schritt 2: Braze einrichten

Verwenden Sie die von Jasper in Schritt 1 generierten `subject`, `preheader` und `body`, um eine POST-Anfrage an die Braze REST API zu [stellen]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) und [eine neue E-Mail-Vorlage zu erstellen]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/). Stellen Sie sicher, dass Ihr Braze REST API-Schlüssel die Berechtigungen `templates.email.create` und `templates.email.update` hat.

### Beispiel für eine Anfrage der Braze API zur Erstellung einer E-Mail-Vorlage

```bash
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endtab %}
{% tab Jasper Studio %}

## Methode: Erstellen Sie eine angepasste App für Braze mit Jasper Studio

Jasper Studio ist eine No-Code-Plattform innerhalb von Jasper, die es Ihnen erlaubt, maßgeschneiderte KI-Apps zu erstellen, ohne dass Sie IT-Unterstützung benötigen. Sie können eine angepasste App entwerfen, die JSON-Strukturen erzeugt, die speziell für die Braze API formatiert sind, oder Inhalte generieren, die manuell zu Ihren Braze Nachrichten hinzugefügt werden können.

1. Wählen Sie auf Ihrem Jasper-Startbildschirm **App erstellen** aus.
2. Geben Sie die App an, die Sie erstellen möchten, z. B. **Braze HTML E-Mail Template** oder **Content-Block Template**.
3. Bearbeiten Sie die Eingabeaufforderungsfelder, die Jasper generiert. Für eine HTML E-Mail-Vorlage können Sie Eingabeformulare für die Betreffzeile, den Preheader, den HTML-Body, die Tags, das Umschalten von Inline-CSS und den Namen der Vorlage einfügen.
4. Integrieren Sie Wissenseinbettungen mit Anleitungen zu Liquid Best Practices für konsistente Personalisierung und dynamischen Content.
5. Verfeinern Sie die Anweisungen, die dem Large Language Model (LLM) für die Inhaltserstellung zur Verfügung gestellt werden.
6. Geben Sie ein Beispiel für die gewünschte Ausgabe an, z.B. eine automatisierte JSON-Ausgabe, die für Braze-Nutzdaten formatiert ist.
7. Generieren und exportieren Sie Folgendes:
- **Direktes Kopieren/Einfügen:** Inhalte können direkt in die Braze Plattform kopiert und eingefügt werden.
- **JSON-Ausgabe:** Generieren Sie eine JSON-Ausgabe. Diese Nutzlast kann dann verwendet werden, um den Endpunkt von Braze über `curl` oder Middleware direkt aufzurufen, oder sie kann in Ihren Workflow für E-Mail-Operationen integriert werden.

![Jasper Braze Angepasste App.]({% image_buster /assets/img/jasper/jasper_custom_app.png %})

{% subtabs %}
{% subtab Sample JSON output (custom app) %}

## Beispiel JSON-Ausgabe (angepasste App)

{% raw %}
```json
{
  "template_name": "email_webinar_2025",
  "subject": "Join Our Webinar, {{${firstname}}}!",
  "preheader": "Unlock the potential of seamless integration.",
  "body": "<html> ... </html>",
  "tags": ["jasperapi"],
  "should_inline_css": true
}
```
{% endraw %}

{% endsubtab %}
{% subtab Sample Braze API request (using custom app output) %}

## Beispiel einer Braze API-Anfrage (mit angepasster App-Ausgabe)

{% raw %}
```bash
curl --location --request POST 'https://rest.iad-03.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_BRAZE_API_KEY>' \
--data '{
  "template_name": "email_template_jasperapi_20231104T142300Z",
  "subject": "GlowUp Serum is Here! Limited-Time 20% Off!",
  "preheader": "GlowUp Serum is here with a 20% launch discount for 7 days only!",
  "body": "<html> ... </html>"
}'
```
{% endraw %}

{% endsubtab %}
{% endsubtabs %}

Alternativ können Sie als Marketer eine angepasste App erstellen, die sich an den Markenrichtlinien orientiert, um Inhalte ohne HTML und Copy & Paste zu generieren, und Braze Templates für das Styling verwenden.

{% endtab %}
{% endtabs %}

{% alert note %}
Weitere Hilfe finden Sie in der [Dokumentation zur Jasper API](https://developers.jasper.ai/reference/gettemplate-1) und im [Jasper Studio Help Center](https://help.jasper.ai/hc/en-us/articles/36783295610395-Jasper-Studio).
{% endalert %}
