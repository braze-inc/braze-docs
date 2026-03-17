---
nav_title: Agenten konzipieren
article_title: Agenten konzipieren
page_order: 3
description: "Erfahren Sie vom AI Decisioning Services-Team, wie Sie Ihren Decisioning Studio Pro-Agenten gestalten können, einschließlich Definition der Zielgruppen, Metriken und Dimensionen."
---

# Agenten konzipieren

> Der erste Schritt bei der Einrichtung Ihres Agenten besteht darin, gemeinsam mit unserem Team für KI-Entscheidungsdienste Ihren Agenten zu entwerfen. Dieser Artikel behandelt die wichtigsten Designentscheidungen und die Definition Ihrer Zielgruppen.

Grundlegende Konzepte zu Entscheidungsagenten – einschließlich Metriken, Dimensionen, Aktionsbanken und Einschränkungen – finden Sie unter [„Entscheidungsagenten entwerfen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)“.

## Wichtige Designentscheidungen

In Zusammenarbeit mit dem Team für KI-Entscheidungsdienste werden Sie die folgenden Entscheidungen treffen:

| Entscheidung | Beschreibung | Beispiele |
|----------|-------------|----------|
| **Erfolgsmetriken** | Was wird der Mitarbeiter bei der Personalisierung des Customer-Engagements optimieren? | Umsatz, LTV, ARPU, Konversionen, Bindung |
| **Zielgruppe** | Für wen wird der Decisioning Studio-Agent Entscheidungen zum Customer-Engagement treffen? | Sehr geehrte Kund:innen, geschätzte Treuekunden, gefährdete Abonnent:innen |
| **Versuchsgruppen** | Wie sollten die randomisierten kontrollierten Studien von Decisioning Studio strukturiert werden? | Entscheidungsstudio, Zufallskontrolle, BAU, Holdout |
| **Format** | Welche Entscheidungen sollte der Agent individuell personalisieren? | Uhrzeit, Betreffzeile, Häufigkeit, Angebote, Kanal |
| **Optionen** | Welche Möglichkeiten stehen dem Makler zur Verfügung? | Spezifische Templates, Angebote, Zeitfenster |
| **Einschränkungen** | Welche Entscheidungen sollte der Makler *niemals* treffen? | Geografische Einschränkungen, Budgetgrenzen, Teilnahmebedingungen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Jede dieser Entscheidungen hat Auswirkungen darauf, wie viel zusätzliches Wachstum der Agent generieren kann und wie schnell dies erfolgt. Unser Team für KI-Entscheidungsdienste arbeitet mit Ihnen zusammen, um einen Agenten zu entwickeln, der unter Einhaltung all Ihrer Geschäftsregeln einen maximalen Mehrwert generiert.

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Ihre Zielgruppe definieren

Anwendungsfälle werden in der Regel in einer Customer-Engagement-Plattform (wie Braze oder Salesforce Marketing Cloud) definiert und anschließend an den Decisioning Studio-Agenten gesendet. Der Agent teilt die Kund:innen anschließend in Behandlungsgruppen ein, um randomisierte kontrollierte Studien durchzuführen.

### Behandlungsgruppen

| Gruppe | Beschreibung |
|-------|-------------|
| **Entscheidungsstudio** | Kunden, die KI-optimierte Empfehlungen erhalten |
| **Zufällige Steuerung** | Kund:innen, die zufällig ausgewählte Optionen erhalten (Basisvergleich) |
| **Business-as-Usual (optional)** | Kunden, die die aktuelle Marketing-Journey erhalten (zum Vergleich mit der bestehenden Performance) |
| **Holdout (optional)** | Kund:innen, die keine Mitteilungen erhalten (zur Messung der Gesamtwirkung der Kampagne) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Konfiguration Ihrer Zielgruppe

{% tabs %}
{% tab Braze %}

**Zielgruppe in Braze konfigurieren:**

1. Erstellen Sie ein Segment für Ihre Zielgruppe, die Sie ansprechen möchten.
2. Bitte geben Sie die Segment-ID an Ihr KI-Decisioning-Services-Team weiter.

{% alert note %}
Für Braze können wir mehrere Segmente erfassen und diese kombinieren, um die Zielgruppe zu erstellen. Das Decisioning Studio kann ein Segment für eine Business-as-Usual-Vergleichskampagne aufnehmen. Alle diese Muster sind akzeptabel.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Zielgruppe in Salesforce Marketing Cloud konfigurieren:**

1. Bitte konfigurieren Sie eine oder mehrere SFMC-Datenerweiterungen für Ihre Zielgruppe und geben Sie die ID der Datenerweiterung an.
2. Richten Sie das installierte SFMC-Paket für die API-Integration mit den entsprechenden Berechtigungen ein, die von Decisioning Studio benötigt werden.
3. Bitte stellen Sie sicher, dass diese Datenerweiterung täglich aktualisiert wird, da Decisioning Studio die neuesten verfügbaren inkrementellen Daten abruft.

Bitte übermitteln Sie die Erweiterungs-ID und den API-Schlüssel an das Braze-Serviceteam. Sie werden bei den nächsten Schritten zur Erfassung von Kundendaten behilflich sein.

{% endtab %}
{% tab Klaviyo %}

**Definieren Sie die Zielgruppe in Klaviyo:**

1. Erstellen Sie ein Segment für die Zielgruppe
2. Bitte generieren Sie einen privaten API-Schlüssel und übermitteln Sie diesen an das Braze AI Decisioning-Team.
3. Bitte übermitteln Sie die Segment-ID und den API-Schlüssel an das Braze-Serviceteam.

Weitere Informationen zur Durchführung dieser Schritte finden Sie in der [Klaviyo-Dokumentation.](https://help.klaviyo.com/hc/en-us/articles/115005237908)

{% endtab %}
{% tab Other Platforms %}

**Google-Cloudspeicher**

Sollte die Zielgruppe derzeit nicht in Braze, SFMC oder Klaviyo gespeichert sein, empfiehlt es sich, eine Automatisierung zum direkten Export in einen von Braze verwalteten Google Cloud Services-Bucket zu konfigurieren.

Um festzustellen, ob dies möglich ist, referenzieren Sie bitte die Dokumentation Ihrer MarTech-Plattform. Beispielsweise bietet mParticle eine [native Integration mit Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/) an. In diesem Fall können wir einen GCS-Bucket zur Verfügung stellen, in den die Daten der Zielgruppen exportiert werden können.

Es gibt ähnliche Seiten für:
- [Twilio-Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Professionelle Funktionen

Decisioning Studio Pro bietet die volle Leistungsstärke der KI-Entscheidungsfindung:

| Fähigkeit | Details |
|------------|---------|
| **Jede Erfolgsmetrik** | Optimieren Sie Umsatz, Konversionen, ARPU, LTV oder andere geschäftliche KPIs. |
| **Unbegrenzte Dimensionen** | Personalisieren Sie Angebote, Kanäle, Zeitpunkte, Häufigkeit, Kreativität und vieles mehr. |
| **Jeder CEP** | Native Integrationen mit Braze, SFMC, Klaviyo sowie angepasste Integrationen für jede Plattform |
| **KI-Entscheidungsserviceleistungen** | Engagierte Unterstützung durch das Data-Science-Team von Braze |
| **Fortgeschrittenes Versuchsdesign** | Vollständig anpassbare Behandlungsgruppen und Holdouts |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Bewährte Praktiken

Einige bewährte Verfahren für die Gestaltung von Decisioning Studio-Agenten:

1. **Maximieren Sie die Datenvielfalt**: Je mehr Informationen die Mitarbeiter über Ihre Kund:innen haben, desto besser wird die Performance sein.
2. **Maßnahmen diversifizieren**: Je vielfältiger die Maßnahmen sind, die der Agent ergreifen kann, desto besser kann er seine Strategie für jede Nutzer:in personalisiert anpassen.
3. **Einschränkungen minimieren**: Je weniger Einschränkungen Ihre Mitarbeiter haben, desto besser. Einschränkungen sollten so gestaltet sein, dass sie Geschäftsregeln berücksichtigen und gleichzeitig agentenorientierte Experimente so weit wie möglich zulassen.

## Nächste Schritte

Sobald die wichtigsten Designentscheidungen getroffen sind, können wir mit der Markteinführung fortfahren:

- [Starten Sie Ihren Agenten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)