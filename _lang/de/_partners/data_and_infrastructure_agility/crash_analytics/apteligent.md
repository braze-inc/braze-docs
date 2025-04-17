---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Apteligent, einer mobilen Anwendung, die Details zu Absturzberichten enthält und es Ihnen erlaubt, kritische Daten in Ihrer bestehenden Braze Lösung zu protokollieren."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) ist eine Plattform für die Performance von mobilen Anwendungen, die Entwicklern:in und Produktmanagern Insights bietet. 

_Diese Integration wird von Apteligent gepflegt._

## Über die Integration

Die Integration von Braze und Apteligent bietet detaillierte iOS-Absturzberichte, die es Ihnen erlauben, kritische Daten in Ihrer bestehenden Braze-Lösung zu protokollieren sowie Nutzer:innen, bei denen es zu Anwendungsabstürzen gekommen ist, zu segmentieren, zu verstehen und mit ihnen in Kontakt zu treten.

## Voraussetzungen 

| Anforderung | Beschreibung |
|---|---|
| TestDrive Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein TestDrive-Konto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert warning %}
Diese Integration wird derzeit nur auf iOS unterstützt.
{% endalert %}

## Integration {#apteligent-ios-integration}

### Schritt 1: Einen Beobachter registrieren

Zunächst müssen Sie einen Beobachter registrieren. Stellen Sie sicher, dass dies geschieht, bevor Sie Apteligent initialisieren.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Schritt 2: Angepasste Analytics für Abstürze protokollieren

Das Apteligent SDK löst eine Benachrichtigung aus, wenn der Nutzer:innen die Anwendung nach einem Absturz lädt. Die Benachrichtigung enthält den Namen des Absturzes, den Grund und das Datum des Vorkommens.

Nach Erhalt der Benachrichtigung protokollieren Sie ein angepasstes Event und aktualisieren die Attribute der Nutzer:innen mit Apteligent's Crash Reporting Analytics:

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

Nach Abschluss des Projekts können Sie die leistungsstarken Segmentierungs- und Engagement-Analysen von Braze nutzen, indem Sie die Absturzinformationen der Apteligent-Plattform verwenden.

