---
nav_title: Andere SDK-Anpassungen
article_title: Andere SDK-Anpassungen für Android und FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel behandelt zusätzliche Anpassungs- und Konfigurationsoptionen wie die ausführliche Protokollierung, die Unterdrückung der Protokollierung und die Implementierung mehrerer API-Schlüssel."

---

# Andere SDK-Anpassungen für Android und FireOS

> Dieser Referenzartikel behandelt zusätzliche Anpassungs- und Konfigurationsoptionen wie die ausführliche Protokollierung, die Unterdrückung der Protokollierung und die Implementierung mehrerer API-Schlüssel.

## Verwendung von R8/ProGuard mit Braze

Die [Codeshrinking](https://developer.android.com/studio/build/shrink-code)-Konfiguration ist automatisch in Ihrer Braze Integration enthalten.

Client-Apps, die den Braze-Code verschleiern, müssen Release-Mapping-Dateien speichern, damit Braze die Stack-Traces interpretieren kann. Wenn Sie den gesamten Braze-Code beibehalten möchten, fügen Sie Folgendes in Ihre ProGuard-Datei ein:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## Protokollieren

Standardmäßig ist der Braze Android SDK Loglevel auf `INFO` eingestellt. Sie können [diese Protokolle unterdrücken](#suppressing-logs) oder [eine andere Protokollstufe einstellen](#enabling-logs), z. B. `VERBOSE`, `DEBUG` oder `WARN`.

### Protokolle aktivieren{#enabling-logs}

Um die Fehlerbehebung in Ihrer App zu erleichtern oder die Bearbeitungszeit beim Braze Support zu verkürzen, sollten Sie ausführliche Protokolle für das SDK aktivieren. Wenn Sie ausführliche Protokolle an den Braze-Support senden, stellen Sie sicher, dass diese beginnen, sobald Sie Ihre Anwendung starten und weit nach dem Auftreten des Problems enden.

Denken Sie daran, dass ausführliche Protokolle nur für Ihre Entwicklungsumgebung gedacht sind. Sie sollten sie also deaktivieren, bevor Sie Ihre App veröffentlichen.

{% alert important %}
Aktivieren Sie ausführliche Protokolle vor allen anderen Aufrufen in `Application.onCreate()`, um sicherzustellen, dass Ihre Protokolle so vollständig wie möglich sind.
{% endalert %}

{% tabs %}
{% tab Anwendung %}
Um Protokolle direkt in Ihrer App zu aktivieren, fügen Sie der Methode `onCreate()` Ihrer Anwendung vor allen anderen Methoden Folgendes hinzu.

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Ersetzen Sie `MIN_LOG_LEVEL` durch die **Konstante** der Protokollstufe, die Sie als minimale Protokollstufe festlegen möchten. Alle Protokolle auf der Ebene `>=`, die Sie unter `MIN_LOG_LEVEL` eingestellt haben, werden an die standardmäßige [`Log`](https://developer.android.com/reference/android/util/Log)-Methode in Android weitergeleitet. Alle Protokolle `<` Ihrer Einstellung `MIN_LOG_LEVEL` werden verworfen.

| Konstant    | Wert          | Beschreibung                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | (2 %)              | Protokolliert die detailliertesten Nachrichten zur Fehlersuche und Entwicklung.            |
| `DEBUG`     | 3              | Protokolliert beschreibende Nachrichten zur Fehlersuche und Entwicklung.                  |
| `INFO`      | (4 %)              | Protokolliert informative Nachrichten für allgemeine Highlights.                       |
| `WARN`      | (5 %)              | Protokolliert Nachrichten mit Warnungen zur Identifizierung potenziell schädlicher Situationen.     |
| `ERROR`     | 6              | Protokolliert Fehlermeldungen, die auf Anwendungsfehler oder schwerwiegende Probleme hinweisen. |
| `ASSERT`    | (7 %)              | Protokolliert Messaging-Nachrichten, wenn Bedingungen während der Entwicklung falsch sind.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Der folgende Code leitet zum Beispiel die Protokollstufen `2`, `3`, `4`, `5`, `6` und `7` an die Methode `Log` weiter.

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab braze.xml %}
Um Protokolle in `braze.xml` zu aktivieren, fügen Sie Folgendes zu Ihrer Datei hinzu:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Ersetzen Sie `MIN_LOG_LEVEL` durch den **Wert** der Protokollstufe, die Sie als minimale Protokollstufe festlegen möchten. Alle Protokolle auf der Ebene `>=`, die Sie unter `MIN_LOG_LEVEL` eingestellt haben, werden an die standardmäßige [`Log`](https://developer.android.com/reference/android/util/Log)-Methode in Android weitergeleitet. Alle Protokolle `<` Ihrer Einstellung `MIN_LOG_LEVEL` werden verworfen.

| Konstant    | Wert          | Beschreibung                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | (2 %)              | Protokolliert die detailliertesten Nachrichten zur Fehlersuche und Entwicklung.            |
| `DEBUG`     | 3              | Protokolliert beschreibende Nachrichten zur Fehlersuche und Entwicklung.                  |
| `INFO`      | (4 %)              | Protokolliert informative Nachrichten für allgemeine Highlights.                       |
| `WARN`      | (5 %)              | Protokolliert Nachrichten mit Warnungen zur Identifizierung potenziell schädlicher Situationen.     |
| `ERROR`     | 6              | Protokolliert Fehlermeldungen, die auf Anwendungsfehler oder schwerwiegende Probleme hinweisen. |
| `ASSERT`    | (7 %)              | Protokolliert Messaging-Nachrichten, wenn Bedingungen während der Entwicklung falsch sind.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Der folgende Code leitet zum Beispiel die Protokollstufen `2`, `3`, `4`, `5`, `6` und `7` an die Methode `Log` weiter.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

### Überprüfen von ausführlichen Protokollen

Um zu überprüfen, ob Ihre Protokolle auf `VERBOSE` eingestellt sind, prüfen Sie, ob `V/Braze` irgendwo in Ihren Protokollen vorkommt. Wenn dies der Fall ist, dann sind die ausführlichen Protokolle aktiviert. Zum Beispiel:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

### Protokolle unterdrücken

Die Standard-Protokollstufe für das Braze Android SDK ist `INFO`. Um alle Protokolle für das Braze Android SDK zu unterdrücken, rufen Sie `BrazeLogger.SUPPRESS` in der Methode `onCreate()` Ihrer Anwendung auf, und zwar _vor_ allen anderen Methoden.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

## Mehrere API-Schlüssel

Der häufigste Anwendungsfall für mehrere API-Schlüssel ist die Trennung von API-Schlüsseln für Debug- und Release-Build-Varianten.

Um in Ihren Builds einfach zwischen mehreren API-Schlüsseln wechseln zu können, empfehlen wir, für jede relevante [Variante des Builds](https://developer.android.com/studio/build/build-variants.html) eine eigene `braze.xml` Datei zu erstellen. Eine Build-Variante ist eine Kombination aus Build-Typ und Produkt-Flavor. Beachten Sie, dass standardmäßig[ein neues Android-Projekt mit den Build-Typen `debug` und `release` ](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types)und ohne Product Flavors konfiguriert ist.

Erstellen Sie für jede relevante Variante des Builds eine neue `braze.xml` in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

Wenn die Build-Variante kompiliert wird, wird sie den neuen API-Schlüssel verwenden.

Schlagen Sie in der Dokumentation zur [Laufzeitkonfiguration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/) nach, wenn Sie einen API-Schlüssel im Code festlegen möchten.
