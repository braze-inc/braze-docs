---
nav_title: Erste Schritte
article_title: Beginnen Sie mit Braze Pilot
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt die erforderlichen Integrationsschritte für Ihre Entwicklerabteilung."
---

# Beginnen Sie mit Braze Pilot

> Dieser Artikel beschreibt, wie Sie mit Braze Pilot beginnen können. Hier führen wir Sie durch den Download der App, die Initialisierung der Verbindung mit Ihrem Braze-Dashboard und den Abschluss der Einrichtung.

## Schritt 1: Braze Pilot herunterladen

Um Braze Pilot nutzen zu können, müssen Sie zunächst die App entweder aus dem Apple App Store oder dem Google Play Store herunterladen. Sie können die App im App Store suchen oder die untenstehenden QR-Codes scannen, um die App-Seite für Ihr Gerät aufzurufen.

## Schritt 2: Bitte akzeptieren Sie die Allgemeinen Geschäftsbedingungen.

Akzeptieren Sie anschließend die Allgemeinen Geschäftsbedingungen und geben Sie Ihre geschäftliche E-Mail-Adresse in das Formular ein. Ihre E-Mail-Adresse wird ausschließlich für Analytics zur Analyse der App-Nutzung verwendet und nicht für Marketingzwecke genutzt.

![Willkommensseite von Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Bitte geben Sie Ihre geschäftliche E-Mail-Adresse ein.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Schritt 3: Initialisieren Sie die Verbindung mit dem Braze SDK.

Mit Braze Pilot können Sie das Braze SDK für jedes Braze-Dashboard initialisieren. Sobald das SDK initialisiert ist, beginnt Pilot mit der Übermittlung von Engagement-Daten an Braze und ermöglicht es Ihnen, alle Nachrichten zu versenden, die über das Braze-Dashboard gestartet werden.

Es gibt zwei Methoden zur Konfiguration der SDK-Verbindung in Pilot: Demo-QR-Codes und der Einrichtungsassistent.

{% tabs local %}
{% tab Demo QR codes %}

### Methode 1: Demo-QR-Codes

Bitte scannen Sie den QR-Code, der alle erforderlichen Details zur Initialisierung des SDK enthält, erstellen Sie Ihr Nutzerprofil und setzen Sie Deeplinks zu einer bestimmten App-Simulation in Braze Pilot. Demo-QR-Codes werden in der Begleitleiste für bestimmte Demo-Kampagnen in Ihrer kostenlosen Demo angezeigt.

| Pilot für Android | Pilot für iOS |
| --- | --- |
| ![QR-Code für Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![QR-Code für iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Methode 2: Einrichtungsassistent

Bitte befolgen Sie die Schritt-für-Schritt-Anleitung zur Initialisierung der Verbindung mit Ihrem Dashboard-Workspace auf der Seite **„App-Einstellungen“** in Ihrem Braze-Dashboard.

![Schritt 1 des Einrichtungsassistenten für Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Diese Verbindung ist Workspace-spezifisch. Dies bedeutet, dass Sie, wenn Sie die Verbindung vom Demo-Workspace aus initialisieren und dann in Ihrem kostenlosen Demo-Dashboard zum Live-Workspace wechseln, das SDK von diesem Workspace aus neu initialisieren müssen, um dort gestartete Kampagnen zu empfangen.

![Das Dropdown-Menü „Workspace“ im Braze-Dashboard mit „Demo – Braze“ als ausgewähltem aktiven Workspace.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Schritt 4: Push-Berechtigungen zulässig machen

Abschließend wird empfohlen, der App die Berechtigung zum Senden von Push-Benachrichtigungen zu erteilen, falls Sie die Push-Funktionen über die App testen möchten. Sie können der App diese Berechtigungen auf folgende Weise erteilen: Aktualisieren Sie die Einstellungen für die App in Ihren Gerätseinstellungen oder senden Sie eine Push-Nachricht von Braze an die App.

{% tabs local %}
{% tab Update the settings for the app %}

Öffnen Sie bitte die Einstellungen Ihres Geräts und suchen Sie nach Braze Pilot. Aktualisieren Sie anschließend die Einstellungen, damit Benachrichtigungen auf Ihrem Sperrbildschirm zulässig sind.

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

Sie können eine Braze-In-App-Nachricht verwenden, um Push-Berechtigungen für die App anzufordern, genau wie Sie es für Ihre eigenen Verbraucher:innen tun würden. Informationen zum Erstellen dieser Art von Nachrichten in Braze finden Sie unter [„Einführung in Push-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages)“.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Schritt 5: Erleben Sie Braze Messaging in Pilot

Nun sind Sie bereit, als Nutzer:in von Braze Pilot Kampagnen und Canvases über Ihr Braze-Dashboard zu empfangen. Besuchen Sie eine der gestarteten Kampagnen in Ihrem Demo-Workspace, um eine kurze Demonstration der Anwendungsfälle von Braze zu erhalten. Wechseln Sie anschließend zu Ihrem Live-Workspace, um mit dem Versand Ihrer eigenen Kampagnen zu beginnen.

Weitere Informationen zum Einrichten von Kampagnen und Canvases in Braze finden Sie unter [Erste Schritte: Kampagnen und Leinwände]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).