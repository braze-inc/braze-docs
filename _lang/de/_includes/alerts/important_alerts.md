{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Eine [neue Version der Shopify-Integration]({{site.baseurl}}/partners/shopify/#new-shopify-integration) wird ab April 2025 schrittweise veröffentlicht. Die Phasen richten sich nach der Art des Shopify-Shops und der externen ID, die zur Einrichtung der ursprünglichen Integration verwendet wurde. <br><br>**Die alte Version der Integration wird nach dem 28. August 2025 nicht mehr verfügbar sein. Aktualisieren Sie vor diesem Datum auf die neue Version, um die Integration weiterhin ohne Probleme nutzen zu können.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Private Browserfenster unterstützen keinen Web-Push.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
Wenn Sie Ihrer Kampagne oder Ihrem Canvas eine BCC-Adresse hinzufügen, verdoppelt sich die Anzahl der abrechnungsfähigen E-Mails für die Kampagne oder Canvas-Komponente, da Braze eine Nachricht an Ihre Nutzer:innen und eine an Ihre BCC-Adresse sendet.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
Die Einstellung „Priorität der Benachrichtigungsanzeige" wird auf Geräten mit Android O oder höher nicht mehr verwendet. Stellen Sie auf diesen Geräten die Priorität über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels#importance) ein.
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
Senden Sie keine gesetzlich vorgeschriebenen Transaktions-E-Mails an SMS-Gateways, da die Wahrscheinlichkeit groß ist, dass diese E-Mails nicht zugestellt werden.
<br><br>
Obwohl E-Mails, die Sie unter Verwendung einer Telefonnummer und der Gateway-Domain des Anbieters (bekannt als MM3) versenden, dazu führen können, dass die E-Mail als SMS empfangen wird, unterstützen einige unserer E-Mail-Anbieter dieses Verhalten nicht. Wenn Sie beispielsweise eine E-Mail an eine T-Mobile-Telefonnummer (wie „9999999999@tmomail.net") senden, wird Ihre SMS-Nachricht an die Person gesendet, die diese Telefonnummer im T-Mobile-Netz besitzt.
<br><br>
Beachten Sie, dass diese E-Mails, auch wenn sie nicht an das SMS-Gateway zugestellt werden, dennoch für Ihre E-Mail-Abrechnung berücksichtigt werden. Um den Versand von E-Mails an nicht unterstützte Gateways zu vermeiden, sehen Sie sich die [Liste der nicht unterstützten Gateway-Domainnamen](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads) an.
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Für zusätzliche Sicherheit empfehlen wir, unser Feature zur [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/authentication/) hinzuzufügen, um einen Identitätswechsel von Nutzer:innen zu verhindern.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Es gibt bestimmte Browser, wie die Naver Android- und iOS-Apps, die das Braze Preference Center nicht unterstützen. Wenn Sie davon ausgehen, dass einige Ihrer Nutzer:innen diese Browser verwenden, sollten Sie alternative Methoden zur Verwaltung ihrer E-Mail-Einstellungen anbieten.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
Die Pläne zur schrittweisen Einstellung des Kauf-Events werden im Jahr 2026 bekannt gegeben. Das Kauf-Event wird letztendlich durch neue [empfohlene E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/) ersetzt, die erweiterte Features für Segmentierung, Berichterstellung, Analytics und mehr bieten werden. Die neuen E-Commerce-Events unterstützen jedoch keine bestehenden Features im Zusammenhang mit dem Kauf-Event, wie z. B. Lifetime-Value (LTV) oder Umsatzberichte in Canvasen oder Kampagnen. Eine vollständige Liste der Features im Zusammenhang mit Kauf-Events finden Sie unter [Kauf-Events protokollieren]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
Die Pläne zur schrittweisen Einstellung des Kauf-Events werden im Jahr 2026 bekannt gegeben. Das Kauf-Event wird letztendlich durch neue [empfohlene E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/) ersetzt, die erweiterte Features für Segmentierung, Berichterstellung, Analytics und mehr bieten werden. Wenn dies geschieht, werden die Segment-Filter nicht mehr unter Kaufverhalten angezeigt. Eine vollständige Liste der Kauf-Events finden Sie unter [Kauf-Events protokollieren]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
In S3-Buckets gespeicherte Exportdateien werden automatisch gelöscht, sobald der Download-Link abläuft (vier Stunden nach Versand der Export-E-Mail, sofern nicht anders angegeben).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Die Shopify-Integration unterstützt Shopify-Webhooks für die Erstellung und Aktualisierung von Kund:innen, die sich in Ihren Datenkonfigurationseinstellungen befinden. Wenn ein Nutzerprofil in Shopify erstellt oder aktualisiert wird, wird ein entsprechendes Nutzerprofil in Braze erstellt oder aktualisiert. <br><br>Diese Aktionen triggern keine angepassten Events in Braze und dienen ausschließlich dazu, [Shopify-Nutzerdaten mit Braze zu synchronisieren]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Die synchronisierten Daten umfassen [angepasste Attribute]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [Standardattribute]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes) und, sofern in Ihrer Konfiguration aktiviert, [den Status von Abo-Gruppen]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Canvas-Eingangs-Eigenschaften sind Teil der Canvas-Kontextvariablen. Das bedeutet, dass `canvas_entry_properties` als `context` referenziert wird. Jede `context`-Variable enthält einen Namen, einen Datentyp und einen Wert, der Liquid enthalten kann. Derzeit sind `canvas_entry_properties` abwärtskompatibel. Weitere Informationen finden Sie unter [Kontext]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) und [Canvas-Kontextobjekt]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
Dieser Partner wird auf Ihrer Seite **Technologiepartner** nur angezeigt, wenn Sie [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) aktiviert haben. Für Unterstützung beim Einstieg wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Auswahl zwischen den Filtertypen „Tag des Jahres" und „Zeit"**: Wenn Sie Kontextvariablen filtern, die Datumsangaben enthalten, wählen Sie den korrekten Vergleichstyp, je nachdem, ob sich das Datum jedes Jahr wiederholt:

- **Verwenden Sie „Tag des Jahres",** wenn sich das Datum jedes Jahr wiederholt (z. B. Geburtstage, Jahrestage oder Feiertage wie Weihnachten). Dieser Vergleichstyp berechnet auf Grundlage des Tages im Jahr (1–365/366) und ignoriert die Jahreskomponente.
- **Verwenden Sie „Zeit",** wenn es sich um ein absolutes Datum handelt, das sich nicht wiederholt (z. B. Vertragsende, Terminvereinbarungen oder Abo-Verlängerungsdaten). Dieser Vergleichstyp berechnet auf Grundlage des vollständigen Zeitstempels einschließlich des Jahres.

Die Verwendung von „Tag des Jahres" für absolute Datumsangaben kann zu falschen oder unerwarteten Ergebnissen führen, da die Berechnung die Jahreskomponente nicht berücksichtigt. Wenn Sie beispielsweise ein zukünftiges Vertragsenddatum im April vergleichen, um festzustellen, ob es innerhalb von 63 Tagen liegt, kann „Tag des Jahres" zu falschen Übereinstimmungen führen, da nur die Tageszahlen (119 gegenüber 359) verglichen werden, ohne zu berücksichtigen, dass der April tatsächlich 188 Tage entfernt ist.

**Allgemeine Richtlinie**: Wiederholt sich dieses Datum jedes Jahr? **Ja** → Verwenden Sie „Tag des Jahres". **Nein** → Verwenden Sie „Zeit".
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
Granulare Berechtigungen befinden sich derzeit in der Early-Access-Phase. Wenn für Ihr Unternehmen eine Migration geplant ist, erhalten Ihre Braze-Administratoren E-Mails und Banner im Dashboard, die sie über die [Migration der granularen Berechtigungen]({{site.baseurl}}/granular_permissions_migration/) informieren.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
Für diese Integration muss der Nutzer-Alias das folgende Format verwenden, damit Braze Webhooks dem richtigen Nutzerprofil zuordnen kann:<br><br>
- `alias_label`: `shopify_cart_${cartToken}`
- `alias_name`: `shopify_cart_token`
{% endalert %}

{% endif %}