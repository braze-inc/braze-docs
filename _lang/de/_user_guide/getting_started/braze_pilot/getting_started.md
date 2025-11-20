---
nav_title: Erste Schritte
article_title: Erste Schritte mit Braze Pilot
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt die erforderlichen Integrationsschritte für Ihre Entwicklerabteilung."
---

# Erste Schritte mit Braze Pilot

> In diesem Artikel erfahren Sie, wie Sie mit Braze Pilot beginnen können. Hier führen wir Sie durch den Download der App, die Initialisierung der Verbindung mit Ihrem Braze-Dashboard und den Abschluss der Einrichtung.

## Schritt 1: Braze Pilot herunterladen

Um Braze Pilot nutzen zu können, müssen Sie zunächst die App entweder aus dem Apple App Store oder dem Google Play Store herunterladen. Sie können im App Shop nach der App suchen oder die QR-Codes unten scannen, um die App-Seite für Ihr Gerät aufzurufen.

## Schritt 2: Akzeptieren Sie die Bedingungen und Konditionen

Akzeptieren Sie dann die Allgemeinen Geschäftsbedingungen und geben Sie Ihre E-Mail in das Formular ein. Ihre E-Mail wird nur für Analytics der App-Nutzung und nicht für Marketingzwecke verwendet.

![Braze Pilot Willkommensseite.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"}![Option zur Eingabe Ihrer beruflichen E-Mail Adresse.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Schritt 3: Initialisieren Sie die Verbindung mit dem Braze SDK

Braze Pilot ermöglicht Ihnen die Initialisierung des Braze SDK für jedes Braze-Dashboard. Sobald das SDK initialisiert ist, beginnt Pilot damit, Engagement-Daten an Braze zu senden und erlaubt es Ihnen, jedes Messaging zu triggern, das von diesem Braze-Dashboard aus gestartet wird.

Es gibt zwei Methoden, um die SDK-Verbindung in Pilot zu konfigurieren: Demo QR-Codes und der Einrichtungsassistent.

{% tabs local %}
{% tab Demo QR codes %}

### Methode 1: Demo QR-Codes

Scannen Sie einen QR Code, der alle Details enthält, die zur Initialisierung des SDK, zur Erstellung Ihres Nutzerprofils und zum Setzen von Deeplinks zu einer bestimmten App-Simulation in Braze Pilot erforderlich sind. Demo QR-Codes werden in der Schublade für bestimmte Demo Kampagnen in Ihrer kostenlosen Testversion angezeigt.

| Pilot für Android | Pilot für iOS |
| --- | --- |
| ![QR-Code für Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![QR-Code für iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Methode 2: Einrichtungsassistent

Folgen Sie der Schritt-für-Schritt-Anleitung für die Initialisierung der Verbindung mit Ihrem Dashboard Workspace auf der Seite **App-Einstellungen** in Ihrem Braze-Dashboard.

![Schritt 1 des Einrichtungsassistenten für Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Diese Verbindung ist workspace-spezifisch. Das bedeutet, dass Sie, wenn Sie die Verbindung vom Demo Workspace aus initialisieren und dann zum Live Workspace in Ihrem kostenlosen Demo Dashboard wechseln, das SDK von diesem Workspace aus neu initialisieren müssen, um alle dort gestarteten Kampagnen zu empfangen.

![Das Workspace-Dropdown im Braze-Dashboard, wobei "Demo - Braze" als aktiver Workspace ausgewählt ist.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Schritt 4: Push-Berechtigungen zulassen

Schließlich sollten Sie der App erlauben, Ihnen Push-Berechtigungen zu senden, wenn Sie die Push-Funktionen über die App testen möchten. Sie können der App diese Berechtigungen auf folgende Weise erteilen: durch ein Update der Einstellungen für die App in den Einstellungen Ihres Geräts oder durch das Starten einer Push-Primer-Nachricht von Braze an die App.

{% tabs local %}
{% tab Update the settings for the app %}

Öffnen Sie die Einstellungen Ihres Geräts und suchen Sie Braze Pilot. Aktualisieren Sie dann die Einstellungen, um die Anzeige von Benachrichtigungen auf Ihrem Sperrbildschirm zuzulassen.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Launch a push primer message %}

Sie können eine In-App-Nachricht von Braze verwenden, um Push-Berechtigungen für die App anzufordern, genau wie bei Ihren eigenen Verbrauchern. Wie Sie diese Art von Nachrichten in Braze erstellen können, erfahren Sie unter [Push-Primer In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Schritt 5: Erleben Sie Braze Messaging in Pilot

Jetzt können Sie als Nutzer:in von Braze Pilot Kampagnen und Canvase über Ihr Braze-Dashboard empfangen! Besuchen Sie eine der eingeführten Kampagnen in Ihrem Workspace, um eine kurze Demo der Anwendungsfälle von Braze zu erhalten, und gehen Sie dann zu Ihrem Live-Workspace, um mit dem Senden Ihrer eigenen Kampagne zu beginnen.

Wie Sie Kampagnen und Canvase in Braze einrichten, erfahren Sie unter [Erste Schritte: Kampagnen und Leinwände]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).