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

Zur Erleichterung finden Sie hier eine Zusammenfassung der unterstützten Personalisierungs-Tags. Wenn Sie mehr über die einzelnen Tag-Typen und Best Practices erfahren möchten, lesen Sie weiter.

{% raw %}

| Personalisierungs-Tag-Typ | Tags |
| -------------  | ---- |
| Standardattribute | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Geräteattribute | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>E-Mail-Listen-Attribute</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Dieses Tag ersetzt das bisherige Tag `{{${unsubscribe_url}}}`. Das ältere Tag funktioniert zwar weiterhin in bereits erstellten E-Mails, wir empfehlen Ihnen jedoch, stattdessen das neuere Tag zu verwenden. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>SMS-Attribute</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>WhatsApp-Attribute</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` |
| Kampagnenattribute und Canvas-Schritt-Attribute | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Canvas-Attribute | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Karten-Attribute | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Geofencing-Events | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Event-Eigenschaften <br> (Diese sind an Ihren Workspace angepasst.)| `{{event_properties.${your_custom_event_property}}}` |
| Canvas-Kontextvariablen | `{{context}}` |
| Angepasste Attribute <br> (Diese sind an Ihren Workspace angepasst.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>API-Trigger-Eigenschaften</a> |`{{api_trigger_properties}}` |
| Canvas-Eingangs-Eigenschaften | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Unterstützte Attribute

Die Attribute für Kampagnen, Karten und Canvas werden nur in den entsprechenden Nachrichten-Templates unterstützt (z. B. ist `dispatch_id` in In-App-Nachricht-Kampagnen nicht verfügbar).

In diesem Hilfeartikel erfahren Sie mehr darüber, [wie sich einige dieser Attribute zwischen den Quellen in Braze unterscheiden]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

### Unterschiede zwischen Canvas- und Kampagnen-Tags 

Das Verhalten der folgenden Tags unterscheidet sich zwischen Canvas und Kampagnen:
{% raw %}
- Das Verhalten von `dispatch_id` unterscheidet sich, da Braze Canvas-Schritte als getriggerte Ereignisse behandelt, auch wenn sie „geplant" sind (mit Ausnahme der Eingangsschritte, die geplant werden können). Mehr erfahren Sie unter [Dispatch-ID-Verhalten]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- Wenn Sie das Tag `{{campaign.${name}}}` mit Canvas verwenden, wird der Name der Canvas-Komponente angezeigt. Wenn Sie dieses Tag mit Kampagnen verwenden, wird der Name der Kampagne angezeigt.
{% endraw %}

## Zuletzt verwendete Geräteinformationen

Sie können die folgenden Attribute für das zuletzt verwendete Gerät der Nutzer:innen über alle Plattformen hinweg als Template verwenden. Wenn eine Nutzer:in Ihre Anwendung nicht verwendet hat (z. B. weil Sie die Nutzer:in über die REST API importiert haben), sind alle diese Werte `null`.

{% raw %}

|Tag | Beschreibung |
|---|---|
|`{{most_recently_used_device.${browser}}}` | Der zuletzt verwendete Browser auf dem Gerät der Nutzer:in. Beispiele sind „Chrome" und „Safari". |
|`{{most_recently_used_device.${id}}}` | Der Braze-Gerätebezeichner. Unter iOS kann dies der Apple Identifier for Vendors (IDFV) oder eine UUID sein. Bei Android und anderen Plattformen handelt es sich um eine zufällig generierte UUID. |
| `{{most_recently_used_device.${carrier}}}` | Der Mobilfunkanbieter des zuletzt verwendeten Geräts, falls verfügbar. Beispiele sind „Verizon" und „Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Ob auf dem Gerät Ad-Tracking aktiviert ist oder nicht. Dies ist ein boolescher Wert (`true` oder `false`). |
| `{{most_recently_used_device.${idfa}}}` | Bei iOS-Geräten ist dieser Wert der Identifier for Advertisers (IDFA), wenn Ihre Anwendung mit unserer [optionalen IDFA-Erfassung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/) konfiguriert ist. Bei Nicht-iOS-Geräten ist dieser Wert null. |
| `{{most_recently_used_device.${google_ad_id}}}` | Bei Android-Geräten ist dieser Wert der Google Play Advertising Identifier, wenn Ihre Anwendung mit unserer optionalen Google Play Advertising ID-Erfassung konfiguriert ist. Bei Nicht-Android-Geräten ist dieser Wert null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Bei Roku-Geräten ist dieser Wert der Roku Advertising Identifier, der erfasst wird, wenn Ihre Anwendung mit Braze konfiguriert ist. Bei Nicht-Roku-Geräten ist dieser Wert null. |
| `{{most_recently_used_device.${model}}}` | Der Modellname des Geräts, falls verfügbar. Beispiele sind „iPhone 6S", „Nexus 6P" und „Firefox". |
| `{{most_recently_used_device.${os}}}` | Das Betriebssystem des Geräts, falls verfügbar. Beispiele sind „iOS 9.2.1", „Android (Lollipop)" und „Windows". |
| `{{most_recently_used_device.${platform}}}` | Die Plattform des Geräts, falls verfügbar. Falls festgelegt, ist der Wert einer von `ios`, `android`, `kindle`, `android_china`, `web` oder `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Da es eine große Bandbreite an Mobilfunkanbietern, Modellnamen und Betriebssystemen gibt, empfehlen wir Ihnen, jedes Liquid, das bedingt von einem dieser Werte abhängt, gründlich zu testen. Diese Werte sind `null`, wenn sie auf einem bestimmten Gerät nicht verfügbar sind.

## Informationen zur Ziel-App

Für In-App-Nachrichten können Sie die folgenden App-Attribute in Liquid verwenden. Die Werte basieren darauf, welchen SDK-API-Schlüssel Ihre Apps für die Anforderung von Nachrichten verwenden.

|Tag | Beschreibung |
|------------------|---|
| `{{app.${api_id}}}` | Der API-Schlüssel der App, die die Nachricht anfordert. Sie verwenden diesen Schlüssel beispielsweise in Verbindung mit `abort_message()` Liquid, um das Senden von In-App-Nachrichten an bestimmte Apps zu vermeiden, z. B. an TV-Plattformen oder Entwicklungs-Builds, die einen separaten SDK-API-Schlüssel verwenden.|
| `{{app.${name}}}` | Der Name der App (wie im Braze-Dashboard definiert), die die Nachricht anfordert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Dieser Liquid-Code bricht zum Beispiel eine Nachricht ab, wenn die anfragenden Apps nicht zu den beiden API-Schlüsseln in der Liste gehören:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Informationen zum Zielgerät

Für Push-Benachrichtigungen, In-App-Nachrichten und Banner können Sie die folgenden Attribute für das Gerät, das die Nachricht empfängt, als Template verwenden. Eine Push-Benachrichtigung, In-App-Nachricht oder ein Banner kann Attribute des Geräts enthalten, auf dem die Nutzer:in die Nachricht liest. Diese Attribute funktionieren nicht für Content Cards oder E-Mails. Bei E-Mails werden Nachrichten vor dem Versand gerendert, sodass zu diesem Zeitpunkt nicht bekannt ist, auf welchem Gerät die Nutzer:in die E-Mail öffnet.

|Tag | Beschreibung |
|------------------|---|
| `{{targeted_device.${id}}}` | Dies ist der Braze-Gerätebezeichner. Unter iOS kann dies der Apple Identifier for Vendors (IDFV) oder eine UUID sein. Bei Android und anderen Plattformen handelt es sich um eine zufällig generierte UUID. Wenn eine Nutzer:in zum Beispiel fünf Geräte hat, wird ein Sendeversuch für alle fünf Geräte unternommen, wobei jeweils der entsprechende Gerätebezeichner verwendet wird. Wenn eine Nachricht so konfiguriert ist, dass sie an das zuletzt verwendete Gerät gesendet wird, erfolgt nur ein Sendeversuch an das über Braze identifizierte zuletzt verwendete Gerät. |
| `{{targeted_device.${carrier}}}` | Der Mobilfunkanbieter des zuletzt verwendeten Geräts, falls verfügbar. Beispiele sind „Verizon" und „Orange". |
| `{{targeted_device.${idfa}}}` | Bei iOS-Geräten ist dieser Wert der Identifier for Advertisers (IDFA), wenn Ihre Anwendung mit unserer [optionalen IDFA-Erfassung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/) konfiguriert ist. Bei Nicht-iOS-Geräten ist dieser Wert null. |
| `{{targeted_device.${google_ad_id}}}` | Bei Android-Geräten entspricht dieser Wert dem Google Play Advertising Identifier, wenn Ihre Anwendung mit unserer [optionalen Google Play Advertising ID-Erfassung] konfiguriert ist. Bei Nicht-Android-Geräten ist dieser Wert null. |
| `{{targeted_device.${roku_ad_id}}}` | Bei Roku-Geräten ist dieser Wert der Roku Advertising Identifier, der erfasst wird, wenn Ihre Anwendung mit Braze konfiguriert ist. Bei Nicht-Roku-Geräten ist dieser Wert null. |
| `{{targeted_device.${model}}}` | Der Modellname des Geräts, falls verfügbar. Beispiele sind „iPhone 6S", „Nexus 6P" und „Firefox". |
| `{{targeted_device.${os}}}` | Das Betriebssystem des Geräts, falls verfügbar. Beispiele sind „iOS 9.2.1", „Android (Lollipop)" und „Windows". |
| `{{targeted_device.${platform}}}` | Die Plattform des Geräts, falls verfügbar. Falls festgelegt, ist der Wert einer von `ios`, `android`, `kindle`, `android_china`, `web` oder `tvos`. Sie können auch das Personalisierungs-Tag `most_recently_used_device` verwenden. |
| `{{targeted_device.${foreground_push_enabled}}}` | Dieser Wert ist `true`, wenn das Zielgerät für Vordergrund-Push aktiviert ist, andernfalls `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

Da es eine große Bandbreite an Mobilfunkanbietern, Modellnamen und Betriebssystemen gibt, empfehlen wir Ihnen, jede Logik, die bedingt von einem dieser Werte abhängt, gründlich zu testen. Diese Werte sind `null`, wenn sie auf einem bestimmten Gerät nicht verfügbar sind. 

Darüber hinaus ist es bei Push-Benachrichtigungen unter bestimmten Umständen möglich, dass Braze das mit der Push-Benachrichtigung verbundene Gerät nicht erkennen kann – z. B. wenn das Push-Token über die API importiert wurde. In diesem Fall sind die Werte für diese Nachrichten `null`.

![Beispiel für die Verwendung des Standardwerts „there" bei der Verwendung einer Vornamenvariable in einer Push-Nachricht.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Bedingte Logik anstelle eines Standardwerts verwenden

Unter bestimmten Umständen kann es sinnvoller sein, [bedingte Logik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) zu verwenden, anstatt einen Standardwert festzulegen. Mit bedingter Logik können Sie Nachrichten versenden, die sich je nach dem Wert eines angepassten Attributs unterscheiden. Außerdem können Sie bedingte Logik verwenden, um Nachrichten an Kund:innen mit null oder leeren Attributwerten [abzubrechen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/). 

#### Anwendungsfall

Nehmen wir an, Sie senden Ihren Kund:innen eine Benachrichtigung über den Rewards-Punktestand. Es gibt keine gute Möglichkeit, Kund:innen mit niedrigem oder fehlendem Guthaben mithilfe von Standardwerten zu berücksichtigen.

In diesem Fall gibt es zwei Optionen, die möglicherweise besser funktionieren als die Festlegung eines Standardwerts:

1. Brechen Sie die Nachricht für Kund:innen mit niedrigem, ungültigem und leerem Guthaben ab.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Senden Sie diesen Kund:innen eine ganz andere Nachricht, z. B.:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

In diesem Anwendungsfall erhält eine Nutzer:in mit einem leeren oder nicht vorhandenen Vornamen die Nachricht „Thanks for downloading!". Sie sollten einen [Standardwert]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) für den Vornamen einfügen, um sicherzustellen, dass Ihre Kund:innen im Falle eines Fehlers keinen Liquid-Code sehen.

{% endraw %}

## Variablen-Tags

Sie können das Tag `assign` verwenden, um eine Variable im Nachrichten-Editor zu erstellen. Wir empfehlen, einen eindeutigen Namen für Ihre Variable zu verwenden. Wenn Sie eine Variable mit einem ähnlichen Namen wie die unterstützten Personalisierungs-Tags erstellen (z. B. `language`), kann dies Ihre Messaging-Logik beeinträchtigen.

Nachdem Sie eine Variable erstellt haben, können Sie diese in Ihrer Nachrichtenlogik oder Nachricht referenzieren. Dieses Tag ist besonders nützlich, wenn Sie Inhalte, die von unserem Feature [Connected Content]({% image_buster /assets/img_archive/personalized_firstname_.png %}) zurückgegeben werden, neu formatieren möchten. Weitere Informationen finden Sie in der Shopify-Dokumentation zu [Variablen-Tags](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert tip %}
Weisen Sie in jeder Nachricht die gleichen Variablen zu? Anstatt das `assign`-Tag immer wieder auszuschreiben, können Sie es als Content-Block speichern und am Anfang Ihrer Nachricht einfügen.

1. [Erstellen Sie einen Content-Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Geben Sie Ihrem Content-Block einen Namen (keine Leerzeichen oder Sonderzeichen).
3. Wählen Sie unten auf der Seite **Bearbeiten**.
4. Geben Sie Ihre `assign`-Tags ein.

Solange sich der Content-Block am Anfang Ihrer Nachricht befindet, verweist die Variable jedes Mal, wenn sie als Objekt in Ihre Nachricht eingefügt wird, auf das von Ihnen gewählte angepasste Attribut!
{% endalert %}

### Anwendungsfall

Nehmen wir an, Sie erlauben Ihren Kund:innen, ihre Rewards-Punkte gegen Preise einzulösen, nachdem sie 100 Rewards-Punkte gesammelt haben. Sie möchten also nur Kund:innen benachrichtigen, deren Punktestand größer oder gleich 100 wäre, wenn sie diesen zusätzlichen Kauf tätigen würden:

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

Nehmen wir an, Sie haben einen Ausverkauf von Nike-Sneakern und möchten Kund:innen benachrichtigen, die Interesse an Nike gezeigt haben. Im Profil jeder Kund:in ist ein Array von angesehenen Produktmarken hinterlegt. Dieses Array kann bis zu 25 Produktmarken enthalten, aber Sie möchten nur Kund:innen benachrichtigen, die ein Nike-Produkt unter ihren 5 letzten Produktansichten hatten.

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

In diesem Anwendungsfall überprüfen wir die ersten fünf Einträge im Array der angesehenen Schuhmarken. Wenn eines dieser Elemente „Converse" ist, erstellen wir die Variable `converse_viewer` und setzen sie auf „true".

Dann senden wir die Verkaufsnachricht, wenn `converse_viewer` wahr ist. Andernfalls brechen wir die Nachricht ab.

Dies ist ein einfaches Beispiel dafür, wie Iterations-Tags im Braze Nachrichten-Editor verwendet werden können. Weitere Informationen finden Sie in der Shopify-Dokumentation zu [Iterations-Tags](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Syntax-Tags

Syntax-Tags können verwendet werden, um zu steuern, wie Liquid gerendert wird. Sie können das Tag `echo` verwenden, um einen Ausdruck zurückzugeben. Dies entspricht dem Umschließen eines Ausdrucks mit geschweiften Klammern, nur dass Sie dieses Tag innerhalb von Liquid-Tags verwenden können. Sie können auch das Tag `liquid` verwenden, um einen Liquid-Block ohne Trennzeichen bei jedem Tag zu erstellen. Jedes Tag muss in einer eigenen Zeile stehen, wenn Sie das Tag `liquid` verwenden. Weitere Informationen und Beispiele finden Sie in der Shopify-Dokumentation zu [Syntax-Tags](https://shopify.dev/api/liquid/tags#syntax-tags).

Mit der [Whitespace-Kontrolle](https://shopify.github.io/liquid/basics/whitespace/) können Sie Leerzeichen um Ihre Tags herum entfernen und so die Liquid-Ausgabe weiter kontrollieren.

## HTTP-Statuscodes {#http-personalization}

Sie können den HTTP-Status aus einem [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)-Aufruf verwenden, indem Sie ihn zunächst als lokale Variable speichern und dann den Schlüssel `__http_status_code__` nutzen. Zum Beispiel:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Dieser Schlüssel wird dem Connected-Content-Objekt nur dann automatisch hinzugefügt, wenn der Endpunkt ein JSON-Objekt zurückgibt. Wenn der Endpunkt ein Array oder einen anderen Typ zurückgibt, kann dieser Schlüssel nicht automatisch in der Antwort gesetzt werden.
{% endalert %}

## Nachrichten basierend auf Sprache, letztem Gebietsschema und Zeitzone senden

In manchen Situationen möchten Sie Nachrichten versenden, die speziell auf bestimmte Regionen zugeschnitten sind. Das brasilianische Portugiesisch zum Beispiel unterscheidet sich typischerweise vom europäischen Portugiesisch.

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

In diesem Anwendungsfall erhalten Kund:innen mit dem letzten Gebietsschema `pt_BR` eine Nachricht in brasilianischem Portugiesisch und Kund:innen mit dem letzten Gebietsschema `pt_PT` eine Nachricht in europäischem Portugiesisch. Kund:innen, die die ersten beiden Bedingungen nicht erfüllen, deren Sprache aber auf Portugiesisch eingestellt ist, erhalten eine Nachricht in der von Ihnen gewählten Standard-Portugiesisch-Variante.

### Anwendungsfall: Nutzer:innen nach Zeitzone ansprechen

Sie können Nutzer:innen auch nach ihrer Zeitzone ansprechen. Senden Sie z. B. eine Nachricht, wenn sie sich in der EST-Zeitzone befinden, und eine andere, wenn sie in PST sind. Dazu speichern Sie die aktuelle Zeit in UTC und vergleichen eine if/else-Anweisung mit der aktuellen Zeit der Nutzer:in, um die richtige Nachricht für die richtige Zeitzone zu senden. Sie sollten die Kampagne so einstellen, dass sie in der Ortszeit der Nutzer:in gesendet wird, damit sie die Kampagne zur richtigen Zeit erhalten. 

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

## Nachrichten mit einer Zufallszahl senden

{% raw %}
Das Tag `{% random %}` gibt eine Zufallszahl zurück. Sie können es für A/B-Test-Logik, Stichproben oder die Variation von Nachrichteninhalten verwenden.

| Tag | Beschreibung |
|-------|--------------|
| `{% random %}` | Eine Gleitkommazahl zwischen 0 und 1 (einschließlich 0, ausschließlich 1). |
| `{% random 10 %}` (ganzzahliges Argument) | Eine Ganzzahl von 0 bis einschließlich der angegebenen Ganzzahl minus 1. Zum Beispiel gibt `{% random 10 %}` eine Ganzzahl von 0 bis 9 zurück. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Anwendungsfall: Nutzer:innen zufällige Varianten senden

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags