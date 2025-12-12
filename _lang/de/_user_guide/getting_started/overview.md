---
nav_title: Braze Übersicht
article_title: "Erste Schritte: Braze Übersicht"
page_order: 1
page_type: reference
description: "Machen Sie sich mit den wichtigsten Konzepten vertraut, die Sie bei der Arbeit mit Braze kennen müssen."

---

# Erste Schritte: Braze Übersicht

Willkommen bei Braze! Diese Artikelsammlung wird Ihnen den Einstieg in unsere Plattform erleichtern und Sie mit den wichtigsten Begriffen, Merkmalen und Funktionalitäten von Braze vertraut machen. Auf dieser Seite werden die wichtigsten Konzepte vorgestellt, die Sie bei der Arbeit mit Braze kennen müssen.

{% alert tip %}
Wir empfehlen Ihnen dringend, neben diesen Artikeln auch unseren kostenlosen Kurs [Braze Foundations for Everyone](https://learning.braze.com/page/braze-foundations-for-everyone) zu besuchen. Für diesen Kurs ist keine spezielle Anmeldung oder ein Konto erforderlich. Wenn Sie ein Entwickler sind und einen technischen Überblick über Braze suchen, sollten Sie sich auch [Getting Started for Developers]({{site.baseurl}}/developer_guide/getting_started/platform_overview/) ansehen.
{% endalert %}

In den Abschnitten zu den ersten Schritten konzentrieren wir uns auf die gängigen Implementierungen von Braze. Braze ist jedoch unglaublich flexibel und kann so angepasst werden, dass es für Ihr Unternehmen auf verschiedene Weise von Nutzen ist. Aus Gründen der Übersichtlichkeit und der Kürze haben wir einen beschreibenden Überblick über die Standardeinstellungen gegeben, anstatt starre Anweisungen zu geben. Wir wissen, dass jedes Unternehmen seine eigenen Bedürfnisse hat, und Braze ist so konzipiert, dass es eine Vielzahl von Anpassungsmöglichkeiten bietet, die auf Ihre speziellen Anforderungen zugeschnitten werden können.

Lassen Sie uns gemeinsam die Macht von Braze entdecken.

## So funktioniert Braze

Braze ist eine Plattform zur Kundenbindung, die Marken jeder Größe dabei hilft, personalisierte und gezielte Kampagnen über verschiedene Kanäle zu erstellen. Braze gibt Ihnen die Möglichkeit, Ihren Kunden zuzuhören, zu verstehen, was ihr Verhalten signalisiert, und dann zu handeln, indem Sie Ihren Kunden die richtige Nachricht über den richtigen Kanal und zur richtigen Zeit schicken.

{% alert tip %}
Stellen Sie sicher, dass Sie [Ihre Kollegen zu Braze hinzufügen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users), damit sie die Plattform gemeinsam mit Ihnen erkunden können.
{% endalert %}

## Benutzer und Segmente

Benutzer sind Ihre Kunden - die Personen, die die Nachrichten erhalten, die Sie mit Braze versenden. Alle Daten, die Sie über einen Benutzer sammeln und in Braze aufnehmen, werden in dessen Benutzerprofil gespeichert, z. B. demografische Daten, persönliche Informationen, Vorlieben und Verhaltensweisen. Diese Informationen sind die Grundlage für Ihre Nachrichten und ermöglichen es Ihnen, Ihre Nachrichten auf den richtigen Nutzer zuzuschneiden.

![]({% image_buster /assets/img/getting_started/user_profile.png %})

Segmente unterteilen Ihren Kundenstamm in kleinere Gruppen, die Sie dann mit spezifischem Messaging ansprechen können. Sie können verschiedene Variablen verwenden, um Segmente zu erstellen. Diese reichen von Merkmalen wie Geschlecht, Standort und Alter bis hin zu Verhaltensweisen wie Interaktionsmustern mit früheren Kampagnen oder der Position auf der Customer Journey.

Segmente sind dynamisch - Nutzer:innen können sich in Realtime in Segmente ein- und ausgliedern, je nachdem, wie sie sich verhalten und wo sie in Bezug auf Ihre Marke stehen. So können Sie sicherstellen, dass Ihre Kunden immer die für sie relevanten Nachrichten erhalten. Sie können so viele Segmente erstellen, wie Sie für Ihr Targeting und Messaging benötigen.

![]({% image_buster /assets/img/getting_started/segment.png %})

Mehr dazu finden Sie hier: [Erste Schritte: Benutzer und Segmente]({{site.baseurl}}/user_guide/getting_started/users_segments/).

## Kampagnen und Canvase

Mit Kampagnen und Canvases senden Sie Nachrichten an Ihre Nutzer.

Kampagnen eignen sich am besten für einzelne Nachrichten, die über verschiedene Kanäle an ein bestimmtes Zielgruppensegment gesendet werden. Sie können jeden unserer unterstützten Messaging-Kanäle in Ihrer Kampagne nutzen (E-Mail, Push, In-App-Nachrichten, SMS und mehr).

Canvases sind fortschrittliche Kampagnen-Workflows, mit denen Sie personalisierte Customer Journeys über mehrere Kanäle hinweg automatisieren und orchestrieren können. Innerhalb eines Canvas können Sie Verzweigungslogiken, Verzögerungen, Entscheidungspunkte und Konversions-Events einrichten, um Kund:innen durch eine Reihe von Interaktionen zu führen. Canvase sorgen für eine konsistente und nahtlose Kommunikation über verschiedene Touchpoints hinweg und erhöhen so die Chancen auf Customer-Engagement und Konversion. 

Mehr dazu finden Sie hier: [Erste Schritte: Kampagnen und Leinwände]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

## Workspaces

Arbeitsbereiche fassen Ihre Daten - Benutzer, Segmente, Kampagnen und Canvases - an einem Ort zusammen. Informationen werden nicht zwischen Workspaces ausgetauscht. Denken Sie also daran, wenn Sie Websites und Apps zu Ihren Workspaces hinzufügen. Es empfiehlt sich, verschiedene Versionen derselben oder sehr ähnlicher Apps nur in einem Workspace zusammenzufassen.

Beispiele für die Verwendung von Workspaces sind:

- Verschiedene Produktlinien oder Anwendungen
- Unterschiedliche Zielgruppen (z. B. Lieferfahrer und Kunden)
- Getrennte Geschäfte
- Testumgebung

Mehr dazu finden Sie hier: [Erste Schritte: Workspaces]({{site.baseurl}}/user_guide/getting_started/workspaces/).

## Integration von Braze

Braze ist so konzipiert, dass Sie es schnell und einfach in Betrieb nehmen können. Unsere durchschnittliche Time-to-Value beträgt sechs Wochen bei unserem Kundenstamm von Hunderten von Marken.

![]({% image_buster /assets/img/getting_started/timetovalue.png %})

Hier ist das Braze-Rahmenwerk, mit dem Sie die Dauer Ihrer Integration anhand von vier Komponenten, an denen Sie parallel arbeiten können, abschätzen können. Die typische Spanne liegt zwischen 30 und 180 Tagen, wobei die meisten Kund:innen ihre Integration innerhalb von 45 bis 60 Tagen abschließen.

- **Komplexitätsgrad der Migration von Kampagnen:** Die Zeit, die Sie für die Migration von Kampagnen benötigen, hängt davon ab, wie viele Sie haben, wie personalisiert sie sind und welche Ressourcen Sie haben. Wenn Sie weniger als zehn Kampagnen zu migrieren haben, dauert die Migration weniger als 60 Tage. Aber wenn Sie mehr als 100 Kampagnen haben, wird es etwas komplizierter. Wenn nur eine Person 100 Kampagnen migriert, ist das etwas anderes als wenn 10 Personen 100 migrieren.

{% alert tip %}
Benötigen Sie Hilfe bei Ihrer Migration? Unsere [zertifizierten Braze-Partner](https://www.braze.com/partners/solutions-partners) können Ihnen helfen!
{% endalert %}

- **E-Mail-Volumen:** Um E-Mails zu versenden, müssen Sie Ihre IPs aufwärmen. [IP-Warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) ist der Prozess des Aufbaus einer Absender-Reputation mit Ihren neu zugewiesenen IP-Adressen. Wenn Sie weniger als 2-3 Millionen E-Mails pro Tag versenden, sollte Ihr IP-Warming 30 Tage oder weniger dauern. Denken Sie daran, Ihre Spitzenwerte zu senden. Wenn Sie normalerweise 2 Millionen E-Mails pro Tag verschicken, aber für einen saisonalen Zeitraum den Versand von 7 Millionen E-Mails planen, sollten Sie sich auf diese "Spitze" einstellen. Absender mit hohem Datenaufkommen können mehrere IPs verwenden, um den Erwärmungsprozess zu beschleunigen.
- **Organisatorische Komplexität:** Unser Onboarding-Prozess kann an die Bedürfnisse Ihres Unternehmens angepasst werden. Ganz gleich, ob Sie eine einzelne Geschäftseinheit, ein Center of Excellence, mehrere unabhängige Einheiten oder Agenturen zur Verstärkung Ihrer Teams einsetzen, Braze hat Erfahrung mit allen Szenarien.
- **Ausgereifte Dateninfrastruktur:** Wenn Sie nur das Braze SDK implementieren oder bereits über eine Customer Data Platform (CDP) verfügen, ist es möglich, alles in nur 30 Tagen einzurichten. Die Verwendung einer modernen CDP kann den Prozess beschleunigen. Wenn Sie jedoch viele Backend-Systeme, -Tools oder -Datenbanken mit Braze verbinden möchten, kann es länger dauern und Sie benötigen mehr Ressourcen, um die Einrichtung abzuschließen.

Mehr dazu finden Sie hier: [Erste Schritte: Übersicht über die Integration]({{site.baseurl}}/user_guide/getting_started/integration/).

