---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Apteligent, einer mobilen Anwendung, die Details zu Absturzberichten liefert und es Ihnen ermöglicht, kritische Daten in Ihrer bestehenden Braze-Lösung zu protokollieren."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) ist eine Plattform für die Performance mobiler Anwendungen, die Tools und Erkenntnisse für Entwickler und Produktmanager bietet. 

Die Integration von Braze und Apteligent bietet detaillierte iOS-Absturzberichte, die es Ihnen ermöglichen, wichtige Daten in Ihrer bestehenden Braze-Lösung zu protokollieren sowie Benutzer, bei denen es zu Anwendungsabstürzen gekommen ist, zu segmentieren, zu verstehen und mit ihnen in Kontakt zu treten.

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

### Schritt 2: Benutzerdefinierte Analyse von Abstürzen protokollieren

Das Apteligent SDK löst eine Benachrichtigung aus, wenn der Benutzer die Anwendung nach einem Absturz lädt. Die Benachrichtigung enthält den Namen des Unfalls, den Grund und das Datum des Auftretens.

Wenn Sie die Benachrichtigung erhalten, protokollieren Sie ein benutzerdefiniertes Absturzereignis und aktualisieren die Benutzerattribute mit der Apteligent-Analyse für Absturzberichte:

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

Danach können Sie die Segmentierungs- und Engagement-Analysen von Braze nutzen, indem Sie die Absturzinformationen aus der Apteligent-Plattform verwenden.