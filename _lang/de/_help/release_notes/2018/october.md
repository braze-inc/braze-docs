---
nav_title: Oktober
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Oktober 2018."
---
# Oktober 2018

{% comment %}
  Fügen Sie diese zu einem späteren Zeitpunkt hinzu...
  Intelligente Auswahl Kontrollgruppe umschalten
  Das Feld Intelligente Auswahl verfügt jetzt über ein Kontrollkästchen, mit dem Sie [die Verwendung einer Kontrollgruppe ein- oder ausschalten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#including-a-control-group) können. Wenn diese Funktion aktiviert ist, beträgt die Kontrollgruppe 20% der Zielgruppe und ändert sich, wenn das Feature Intelligente Auswahl die Zielgruppengrößen pro Variante optimiert.
  Assistent für Canvas-Eingangseinstellungen (Beta)
  Das Canvas UI wird vereinfacht, um verpasste Aufgaben und daraus resultierende Fehler zu vermeiden. Die Canvas-Konfigurationen werden jetzt in einem Assistenten angezeigt, der dem Design des Assistenten für Kampagnen ähnelt. Dies spiegelt sich derzeit noch nicht in unserer Dokumentation wider, da es schrittweise eingeführt wird. Lesen Sie bald mehr darüber!
  Abo-Gruppe API (ausgeblendet)
  Braze hat einen neuen GET-Aufruf zur Verfügung gestellt, der es Ihnen ermöglicht, eine Anfrage auf der Grundlage einer externen ID oder E-Mail zu stellen. Sie erhalten dann alle Abo-Gruppen, die mit diesem Nutzer:innen verbunden sind.
{% endcomment %}

## Berechnen Sie genaue Statistiken über Zielgruppen für Kampagnen

Sie können jetzt zu **Campaign Analytics** gehen und die genauen Statistiken für Ihre Zielgruppe berechnen. Klicken Sie in der Fußzeile des Abschnitts **Targeting** auf **Exakte Statistiken berechnen**, und die genauen Statistiken für die Zielgruppe werden angezeigt. Sie müssen die Kampagne vor dem Berechnen speichern (Kampagnenentwürfe werden als Entwürfe gespeichert).

## Veraltung von Windows 8

Braze unterstützt Windows 8 seit dem 10\. Oktober 2018 nicht mehr.

## Drehscheibe für Partnerschaften

Sie finden jetzt eine Liste Ihrer Integrationen auf der Braze Plattform unter **Integrationen**, zusammen mit den Integrationsschlüsseln und Anweisungen.

## E-Mail Analytics Berechnungen

Braze berechnet jetzt alle E-Mail-Analysen anhand der Ereignisdaten unseres Partners für den E-Mail-Versand (ESP), um die Genauigkeit unserer Analytics deutlich zu verbessern. Diese Lösung nutzt Postgres, eine Open Source-Datenbanklösung, um die Integrität der Daten zu gewährleisten.

{% alert important %}
Eindeutige Öffnungen und eindeutige Klicks hängen derzeit noch von den aggregierten Daten ab, die von unseren Partnern für den Versand von E-Mails bereitgestellt werden. Es wird daran gearbeitet, diese eindeutigen Statistiken mit der gleichen Infrastruktur zu berechnen, die in dieser Version eingeführt wurde.
{% endalert %}

## Bedienelemente des Composer Panels

Die Steuerelemente des Nachrichten-Editors wurden aufgefrischt und enthalten nun einen Text, der mit den Symbolen verknüpft ist, um eine bessere Benutzerfreundlichkeit und Navigation zu ermöglichen.

## Azure für Currents

Braze-Kunden, die Currents verwenden, können [Azure]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents#microsoft-azure-blob-storage) jetzt als eine mögliche Integration betrachten.

## Eingabefeld-Erweiterungen

Sie können jetzt die Eingabefelder für E-Mail Betreffzeilen und Push-Titel erweitern.
