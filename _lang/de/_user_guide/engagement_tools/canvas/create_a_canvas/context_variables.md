---
nav_title: Kontextvariablen
article_title: Kontextvariablen
page_type: reference
description: "Dieser Referenzartikel erläutert Kontextvariablen in Braze Canvases, einschließlich ihrer Typen, Verwendung und bewährten Verfahren."
---

# Kontextvariablen

> Kontextvariablen sind temporäre Datenelemente, die Sie erstellen und innerhalb der Reise der Nutzer:innen durch ein bestimmtes Canvas verwenden können. Sie ermöglichen es Ihnen, Verzögerungen individuell zu personalisieren, Nutzer:innen dynamisch zu segmentieren und Nachrichten zu bereichern, ohne das Profil einer Nutzer:in dauerhaft zu verändern. Kontextvariablen existieren nur innerhalb der Canvas-Sitzung und sind nicht über verschiedene Canvases hinweg oder außerhalb der Sitzung persistent.

## Wie Kontextvariablen funktionieren

Kontextvariablen können auf zwei Arten festgelegt werden:

- **Am Eingang von Canvas:** Wenn Nutzer:innen ein Canvas betreten, können Daten aus dem Ereignis oder dem API-Trigger automatisch Kontextvariablen auffüllen.
- **In einem Context-Schritt:** Sie können Kontextvariablen manuell innerhalb des Canvas definieren oder ein Update durchführen, indem Sie einen [Kontext-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) hinzufügen.

Jede Kontextvariable umfasst:

- Ein Name (wie `flight_time` oder `subscription_renewal_date`)
- Ein Datentyp (wie beispielsweise Zahl, String, Zeit oder Array)
- Ein Wert, den Sie mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) oder über das Tool **Personalisierung hinzufügen** zuweisen.

Wenn Sie eine Kontextvariable definiert haben, können Sie sie im gesamten Canvas verwenden, indem Sie sie in diesem Format referenzieren: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Beispielsweise könnte die Zeit im Zeitplan der Nutzer:{% raw %}`{{context.${flight_time}}}`{% endraw %}innen für den Flug zurückgegeben werden.

Jedes Mal, wenn ein Nutzer:innen den Canvas betritt - auch wenn er ihn schon einmal betreten hat - werden die Kontextvariablen auf der Grundlage der letzten Eingabedaten und der Canvas-Einstellungen neu definiert. Dieser zustandsbehaftete Ansatz ermöglicht es jedem Canvas-Eintrag, seinen eigenen unabhängigen Kontext beizubehalten, sodass Nutzer:innen mehrere aktive Zustände innerhalb derselben Journey haben können, während der spezifische Kontext für jeden Zustand erhalten bleibt.

Wenn eine Kund:in beispielsweise zwei bevorstehende Flüge hat, gibt es zwei separate Reisestatus, die gleichzeitig ablaufen – jeder mit seinen eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Ziel:e. Auf diese Weise ist es zulässig, personalisierte Erinnerungen für den Flug um 14 Uhr nach New York zu versenden und gleichzeitig verschiedene Updates für den Flug um 8 Uhr nach Los Angeles morgen bereitzustellen, sodass jede Nachricht für die jeweilige Buchung relevant bleibt.

## Überlegungen

Sie können bis zu 10 Kontextvariablen pro [Kontextschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/) definieren. Jeder Variablenname kann bis zu 100 Zeichen lang sein und darf nur Buchstaben, Zahlen oder Unterstriche enthalten.

Kontextvariable-Definitionen können bis zu 10.240 Zeichen umfassen. Wenn Sie Kontextvariablen an ein API-gesteuertes Canvas übergeben, verwenden diese denselben Namespace wie Variablen, die in einem Kontext-Schritt erstellt wurden. Wenn Sie beispielsweise eine Variable`purchased_item`im [`/canvas/trigger/send`Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)-Objekt referenzieren, können Sie diese {% raw %}`{{context.${purchased_item}}}`{% endraw %}referenzieren. Wenn Sie diese Variable in einem Kontext-Schritt neu definieren, überschreibt der neue Wert den API-Wert für die Journey dieser Nutzer:innen.

Sie können bis zu 50 KB pro Kontext-Schritt speichern, verteilt auf bis zu 10 Variablen. Wenn die Gesamtgröße aller Variablen in einem Schritt 50 KB überschreitet, werden alle Variablen, die diese Grenze überschreiten, nicht ausgewertet oder gespeichert. Wenn Sie beispielsweise drei Variablen in einem Kontext-Schritt haben:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

Die Variable 3 wird nicht ausgewertet oder gespeichert, da die Summe der vorherigen Variablen 50 KB überschreitet.

## Daten-Typen

Kontextvariablen, die in dem Schritt erstellt oder aktualisiert werden, können die folgenden Datentypen zugewiesen werden.

{% alert note %}
Kontextvariablen haben dieselben erwarteten Formate für Datentypen wie [angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Bei Verwendung des Array-Typs versucht Braze, den Wert als JSON zu analysieren, wodurch Arrays von Objekten erfolgreich erstellt werden können. Wenn die Objekte in Ihren Arrays kein gültiges JSON sind, ist das Ergebnis ein einfaches String-Array. <br><br>Für verschachtelte Objekte und Objekt-Arrays verwenden Sie bitte den[`as_json_string`](#converting-connected-content-strings-to-json)[Liquid-Filter](#converting-connected-content-strings-to-json). Wenn Sie dasselbe Objekt in einem Kontext-Schritt erstellen, müssen Sie das Objekt mit Hilfe `as_json_string`von rendern, beispielsweise {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Datentyp | Beispiel für einen Variablennamen | Beispielwert |
|---|---|---|
|Boolesch| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Zahl| credit_score |{% raw %}<code>740</code>{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Array (von Objekten)| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|Zeit (in UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objekt (abgeflacht) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Standardmäßig ist der Datentyp „Zeit“ auf UTC eingestellt. Wenn Sie einen Zeitwert mit dem Datentyp „String“ speichern, können Sie die Zeit als andere Zeitzone, beispielsweise PST, definieren. 

Wenn Sie beispielsweise einer Nutzer:in einen Tag vor ihrem Geburtstag eine Nachricht senden möchten, sollten Sie die Kontextvariable als Zeitdatentyp speichern, da mit dem Versand am Vortag eine Liquid-Logik verbunden ist. Wenn Sie jedoch eine Weihnachtsnachricht am ersten Weihnachtsfeiertag (25\. Dezember) versenden, ist es nicht erforderlich, die Uhrzeit als dynamische Variable zu referenzieren, sodass die Verwendung eines String-Datentyps vorzuziehen wäre.

## Verwendung von Kontextvariablen

Sie können Kontextvariablen überall dort verwenden, wo Sie Liquid in einem Canvas einsetzen, beispielsweise in den Schritten [„Nachricht“]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) und [„Benutzerupdate“]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update), indem Sie **„Personalisierung hinzufügen“** auswählen.

Nehmen wir zum Beispiel an, Sie möchten Passagiere vor ihrem nächsten Flug über ihren Zugang zur VIP-Lounge informieren. Diese Nachricht sollte nur an Passagiere gesendet werden, die ein First-Class-Ticket gekauft haben. Eine Kontextvariable ist eine flexible Möglichkeit, diese Informationen zu tracken.

Nutzer:innen betreten das Canvas, wenn sie ein Flugticket kaufen. Um die Zugriffsberechtigung auf die Lounge zu bestimmen, erstellen wir in einem Kontextschritt eine Kontextvariable mit dem Namen `lounge_access_granted` und referenzieren diese Kontextvariable dann in den nachfolgenden Schritten der User:in.

![Kontextvariable eingerichtet für Tracking, um zu verfolgen, ob ein Passagier für den Zugang zur VIP-Lounge qualifiziert ist.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

In diesem Schritt von Context verwenden wir {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %}, um festzustellen, ob die Art des Fluges, den sie gekauft haben, `first_class` ist.

Als Nächstes erstellen wir einen Schritt "Nachricht", um Nutzer:innen zu targetieren, bei denen {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} `true` ist. Diese Nachricht wird als Push-Benachrichtigung versendet und enthält personalisierte Informationen zur Lounge. Auf der Grundlage dieser Kontextvariablen erhalten die in Frage kommenden Passagiere die entsprechenden Nachrichten vor ihrem Flug.

- Passagiere der ersten Klasse erhalten ein Ticketing: "Genießen Sie exklusiven Zugang zur VIP-Lounge!"
- Passagiere von Business- und Economy-Tickets erhalten: "Upgraden Sie Ihren Flug für exklusiven Zugang zur VIP-Lounge."

![Ein Nachrichtenschritt mit unterschiedlichen Nachrichten, die je nach Art des gekauften Flugtickets versendet werden.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Sie können [personalisierte Verzögerungsoptionen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) mit den Informationen aus dem Schritt Kontext hinzufügen, d.h. Sie können die Variable auswählen, die Nutzer:innen verzögert.
{% endalert %}

### Für Aktions-Pfade und Ausstiegskriterien

Sie können in diesen Trigger-Aktionen den Vergleich von Eigenschaftsfiltern mit Kontextvariablen oder angepassten Attributen nutzen: **Passen Sie ein angepasstes Event an** und **tätigen Sie einen Kauf**. Diese Aktionsauslöser unterstützen auch Filter für grundlegende und verschachtelte Eigenschaften. 

- Beim Vergleich mit grundlegenden Eigenschaften entsprechen die verfügbaren Vergleiche dem Typ der Eigenschaft, die durch das angepasste Event definiert ist. Beispielsweise weisen String-Eigenschaften exakt gleiche Regex-Übereinstimmungen auf. Boolesche Eigenschaften können entweder wahr oder falsch sein. 
- Im Gegensatz zu verschachtelten Eigenschaften sind die Typen nicht vordefiniert, sodass Sie Vergleiche über mehrere Datentypen hinweg für Boolesche Werte, Zahlen, Strings, Uhrzeiten und Tage des Jahres auswählen können, ähnlich wie bei den Vergleichen für verschachtelte angepasste Attribute. Wenn Sie einen Datentyp auswählen, der zum Zeitpunkt des Vergleichs nicht mit dem tatsächlichen Datentyp der verschachtelten Eigenschaft übereinstimmt, wird der Nutzer:in den Aktions-Pfad oder die Ausstiegskriterien nicht erfüllen.

#### Beispiele für Aktions-Pfade

{% alert important %}
Für den Vergleich von benutzerdefinierten Attributen verwenden wir den Wert des benutzerdefinierten Attributs zum Zeitpunkt der Ausführung der Aktion. Dies bedeutet, dass eine Nutzer:in nicht mit der Aktions-Pfad-Gruppe übereinstimmt, wenn dieses benutzerdefinierte Attribut zum Zeitpunkt des Vergleichs nicht ausgefüllt ist oder wenn der Wert des benutzerdefinierten Attributs nicht mit den definierten Eigenschaftsvergleichen übereinstimmt. Dies gilt auch dann, wenn die Nutzer:innen beim Aufrufen des Schritts „Aktions-Pfad“ übereinstimmen.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

Der folgende Aktions-Pfad ist eingerichtet, um Nutzer:innen, die das angepasste Event`Account_Created`mit der Grundeigenschaft ausgeführt haben, in `source`die Kontextvariable zu `app_source_variable`sortieren.

![Ein Beispiel für einen Aktions-Pfad, der bei der Ausführung eines angepassten Events auf eine Kontextvariable referenziert.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

Der folgende Aktions-Pfad ist so eingerichtet, dass er die grundlegende Eigenschaft`brand`für den spezifischen Produktnamen`shoes`einer Kontextvariablen zuordnet`promoted_shoe_brand`.

![Ein Beispiel für einen Aktions-Pfad, der beim Kauf eine Kontextvariable referenziert.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Beispiele für Austrittskriterien

{% tabs %}
{% tab Perform custom event %}

Die Ausstiegskriterien besagen, dass eine Nutzer:in zu jedem Zeitpunkt ihrer Reise im Canvas den Canvas verlässt, wenn:

- Sie führen das angepasste Event **„Warenkorb verlassen**“ aus und
- Die grundlegende Eigenschaft **„Artikel im Warenkorb**“ entspricht dem String-Wert der Kontextvariablen`cart_item_threshold`.

![Beendigungskriterien, die festgelegt werden, um einen Nutzer:in zu beenden, wenn er ein angepasstes Event basierend auf der Kontextvariablen ausführt.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Die Ausstiegskriterien besagen, dass eine Nutzer:in zu jedem Zeitpunkt ihrer Reise im Canvas den Canvas verlässt, wenn:

- Sie tätigen einen spezifischen Kauf für das Produkt mit dem Namen „Buch“ und
- Die verschachtelte Eigenschaft dieses "loyalty_program"Kaufs entspricht dem benutzerdefinierten Attribut „VIP” des Nutzers.

![Es wurden Kriterien festgelegt, um eine Nutzer:in zu entfernen, wenn sie einen Kauf tätigt.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Kontextvariable Filter

Sie können Filter erstellen, die zuvor in den Schritten [„Zielgruppen-Pfade“]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [„Decision-Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)-Schritte“ deklarierte Kontextvariablen verwenden.

{% alert note %}
Kontextvariable Filter sind ausschließlich für Zielgruppen-Pfade und Decision-Split-Schritte verfügbar.
{% endalert %}

Kontextvariablen werden deklariert und sind nur im Bereich eines Canvas zugänglich, was bedeutet, dass sie in Segmenten nicht referenziert werden können. Kontextvariable Filter funktionieren in Zielgruppen-Pfaden und Decision-Split-Schritten ähnlich – Zielgruppen-Pfade repräsentieren mehrere Gruppen, während Decision-Split-Schritte binäre Entscheidungen darstellen.

![Decision-Split-Schritt-Beispiel mit der Option, einen Filter mit einer Kontextvariablen zu erstellen.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Ähnlich wie Canvas-Kontextvariablen vordefinierte Typen haben, müssen die Vergleiche zwischen Kontextvariablen und statischen Werten [übereinstimmende Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types) aufweisen. Der Kontextvariablenfilter ermöglicht Vergleiche zwischen mehreren Datentypen für Boolesche Werte, Zahlen, Strings, Uhrzeiten und Tage des Jahres, ähnlich wie bei den Vergleichen für [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Verwenden Sie für Ihre Kontextvariable und den Vergleich denselben Datentyp. Wenn Ihre Kontextvariable beispielsweise vom Datentyp „Zeit“ ist, verwenden Sie Zeitvergleiche (wie „vor“ oder „nach“). Die Verwendung nicht übereinstimmender Datentypen (wie beispielsweise String-Vergleiche mit einer Zeitkontextvariablen) kann zu unerwartetem Verhalten führen.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Hier ist ein Beispiel für einen Kontextvariablen-Filter, der die Kontextvariable`product_name`mit dem Regex vergleicht`/braze/`.

![Eine Filtereinstellung für die Kontextvariable, "product_name"die mit dem Regex „/Braze/“ übereinstimmt.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Vergleich mit Kontextvariablen oder benutzerdefinierten Attributen

Durch Auswahl der Option **„Mit einer Kontextvariablen oder einem benutzerdefinierten Attribut vergleichen**“ können Sie Filter erstellen, die mit zuvor definierten Kontextvariablen oder benutzerdefinierten Attributen verglichen werden. Dies kann nützlich sein, um dynamische Vergleiche pro Nutzer:in durchzuführen, beispielsweise API-gesteuerte`context`, oder um komplexe Vergleichslogik zu verdichten, die über Kontextvariablen definiert ist.

{% tabs %}
{% tab Example 1 %}

Angenommen, Sie möchten eine personalisierte Erinnerung an Nutzer:innen senden, die eine dynamische Zeit lang inaktiv waren. Das betrifft alle Nutzer:innen, die sich in den letzten drei Tagen nicht in Ihrer App angemeldet haben und eine Nachricht erhalten sollen.

Sie verfügen über eine Kontextvariable, `re_engagement_date`die wie folgt definiert{% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} ist. Bitte beachten Sie, dass`3 days`es sich um einen variablen Betrag handeln kann, der ebenfalls als benutzerdefiniertes Attribut gespeichert wird. Wenn also das  nach dem`last_login_date`  (als benutzerdefiniertes `re_engagement_date`Attribut im Nutzerprofil gespeichert) steht, wird eine Nachricht an den Nutzer gesendet.

![Eine Filtereinstellung mit angepassten Attributen als Personalisierungstyp für die Kontextvariable"re_engagement_date"nach dem angepassten Attribut/assets/img/context_variable_filter2.pngimage_buster"last_login_date".]({%%})

{% endtab %}
{% tab Example 2 %}

Der folgende Filter vergleicht die Kontextvariable`reminder_date`  mit der Kontextvariable `appointment_deadline`. Dies kann Gruppennutzer:innen in einem Schritt „Zielgruppen-Pfade“ dabei helfen, zu entscheiden, ob sie vor Ablauf ihrer Terminfrist zusätzliche Erinnerungen erhalten sollten.

![Eine Filtereinstellung mit Kontextvariablen als Typ der Personalisierung für die Kontextvariable"reminder_date"auf der Kontextvariable/assets/img/context_variable_filter3.pngimage_buster"appointment_deadline".]({%%})

{% endtab %}
{% endtabs %}

## Standardisierung der Zeitzonenkonsistenz

Während die meisten Event-Eigenschaften, die den Zeitstempeltyp verwenden, in Canvas bereits in UTC vorliegen, gibt es einige Ausnahmen. Mit der Einführung von Canvas Context werden alle Standard-Zeitstempel-Event-Eigenschaften in aktionsbasierten Canvases einheitlich in UTC angegeben. Diese Änderung ist Teil einer umfassenderen Maßnahme, um eine vorhersehbarere und konsistentere Erfahrung bei der Bearbeitung von Canvas-Schritten und -Nachrichten zu gewährleisten. Bitte beachten Sie, dass diese Änderung Auswirkungen auf alle aktionsbasierten Canvases hat, unabhängig davon, ob das jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

{% alert important %}
Unter allen Umständen empfehlen wir dringend, [time_zoneLiquid-Filter]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) für Zeitstempel zu verwenden, die in der gewünschten Zeitzone dargestellt werden sollen. Sie können diese [häufig gestellte Frage im Artikel zum Kontext-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) referenzieren und als Beispiel verwenden.
{% endalert %}

## Ähnliche Artikel

- [Kontextschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalisierung und dynamischer Content mit Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
