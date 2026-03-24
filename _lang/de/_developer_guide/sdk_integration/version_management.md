---
page_order: 10
nav_title: Versionsverwaltung
article_title: Über die Versionsverwaltung für das Braze SDK
description: "Erfahren Sie mehr über die Versionsverwaltung für das Braze SDK."
---

# Über die Versionsverwaltung

> Erfahren Sie mehr über die Versionsverwaltung für das Braze SDK, damit Ihre App immer mit den neuesten Features und Qualitätsverbesserungen ausgestattet ist. Da ältere Versionen des SDK möglicherweise nicht die neuesten Patches, Bugfixes oder den neuesten Support erhalten, empfehlen wir Ihnen, Ihr SDK im Rahmen Ihres laufenden Entwicklungszyklus stets auf dem neuesten Stand zu halten.

## Empfehlungen zur Versionierung

Alle Braze SDKs halten sich an die [Semantic Versioning Specification (SemVer)](https://semver.org/). Daher empfehlen wir bei einer Versionsnummer `MAJOR.MINOR.PATCH` Folgendes:

|Version|Über diese Version|Empfehlung|
|-------|------------------|--------------|
| `PATCH` | Updates sind immer abwärtskompatibel und enthalten wichtige Fehlerbehebungen. Sie sind immer sicher. | Sie sollten immer versuchen, sofort auf die neueste Patch-Version Ihrer aktuellen Haupt- und Nebenversion zu aktualisieren. |
| `MINOR` | Updates sind immer abwärtskompatibel und enthalten neue Funktionalität. Sie erfordern keine Änderungen am Code Ihrer Anwendung. | Sie müssen dies zwar nicht sofort tun, aber Sie sollten so bald wie möglich auf die neueste Nebenversion Ihrer aktuellen Hauptversion aktualisieren. 
| `MAJOR` | Updates enthalten grundlegende Änderungen, die möglicherweise Anpassungen an Ihrem Anwendungscode erfordern. | Da dies möglicherweise Code-Änderungen erfordert, aktualisieren Sie auf die neueste Hauptversion in einem Zeitrahmen, der für Ihr Team am besten geeignet ist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Manchmal erfordern neue Android- oder Apple-OS-Updates Änderungen am Braze SDK. Um sicherzustellen, dass Ihre App mit neueren Geräten kompatibel bleibt, ist es wichtig, dass Sie Ihr SDK auf dem neuesten Stand halten.
{% endalert %}

## Benachrichtigungen über neue Releases erhalten

Um automatische Benachrichtigungen zu erhalten, wenn eine neue SDK-Version veröffentlicht wird, können Sie das GitHub-Repository eines beliebigen Braze SDK beobachten:

1. Rufen Sie das GitHub-Repository des SDK auf (z. B. [braze-android-sdk](https://github.com/braze-inc/braze-android-sdk), [braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk) oder [braze-web-sdk](https://github.com/braze-inc/braze-web-sdk)).
2. Klicken Sie oben rechts auf **Watch**.
3. Klicken Sie auf **Custom**, wählen Sie dann **Releases** aus und klicken Sie auf **Apply**.

Sie erhalten eine GitHub-Benachrichtigung (und je nach Ihren [Benachrichtigungseinstellungen](https://github.com/settings/notifications) auch eine E-Mail), sobald ein neues Release veröffentlicht wird. Die vollständige Liste der SDK-Repositories finden Sie unter [Referenzen, Repositories und Beispiel-Apps]({{site.baseurl}}/developer_guide/references/).

## Über bekannte Probleme

Um sicherzustellen, dass unsere Änderungen Ihre Build-Pipelines nicht beeinträchtigen, **werden wir niemals ein Release ändern oder entfernen, nachdem es in einem Distributionssystem veröffentlicht wurde**&#8212;selbst wenn dieses bestimmte Release bekannte Probleme aufweist.

In diesen Fällen dokumentieren wir das Problem im [Changelog des Braze SDK]({{site.baseurl}}/developer_guide/changelogs/) und veröffentlichen dann so schnell wie möglich einen neuen Patch für die betroffenen Haupt- oder Nebenversionen.