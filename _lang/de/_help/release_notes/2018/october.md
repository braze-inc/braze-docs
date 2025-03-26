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
  Intelligente Auswahl Kontrollgruppe Toggle
  Das Feld Intelligente Auswahl verfügt jetzt über ein Kontrollkästchen, mit dem Sie [die Verwendung einer Kontrollgruppe ein- oder ausschalten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#including-a-control-group) können. Wenn diese Funktion aktiviert ist, beträgt die Kontrollgruppe 20% der Zuschauerzahl und ändert sich, wenn die Funktion Intelligente Auswahl die Zuschauerzahlen pro Variante optimiert.
  Assistent für Canvas-Einstellungen (Beta)
  Die Canvas-Benutzeroberfläche wird vereinfacht, um verpasste Aufgaben und daraus resultierende Fehler zu vermeiden. Die Canvas-Konfigurationen werden jetzt in einem Assistenten angezeigt, der dem Kampagnen-Assistenten ähnelt. Dies wird derzeit in unserer Dokumentation noch nicht berücksichtigt, da es schrittweise eingeführt wird. Lesen Sie bald mehr darüber!
  Abonnementgruppen-API (versteckt)
  Braze hat einen neuen GET-Aufruf zur Verfügung gestellt, mit dem Sie eine Anfrage auf der Grundlage einer externen ID oder E-Mail-Adresse stellen können. Sie erhalten dann alle Abonnementgruppen, die mit diesem Benutzer verbunden sind.
{% endcomment %}

## Berechnen Sie genaue Zielgruppenstatistiken für Kampagnen

Sie können nun zu **Campaign Analytics** gehen und die genauen Statistiken für Ihr Publikum berechnen. Klicken Sie in der Fußzeile des Abschnitts **Zielbenutzer** auf **Genaue Statistiken berechnen**, und die genauen Zielgruppenstatistiken werden eingeblendet. Sie müssen die Kampagne vor dem Berechnen speichern (Kampagnenentwürfe werden als Entwürfe gespeichert).

## Veraltung von Windows 8

Braze unterstützt Windows 8 seit dem 10\. Oktober 2018 nicht mehr.

## Drehscheibe für Partnerschaften

Sie finden jetzt eine Liste Ihrer Integrationen auf der Braze-Plattform unter **Integrationen**, zusammen mit den Integrationsschlüsseln und Anweisungen.

## Berechnungen zur E-Mail-Analyse

Braze berechnet jetzt alle E-Mail-Analysen anhand der Ereignisdaten unseres E-Mail-Versandpartners (ESP), um die Genauigkeit unserer E-Mail-Analysen erheblich zu verbessern. Diese Lösung verwendet Postgres, eine Open-Source-Datenbanklösung, um die Datenintegrität zu gewährleisten.

{% alert important %}
Unique Opens und Unique Clicks sind derzeit noch von den aggregierten Daten abhängig, die von unseren E-Mail-Versandpartnern bereitgestellt werden. Es wird daran gearbeitet, diese Einzigartigkeitsstatistiken mit der gleichen Infrastruktur zu berechnen, die in dieser Version eingeführt wurde.
{% endalert %}

## Bedienelemente des Composer-Panels

Die Steuerelemente des Message Composers wurden überarbeitet und enthalten nun einen Text, der mit den Symbolen verknüpft ist, um eine bessere Benutzerfreundlichkeit und Navigation zu ermöglichen.

## Azurblau für Ströme

Braze-Kunden, die Currents verwenden, können jetzt [Azure]({{site.baseurl}}/partners/braze_currents/data_storage_integrations/partners/microsoft_azure_blob_storage/) als mögliche Integration sehen.

## Eingabefeld-Erweiterungen

Sie können jetzt die Eingabefelder für E-Mail-Betreffzeilen und Push-Titel erweitern.
