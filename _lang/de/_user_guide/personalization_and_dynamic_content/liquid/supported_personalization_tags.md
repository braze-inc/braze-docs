---
nav_title: Unterstützte Personalisierungs-Tags
article_title: Unterstützte Liquid Personalization Tags
page_order: 1
description: "Dieser Referenzartikel enthält eine vollständige Liste der unterstützten Liquid Personalisierungs-Tags."
search_rank: 1
---

# Unterstützte Personalisierungs-Tags

> Dieser Referenzartikel enthält eine vollständige Liste der unterstützten Liquid Personalisierungs-Tags.

## Zusammenfassung der unterstützten Tags

Zur Erleichterung finden Sie hier eine Zusammenfassung der unterstützten Personalisierungs-Tags. Wenn Sie mehr über die einzelnen Arten von Tags und bewährte Verfahren erfahren möchten, lesen Sie weiter.

{% raw %}

| Personalisierungs-Tag-Typ | Tags |
| -------------  | ---- |
| Standardattribute | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Geräteattribute | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>E-Mail-Liste Attribute</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Dieses Tag ersetzt das bisherige Tag `{{${unsubscribe_url}}}`. Das ältere Tag funktioniert zwar auch in bereits erstellten E-Mails, aber wir empfehlen Ihnen, stattdessen das neuere Tag zu verwenden. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>SMS Attribute</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>WhatsApp Attribute</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` |
| Kampagnenattribute | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Canvas-Attribute | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Canvas Schritt Attribute | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Karten-Attribute | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Geofencing-Events | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Event-Eigenschaften <br> (Diese sind an Ihren Workspace angepasst.)| `{{event_properties.${your_custom_event_property}}}` |
| Canvas-Kontextvariablen | `{{context}}` |
| Angepasste Attribute <br> (Diese sind an Ihren Workspace angepasst.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>API triggern Eigenschaften</a> |`{{api_trigger_properties}}` |
| Entry-Eigenschaften für Canvas | `{{canvas_entry_properties.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Unterstützte Attribute

Die Attribute „Kampagne“, „Karte“ und „Canvas“ werden nur in den entsprechenden Nachrichten-Templates unterstützt (z. B. ist `dispatch_id` in In-App-Nachrichtenkampagnen nicht verfügbar).

In diesem Hilfeartikel erfahren Sie mehr darüber, [wie sich einige dieser Attribute zwischen den Quellen in Braze unterscheiden]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

### Unterschiede zwischen Canvas- und Kampagnen-Tags 

Das Verhalten für die folgenden Tags unterscheidet sich zwischen Canvas und Kampagnen:
{% raw %}
- `dispatch_id` Das Verhalten unterscheidet sich, da Braze Canvas-Schritte als getriggerte Ereignisse behandelt, auch wenn sie "geplant" sind (mit Ausnahme der Eingangsschritte, die geplant werden können). Wenn Sie mehr darüber erfahren möchten, lesen Sie bitte [Dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- Wenn Sie das Tag `{{campaign.${name}}}` mit Canvas verwenden, wird der Name der Canvas-Komponente angezeigt. Wenn Sie dieses Tag mit Kampagnen verwenden, wird der Name der Kampagne angezeigt.
{% endraw %}

## Zuletzt verwendete Geräteinformationen

Sie können die folgenden Attribute für das letzte Gerät des Nutzers über alle Plattformen hinweg als Template verwenden. Wenn eine Nutzer:in Ihre Anwendung nicht verwendet hat (z. B. weil Sie den oder die Nutzer:in über die REST-API importiert haben), dann lauten diese Werte alle `null`.

{% raw %}

|Taggen | Beschreibung |
|---|---|
|`{{most_recently_used_device.${browser}}}` | Der zuletzt verwendete Browser auf dem Gerät des Benutzers. Beispiele sind "Chrome" und "Safari". |
|`{{most_recently_used_device.${id}}}` | Der Bezeichner des Braze-Geräts. Unter iOS kann dies der Apple Identifier for Vendor (IDFV) oder eine UUID sein. Bei Android und anderen Plattformen handelt es sich um eine zufällig generierte UUID. |
| `{{most_recently_used_device.${carrier}}}` | Der zuletzt verwendete Telefondienstanbieter des Geräts, falls verfügbar. Beispiele hierfür sind „Verizon“ und „Orange“. |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Ob auf dem Gerät die Anzeigenverfolgung aktiviert ist oder nicht. Dies ist ein boolescher Wert (`true` oder `false`). |
| `{{most_recently_used_device.${idfa}}}` | Bei iOS-Geräten ist dieser Wert der Identifier for Advertisers (IDFA), wenn Ihre Anwendung mit unserer [optionalen IDFA-Sammlung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/) konfiguriert ist. Bei Nicht-iOS-Geräten ist dieser Wert gleich Null. |
| `{{most_recently_used_device.${google_ad_id}}}` | Bei Android-Geräten ist dieser Wert der Google Play Advertising Identifier, wenn Ihre Anwendung mit unserer optionalen Google Play Advertising ID-Sammlung konfiguriert ist. Bei Nicht-Android-Geräten ist dieser Wert gleich Null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Bei Roku-Geräten ist dieser Wert der Roku Advertising Identifier, der erfasst wird, wenn Ihre Anwendung mit Braze konfiguriert wird. Bei Geräten, die nicht von Roku stammen, ist dieser Wert gleich Null. |
| `{{most_recently_used_device.${model}}}` | Der Modellname des Geräts, falls verfügbar. Beispiele sind "iPhone 6S" und "Nexus 6P" und "Firefox". |
| `{{most_recently_used_device.${os}}}` | Das Betriebssystem des Geräts, falls verfügbar. Beispiele sind "iOS 9.2.1" und "Android (Lollipop)" und "Windows". |
| `{{most_recently_used_device.${platform}}}` | Die Plattform des Geräts, falls verfügbar. Falls festgelegt, ist der Wert einer von `ios`, `android`, `kindle`, `android_china`, `web` oder `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Da es eine so große Bandbreite an Geräteträgern, Modellnamen und Betriebssystemen gibt, raten wir Ihnen, jedes Liquid, das von einem dieser Werte abhängt, gründlich zu testen. Diese Werte werden unter `null` angezeigt, wenn sie auf einem bestimmten Gerät nicht verfügbar sind.

## Informationen zur jeweiligen App

Für In-App-Nachrichten können Sie die folgenden App-Attribute in Liquid verwenden. Die Werte hängen davon ab, welchen SDK-API-Schlüssel Ihre Anwendungen für die Anforderung von Nachrichten verwenden.

|Taggen | Beschreibung |
|------------------|---|
| `{{app.${api_id}}}` | Der API-Schlüssel der App, die die Nachricht anfordert. Sie verwenden diesen Schlüssel beispielsweise in Verbindung mit `abort_message()` Liquid, um das Senden von In-App-Nachrichten an bestimmte Apps zu vermeiden, z. B. an TV-Plattformen oder Entwicklungs-Builds, die einen separaten SDK-API-Schlüssel verwenden.|
| `{{app.${name}}}` | Der Name der App (wie im Braze-Dashboard definiert), die die Nachricht anfordert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Dieser Liquid-Code bricht zum Beispiel eine Nachricht ab, wenn die anfragenden Anwendungen nicht zu den beiden API-Schlüsseln in der Liste gehören:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Informationen zum jeweiligen Gerät

Für Push-Benachrichtigungen und In-App-Kanäle für Nachrichten können Sie die folgenden Attribute für das Gerät, an das eine Nachricht gesendet wird, als Template eingeben. Das heißt, eine Push-Benachrichtigung oder In-App-Nachricht kann Geräteattribute des Geräts enthalten, auf dem die Nachricht gelesen wird. Beachten Sie, dass diese Attribute bei Content-Karten nicht funktionieren. 

|Taggen | Beschreibung |
|------------------|---|
| `{{targeted_device.${id}}}` | Dies ist der Bezeichner des Braze-Geräts. Unter iOS kann dies der Apple Identifier for Vendor (IDFV) oder eine UUID sein. Bei Android und anderen Plattformen handelt es sich um eine zufällig generierte UUID. Wenn ein Nutzer:innen zum Beispiel fünf Geräte hat, wird ein Sendeversuch für alle fünf Geräte unternommen, wobei jeder den entsprechenden Bezeichner des Geräts verwendet. Wenn eine Nachricht so konfiguriert ist, dass sie an das zuletzt verwendete Gerät eines Nutzers:innen gesendet wird, erfolgt nur ein Sendeversuch an das über Braze identifizierte zuletzt verwendete Gerät. |
| `{{targeted_device.${carrier}}}` | Der zuletzt verwendete Telefondienstanbieter des Geräts, falls verfügbar. Beispiele hierfür sind „Verizon“ und „Orange“. |
| `{{targeted_device.${idfa}}}` | Bei iOS-Geräten ist dieser Wert der Identifier for Advertisers (IDFA), wenn Ihre Anwendung mit unserer [optionalen IDFA-Sammlung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/) konfiguriert ist. Bei Nicht-iOS-Geräten ist dieser Wert gleich Null. |
| `{{targeted_device.${google_ad_id}}}` | Bei Android Geräten ist dieser Wert der Google Play Advertising Bezeichner, wenn Ihre Anwendung mit unserer [optionalen Google Play Advertising ID Sammlung] konfiguriert ist. Bei Nicht-Android-Geräten ist dieser Wert gleich Null. |
| `{{targeted_device.${roku_ad_id}}}` | Bei Roku-Geräten ist dieser Wert der Roku Advertising Identifier, der erfasst wird, wenn Ihre Anwendung mit Braze konfiguriert wird. Bei Geräten, die nicht von Roku stammen, ist dieser Wert gleich Null. |
| `{{targeted_device.${model}}}` | Der Modellname des Geräts, falls verfügbar. Beispiele sind "iPhone 6S" und "Nexus 6P" und "Firefox". |
| `{{targeted_device.${os}}}` | Das Betriebssystem des Geräts, falls verfügbar. Beispiele sind "iOS 9.2.1" und "Android (Lollipop)" und "Windows". |
| `{{targeted_device.${platform}}}` | Die Plattform des Geräts, falls verfügbar. Falls festgelegt, ist der Wert einer von `ios`, `android`, `kindle`, `android_china`, `web` oder `tvos`. Sie können auch das Personalisierungs-Tag `most_recently_used_device` verwenden. |
| `{{targeted_device.${foreground_push_enabled}}}` | Dieser Wert ist `true`, wenn das Zielgerät für den Vordergrund-Push aktiviert ist, andernfalls `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

Da es eine so große Bandbreite an Geräteträgern, Modellnamen und Betriebssystemen gibt, raten wir Ihnen, jede Logik, die von einem dieser Werte abhängig ist, gründlich zu testen. Diese Werte werden unter `null` angezeigt, wenn sie auf einem bestimmten Gerät nicht verfügbar sind. 

Darüber hinaus ist es möglich, dass Braze bei Push-Benachrichtigungen unter bestimmten Umständen nicht in der Lage ist, das mit der Push-Benachrichtigung verbundene Gerät zu erkennen, z.B. wenn das Push-Token über die API importiert wurde, was dazu führt, dass die Werte für diese Nachrichten `null` sind.

![Beispiel für die Verwendung des Standardwerts "there" bei Verwendung einer Variable für den Vornamen in einer Push Nachricht.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Verwendung einer bedingten Logik anstelle eines Standardwerts

Unter bestimmten Umständen können Sie sich für die Verwendung einer [bedingten Logik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) entscheiden, anstatt einen Standardwert festzulegen. Mit der bedingten Logik können Sie Nachrichten versenden, die sich je nach dem Wert eines benutzerdefinierten Attributs unterscheiden. Außerdem können Sie bedingte Logik verwenden, um Nachrichten an Kund:in mit null oder leeren Attribut-Werten [abzubrechen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/). 

#### Anwendungsfall

Nehmen wir an, Sie senden Ihren Kund:innen eine Benachrichtigung über den Rewards-Punktestand. Es gibt keine gute Möglichkeit, Kund:innen mit niedrigem und ohne Guthaben mit Standardwerten zu berücksichtigen.

In diesem Fall gibt es zwei Optionen, die möglicherweise besser funktionieren als die Festlegung eines Standardwerts:

1. Brechen Sie die Nachricht für Kunden mit niedrigem, ungültigem und leerem Saldo ab.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Senden Sie diesen Kund:innen eine ganz andere Nachricht, z. B.:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

In diesem Anwendungsfall erhält ein:e Nutzer:in mit einem nicht ausgefüllten oder leeren Vornamen die Nachricht „Vielen Dank für den Download“. Sie sollten einen [Standardwert]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) für den Vornamen einfügen, um sicherzustellen, dass Ihr Kund:in im Falle eines Fehlers nicht Liquid sieht.

{% endraw %}

## Variablen-Tags

Sie können das Tag `assign` verwenden, um eine Variable im Nachrichten-Editor zu erstellen. Wir empfehlen, einen eindeutigen Namen für Ihre Variable zu verwenden. Wenn Sie eine Variable mit einem ähnlichen Namen wie die unterstützten Tags für die Personalisierung erstellen (z.B. `language`), kann dies Ihre Messaging-Logik beeinträchtigen.

Nachdem Sie eine Variable erstellt haben, können Sie diese Variable in Ihrer Nachrichtenlogik oder Nachricht referenzieren. Dieses Tag ist nützlich, wenn Sie Content, der von unserer Funktion [Connected-Content]({% image_buster /assets/img_archive/personalized_firstname_.png %}) zurückgegeben wird, neu formatieren möchten. Weitere Informationen finden Sie in der Shopify-Dokumentation über [variable Tags](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert tip %}
Haben Sie das Gefühl, dass Sie in jeder Nachricht die gleichen Variablen zuweisen? Anstatt den `assign` Tag immer wieder auszuschreiben, können Sie diesen Tag als Inhaltsblock speichern und ihn stattdessen am Anfang Ihrer Nachricht einfügen.

1. [Erstellen Sie einen Content-Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Geben Sie Ihrem Inhaltsblock einen Namen (keine Leerzeichen oder Sonderzeichen).
3. Wählen Sie unten auf der Seite **Bearbeiten**.
4. Geben Sie Ihre `assign`-Tags ein.

Solange sich der Inhaltsblock am Anfang Ihrer Nachricht befindet, wird die Variable jedes Mal, wenn sie als Objekt in Ihre Nachricht eingefügt wird, auf das von Ihnen gewählte benutzerdefinierte Attribut verweisen!
{% endalert %}

### Anwendungsfall

Nehmen wir an, Sie erlauben Ihren Kunden, ihre Rewards-Punkte gegen Preise einzulösen, nachdem sie 100 Rewards-Punkte gesammelt haben. Sie möchten also nur Kund:innen benachrichtigen, deren Punktestand größer oder gleich 100 wäre, wenn sie diesen zusätzlichen Kauf tätigen würden:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Iterations-Tags

{% raw %}
Iterations-Tags können verwendet werden, um einen Codeblock wiederholt auszuführen. Der folgende Anwendungsfall zeigt das Tag `for`.

### Anwendungsfall

Nehmen wir an, Sie haben einen Ausverkauf von Nike-Turnschuhen und möchten Kunden, die Interesse an Nike bekundet haben, eine Nachricht zukommen lassen. Sie haben eine Reihe von Produktmarken, die im Profil jedes Kunden oder jeder Kundin angezeigt werden. Dieses Array kann bis zu 25 Produktmarken enthalten, aber Sie möchten nur Kund:innen benachrichtigen, die ein Nike-Produkt als eine ihrer 5 letzten Produktansichten angesehen haben.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

In diesem Anwendungsfall überprüfen wir die ersten fünf Einträge im Array der angesehenen Schuhmarken. Wenn eines dieser Elemente umgekehrt ist, erstellen wir die Variable `converse_viewer` und setzen sie auf „true“.

Dann senden wir die Verkaufsnachricht, wenn `converse_viewer` wahr ist. Andernfalls brechen wir die Nachricht ab.

Dies ist ein einfaches Beispiel dafür, wie Iterations-Tags im Braze Message Composer verwendet werden können. Weitere Informationen finden Sie in der Dokumentation von Shopify zu [Iterations-Tags](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Syntax-Tags

Syntax-Tags können verwendet werden, um zu steuern, wie Liquid gerendert wird. Sie können das Tag `echo` verwenden, um einen Ausdruck zurückzugeben. Dies ist dasselbe wie das Umschließen eines Ausdrucks mit geschweiften Klammern, nur dass Sie dieses Tag innerhalb von Liquid-Tags verwenden können. Sie können auch das `liquid` Tag verwenden, um einen Block von Liquid ohne Trennzeichen auf jedem Tag zu haben. Jedes Tag muss in einer eigenen Zeile stehen, wenn Sie das Tag `liquid` verwenden. Weitere Informationen und Beispiele finden Sie in der Shopify-Dokumentation zu [Syntax-Tags](https://shopify.dev/api/liquid/tags#syntax-tags).

Mit der [Whitespace-Kontrolle](https://shopify.github.io/liquid/basics/whitespace/) können Sie Leerzeichen um Ihre Tags herum entfernen und so das Aussehen der Liquid-Ausgabe weiter kontrollieren.

## HTTP-Statuscodes {#http-personalization}

Sie können den HTTP-Status aus einem Aufruf von [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) verwenden, indem Sie ihn zunächst als lokale Variable speichern und dann die Taste `__http_status_code__` verwenden. Zum Beispiel:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Dieser Schlüssel wird dem Connected-Content-Objekt nur dann automatisch hinzugefügt, wenn der Endpunkt ein JSON-Objekt zurückgibt. Wenn der Endpunkt ein Array oder einen anderen Typ zurückgibt, dann kann dieser Schlüssel nicht automatisch in der Antwort gesetzt werden.
{% endalert %}

## Senden von Nachrichten basierend auf Sprache, letztem Gebietsschema und Zeitzone

In manchen Situationen möchten Sie vielleicht Nachrichten versenden, die speziell für bestimmte Regionen bestimmt sind. Das brasilianische Portugiesisch zum Beispiel unterscheidet sich typischerweise vom europäischen Portugiesisch.

### Anwendungsfall: Basierend auf dem aktuellen Gebietsschema lokalisieren

Hier sehen Sie einen Anwendungsfall, wie Sie das neueste Gebietsschema verwenden können, um eine internationalisierte Nachricht weiter zu lokalisieren.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

In diesem Anwendungsfall erhalten Kund:innen mit dem letzten Gebietsschema `pt_BR` eine Nachricht in brasilianischem Portugiesisch und Kund:innen mit dem letzten Gebietsschema `pt_PT` erhalten eine Nachricht in europäischem Portugiesisch. Kunden, die die ersten beiden Bedingungen nicht erfüllen, deren Sprache aber auf Portugiesisch eingestellt ist, erhalten eine Nachricht in der Sprache, die Sie als Standardeinstellung für Portugiesisch gewählt haben.

### Anwendungsfall: Zielbenutzer nach Zeitzone

Sie können Nutzer:innen auch nach ihrer Zeitzone auswählen. Senden Sie z.B. eine Nachricht, wenn Sie in EST wohnen und eine andere, wenn Sie in PST wohnen. Dazu speichern Sie die aktuelle Zeit in UTC und vergleichen eine if/else-Anweisung mit der aktuellen Zeit des Benutzers, um die richtige Nachricht für die richtige Zeitzone zu senden. Sie sollten die Kampagne so einstellen, dass sie in der lokalen Zeitzone des Benutzers gesendet wird, damit er die Kampagne zur richtigen Zeit erhält. 

Im folgenden Anwendungsfall sehen Sie, wie Sie eine Nachricht verfassen, die zwischen 14 und 15 Uhr versendet wird und für jede Zeitzone eine eigene Nachricht enthält.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
