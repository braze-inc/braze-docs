---
nav_title: Shopify checkout.liquid
page_order: 7
description: "Dieser Artikel erklärt die Abschaffung von Shopify checkout.liquid, einschließlich der Auswirkungen auf Ihre Shopify Integration und der Anleitung für Entwickler:innen."
page_type: update

---

# Shopify checkout.liquid Verwerfung

Shopify hat alle Händler über die Abschaffung von `checkout.liquid` und die Migration zu [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions) informiert, einer neuen Grundlage für den Aufbau angepasster Checkout-Erlebnisse. 

Shopify wird `checkout.liquid` in zwei Phasen abschaffen:

1. **[August 13, 2024](#phase-one-august-13-2024):** Deadline für das Upgraden Ihrer Informations-, Versand- und Zahlungsseiten.
2. **[August 28, 2025](#phase-two-august-28-2025):** Deadline zum Upgraden Ihrer Dankes- und Bestellstatusseiten, einschließlich Ihrer Apps mit Script Tags und zusätzlichen Scripts.

Allgemeine Informationen zum Upgrade auf Checkout Extensibilty finden Sie in [der Upgrade-Anleitung von Shopify](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Auswirkungen auf Ihre Integration

Die Braze und Shopify Integration verwendet [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy), um das Braze Web SDK für nicht-kopflose Websites zu laden. Wir planen, eine neue Version der Integration vor der Frist 2025 auf den Markt zu bringen, um alle Kund:in zu unterstützen, bevor `checkout.liquid` vollständig veraltet ist. 

Für die bevorstehenden Änderungen am 13\. August 2024 prüfen Sie bitte anhand der nachstehenden Details, ob Ihr Entwickler:in Team davon betroffen sein wird.

### Phase eins: August 13, 2024

Bei der Standard Integration von Braze und Shopify werden die Informations-, Versand- und Zahlungsseiten innerhalb der Kaufabwicklung nicht verwendet. Die Standard Integration ist daher nicht betroffen. 

#### Shopify Plus

Für Shopify Plus Kunden werden alle angepassten SDK Code Snippets, die `checkout.liquid` für die Informations-, Versand- oder Zahlungsseiten ändern, nach diesem Datum inaktiv. Angepasster Code, der Ereignisse von diesen Seiten protokolliert, wird zum Beispiel nicht mehr funktionieren. Wenn Sie angepassten SDK Code haben, sehen Sie sich unsere [Anleitung für Entwickler](#developer-guidance):in zur Migration an.

#### Nicht-Shopify Plus

Für Kunden:in, die nicht Shopify Plus sind, müssen Sie, wenn Sie die Informations-, Zahlungs- und Versandseiten anpassen möchten, [auf Shopify Plus upgraden](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) und dann den [Anweisungen der Entwickler:in](#developer-guidance) folgen.

### Phase zwei: August 28, 2025

Shopify wird die Unterstützung für [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) auf `checkout.liquid` Seiten, die in der Integration verwendet werden, verwerfen. Als Antwort darauf arbeiten wir aktiv an einer neuen Version der Shopify Integration, die wir rechtzeitig vor dem Stichtag im August 2025 veröffentlichen wollen. Bleiben Sie dran für weitere Informationen vom Braze Produkt Team. 

## Anleitung für Entwickler:in

Diese Anleitung gilt für Shopify Plus Kunden, die angepasste SDK Code Snippets zu den Informations-, Versand- oder Zahlungsseiten in `checkout.liquid` hinzugefügt haben. Wenn Sie diese Anpassungen nicht vorgenommen haben, können Sie diese Anleitung ignorieren.

Sie werden nicht mehr in der Lage sein, angepasste SDK Code Snippets zu den Informations-, Versand- oder Zahlungsseiten in `checkout.liquid` hinzuzufügen. Stattdessen müssen Sie angepasste SDK Code-Snippets zu den Dankes- oder Bestellstatusseiten hinzufügen. Damit können Sie Nutzer:innen, die den Checkout abgeschlossen haben, abgleichen.
1. Laden Sie das Braze Web SDK auf den Dankes- und Bestellstatusseiten.
2. Rufen Sie die E-Mail des Nutzers:innen ab.
3. Rufen Sie `setEmail` an.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4\. Auf Braze führen Sie die Nutzerprofile per E-Mail zusammen.

Wenn Sie auf doppelte Nutzer:innen-Profile stoßen, können Sie unser [Tool zur Zusammenführung von]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) Daten verwenden, um Ihre Daten zu bereinigen. 
