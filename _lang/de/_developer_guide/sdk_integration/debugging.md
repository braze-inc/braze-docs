---
page_order: 1.3
nav_title: Fehlersuche
article_title: Fehlersuche im Braze SDK 
description: "Erfahren Sie, wie Sie den Braze SDK-Debugger verwenden, damit Sie Probleme in Ihren SDK-gestützten Kanälen beheben können, ohne die ausführliche Protokollierung in Ihrer App manuell aktivieren zu müssen."
---

# Fehlersuche im Braze SDK

> Erfahren Sie, wie Sie den integrierten Debugger des Braze SDK verwenden, damit Sie Probleme in Ihren SDK-gestützten Kanälen beheben können, ohne die ausführliche Protokollierung in Ihrer App aktivieren zu müssen.

{% alert tip %}
Für eine eingehendere Untersuchung können Sie auch [die ausführliche Protokollierung aktivieren]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), um detaillierte SDK-Ausgaben zu erfassen, und [erfahren, wie Sie ausführliche Protokolle lesen]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) – für bestimmte Kanäle.
{% endalert %}

## Voraussetzungen

Um den Braze SDK-Debugger nutzen zu können, benötigen Sie die granularen Berechtigungen „View PII" und „View User Profiles (PII Redacted)" (oder die Legacy-Berechtigung „View User Profiles PII Compliant"). Um Ihre Debugging-Sitzungsprotokolle herunterzuladen, benötigen Sie außerdem die Berechtigung „Export User Data". Darüber hinaus muss Ihr Braze SDK die folgenden Mindestversionen erfüllen oder darauf verweisen: 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Fehlersuche im Braze SDK

{% alert tip %}
Um das Debugging für das Braze Web SDK zu aktivieren, können Sie [einen URL-Parameter verwenden]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).
{% endalert %}

### 1. Schritt: Schließen Sie Ihre App

Bevor Sie mit der Fehlersuche beginnen, schließen Sie die App, bei der gerade ein Problem auftritt. Sie können die App zu Beginn Ihrer Sitzung neu starten.

### 2. Schritt: Erstellen Sie eine Debugging-Sitzung

Gehen Sie in Braze zu **Einstellungen** und wählen Sie dann unter **Einrichtung und Testen** die Option **SDK Debugger** aus.

![Der Abschnitt „Einrichtung und Testen" mit hervorgehobenem „SDK Debugger".]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Wählen Sie **Debugging-Sitzung erstellen**.

![Die Seite „SDK Debugger".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### 3. Schritt: Nutzer:in auswählen

Suchen Sie nach einer Nutzer:in anhand der E-Mail-Adresse, `external_id`, des Nutzer-Alias oder des Push-Tokens. Wenn Sie bereit sind, Ihre Sitzung zu starten, wählen Sie **Nutzer:in auswählen**.

![Die Debugging-Seite für die ausgewählte Nutzer:in.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### 4. Schritt: App neu starten

Starten Sie zunächst die App und bestätigen Sie, dass Ihr Gerät gekoppelt ist. Wenn die Kopplung erfolgreich war, starten Sie Ihre App neu&#8212;so stellen Sie sicher, dass die Initialisierungsprotokolle der App vollständig erfasst werden.

### 5. Schritt: Führen Sie die Reproduktionsschritte durch

Nachdem Sie Ihre App neu gestartet haben, folgen Sie den Schritten, um den Fehler zu reproduzieren.

{% alert tip %}
Achten Sie bei der Reproduktion des Fehlers darauf, die Reproduktionsschritte so genau wie möglich zu befolgen, damit Sie [hochwertige Protokolle](#step-6-export-your-session-logs-optional) erstellen können.
{% endalert %}

### 6. Schritt: Beenden Sie die Sitzung

Wenn Sie mit Ihren Reproduktionsschritten fertig sind, wählen Sie **Sitzung beenden** > **Schließen**.

![Die Debugging-Sitzung mit dem Button „Sitzung beenden".]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Es kann einige Minuten dauern, bis die Protokolle generiert sind – je nach Länge der Sitzung und der Qualität der Netzwerkverbindung.
{% endalert %}

### 7. Schritt: Sitzung teilen oder exportieren (optional)

Nach der Sitzung können Sie Ihre Sitzungsprotokolle als CSV-Datei exportieren. Außerdem können andere Personen Ihre **Sitzungs-ID** verwenden, um nach Ihrer Debug-Sitzung zu suchen, sodass Sie ihnen Ihre Protokolle nicht direkt senden müssen.

![Die Debugging-Seite mit den Optionen „Protokolle exportieren" und „Sitzungs-ID kopieren", die nach der Sitzung angezeigt werden.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})