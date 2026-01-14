---
nav_title: Branch für Deeplinks setzen
article_title: Branch für Deeplinks setzen
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Branch und wie Sie diese nutzen können, um Ihre Deeplinks zu setzen."
search_tag: Partner

---

# Branch für Deeplinks setzen {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://branch.io/), eine mobile Verknüpfungsplattform, unterstützt Sie bei der Akquise, dem Engagement und der Messung über alle Geräte, Kanäle und Plattformen hinweg, indem sie einen ganzheitlichen Überblick über alle Nutzer:innen-Touchpoints bietet.

_Diese Integration wird von Branch gepflegt._

## Über die Integration

Die Integration von Braze und Branch ermöglicht es Ihnen, Ihren Nutzern:in bessere Erlebnisse zu bieten, indem Sie den Beginn ihrer Customer Journey richtig [attributieren]({{site.baseurl}}/partners/message_orchestration/attribution/branch_for_attribution/) und sie über Deeplinks mit dem gewünschten Standort verbinden können.

## Integration

Folgen Sie dem [Leitfaden zur SDK-Integration von Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview), um Ihre Branch-Integration zum Laufen zu bringen. Im Folgenden finden Sie weitere Anwendungsfälle.

### Unterstützung von iOS Universal Links

Zur Unterstützung des Versendens von iOS Universal-Links als Deeplinks von Braze aus:

1. Folgen Sie der Dokumentation von Branch, um [universelle Verknüpfungen](https://help.branch.io/developers-hub/docs/ios-universal-links) einzurichten.
2. Implementieren Sie die [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate) Methode [braze(_:shouldOpenURL:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5) in Ihrer Braze SDK-Integration, um von Ihrer App aus [universelle Links weiterzuleiten]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization).

### Deeplinking in E-Mails setzen

Lesen Sie unsere Dokumentation über [Universal Links und App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)
oder lesen Sie [die Dokumentation von Branch](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work), um Deeplinks von E-Mails einzurichten, die über Braze gesendet werden.

Das Verknüpfen mit Telefonnummern (Anhängen von `tel` an `href`) wird in der Gmail App für iOS nicht unterstützt, es sei denn, ein Nutzer:innen gewährt der App Anrufrechte.

Abhängig von Ihrem ESP sind möglicherweise zusätzliche Anpassungen erforderlich, um universelle Links mit Klick-Tracking zu unterstützen. Diese Informationen finden Sie in unserem entsprechenden Artikel. Sie können auch auf die folgenden Referenzen verweisen, um mehr zu erfahren:

- [SendGrid](https://help.branch.io/using-branch/page/braze-sendgrid)
- [SparkPost](https://help.branch.io/using-branch/page/braze-sparkpost)


