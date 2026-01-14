---
nav_title: Kontext 
article_title: Kontext 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "Dieser referenzierte Artikel beschreibt, wie Sie Kontext-Schritte in Ihrem Canvas erstellen und verwenden."
tool: Canvas

---

# Kontext

> Kontextschritte erlauben es Ihnen, eine oder mehrere Variablen für einen Nutzer:innen zu erstellen und zu aktualisieren, während er sich durch ein Canvas bewegt. Wenn Sie zum Beispiel ein Canvas haben, das saisonale Rabatte verwaltet, können Sie eine Kontextvariable verwenden, um jedes Mal, wenn ein Nutzer:in das Canvas eintritt, einen anderen Rabattcode zu speichern.

{% alert important %}
Context Steps befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Konto Manager:in, wenn Sie an der Teilnahme an diesem frühen Zugang interessiert sind.<br><br>Beachten Sie, dass sich durch das Opt-in für den frühen Zugriff auf den Canvas-Kontext-Schritt die Handhabung von Zeitstempeln in allen Ihren Canvase ändert. Um mehr darüber zu erfahren, referenzieren Sie auf [Standardisierung der Zeitzonenkonsistenz](#time-zone-consistency-standardization).
{% endalert %}

## Funktionsweise

![Ein Context-Schritt als erster Schritt eines Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Mit Kontextschritten können Sie temporäre Daten während der Reise eines Nutzers:innen durch einen bestimmten Canvas erstellen und verwenden. Diese Daten existieren nur innerhalb dieser Canvas-Reise und bleiben nicht über verschiedene Canvase oder außerhalb der Sitzung bestehen.

Innerhalb dieses Rahmens kann jeder Kontextschritt mehrere Kontextvariablen definieren - temporäre Daten, die es Ihnen ermöglichen, Verzögerungen zu personalisieren, Nutzer:innen dynamisch zu segmentieren und Messaging anzureichern, ohne die Profilinformationen eines Nutzers dauerhaft zu verändern.

Wenn Sie zum Beispiel Flugbuchungen verwalten, könnten Sie eine Kontextvariable für die geplante Flugzeit jedes Nutzers:innen erstellen. Sie könnten dann Verzögerungen in Bezug auf die Flugzeit jedes Nutzers:innen festlegen und personalisierte Erinnerungen von demselben Canvas aus versenden.

Sie können Kontextvariablen auf zwei Arten setzen:

- **Am Eingang von Canvas:** Wenn Nutzer:innen ein Canvas betreten, können Daten aus dem Ereignis oder dem API-Trigger automatisch Kontextvariablen auffüllen.
- **In einem Context-Schritt:** Sie können Kontextvariablen innerhalb des Canvas manuell definieren oder aktualisieren, indem Sie einen Context-Schritt hinzufügen.

Jede Kontextvariable umfasst:

- Ein Name (wie `flight_time` oder `subscription_renewal_date`)
- Ein [Datentyp](#context-variable-types) (z. B. Zahl, String, Zeit oder Array)
- Ein Wert, den Sie mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) oder über das Tool **Personalisierung hinzufügen** zuweisen.

Wenn Sie eine Kontextvariable definiert haben, können Sie sie im gesamten Canvas verwenden, indem Sie sie in diesem Format referenzieren: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Zum Beispiel könnte {% raw %}`{{context.${flight_time}}}`{% endraw %} die geplante Flugzeit des Nutzers:in zurückgeben.

Jedes Mal, wenn ein Nutzer:innen den Canvas betritt - auch wenn er ihn schon einmal betreten hat - werden die Kontextvariablen auf der Grundlage der letzten Eingabedaten und der Canvas-Einstellungen neu definiert. Dieser zustandsbasierte Ansatz lässt zu, dass jeder Canvas-Eingang seinen eigenen unabhängigen Kontext beibehält, so dass Nutzer:innen innerhalb ein und derselben Reise mehrere aktive Zustände haben können, während der spezifische Kontext für jeden Zustand beibehalten wird.

Wenn eine Kund:in beispielsweise zwei Flüge ansteht, hat sie zwei verschiedene Reisezustände, die gleichzeitig ablaufen - jeder mit seinen eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Ziel. So ist es zulässig, personalisierte Erinnerungen an den 14-Uhr-Flug nach New York zu senden und gleichzeitig verschiedene Updates für den morgigen 8-Uhr-Flug nach Los Angeles zu verschicken, so dass jede Nachricht für die jeweilige Buchung relevant bleibt.

## Überlegungen

- Sie können bis zu 10 Kontextvariablen pro Context-Schritt haben.
- Jeder Name einer Kontextvariablen kann bis zu 100 Zeichen lang sein.
- Die Namen der Kontextvariablen müssen gültige Bezeichner sein (nur Buchstaben, Zahlen, Unterstriche).
- Kontextvariablendefinitionen können bis zu 10.240 Zeichen lang sein. 
- Kontextvariablen, die an ein API-getriggertes Canvas übergeben werden, teilen sich dieselben Namespaces wie Kontextvariablen, die in einem Context-Schritt in einem Canvas erstellt werden. Das bedeutet, wenn Sie eine Variable `purchased_item` im [Endpunkt-Kontextobjekt]({{site.baseurl}}/api/objects_filters/context_object) `/canvas/trigger/send` senden, kann sie als {% raw %}`{context.${purchased_item}}`{% endraw %} referenziert werden. Wenn Sie diese Variable in einem Kontext-Schritt im Canvas erneut deklarieren, wird das, was zuvor gesendet wurde, außer Kraft gesetzt.
- Sie können bis zu 50 KB pro Kontextschritt speichern, verteilt auf bis zu 10 Variablen pro Schritt. Variablengrößen, die sich in einem Schritt auf über 50 KB summieren, werden für die Nutzer:innen nicht ausgewertet oder gespeichert. Diese Größen werden nacheinander berechnet. Wenn Sie zum Beispiel 3 Variablen in einem Kontextschritt haben:
  - Variable 1: 30 KB
  - Variable 2: 19 KB
  - Variable 3: 2 KB
  - Das bedeutet, dass die Variable 3 nicht ausgewertet oder gespeichert wird, weil die Summe aller anderen Kontextvariablen 50 KB übersteigt.

## Erstellen eines Kontextschritts

### Schritt 1: Einen Schritt hinzufügen

Fügen Sie Ihrem Canvas einen Schritt hinzu, und ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> und dann **Kontext**.

### Schritt 2: Definieren Sie die Variablen

{% alert note %}
Sie können bis zu 10 Kontextvariablen für jeden Context-Schritt definieren.
{% endalert %}

So definieren Sie eine Kontextvariable:

1. Geben Sie Ihrer Kontextvariablen einen **Namen**.
2. Wählen Sie einen [Datentyp](#context-variable-types) aus.
3. Schreiben Sie einen Liquid-Ausdruck manuell oder verwenden Sie **Personalisierung hinzufügen**, um ein Liquid-Snippet aus bereits vorhandenen Attributen zu erstellen.
4. Wählen Sie **Vorschau**, um den Wert Ihrer Kontextvariablen zu überprüfen.
5. (Optional) Um weitere Variablen hinzuzufügen, wählen Sie **Kontextvariable hinzufügen** und wiederholen Sie die Schritte 1-4.
6. Wenn Sie fertig sind, wählen Sie **Fertig**.

Jetzt können Sie Ihre Kontextvariable überall dort verwenden, wo Sie Liquid einsetzen, z.B. in den Schritten Nachrichten und Nutzer:innen Update, indem Sie **Personalisierung hinzufügen** auswählen. Eine vollständige Anleitung finden Sie unter [Verwendung von Kontextvariablen](#using-context-variables).

## Kontextvariable Datentypen {#context-variable-types}

Kontextvariablen, die in dem Schritt erstellt oder aktualisiert werden, können die folgenden Datentypen zugewiesen werden.

{% alert note %}
Kontextvariablen haben die gleichen erwarteten Formate für Datentypen wie [angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Für verschachtelte Objekte und Arrays von Objekten verwenden Sie den [`as_json_string` Liquid Filter](#converting-connected-content-strings-to-json). Wenn Sie das gleiche Objekt in einem Context-Schritt erstellen, müssen Sie das Objekt mit `as_json_string` rendern. {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Datentyp | Beispiel für einen Variablennamen | Beispielwert |
|---|---|---|
|Boolesch| loyalty_program |{% raw %}<code>wahr</code>{% endraw %}| 
|Zahl| credit_score |{% raw %}<code>740{% endraw %}|
|String| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Array| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Uhrzeit (in UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objekt (abgeflacht) | user_profile|{% raw %}<code>{<br> "first_name": "{{user.first_name}}",<br> "last_name": "{{user.last_name}}",<br> "E-Mail": "{{user.email}}",<br> "loyalty_points": {{user.loyalty_points}},<br> "preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Standardmäßig sind die Daten in UTC angegeben. Wenn Sie einen String-Datentyp verwenden, um einen Zeitwert zu speichern, können Sie die Zeit als eine andere Zeitzone wie PST definieren. 

Wenn Sie z.B. eine Nachricht an einen Nutzer am Tag vor seinem Geburtstag senden, würden Sie die Kontextvariable als Zeitdatentyp speichern, da mit dem Senden am Vortag eine Liquid-Logik verbunden ist. Wenn Sie jedoch eine Nachricht zu Weihnachten (25\. Dezember) versenden, brauchen Sie die Uhrzeit nicht als dynamische Variable zu referenzieren, so dass die Verwendung eines String-Datentyps vorzuziehen ist.

## Verwendung von Kontextvariablen {#using-context-variables}

Nehmen wir zum Beispiel an, Sie möchten Passagiere vor ihrem nächsten Flug über ihren Zugang zur VIP-Lounge informieren. Diese Nachricht sollte nur an Passagiere gesendet werden, die ein First-Class-Ticket gekauft haben. Eine Kontextvariable ist eine flexible Möglichkeit, diese Informationen zu tracken.

Nutzer:innen betreten das Canvas, wenn sie ein Flugticket kaufen. Um die Zugriffsberechtigung auf die Lounge zu bestimmen, erstellen wir in einem Kontextschritt eine Kontextvariable mit dem Namen `lounge_access_granted` und referenzieren diese Kontextvariable dann in den nachfolgenden Schritten der User:in.

Kontextvariable zum Tracking, ob sich ein Passagier für den Zugang zur VIP-Lounge qualifiziert.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

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

- Beim Vergleich mit grundlegenden Eigenschaften entsprechen die verfügbaren Vergleiche dem Typ der Eigenschaft, die durch das angepasste Event definiert ist. Für die Eigenschaften von Strings gibt es zum Beispiel genau gleiche Regex-Treffer. Boolesche Eigenschaften sind true oder false. 
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

![Beendigungskriterien, die so eingerichtet sind, dass ein Nutzer:in beendet wird, wenn er ein angepasstes Event auf der Grundlage der Kontextvariablen ausführt.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Die Ausstiegskriterien besagen, dass ein Nutzer:in den Canvas einsteigen kann, wenn er den Canvas an einem beliebigen Punkt verlässt:

- Sie kaufen gezielt den Produktnamen "Buch", und
- Die verschachtelte Eigenschaft "loyalty_program" dieses Kaufs ist gleich dem angepassten Attribut "VIP" des Nutzers:in.

![Exit-Kriterien eingerichtet, um Nutzer:innen zu verlassen, wenn sie einen Kauf tätigen.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Kontextabhängige Filter

Sie können Filter erstellen, die zuvor deklarierte Kontextvariablen in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [Decision-Split-Schritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) verwenden.

{% alert important %}
Kontextvariable Filter sind nur für Zielgruppen-Pfade und Decision-Split-Schritte verfügbar.
{% endalert %}

Kontextvariablen werden deklariert und sind nur im Bereich eines Canvas zugänglich, d.h. sie können nicht in Segmenten referenziert werden. Kontextvariable Filter funktionieren in Zielgruppen-Pfaden und Decision-Split-Schritten ähnlich - Zielgruppen-Pfade repräsentieren mehrere Gruppen, während Decision-Split-Schritte binäre Entscheidungen darstellen.

![Beispiel für einen Decision-Split-Schritt mit der Option, einen Filter mit einer Kontextvariablen zu erstellen.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Ähnlich wie Canvas-Kontextvariablen vordefinierte Typen haben, müssen die Vergleiche zwischen Kontextvariablen und statischen Werten [übereinstimmende Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types) haben. Der Filter für Kontextvariablen lässt Vergleiche über mehrere Datentypen für Boolesche Werte, Zahlen, Strings, Zeit und Tag des Jahres zu, ähnlich wie bei den Vergleichen für [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Verwenden Sie für Ihre Kontextvariable und den Vergleich denselben Datentyp. Wenn es sich bei Ihrer Kontextvariablen beispielsweise um einen Datentyp mit Zeitangaben handelt, verwenden Sie Zeitvergleiche (wie "vor" oder "nach"). Die Verwendung nicht übereinstimmender Datentypen (z.B. String-Vergleiche mit einer Zeitkontextvariablen) kann zu unerwartetem Verhalten führen.
{% endalert %}

Hier ist ein Beispiel für einen Filter für Kontextvariablen, der die Kontextvariable `product_name` mit der Regex `/braze/` vergleicht.

![Ein Filter, der für die Kontextvariable "product_name" eingerichtet wurde, um mit der Regex "/braze/" übereinzustimmen.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Abgleich mit Kontextvariablen oder angepassten Attributen

Wenn Sie die Option **Mit einer Kontextvariablen oder einem angepassten Attribut vergleichen** auswählen, können Sie Filter für Kontextvariablen erstellen, die mit zuvor definierten Kontextvariablen oder angepassten Attributen von Nutzern:innen verglichen werden. Dies kann nützlich sein, um Vergleiche durchzuführen, die dynamisch pro Nutzer:in sind, wie z.B. API-getriggerte `context`, oder um komplexe Vergleichslogik, die über Kontextvariablen definiert ist, zu verdichten.

{% tabs %}
{% tab Example 1 %}

Nehmen wir an, Sie möchten Nutzern:innen nach einer dynamischen Inaktivitätsperiode eine personalisierte Erinnerung schicken. Dazu gehört, dass jeder, der sich in den letzten drei Tagen nicht in Ihrer App angemeldet hat, eine Nachricht erhalten soll.

Sie haben eine Kontextvariable `re_engagement_date`, die als {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} definiert ist. Beachten Sie, dass `3 days` ein variabler Betrag sein kann, der auch als angepasstes Attribut eines Nutzers:innen gespeichert wird. Wenn also die `re_engagement_date` nach der `last_login_date` steht (die als angepasstes Attribut im Nutzerprofil gespeichert ist), wird ihnen eine Nachricht geschickt.

![Eine Filtereinrichtung mit angepassten Attributen als Personalisierungstyp für die Kontextvariable "re_engagement_date" nach dem angepassten Attribut "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

Der folgende Filter vergleicht, ob die Kontextvariable `reminder_date` vor der Kontextvariablen `appointment_deadline` liegt. Auf diese Weise können Sie Nutzer:innen in einem Zielgruppen-Pfad gruppieren, um festzustellen, ob sie vor ihrem Termin zusätzliche Erinnerungen erhalten sollen.

![Eine Filtereinrichtung mit Kontextvariablen als Personalisierungstyp für die Kontextvariable "reminder_date" auf der Kontextvariable "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Vorschau der Nutzer:innen Pfade

Wir empfehlen Ihnen, [Ihre Nutzer:innen-Pfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) zu testen und [eine Vorschau zu erstellen]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths), um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet und die Kontextvariablen entsprechend den erwarteten Ergebnissen ausgewertet werden.

{% alert note %}
Wenn Sie eine Vorschau Ihres Canvas im Bereich **Vorschau & Testversand** des Editors anzeigen, wird der Zeitstempel in der Vorschau der Testnachricht **nicht** auf UTC standardisiert, da dieses Panel Vorschauen als Strings generiert. Das bedeutet, wenn ein Canvas so eingerichtet ist, dass er ein `time` Objekt akzeptiert, wird die Vorschau der Nachricht nicht genau das anzeigen, was passiert, wenn der Canvas live ist. Um Ihr Canvas möglichst genau zu testen, empfehlen wir stattdessen eine Vorschau der Nutzer:innen.
{% endalert %}

Achten Sie auf häufige Szenarien, die ungültige Kontextvariablen erzeugen. Bei der Vorschau Ihres Nutzer-Pfads können Sie die Ergebnisse der personalisierten Verzögerungsschritte unter Verwendung von Kontextvariablen sowie alle Zielgruppen-, Entscheidungs- oder Aktions-Pfad-Schrittvergleiche sehen, die Nutzer:innen mit Kontextvariablen abgleichen.

Wenn die Kontextvariable gültig ist, können Sie die Variable in Ihrem gesamten Canvas referenzieren. Wenn die Kontextvariable jedoch nicht korrekt erstellt wurde, werden auch zukünftige Schritte in Ihrem Canvas nicht korrekt ausgeführt. Wenn Sie beispielsweise einen Kontextschritt erstellen, um Nutzern:innen einen Termin zuzuweisen, aber den Wert des Termins auf ein vergangenes Datum setzen, wird die Erinnerungs-E-Mail in Ihrem Schritt Nachricht nie versendet werden.

## Connected-Content-Strings in JSON umwandeln

Bei einem [Connected-Content-Aufruf]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) in einem Context-Schritt wird das vom Aufruf zurückgegebene JSON aus Gründen der Konsistenz und Fehlervermeidung als String-Datentyp ausgewertet. Wenn Sie diesen String in JSON umwandeln möchten, konvertieren Sie ihn mit `as_json_string`. Zum Beispiel:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Standardisierung der Zeitzonenkonsistenz

Mit der Hinzufügung von Canvas Context werden alle Zeitstempel vom [Typ datetime]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) aus [Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) in aktionsbasierten Canvase immer auf [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) normalisiert. Zuvor waren die Zeitstempel für Event-Eigenschaften mit [einigen Ausnahmen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) auf UTC normalisiert. Damit wird die Bearbeitung von Canvas-Schritten und -Nachrichten einheitlicher.

Betrachten Sie dieses Beispiel, wie sich diese Änderung auf einen Zeitstempel in Canvas auswirken könnte. Nehmen wir an, wir haben ein aktionsbasiertes Canvas, das eine Event-Eigenschaft im ersten Schritt des Canvas mit dem folgenden Schritt der Nachricht verwendet: 

{% raw %}
`Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!`
{% endraw %}

![Kontextreise mit einer Nachricht als erstem Schritt.]({% image_buster /assets/img/context_timezone_example.png %}){: style="max-width:50%"}

Der Schritt hat auch eine Ereignis-Nutzlast wie: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
}
```

Historisch gesehen würde die Nachricht lauten: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

Mit dem frühen Zugang zu Canvas Context lautet die Nachricht jetzt: `Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!` Das liegt daran, dass der Zeitstempel in UTC angegeben ist, was 8 Stunden vor der Pazifikzeit liegt (die Zeitzone, die in der ursprünglichen Nutzlast mit `-08:00` angegeben wurde).

{% alert important %}
Um dieser Zeitstempeländerung Rechnung zu tragen, empfehlen wir unter allen Umständen die [Verwendung von Liquid Filtern]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) für Zeitstempel, die in der gewünschten Zeitzone dargestellt werden.
{% endalert %}

### Liquid verwenden, um einen Zeitstempel in Ihrer bevorzugten Zeitzone anzugeben

Betrachten Sie das folgende Liquid Snippet:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Diese Logik führt zu der folgenden Ausgabe: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

Die bevorzugte Zeitzone kann auch in der Nutzlast der Event-Eigenschaften gesendet und in der Liquid-Logik verwendet werden: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

Dies ist ein Beispiel für ein Liquid Snippet:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: canvas_entry_properties.${user_timezone} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

## Fehlerbehebung {#troubleshooting}

### Ungültige Kontextvariablen

Eine Kontextvariable wird als ungültig betrachtet, wenn:
- Ein Aufruf eines eingebetteten Connected-Content schlägt fehl.
- Der Liquid-Ausdruck gibt zur Laufzeit einen Wert zurück, der nicht mit dem Datentyp übereinstimmt oder leer ist (null).

Wenn zum Beispiel der Datentyp der Kontextvariablen **Number** ist, der Liquid-Ausdruck aber einen String zurückgibt, ist er ungültig.

Unter diesen Umständen: 
- Der Nutzer:in wird zum nächsten Schritt vorbringen. 
- Die Analytics des Canvas-Schrittes zählen dies als _Nicht aktualisiert_.

Überwachen Sie bei der Fehlerbehebung die Metrik _Nicht aktualisiert_, um zu prüfen, ob Ihre Kontextvariable korrekt aktualisiert wird. Wenn die Kontextvariable ungültig ist, können Ihre Nutzer:innen nach dem Kontext-Schritt in Ihrem Canvas weitermachen, sich aber möglicherweise nicht für spätere Schritte qualifizieren.

Unter [Kontextvariable Datentypen](#context-variable-types) finden Sie die Beispiel-Setups für jeden Datentyp.

## Häufig gestellte Fragen

### Wie unterscheiden sich die Kontextvariablen von den Eigenschaften der Canvas-Eingänge?

Wenn Sie am frühen Zugriff auf den Canvas-Schritt teilnehmen, sind die Eingangs-Eigenschaften von Canvas jetzt als Canvas-Kontextvariablen enthalten. Das bedeutet, dass Sie die Eingangs-Eigenschaften von Canvas über die Braze API senden und in anderen Schritten referenzieren können, ähnlich wie bei der Verwendung einer Kontextvariablen mit dem Liquid-Snippet.

### Können sich Variablen in einem Singular Context Schritt gegenseitig referenzieren?

Ja Alle Variablen in einem Kontextschritt werden nacheinander ausgewertet, d.h. Sie könnten die folgenden Kontextvariablen eingerichtet haben:

| Kontextvariable | Wert | Beschreibung |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Die Lieblingsküche eines Nutzers:in. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | Der verfügbare Rabattcode für einen Nutzer:innen. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | Eine personalisierte Nachricht, die die vorherigen Variablen kombiniert. In einem Messaging-Schritt könnten Sie das Liquid Snippet {% raw %}`{{context.${personalized_message}}}`{% endraw %} verwenden, um die Kontextvariable zu referenzieren und jedem Nutzer:in eine personalisierte Nachricht zu liefern. Sie können auch einen Context-Schritt verwenden, um den Wert des [Promo-Codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) zu speichern und ihn als Template in anderen Schritten in einem Canvas zu verwenden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Dies gilt auch für mehrere Context-Schritte. Stellen Sie sich zum Beispiel diese Sequenz vor:
1. Ein anfänglicher Context-Schritt erstellt eine Variable namens `JobInfo` mit dem Wert `job_title`.
2. Der Schritt Nachricht referenziert {% raw %}`{{context.${JobInfo}}}`{% endraw %} und zeigt dem Nutzer:innen `job_title` an.
3. Später aktualisiert ein Context-Schritt die Kontextvariable und ändert den Wert von `JobInfo` in `job_description`.
4. Alle nachfolgenden Schritte, die auf `JobInfo` referenzieren, verwenden nun den aktualisierten Wert `job_description`.

Kontextvariablen verwenden im gesamten Canvas ihren neuesten Wert, wobei sich jedes Update auf alle folgenden Schritte auswirkt, die auf diese Variable referenzieren.

### Hat die Standardisierung der Zeitzonenkonsistenz von Canvas Context Auswirkungen auf API-getriggerte Canvase?

Nein, diese Änderung wirkt sich nur auf Canvase aus, die durch Aktionen getriggert werden. Zeitstempel, die in API-getriggerte Canvase gesendet werden, haben den String-Typ, nicht den Zeittyp, so dass die ursprüngliche Zeitzone immer erhalten bleibt.

### Wie verhält sich dies zu den Ausnahmen, die in den Eingangs-Eigenschaften und Event-Eigenschaften von Canvas vermerkt sind?

Durch die Teilnahme am Canvas Context-Frühzugang werden [diese Ausnahmen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) aufgehoben, unabhängig davon, ob Sie einen Canvas Context-Schritt verwenden.
