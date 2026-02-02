---
nav_title: Kontext-Variablen
article_title: Kontext-Variablen
page_type: reference
description: "Dieser referenzierte Artikel erklärt die Kontextvariablen in Braze Canvase, einschließlich ihrer Typen, ihrer Verwendung und der besten Methoden."
---

# Kontext-Variablen

> Kontextvariablen sind temporäre Daten, die Sie innerhalb der Reise eines Nutzers:innen durch ein bestimmtes Canvas erstellen und verwenden können. Sie ermöglichen es Ihnen, Verspätungen zu personalisieren, Nutzer:innen dynamisch zu segmentieren und Messaging anzureichern, ohne die Profil-Informationen eines Nutzers dauerhaft zu verändern. Kontextvariablen existieren nur innerhalb der Canvas-Sitzung und bleiben nicht über verschiedene Canvase oder außerhalb der Sitzung bestehen.

## Wie Kontextvariablen funktionieren

Kontextvariablen können auf zwei Arten gesetzt werden:

- **Am Eingang von Canvas:** Wenn Nutzer:innen ein Canvas betreten, können Daten aus dem Ereignis oder dem API-Trigger automatisch Kontextvariablen auffüllen.
- **In einem Context-Schritt:** Sie können Kontextvariablen innerhalb des Canvas manuell definieren oder aktualisieren, indem Sie einen [Context-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) hinzufügen.

Jede Kontextvariable umfasst:

- Ein Name (wie `flight_time` oder `subscription_renewal_date`)
- Ein Datentyp (z. B. Zahl, String, Zeit oder Array)
- Ein Wert, den Sie mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) oder über das Tool **Personalisierung hinzufügen** zuweisen.

Wenn Sie eine Kontextvariable definiert haben, können Sie sie im gesamten Canvas verwenden, indem Sie sie in diesem Format referenzieren: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Zum Beispiel könnte {% raw %}`{{context.${flight_time}}}`{% endraw %} die geplante Flugzeit des Nutzers:in zurückgeben.

Jedes Mal, wenn ein Nutzer:innen den Canvas betritt - auch wenn er ihn schon einmal betreten hat - werden die Kontextvariablen auf der Grundlage der letzten Eingabedaten und der Canvas-Einstellungen neu definiert. Dieser zustandsbasierte Ansatz lässt zu, dass jeder Canvas-Eingang seinen eigenen unabhängigen Kontext beibehält, so dass Nutzer:innen innerhalb ein und derselben Reise mehrere aktive Zustände haben können, während der spezifische Kontext für jeden Zustand beibehalten wird.

Wenn eine Kund:in beispielsweise zwei Flüge ansteht, hat sie zwei verschiedene Reisezustände, die gleichzeitig ablaufen - jeder mit seinen eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Ziel. So ist es zulässig, personalisierte Erinnerungen an den 14-Uhr-Flug nach New York zu senden und gleichzeitig verschiedene Updates für den morgigen 8-Uhr-Flug nach Los Angeles zu verschicken, so dass jede Nachricht für die jeweilige Buchung relevant bleibt.

## Überlegungen

Sie können bis zu 10 Kontextvariablen pro [Context-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/) definieren. Jeder Variablenname kann bis zu 100 Zeichen lang sein und darf nur Buchstaben, Zahlen oder Unterstriche enthalten.

Kontextvariablendefinitionen können bis zu 10.240 Zeichen lang sein. Wenn Sie Kontextvariablen in ein API-getriggertes Canvas übergeben, teilen sie sich denselben Namensraum wie Variablen, die in einem Kontext-Schritt erstellt wurden. Wenn Sie zum Beispiel eine Variable `purchased_item` im [Endpunkt-Kontextobjekt`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) senden, können Sie sie als {% raw %}`{{context.${purchased_item}}}`{% endraw %} referenzieren. Wenn Sie diese Variable in einem Kontextschritt neu definieren, überschreibt der neue Wert den API-Wert für die Reise des Nutzers:innen.

Sie können bis zu 50 KB pro Context-Schritt speichern, verteilt auf bis zu 10 Variablen. Wenn die Gesamtgröße aller Variablen in einem Schritt 50 KB überschreitet, werden alle Variablen, die diese Grenze überschreiten, nicht ausgewertet oder gespeichert. Wenn Sie beispielsweise drei Variablen in einem Context-Schritt haben:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

Die Variable 3 wird nicht ausgewertet oder gespeichert, da die Summe der vorherigen Variablen 50 KB überschreitet.

## Daten-Typen

Kontextvariablen, die in dem Schritt erstellt oder aktualisiert werden, können die folgenden Datentypen zugewiesen werden.

{% alert note %}
Kontextvariablen haben die gleichen erwarteten Formate für Datentypen wie [angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Bei der Verwendung des Array-Typs versucht Braze, den Wert als JSON zu parsen, wodurch Arrays von Objekten erfolgreich erstellt werden können. Wenn die Objekte in Ihren Arrays kein gültiges JSON sind, ist das Ergebnis ein einfaches String-Array. <br><br>Für verschachtelte Objekte und Arrays von Objekten verwenden Sie den [`as_json_string` Liquid Filter](#converting-connected-content-strings-to-json). Wenn Sie das gleiche Objekt in einem Context-Schritt erstellen, müssen Sie das Objekt mit `as_json_string` rendern. {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Datentyp | Beispiel für einen Variablennamen | Beispielwert |
|---|---|---|
|Boolesch| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Zahl| credit_score |{% raw %}<code>740</code>{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Array (von Objekten)| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|Uhrzeit (in UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objekt (abgeflacht) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Standardmäßig sind die Daten in UTC angegeben. Wenn Sie einen String-Datentyp verwenden, um einen Zeitwert zu speichern, können Sie die Zeit als eine andere Zeitzone wie PST definieren. 

Wenn Sie z.B. eine Nachricht an einen Nutzer am Tag vor seinem Geburtstag senden, würden Sie die Kontextvariable als Zeitdatentyp speichern, da mit dem Senden am Vortag eine Liquid-Logik verbunden ist. Wenn Sie jedoch eine Nachricht zu Weihnachten (25\. Dezember) versenden, brauchen Sie die Uhrzeit nicht als dynamische Variable zu referenzieren, so dass die Verwendung eines String-Datentyps vorzuziehen ist.

## Verwendung von Kontextvariablen

Sie können Kontextvariablen überall dort verwenden, wo Sie Liquid in einem Canvas einsetzen, z.B. in den Schritten für [Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) und [Nutzer:innen-Updates]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update), indem Sie **Personalisierung hinzufügen** auswählen.

Nehmen wir zum Beispiel an, Sie möchten Passagiere vor ihrem nächsten Flug über ihren Zugang zur VIP-Lounge informieren. Diese Nachricht sollte nur an Passagiere gesendet werden, die ein First-Class-Ticket gekauft haben. Eine Kontextvariable ist eine flexible Möglichkeit, diese Informationen zu tracken.

Nutzer:innen betreten das Canvas, wenn sie ein Flugticket kaufen. Um die Zugriffsberechtigung auf die Lounge zu bestimmen, erstellen wir in einem Kontextschritt eine Kontextvariable mit dem Namen `lounge_access_granted` und referenzieren diese Kontextvariable dann in den nachfolgenden Schritten der User:in.

![Kontextvariable, mit der Sie verfolgen können, ob sich ein Passagier für den Zugang zur VIP-Lounge qualifiziert.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

In diesem Schritt von Context verwenden wir {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %}, um festzustellen, ob die Art des Fluges, den sie gekauft haben, `first_class` ist.

Als Nächstes erstellen wir einen Schritt "Nachricht", um Nutzer:innen zu targetieren, bei denen {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} `true` ist. Bei dieser Nachricht handelt es sich um eine Push-Benachrichtigung, die personalisierte Lounge-Informationen enthält. Auf der Grundlage dieser Kontextvariablen erhalten die in Frage kommenden Passagiere die entsprechenden Nachrichten vor ihrem Flug.

- Passagiere der ersten Klasse erhalten ein Ticketing: "Genießen Sie exklusiven Zugang zur VIP-Lounge!"
- Passagiere von Business- und Economy-Tickets erhalten: "Upgraden Sie Ihren Flug für exklusiven Zugang zur VIP-Lounge."

![Ein Nachrichtenschritt mit verschiedenen Nachrichten, die Sie je nach Art des gekauften Flugtickets versenden können.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Sie können [personalisierte Verzögerungsoptionen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) mit den Informationen aus dem Schritt Kontext hinzufügen, d.h. Sie können die Variable auswählen, die Nutzer:innen verzögert.
{% endalert %}

### Für Aktions-Pfade und Ausstiegskriterien

In diesen triggernden Aktionen können Sie Filter zum Vergleich von Eigenschaften entweder mit Kontextvariablen oder angepassten Attributen nutzen: **Passen Sie ein angepasstes Event an** und **tätigen Sie einen Kauf**. Diese Aktion triggern unterstützt auch Eigenschaftsfilter sowohl für einfache als auch für verschachtelte Eigenschaften. 

- Beim Vergleich mit grundlegenden Eigenschaften entsprechen die verfügbaren Vergleiche dem Typ der Eigenschaft, die durch das angepasste Event definiert ist. Für die Eigenschaften von Strings gibt es zum Beispiel genau gleiche Regex-Übereinstimmungen. Boolesche Eigenschaften sind true oder false. 
- Beim Vergleich mit verschachtelten Eigenschaften sind die Typen nicht vordefiniert, so dass Sie ähnlich wie bei den Vergleichen für verschachtelte angepasste Attribute Vergleiche über mehrere Datentypen für Boolesche Werte, Zahlen, Strings, Zeit und Tag des Jahres auswählen können. Wenn Sie einen Datentyp auswählen, der nicht mit dem tatsächlichen Datentyp der verschachtelten Eigenschaft zum Zeitpunkt des Vergleichs übereinstimmt, wird der Nutzer:in nicht mit dem Aktions-Pfad oder den Ausstiegskriterien übereinstimmen.

#### Aktions-Pfad Beispiele

{% alert important %}
Für angepasste Attribut-Vergleiche verwenden wir den Wert des angepassten Attributs zu dem Zeitpunkt, an dem die Aktion ausgeführt wird. Das bedeutet, dass ein Nutzer:innen nicht mit der Gruppe Aktions-Pfad übereinstimmt, wenn dieses angepasste Attribut zum Zeitpunkt des Vergleichs nicht ausgefüllt ist oder wenn der Wert des angepassten Attributs nicht mit den definierten Eigenschaften übereinstimmt. Dies ist selbst dann der Fall, wenn der Nutzer:innen bei der Eingabe des Schritts Aktions-Pfad einen Treffer erzielt hätte.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

Der folgende Aktions-Pfad ist so eingerichtet, dass Nutzer:innen, die das angepasste Event `Account_Created` mit der grundlegenden Eigenschaft `source` ausgeführt haben, nach der Kontextvariablen `app_source_variable` sortiert werden.

![Ein Beispiel für einen Aktions-Pfad, der eine Kontextvariable referenziert, wenn ein angepasstes Event ausgeführt wird.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

Der folgende Aktions-Pfad wurde eingerichtet, um die grundlegende Eigenschaft `brand` für den spezifischen Produktnamen `shoes` mit einer Kontextvariablen `promoted_shoe_brand` abzugleichen.

![Ein Beispiel für einen Aktions-Pfad, der eine Kontextvariable referenziert, wenn Sie einen Kauf tätigen.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Beispiele für Ausstiegskriterien

{% tabs %}
{% tab Perform custom event %}

Die Ausstiegskriterien besagen, dass ein Nutzer:in den Canvas einsteigen kann, wenn er den Canvas an einem beliebigen Punkt verlässt:

- Sie führen das angepasste Event **Warenkorb-Abbruch** durch, und
- Die grundlegende Eigenschaft **Artikel im Warenkorb** entspricht dem String-Wert der Kontextvariablen `cart_item_threshold`.

![Beendigungskriterien, die eingerichtet wurden, um einen Nutzer:in zu beenden, wenn er ein angepasstes Event auf der Basis der Kontextvariablen ausführt.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Die Ausstiegskriterien besagen, dass ein Nutzer:in den Canvas einsteigen kann, wenn er den Canvas an einem beliebigen Punkt verlässt:

- Sie kaufen gezielt den Produktnamen "Buch", und
- Die verschachtelte Eigenschaft "loyalty_program" dieses Kaufs ist gleich dem angepassten Attribut "VIP" des Nutzers:in.

![Beendigungskriterien, um einen Nutzer:innen zu beenden, wenn er einen Kauf tätigt.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Kontextabhängige Filter

Sie können Filter erstellen, die zuvor deklarierte Kontextvariablen in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [Decision-Split-Schritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) verwenden.

{% alert note %}
Kontextvariable Filter sind nur für Zielgruppen-Pfade und Decision-Split-Schritte verfügbar.
{% endalert %}

Kontextvariablen werden deklariert und sind nur im Bereich eines Canvas zugänglich, d.h. sie können nicht in Segmenten referenziert werden. Kontextvariable Filter funktionieren in Zielgruppen-Pfaden und Decision-Split-Schritten ähnlich - Zielgruppen-Pfade repräsentieren mehrere Gruppen, während Decision-Split-Schritte binäre Entscheidungen darstellen.

![Beispiel für einen Decision-Split-Schritt mit der Option, einen Filter mit einer Kontextvariablen zu erstellen.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Ähnlich wie Canvas-Kontextvariablen vordefinierte Typen haben, müssen die Vergleiche zwischen Kontextvariablen und statischen Werten [übereinstimmende Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types) haben. Der Filter für Kontextvariablen lässt Vergleiche über mehrere Datentypen für Boolesche Werte, Zahlen, Strings, Zeit und Tag des Jahres zu, ähnlich wie bei den Vergleichen für [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Verwenden Sie für Ihre Kontextvariable und den Vergleich denselben Datentyp. Wenn es sich bei Ihrer Kontextvariablen beispielsweise um einen zeitlichen Datentyp handelt, verwenden Sie Zeitvergleiche (wie "vor" oder "nach"). Die Verwendung nicht übereinstimmender Datentypen (z.B. String-Vergleiche mit einer Zeitkontextvariablen) kann zu unerwartetem Verhalten führen.
{% endalert %}

Hier ist ein Beispiel für einen Filter für Kontextvariablen, der die Kontextvariable `product_name` mit der Regex `/braze/` vergleicht.

![Ein Filter, der für die Kontextvariable "product_name" eingerichtet wurde, um mit der Regex "/braze/" übereinzustimmen.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Abgleich mit Kontextvariablen oder angepassten Attributen

Wenn Sie die Option **Mit einer Kontextvariablen oder einem angepassten Attribut vergleichen** auswählen, können Sie Filter für Kontextvariablen erstellen, die mit zuvor definierten Kontextvariablen oder angepassten Attributen von Nutzern:innen verglichen werden. Dies kann nützlich sein, um Vergleiche durchzuführen, die dynamisch pro Nutzer:in sind, wie z.B. API-getriggerte `context`, oder um komplexe Vergleichslogik, die über Kontextvariablen definiert ist, zu verdichten.

{% tabs %}
{% tab Example 1 %}

Nehmen wir an, Sie möchten Nutzern:innen nach einer dynamischen Inaktivitätsperiode eine personalisierte Erinnerung schicken. Das bedeutet, dass jeder, der sich in den letzten drei Tagen nicht in Ihrer App angemeldet hat, eine Nachricht erhalten soll.

Sie haben eine Kontextvariable `re_engagement_date`, die als {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} definiert ist. Beachten Sie, dass `3 days` ein variabler Betrag sein kann, der auch als angepasstes Attribut eines Nutzers:innen gespeichert wird. Wenn also die `re_engagement_date` nach der `last_login_date` steht (die als angepasstes Attribut im Nutzerprofil gespeichert ist), wird ihnen eine Nachricht geschickt.

![Eine Filtereinrichtung mit angepassten Attributen als Personalisierungstyp für die Kontextvariable "re_engagement_date" nach dem angepassten Attribut "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

Der folgende Filter vergleicht, ob die Kontextvariable `reminder_date` vor der Kontextvariablen `appointment_deadline` liegt. Auf diese Weise können Sie Nutzer:innen in einem Zielgruppen-Pfad gruppieren, um festzustellen, ob sie vor ihrem Termin zusätzliche Erinnerungen erhalten sollen.

![Eine Filtereinrichtung mit Kontextvariablen als Personalisierungstyp für die Kontextvariable "reminder_date" auf der Kontextvariable "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Standardisierung der Zeitzonenkonsistenz

Während die meisten Event-Eigenschaften, die den Typ Zeitstempel verwenden, in Canvas bereits in UTC vorliegen, gibt es einige Ausnahmen. Mit der Hinzufügung von Canvas Context werden alle Standard Zeitstempel Event-Eigenschaften in aktionsbasierten Canvase durchgängig in UTC angegeben. Diese Änderung ist Teil umfassenderer Bemühungen, die Bearbeitung von Canvas-Schritten und Nachrichten berechenbarer und konsistenter zu gestalten. Beachten Sie, dass sich diese Änderung auf alle aktionsbasierten Canvase auswirkt, unabhängig davon, ob das jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

{% alert important %}
In jedem Fall empfehlen wir dringend die Verwendung von [Liquid time_zone Filtern]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know), damit die Zeitstempel in der gewünschten Zeitzone dargestellt werden. Sie können diese [häufig gestellte Frage in dem Artikel Kontextschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) als Beispiel referenzieren.
{% endalert %}

## Ähnliche Artikel

- [Schritt zum Kontext]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalisierung und dynamischer Content mit Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
