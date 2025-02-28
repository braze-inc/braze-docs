---
nav_title: Shopify checkout.liquid
page_order: 7
description: "Dieser Artikel erklärt die Abschaffung von Shopify checkout.liquid, einschließlich der Auswirkungen auf Ihre Shopify-Integration und der Anleitung für Entwickler."
page_type: update

---

# Shopify checkout.liquid Verwerfung

Shopify hat alle Händler über die Abschaffung von `checkout.liquid` und die Umstellung auf [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions) informiert, eine neue Grundlage für die Erstellung individueller Checkout-Erlebnisse. 

Shopify wird `checkout.liquid` in zwei Phasen abschaffen:

1. **[August 13, 2024](#phase-one-august-13-2024):** Deadline für die Aktualisierung Ihrer Informations-, Versand- und Zahlungsseiten.
2. **[August 28, 2025](#phase-two-august-28-2025):** Deadline für die Aktualisierung Ihrer Dankes- und Bestellstatusseiten, einschließlich Ihrer Apps mit Script-Tags und zusätzlichen Scripts.

Allgemeine Informationen zum Upgrade auf Checkout Extensibilty finden Sie in [der Upgrade-Anleitung von Shopify](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Auswirkungen auf Ihre Integration

Die Integration von Braze und Shopify verwendet [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy), um das Braze Web SDK für nicht-kopflose Websites zu laden. Wir planen, eine neue Version der Integration vor der Frist 2025 auf den Markt zu bringen, um alle Kunden zu unterstützen, bevor `checkout.liquid` vollständig veraltet ist. 

Für die bevorstehenden Änderungen am 13\. August 2024 finden Sie unten die Details, um zu sehen, ob Ihr Entwicklungsteam davon betroffen ist.

### Phase eins: August 13, 2024

Die standardmäßige Braze- und Shopify-Integration verwendet die Informations-, Versand- und Zahlungsseiten innerhalb der Kaufabwicklung nicht. Die Standard-Integration wird dadurch nicht beeinträchtigt. 

#### Shopify Plus

Für Shopify Plus-Kunden werden alle benutzerdefinierten SDK-Code-Snippets, die `checkout.liquid` für die Informations-, Versand- oder Zahlungsseiten ändern, nach diesem Datum inaktiv. Zum Beispiel wird benutzerdefinierter Code, der Ereignisse von diesen Seiten protokolliert, nicht mehr funktionieren. Wenn Sie über benutzerdefinierten SDK-Code verfügen, lesen Sie unsere [Anleitung für Entwickler](#developer-guidance) zur Migration.

#### Nicht-Shopify Plus

Wenn Sie als Nicht-Shopify Plus-Kunde die Informations-, Zahlungs- und Versandseiten anpassen möchten, [müssen Sie ein Upgrade auf Shopify Plus durchführen](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) und dann die [Anleitung für Entwickler](#developer-guidance) befolgen.

### Phase zwei: August 28, 2025

Shopify wird die Unterstützung für [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) auf `checkout.liquid` Seiten, die in der Integration verwendet werden, verwerfen. Als Antwort darauf arbeiten wir aktiv an einer neuen Version der Shopify-Integration, die wir rechtzeitig vor dem Stichtag im August 2025 veröffentlichen wollen. Bleiben Sie dran für weitere Informationen vom Braze Produktteam. 

## Anleitung für Entwickler

Diese Anleitung gilt für Shopify Plus-Kunden, die benutzerdefinierte SDK-Code-Snippets zu den Informations-, Versand- oder Zahlungsseiten in `checkout.liquid` hinzugefügt haben. Wenn Sie diese Anpassungen nicht vorgenommen haben, können Sie diese Anleitung ignorieren.

Sie werden nicht mehr in der Lage sein, benutzerdefinierte SDK-Code-Snippets zu den Informations-, Versand- oder Zahlungsseiten in `checkout.liquid` hinzuzufügen. Stattdessen müssen Sie benutzerdefinierte SDK-Codefragmente zu den Dankes- oder Bestellstatusseiten hinzufügen. So können Sie Benutzer, die den Checkout abgeschlossen haben, abgleichen.
1. Laden Sie das Braze Web SDK auf den Dankes- und Bestellstatusseiten.
2. Rufen Sie die E-Mail des Benutzers ab.
3. Rufen Sie `setEmail` an.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4\. Führen Sie auf Braze die Benutzerprofile per E-Mail zusammen.

Wenn Sie auf doppelte Benutzerprofile stoßen, können Sie unser [Tool zur Massenzusammenführung]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) verwenden, um Ihre Daten zu bereinigen. 
