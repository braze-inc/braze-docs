---
nav_title: Kontextvariablen
article_title: Kontextvariablen
page_type: reference
description: "Dieser Referenzartikel erläutert Kontextvariablen in Braze Canvases, einschließlich ihrer Typen, Verwendung und Best Practices."
---

# Kontextvariablen

> Kontextvariablen sind temporäre Datenelemente, die Sie erstellen und innerhalb der Journey von Nutzer:innen durch ein bestimmtes Canvas verwenden können. Sie ermöglichen es Ihnen, Verzögerungen individuell zu personalisieren, Nutzer:innen dynamisch zu segmentieren und Nachrichten anzureichern, ohne die Profilinformationen von Nutzer:innen dauerhaft zu verändern. Kontextvariablen existieren nur innerhalb der Canvas-Sitzung und bleiben weder über verschiedene Canvase hinweg noch außerhalb der Sitzung bestehen.

## Wie Kontextvariablen funktionieren

Kontextvariablen können auf zwei Arten festgelegt werden:

- **Beim Canvas-Eingang:** Wenn Nutzer:innen ein Canvas betreten, können Daten aus dem Event oder dem API-Trigger automatisch Kontextvariablen befüllen.
- **In einem Kontext-Schritt:** Sie können Kontextvariablen manuell innerhalb des Canvas definieren oder aktualisieren, indem Sie einen [Kontext-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) hinzufügen.

Jede Kontextvariable umfasst:

- Einen Namen (wie `flight_time` oder `subscription_renewal_date`)
- Einen Datentyp (wie beispielsweise Zahl, String, Zeit oder Array)
- Einen Wert, den Sie mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) oder über das Tool **Personalisierung hinzufügen** zuweisen.

Wenn Sie eine Kontextvariable definiert haben, können Sie sie im gesamten Canvas verwenden, indem Sie sie in diesem Format referenzieren: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Beispielsweise könnte {% raw %}`{{context.${flight_time}}}`{% endraw %} die geplante Flugzeit der Nutzer:in zurückgeben.

Jedes Mal, wenn Nutzer:innen das Canvas betreten – auch wenn sie es schon einmal betreten haben – werden die Kontextvariablen auf Grundlage der aktuellen Eingabedaten und der Canvas-Konfiguration neu definiert. Dieser zustandsbehaftete Ansatz ermöglicht es jedem Canvas-Eintrag, seinen eigenen unabhängigen Kontext beizubehalten, sodass Nutzer:innen mehrere aktive Zustände innerhalb derselben Journey haben können, während der spezifische Kontext für jeden Zustand erhalten bleibt.

Wenn eine Kund:in beispielsweise zwei bevorstehende Flüge hat, gibt es zwei separate Journey-Zustände, die gleichzeitig ablaufen – jeder mit seinen eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Ziel. Auf diese Weise können Sie personalisierte Erinnerungen für den Flug um 14 Uhr nach New York versenden und gleichzeitig andere Updates für den Flug um 8 Uhr nach Los Angeles am nächsten Tag bereitstellen, sodass jede Nachricht für die jeweilige Buchung relevant bleibt.

## Überlegungen

Sie können bis zu 10 Kontextvariablen pro [Kontext-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/) definieren. Jeder Variablenname kann bis zu 100 Zeichen lang sein und darf nur Buchstaben, Zahlen oder Unterstriche enthalten.

Kontextvariablen-Definitionen können bis zu 10.240 Zeichen umfassen. Wenn Sie Kontextvariablen an ein API-getriggertes Canvas übergeben, teilen diese sich denselben Namespace wie Variablen, die in einem Kontext-Schritt erstellt wurden. Wenn Sie beispielsweise eine Variable `purchased_item` im Kontextobjekt des [`/canvas/trigger/send`-Endpunkts]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) senden, können Sie diese als {% raw %}`{{context.${purchased_item}}}`{% endraw %} referenzieren. Wenn Sie diese Variable in einem Kontext-Schritt neu definieren, überschreibt der neue Wert den API-Wert für die Journey dieser Nutzer:in.

Sie können bis zu 50 KB pro Kontext-Schritt speichern, verteilt auf bis zu 10 Variablen. Wenn die Gesamtgröße aller Variablen in einem Schritt 50 KB überschreitet, werden Variablen, die über diese Grenze hinausgehen, nicht ausgewertet oder gespeichert. Wenn Sie beispielsweise drei Variablen in einem Kontext-Schritt haben:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

Variable 3 wird nicht ausgewertet oder gespeichert, da die Summe der vorherigen Variablen 50 KB überschreitet.

## Datentypen

Kontextvariablen, die im Schritt erstellt oder aktualisiert werden, können die folgenden Datentypen zugewiesen bekommen.

{% alert note %}
Kontextvariablen haben dieselben erwarteten Formate für Datentypen wie [angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Bei Verwendung des Array-Typs versucht Braze, den Wert als JSON zu parsen, wodurch Arrays von Objekten erfolgreich erstellt werden können. Wenn die Objekte in Ihren Arrays kein gültiges JSON sind, ist das Ergebnis ein einfaches String-Array. <br><br>Für verschachtelte Objekte und Objekt-Arrays verwenden Sie den [`as_json_string` Liquid-Filter](#converting-connected-content-strings-to-json). Wenn Sie dasselbe Objekt in einem Kontext-Schritt erstellen, müssen Sie das Objekt mit `as_json_string` rendern, beispielsweise {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Datentyp | Beispiel für einen Variablennamen | Beispielwert |
|---|---|---|
|Boolescher Wert| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Zahl| credit_score |{% raw %}<code>740</code>{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Array (von Objekten)| pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
|Zeit (in UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objekt (abgeflacht) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Standardmäßig ist der Datentyp „Zeit" auf UTC eingestellt. Wenn Sie einen Zeitwert mit dem Datentyp „String" speichern, können Sie die Zeit in einer anderen Zeitzone definieren, beispielsweise PST. 

Wenn Sie beispielsweise einer Nutzer:in einen Tag vor ihrem Geburtstag eine Nachricht senden möchten, sollten Sie die Kontextvariable als Zeitdatentyp speichern, da mit dem Versand am Vortag eine Liquid-Logik verbunden ist. Wenn Sie jedoch eine Feiertagsnachricht am ersten Weihnachtsfeiertag (25. Dezember) versenden, müssen Sie die Uhrzeit nicht als dynamische Variable referenzieren, sodass die Verwendung eines String-Datentyps vorzuziehen wäre.

Für Objekt-Datentypen können Sie die Punktnotation verwenden, um einen Pfad durch die Daten anzugeben. Wenn Ihr Kontext-Schritt beispielsweise eine Kontextvariable `order_summary` mit dieser Struktur definiert:

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

In einem [Zielgruppenpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/)- oder [Decision-Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/)-Filter geben Sie den Pfad als Kontextvariablennamen in Punktnotation ein (z. B. `order_summary.shipping.carrier`). Wenn der Filter ausgewertet wird, löst Braze diesen Pfad zum Wert `overnight` auf.

In Liquid (z. B. in einem [Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)-Schritt) verwenden Sie stattdessen {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %}.

## Verwendung von Kontextvariablen

Sie können Kontextvariablen überall dort verwenden, wo Sie Liquid in einem Canvas einsetzen, beispielsweise in den Schritten [Nachricht]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) und [Benutzerupdate]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update), indem Sie **Personalisierung hinzufügen** auswählen. Für In-App-Nachrichten und Banner in Nachrichten-Schritten können Sie Kontextvariablen auswählen, um festzulegen, wann die Nachricht ablaufen soll.

Nehmen wir zum Beispiel an, Sie möchten Passagiere vor ihrem nächsten Flug über ihren Zugang zur VIP-Lounge informieren. Diese Nachricht sollte nur an Passagiere gesendet werden, die ein First-Class-Ticket gekauft haben. Eine Kontextvariable ist eine flexible Möglichkeit, diese Information zu tracken.

Nutzer:innen betreten das Canvas, wenn sie ein Flugticket kaufen. Um die Berechtigung für den Lounge-Zugang zu bestimmen, erstellen wir in einem Kontext-Schritt eine Kontextvariable mit dem Namen `lounge_access_granted` und referenzieren diese Kontextvariable dann in den nachfolgenden Schritten der User Journey.

![Kontextvariable eingerichtet, um zu verfolgen, ob ein Passagier für den Zugang zur VIP-Lounge qualifiziert ist.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

In diesem Kontext-Schritt verwenden wir {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %}, um festzustellen, ob die Art des gekauften Fluges `first_class` ist.

Als Nächstes erstellen wir einen Nachrichten-Schritt, um Nutzer:innen anzusprechen, bei denen {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} den Wert `true` hat. Diese Nachricht wird als Push-Benachrichtigung versendet und enthält personalisierte Informationen zur Lounge. Auf Grundlage dieser Kontextvariablen erhalten die berechtigten Passagiere die entsprechenden Nachrichten vor ihrem Flug.

- Passagiere der ersten Klasse erhalten: „Genießen Sie exklusiven Zugang zur VIP-Lounge!"
- Passagiere mit Business- und Economy-Tickets erhalten: „Upgraden Sie Ihren Flug für exklusiven Zugang zur VIP-Lounge."

![Ein Nachrichten-Schritt mit unterschiedlichen Nachrichten, die je nach Art des gekauften Flugtickets versendet werden.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Sie können [personalisierte Verzögerungsoptionen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) mit den Informationen aus dem Kontext-Schritt hinzufügen, d. h. Sie können die Variable auswählen, die Nutzer:innen verzögert.
{% endalert %}

### Für Aktionspfade und Ausstiegskriterien

Sie können in diesen Trigger-Aktionen den Vergleich von Eigenschaftsfiltern mit Kontextvariablen oder angepassten Attributen nutzen: **Angepasstes Event ausführen** und **Kauf tätigen**. Diese Aktions-Trigger unterstützen auch Eigenschaftsfilter für grundlegende und verschachtelte Eigenschaften. 

- Beim Vergleich mit grundlegenden Eigenschaften entsprechen die verfügbaren Vergleiche dem Typ der Eigenschaft, die durch das angepasste Event definiert ist. Beispielsweise haben String-Eigenschaften die Vergleichsoptionen „exakt gleich" oder „Regex-Übereinstimmung". Boolesche Eigenschaften können entweder wahr oder falsch sein. 
- Beim Vergleich mit verschachtelten Eigenschaften sind die Typen nicht vordefiniert, sodass Sie Vergleiche über mehrere Datentypen hinweg für Boolesche Werte, Zahlen, Strings, Uhrzeiten und Tage des Jahres auswählen können, ähnlich wie bei den Vergleichen für verschachtelte angepasste Attribute. Wenn Sie einen Datentyp auswählen, der zum Zeitpunkt des Vergleichs nicht mit dem tatsächlichen Datentyp der verschachtelten Eigenschaft übereinstimmt, wird die Nutzer:in den Aktionspfad oder die Ausstiegskriterien nicht erfüllen.

#### Beispiele für Aktionspfade

{% alert important %}
Für den Vergleich angepasster Attribute wird der Wert des angepassten Attributs zum Zeitpunkt der Ausführung der Aktion herangezogen. Das bedeutet, dass eine Nutzer:in nicht mit der Aktionspfad-Gruppe übereinstimmt, wenn dieses angepasste Attribut zum Zeitpunkt des Vergleichs nicht befüllt ist oder wenn der Wert des angepassten Attributs nicht mit den definierten Eigenschaftsvergleichen übereinstimmt. Dies gilt auch dann, wenn die Nutzer:in beim Betreten des Aktionspfad-Schritts übereingestimmt hätte.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

Der folgende Aktionspfad ist eingerichtet, um Nutzer:innen zu sortieren, die das angepasste Event `Account_Created` mit der grundlegenden Eigenschaft `source` zur Kontextvariable `app_source_variable` ausgeführt haben.

![Ein Beispiel für einen Aktionspfad, der bei der Ausführung eines angepassten Events auf eine Kontextvariable referenziert.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

Der folgende Aktionspfad ist so eingerichtet, dass er die grundlegende Eigenschaft `brand` für den spezifischen Produktnamen `shoes` mit einer Kontextvariablen `promoted_shoe_brand` abgleicht.

![Ein Beispiel für einen Aktionspfad, der beim Kauf eine Kontextvariable referenziert.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Beispiele für Ausstiegskriterien

{% tabs %}
{% tab Perform custom event %}

Die Ausstiegskriterien besagen, dass Nutzer:innen zu jedem Zeitpunkt ihrer Journey im Canvas das Canvas verlassen, wenn:

- Sie das angepasste Event **Warenkorb verlassen** ausführen und
- die grundlegende Eigenschaft **Artikel im Warenkorb** dem String-Wert der Kontextvariablen `cart_item_threshold` entspricht.

![Ausstiegskriterien, die eingerichtet wurden, um Nutzer:innen zu entfernen, wenn sie ein angepasstes Event basierend auf der Kontextvariablen ausführen.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Die Ausstiegskriterien besagen, dass Nutzer:innen zu jedem Zeitpunkt ihrer Journey im Canvas das Canvas verlassen, wenn:

- Sie einen spezifischen Kauf für das Produkt mit dem Namen „book" tätigen und
- die verschachtelte Eigenschaft „loyalty_program" dieses Kaufs dem angepassten Attribut „VIP" der Nutzer:in entspricht.

![Ausstiegskriterien, die eingerichtet wurden, um Nutzer:innen zu entfernen, wenn sie einen Kauf tätigen.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Ablauf festlegen

Für [Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/) und [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) in einem Canvas-[Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)-Schritt wählen Sie **Eine Dauer nach Verfügbarkeit des Schritts** als Ablauf und aktivieren dann **Dauer personalisieren**, um das Verfügbarkeitsfenster über eine Kontextvariable zu steuern – beispielsweise um es an eine Aktions- oder Buchungsdauer aus einem Kontext-Schritt anzupassen.

**Dauer personalisieren** gilt für diese dauerbasierte Ablaufoption. Wenn Sie stattdessen **An einem bestimmten Datum und Uhrzeit** wählen, legen Sie den Ablauf über die Datums- und Uhrzeitsteuerungen fest.

### Aktionspfad-Verzögerungen

In einem [Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)-Schritt aktivieren Sie unter **Auswertungsfenster** die Option **Verzögerung personalisieren**, um festzulegen, wie lange Nutzer:innen im Schritt gehalten werden – basierend auf einer Kontextvariablen. Verwenden Sie dies, wenn die Wartezeit je nach Nutzer:in variieren soll, z. B. abhängig von Details wie Stufe oder Region.

### Kontextvariablen-Filter

Sie können Filter erstellen, die zuvor deklarierte Kontextvariablen in den Schritten [Zielgruppenpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [Decision-Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) verwenden.

{% alert note %}
Kontextvariablen-Filter sind ausschließlich für Zielgruppenpfade und Decision-Split-Schritte verfügbar.
{% endalert %}

Kontextvariablen werden deklariert und sind nur im Geltungsbereich eines Canvas zugänglich, d. h. sie können nicht in Segmenten referenziert werden. Kontextvariablen-Filter funktionieren in Zielgruppenpfaden und Decision-Split-Schritten ähnlich – Zielgruppenpfade repräsentieren mehrere Gruppen, während Decision-Split-Schritte binäre Entscheidungen darstellen.

![Decision-Split-Schritt-Beispiel mit der Option, einen Filter mit einer Kontextvariablen zu erstellen.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Ähnlich wie Canvas-Kontextvariablen vordefinierte Typen haben, müssen die Vergleiche zwischen Kontextvariablen und statischen Werten [übereinstimmende Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types) aufweisen. Der Kontextvariablen-Filter ermöglicht Vergleiche über mehrere Datentypen hinweg für Boolesche Werte, Zahlen, Strings, Uhrzeiten und Tage des Jahres, ähnlich wie bei den Vergleichen für [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Verwenden Sie für Ihre Kontextvariable und den Vergleich denselben Datentyp. Wenn Ihre Kontextvariable beispielsweise vom Datentyp „Zeit" ist, verwenden Sie Zeitvergleiche (wie „vor" oder „nach"). Die Verwendung nicht übereinstimmender Datentypen (wie beispielsweise String-Vergleiche mit einer Zeit-Kontextvariablen) kann zu unerwartetem Verhalten führen.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Hier ist ein Beispiel für einen Kontextvariablen-Filter, der die Kontextvariable `product_name` mit dem Regex `/braze/` vergleicht.

![Eine Filtereinstellung für die Kontextvariable „product_name", die mit dem Regex „/braze/" übereinstimmt.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Vergleich mit Kontextvariablen oder angepassten Attributen

Durch Aktivieren der Option **Mit einer Kontextvariablen oder einem angepassten Attribut vergleichen** können Sie Kontextvariablen-Filter erstellen, die mit zuvor definierten Kontextvariablen oder angepassten Attributen von Nutzer:innen verglichen werden. Dies kann nützlich sein, um dynamische Vergleiche pro Nutzer:in durchzuführen, beispielsweise mit API-getriggertem `context`, oder um komplexe Vergleichslogik zu verdichten, die über Kontextvariablen definiert ist.

{% tabs %}
{% tab Example 1 %}

Angenommen, Sie möchten eine personalisierte Erinnerung an Nutzer:innen senden, die eine dynamische Zeit lang inaktiv waren. Das betrifft alle, die sich in den letzten drei Tagen nicht in Ihrer App angemeldet haben und eine Nachricht erhalten sollen.

Sie verfügen über eine Kontextvariable `re_engagement_date`, die wie folgt definiert ist: {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Beachten Sie, dass `3 days` ein variabler Wert sein kann, der ebenfalls als angepasstes Attribut der Nutzer:in gespeichert wird. Wenn also das `re_engagement_date` nach dem `last_login_date` (als angepasstes Attribut im Nutzerprofil gespeichert) liegt, wird eine Nachricht gesendet.

![Eine Filtereinstellung mit angepassten Attributen als Personalisierungstyp für die Kontextvariable „re_engagement_date" nach dem angepassten Attribut „last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

Der folgende Filter vergleicht die Kontextvariable `reminder_date` dahingehend, ob sie vor der Kontextvariable `appointment_deadline` liegt. Dies kann dabei helfen, Nutzer:innen in einem Zielgruppenpfade-Schritt zu gruppieren, um zu entscheiden, ob sie vor Ablauf ihrer Terminfrist zusätzliche Erinnerungen erhalten sollten.

![Eine Filtereinstellung mit Kontextvariablen als Personalisierungstyp für die Kontextvariable „reminder_date" auf der Kontextvariable „appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Standardisierung der Zeitzonenkonsistenz

Während die meisten Event-Eigenschaften mit dem Zeitstempeltyp in Canvas bereits in UTC vorliegen, gibt es einige Ausnahmen. Mit der Einführung von Canvas Context werden alle Standard-Zeitstempel-Event-Eigenschaften in aktionsbasierten Canvases einheitlich in UTC angegeben. Diese Änderung ist Teil einer umfassenderen Maßnahme, um eine vorhersehbarere und konsistentere Erfahrung bei der Bearbeitung von Canvas-Schritten und -Nachrichten zu gewährleisten. Bitte beachten Sie, dass diese Änderung alle aktionsbasierten Canvase betrifft, unabhängig davon, ob das jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

{% alert important %}
Unter allen Umständen empfehlen wir dringend, [Liquid time_zone-Filter]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) für Zeitstempel zu verwenden, damit diese in der gewünschten Zeitzone dargestellt werden. Ein Beispiel finden Sie in dieser [häufig gestellten Frage im Artikel zum Kontext-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example).
{% endalert %}

## Verwandte Artikel

- [Kontext-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalisierung und dynamischer Content mit Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)