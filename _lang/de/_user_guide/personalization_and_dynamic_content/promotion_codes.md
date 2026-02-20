---
nav_title: Aktionscodes
article_title: Aktionscodes
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Erfahren Sie mehr über Aktionscode-Listen, damit Sie sie Ihren Kampagnen und Canvase hinzufügen können."
---

# Aktionscodes

> Erfahren Sie mehr über Aktionscode-Listen, damit Sie sie Ihren Kampagnen und Canvase hinzufügen können.

## Über Aktionscodes

Mit Aktionscodes können Sie eindeutige, zeitlich begrenzte Werte in Nachrichten einfügen, um die Konversion zu fördern. Jede Liste kann bis zu 20 Millionen Codes enthalten, und jeder Code kann bis zu sechs Monate lang gültig sein, bevor er abläuft.

Wenn Braze eine Nachricht mit einem Aktionscode versendet, wird der Code abgezogen, bevor die Nachricht versendet wird. Um sicherzustellen, dass die Codes konsistent und eindeutig sind und nie wieder verwendet werden:

- Bei einer fehlgeschlagenen Nachricht wird der Code trotzdem verbraucht.
- Bei Mehrkanalsendungen wird auf allen Kanälen derselbe Code verwendet.
- Bei bedingtem Liquid werden bei allen referenzierten Listen Codes abgezogen, auch wenn nur ein Zweig angezeigt wird.
- Wenn Sie einen Canvas-Schritt eingeben oder erneut eingeben, wird ein neuer Code verbraucht.

Wenn Sie mehrere Snippets aus derselben Liste in einer Nachricht platzieren, wendet Braze denselben Code auf alle Snippets an. Um zu vermeiden, dass Ihnen die Codes ausgehen, empfehlen wir Ihnen, mehr Codes hochzuladen, als Sie voraussichtlich verwenden werden.

{% tabs local %}
{% tab Example %}
Stellen Sie sich Aktionscodes wie Gutscheine in einer Postfiliale vor. Sobald der Angestellte einen Coupon für Ihren Brief aus dem Stack zieht, ist er weg - auch wenn der Brief nie ankommt.  

In dem folgenden bedingten Liquid werden beispielsweise Codes aus beiden Listen (`vip-deal` und `regular-deal`) abgezogen, obwohl jeder Nutzer:innen nur einen Zweig sieht:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Aktionscodes können nicht in In-App-Nachrichten in Canvas verschickt werden.
{% endalert %}

## Nächste Schritte

Suchen Sie nach den nächsten Schritten? Beginnen Sie hier:

- [Erstellen einer Liste von Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/)
- [Aktionscodes verwenden]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes)
- [Anzeigen der Verwendung von Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#viewing-promotion-code-usage)

## Häufig gestellte Fragen

### Welche Nachrichtenkanäle kann ich mit Aktionscodes verwenden?

Promotion-Codes werden derzeit für E-Mail, Mobile Push, Web Push, Content Cards, Webhook, SMS und WhatsApp unterstützt. Transaktions-E-Mail-Kampagnen und In-App-Nachrichten von Braze unterstützen derzeit keine Promotion-Codes.

### Zählen Test- und Seed-Sendungen zur Nutzung?

Standardmäßig werden bei Test- und Seed-Gruppen-E-Mail-Sendungen Aktionscodes pro Nutzer:in und Testversand verwendet. Sie können sich jedoch an Ihren Braze-Konto Manager:in wenden, um dieses Verhalten so zu aktualisieren, dass Aktionscodes während der Testphase nicht verwendet werden.

### Was passiert, wenn mehrere Messaging-Kanäle denselben Aktionscode-Snippet verwenden?

Wenn ein bestimmter Nutzer:innen für den Erhalt eines Codes über mehrere Kanäle berechtigt ist, erhält er denselben Code über jeden Kanal. Unabhängig von den empfangenen Kanälen wird nur ein Promo Code verwendet.

### Kann ich mehrere Liquid Snippets verwenden, um dieselbe Liste von Aktionscodes in einer Nachricht zu referenzieren?

Ja Braze wendet denselben Aktionscode auf alle Instanzen dieses Snippets in der Nachricht an und stellt so sicher, dass der Nutzer:innen nur einen eindeutigen Code erhält.

### Was passiert, wenn eine Aktionscode-Liste abgelaufen oder leer ist?

Abgelaufene Codes werden nach sechs Monaten gelöscht.

Wenn die Nachricht einen Aktionscode aus einer leeren oder abgelaufenen Liste enthalten sollte, wird die Nachricht storniert. 

Wenn die Nachricht eine Liquid-Logik enthält, die bedingt einen Aktionscode einfügt, wird die Nachricht nur dann storniert, wenn sie einen Aktionscode hätte enthalten sollen. Wenn die Nachricht keinen Aktionscode enthalten sollte, wird die Nachricht normal gesendet.

### Wenn ich die falschen Aktionscodes hochgeladen habe, kann ich sie dann aktualisieren?

Ja Sie können dieses Problem lösen, indem Sie die gesamte Liste verwerfen oder einen Platzhalter verwenden, um die Liste zu löschen. Weitere Informationen finden Sie unter [Aktualisieren einer Liste von Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#updating-a-promotion-code-list).

### Kann ich einen Aktionscode im Profil eines Nutzers:innen für zukünftige Nachrichten speichern?

Ja Sie können Aktionscodes im Profil eines Nutzers:innen über den Schritt User Update speichern. Weitere Informationen finden Sie unter [Aktionscodes in Nutzerprofilen speichern]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#save-to-profile).
