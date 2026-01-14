---
page_order: 10
nav_title: Versionsverwaltung
article_title: Über die Versionsverwaltung für das Braze SDK
description: "Erfahren Sie mehr über die Versionsverwaltung für das Braze SDK."
---

# Über die Versionsverwaltung

> Erfahren Sie mehr über die Versionsverwaltung für das Braze SDK, damit Ihre App immer mit den neuesten Features und Qualitätsverbesserungen ausgestattet ist. Da ältere Versionen des SDK möglicherweise nicht die neuesten Patches, Bugfixes oder Support erhalten, empfehlen wir Ihnen, Ihr SDK immer auf dem neuesten Stand zu halten, da dies Teil Ihres laufenden Entwicklungszyklus ist.

## Empfehlungen zur Versionierung

Alle Braze SDKs halten sich an die [Semantic Versioning Specification (SemVer](https://semver.org/)). Daher empfehlen wir bei einer Versionsnummer `MAJOR.MINOR.PATCH` folgendes:

|Version|Über diese Version|Empfehlung|
|-------|------------------|--------------|
| `PATCH` | Die Updates sind immer ununterbrochen und enthalten wichtige Fehlerbehebungen. Sie werden immer in Sicherheit sein. | Sie sollten immer versuchen, sofort auf die neueste Patch-Version Ihrer aktuellen Haupt- und Nebenversion zu aktualisieren. |
| `MINOR` | Updates sind immer nicht unterbrechungsfrei und enthalten neue Funktionen. Sie erfordern keine Änderungen am Code Ihrer Anwendung. | Sie müssen dies zwar nicht sofort tun, aber Sie sollten so bald wie möglich auf die neueste Unterversion Ihrer aktuellen Hauptversion aktualisieren. 
| `MAJOR` | Bei Updates handelt es sich um grundlegende Änderungen, die möglicherweise Änderungen in Ihrem Code erfordern. | Da dies möglicherweise Code-Änderungen erfordert, aktualisieren Sie auf die neueste Hauptversion in einem Zeitrahmen, der für Ihr Team am besten geeignet ist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Manchmal erfordern neue Android oder Apple OS Updates Änderungen am Braze SDK. Um sicherzustellen, dass Ihre App mit neueren Handys kompatibel ist, ist es wichtig, dass Sie Ihr SDK auf dem neuesten Stand halten.
{% endalert %}

## Über bekannte Probleme

Um sicherzustellen, dass unsere Änderungen Ihre Build-Pipelines nicht zerstören, **werden wir niemals eine Version ändern oder entfernen, nachdem sie in einem Distributionssystem veröffentlicht wurde - selbst**wenn diese bestimmte Version bekannte Probleme aufweist.

In diesen Fällen dokumentieren wir das Problem im [Changelog des Braze SDK]({{site.baseurl}}/developer_guide/changelogs/) und veröffentlichen dann so schnell wie möglich einen neuen Patch für die betroffenen Haupt- oder Nebenversionen.
