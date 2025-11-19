{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Eine [neue Version der Shopify Integration]({{site.baseurl}}/partners/shopify/#new-shopify-integration) wird schrittweise ab April 2025 veröffentlicht. Die Phasen richten sich nach der Art des Shopify Shops und der externen ID, die zur Einrichtung der ersten Integration verwendet wurde. <br><br>**Die alte Version der Integration wird nach dem 28\. August 2025 nicht mehr verfügbar sein. Aktualisieren Sie vor diesem Datum auf die neue Version, um die Integration weiterhin ohne Probleme nutzen zu können.**
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
Senden Sie keine gesetzlich vorgeschriebenen Transaktions-E-Mails an SMS-Gateways, da die Wahrscheinlichkeit groß ist, dass diese E-Mails nicht zugestellt werden.
<br><br>
Obwohl E-Mails, die Sie unter Verwendung einer Telefonnummer und der Gateway-Domäne des Anbieters (bekannt als MM3) versenden, dazu führen können, dass die E-Mail als SMS empfangen wird, unterstützen einige unserer E-Mail-Anbieter dieses Verhalten nicht. Wenn Sie beispielsweise eine E-Mail an eine T-Mobile Telefonnummer (wie "9999999999@tmomail.net") senden, wird Ihre SMS-Nachricht an die Person gesendet, die diese Telefonnummer im T-Mobile Netz besitzt.
<br><br>
Denken Sie daran, dass diese E-Mails, auch wenn sie nicht an den SMS-Gateway zugestellt werden, dennoch für Ihre E-Mail-Abrechnung berücksichtigt werden. Um den Versand von E-Mails an nicht unterstützte Gateways zu vermeiden, sehen Sie sich die [Liste der nicht unterstützten Gateway-Domainnamen](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads) an.
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Für zusätzliche Sicherheit empfehlen wir Ihnen, unser [SDK-Authentifizierungsfeature]({{site.baseurl}}/developer_guide/authentication/) hinzuzufügen, um Identitätswechsel von Nutzer:innen zu verhindern.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Es gibt bestimmte Browser, wie die Naver Android und iOS Apps, die das Braze Einstellungszentrum nicht unterstützen. Wenn Sie davon ausgehen, dass einige Ihrer Nutzer diese Browser verwenden, sollten Sie ihnen alternative Methoden zur Verwaltung ihrer E-Mail-Einstellungen anbieten.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
Die Pläne zum Auslaufen des Kauf-Events werden Ende 2025 bekannt gegeben. Langfristig wird das Kauf-Event durch neue [empfohlene E-Commerce-Ereignisse]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/) ersetzt werden, die mit verbesserten Features für Segmentierung, Berichterstattung, Analytics und mehr ausgestattet sein werden. Die neuen E-Commerce-Events unterstützen jedoch keine bestehenden Features im Zusammenhang mit dem Kauf-Event, wie z.B. Lifetime-Value (LTV) oder Umsatzberichte in Canvase oder Kampagnen. Eine vollständige Liste der Features im Zusammenhang mit Kauf-Ereignissen finden Sie unter [Protokollierung von Kauf-Ereignissen]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
In S3-Buckets gespeicherte Exportdateien werden automatisch gelöscht, nachdem der Download-Link abgelaufen ist (vier Stunden nach dem Versand der Export-E-Mail, sofern nicht anders angegeben).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Die Shopify Integration unterstützt Webhooks zum Anlegen und Aktualisieren von Kunden in Shopify, die sich in Ihren Datenkonfigurationseinstellungen befinden. Wenn ein Nutzerprofil in Shopify erstellt oder aktualisiert wird, wird auch ein entsprechendes Nutzerprofil in Braze erstellt oder aktualisiert. <br><br>Diese Aktionen triggern keine angepassten Events in Shopify und dienen ausschließlich dazu, [Nutzerdaten von Shopify mit Braze zu synchronisieren]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Die synchronisierten Daten umfassen [angepasste Attribute]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [Standardattribute]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes) und, falls in Ihrer Konfiguration aktiviert, [Abo-Gruppen-Status]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Wenn Sie am Canvas-Kontext-Frühzugang teilnehmen, sind die Eingangs-Eigenschaften von Canvas Teil der Canvas-Kontextvariablen. Das bedeutet, dass `canvas_entry_properties` jetzt als `context` referenziert wird. Jede Kontextvariable enthält einen Namen, einen Datentyp und einen Wert, der Liquid enthalten kann. Derzeit ist `canvas_entry_properties` noch abwärtskompatibel. Weitere Einzelheiten finden Sie unter [Kontext]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) und [Canvas-Kontextobjekt]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}