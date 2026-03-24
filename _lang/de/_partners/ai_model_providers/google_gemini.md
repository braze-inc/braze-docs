---
nav_title: Google Gemini
article_title: Google Gemini
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Google Gemini, die es Ihnen ermöglicht, Gemini-Modelle mit Braze zu verbinden, um sie mit angepassten KI-Agenten zu verwenden."
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [Google Gemini](https://deepmind.google/technologies/gemini/) ist Googles Familie von KI-Modellen, die fortschrittliches Denken über Text, Code und Bilder hinweg kombiniert, um Marken dabei zu helfen, intelligentere und personalisiertere Erlebnisse zu schaffen.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Diese Integration wird von Google gepflegt._

## Über die Integration

Mit der Integration von Braze und Google Gemini können Sie Ihren Google Gemini API-Schlüssel oder Vertex AI-Schlüssel mit Braze verbinden, um Gemini-Modelle beim Erstellen angepasster KI-Agenten zu verwenden. Mit dieser Integration können Ihre Agenten personalisierte Texte generieren, Entscheidungen in Realtime treffen oder Katalog-Felder mithilfe der Gemini-Modelle von Google aktualisieren.

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| Google Cloud-Konto mit Gemini API-Schlüssel oder Vertex AI-Schlüssel | Ein Google Cloud-Konto mit einem Gemini API-Schlüssel oder Vertex AI-Schlüssel. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Administrator oder den [Google Cloud-Support](https://cloud.google.com/support). |
| Braze-Instanz | Sie finden Ihre Braze-Instanz auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints) oder über Ihre:n Braze Onboarding-Manager:in. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

So verbinden Sie Ihren Google Gemini API-Schlüssel mit Braze:

1. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und suchen Sie Google Gemini.
2. Wählen Sie unter **API Type** entweder **Gemini API** oder **Vertex AI** aus.
3. Geben Sie Ihren API-Schlüssel von Google ein. Für Vertex AI geben Sie die Projekt-ID ein.
4. Wählen Sie **Speichern**.

Nach dem Speichern können Sie Gemini-Modelle auswählen, wenn Sie [einen angepassten Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) – direkt in der Agentenkonsole.

Wenden Sie sich an den [Google Cloud-Support](https://cloud.google.com/support), wenn Sie Probleme oder Fragen zu Ihrer Integration haben.