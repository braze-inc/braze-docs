---
nav_title: Verzweigung für Deep Linking
article_title: Verzweigung für Deep Linking
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Branch und wie Sie diese zur Unterstützung Ihrer Deep Linking-Praktiken nutzen können."
search_tag: Partner

---

# Verzweigung für Deep Linking {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch][1], eine Plattform für die Verknüpfung von Mobilgeräten, hilft Ihnen bei der Akquise, dem Engagement und der Messung über alle Geräte, Kanäle und Plattformen hinweg, indem sie einen ganzheitlichen Überblick über alle Berührungspunkte mit dem Benutzer bietet.

Die Integration von Braze und Branch ermöglicht es Ihnen, Ihren Kunden ein besseres Erlebnis zu bieten, indem Sie den Beginn ihrer User Journey richtig [zuordnen]({{site.baseurl}}/partners/advertising_technologies/attribution/branch_for_attribution/) und sie über Deep Links mit dem gewünschten Ort verbinden können.

## Integration

Folgen Sie dem [SDK-Integrationsleitfaden von Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview), um Ihre Branch-Integration zum Laufen zu bringen. Im Folgenden finden Sie weitere Anwendungsfälle.

### Unterstützung von iOS Universal Links

Unterstützung des Versands von iOS-Universal-Links als Deep-Links aus Braze heraus:

1. Folgen Sie der Branch-Dokumentation zum Einrichten von [Universal-Links][3].
2. Implementieren Sie die [`BrazeDelegate`][4] Methode [braze(_:shouldOpenURL:)][5] in Ihrer Braze SDK-Integration, um [universelle Links][6] von Ihrer App aus [weiterzuleiten][6].

### Deep Linking in E-Mails

Lesen Sie unsere Dokumentation über [Universal Links und App Links]({{site.baseurl}}/help/help_articles/email/universal_links/)
oder lesen Sie in [der Branch-Dokumentation](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work) nach, wie Sie Deep Linking von E-Mails einrichten, die über Braze gesendet werden.

Das Verknüpfen mit Telefonnummern (Anhängen von `tel` an `href`) wird in der Google Mail-App für iOS nicht unterstützt, es sei denn, ein Benutzer erteilt der App die Berechtigung zum Anrufen.

Abhängig von Ihrem ESP sind möglicherweise zusätzliche Anpassungen erforderlich, um universelle Links mit Click-Tracking zu unterstützen. Diese Informationen finden Sie in unserem entsprechenden Artikel. Sie können auch die folgenden Referenzen lesen, um mehr zu erfahren:

- [SendGrid][7]
- [SparkPost][9]

[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://help.branch.io/developers-hub/docs/ios-universal-links
[4]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization
[7]: https://help.branch.io/using-branch/page/braze-sendgrid
[9]: https://help.branch.io/using-branch/page/braze-sparkpost
