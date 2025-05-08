---
page_order: 4.3
nav_title: SDK-Fehlersuche
article_title: Fehlersuche im Braze SDK 
description: "Erfahren Sie, wie Sie den Braze SDK-Debugger verwenden, damit Sie Fehlerbehebungen für Ihre SDK-gesteuerten Kanäle vornehmen können, ohne die ausführliche Protokollierung in Ihrer App manuell zu aktivieren."
---

# Fehlersuche im Braze SDK

> Lernen Sie, wie Sie den integrierten Debugger des Braze SDK verwenden, damit Sie Fehlerbehebungen für Ihre SDK-gestützten Kanäle durchführen können, ohne die ausführliche Protokollierung in Ihrer App aktivieren zu müssen.

## Voraussetzungen

Um den Braze SDK Debugger zu verwenden, benötigen Sie die Berechtigungen `View PII` und `Export User Data`. Außerdem muss Ihr Braze SDK die folgenden Mindestversionen erfüllen oder auf diese verweisen: 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Fehlersuche im Braze SDK

{% alert tip %}
Um das Debugging für das Braze Web SDK zu aktivieren, können Sie [einen URL-Parameter verwenden]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).
{% endalert %}

### Schritt 1: Schließen Sie Ihre App

Bevor Sie mit der Fehlersuche beginnen, schließen Sie die App, bei der gerade ein Problem auftritt. Sie können die App zu Beginn Ihrer Sitzung neu starten.

### Schritt 2: Erstellen Sie eine Debugging-Sitzung

Gehen Sie in Braze zu **Einstellungen** und wählen Sie dann unter **Einrichtung und Testen** **SDK Debugger** aus.

![Der Abschnitt "Einrichten und Tests" mit "SDK Debugger" hervorgehoben.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Wählen Sie **Debugging-Sitzung erstellen**.

![Die Seite "SDK Debugger".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Schritt 3: Wählen Sie einen Nutzer aus

Suchen Sie nach einem Nutzer über die E-Mail Adresse, `external_id`, Nutzer-Alias oder Push-Token. Wenn Sie bereit sind, Ihre Sitzung zu starten, wählen Sie **Nutzer auswählen**.

![Die Debugging-Seite für den ausgewählten Nutzer:innen.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Schritt 4: App neu starten

Starten Sie zunächst die App und bestätigen Sie, dass Ihr Gerät gekoppelt ist. Wenn das Pairing erfolgreich war, starten Sie Ihre App neu. So stellen Sie sicher, dass die Initialisierungsprotokolle der App vollständig erfasst werden.

### Schritt 5: Schließen Sie die Reproduktionsschritte ab

Nachdem Sie Ihre App neu gestartet haben, folgen Sie den Schritten, um den Fehler zu reproduzieren.

{% alert tip %}
Achten Sie bei der Reproduktion des Fehlers darauf, dass Sie die Reproduktionsschritte so genau wie möglich befolgen, damit Sie [hochwertige Protokolle](#step-6-export-your-session-logs-optional) erstellen können.
{% endalert %}

### Schritt 6: Beenden Sie die Sitzung

Wenn Sie mit Ihren Reproduktionsschritten fertig sind, wählen Sie **Sitzung beenden** > **Schließen**.

![Die Debugging-Sitzung zeigt den Button "Sitzung beenden" an.]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Es kann einige Minuten dauern, bis die Protokolle erstellt sind, je nach Länge der Sitzung und der Qualität der Netzwerkverbindung.
{% endalert %}

### Schritt 7: Teilen oder exportieren Sie die Sitzung (optional)

Nach der Sitzung können Sie Ihre Sitzungsprotokolle als CSV-Datei exportieren. Außerdem können andere Personen Ihre **Sitzungs-ID** verwenden, um nach Ihrer Debug-Sitzung zu suchen, sodass Sie ihnen Ihre Protokolle nicht direkt schicken müssen.

![Die Debugging-Seite mit "Protokolle exportieren" und "Sitzungs-ID kopieren" wird nach der Sitzung angezeigt.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})
