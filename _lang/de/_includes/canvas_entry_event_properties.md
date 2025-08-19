Sie können Canvas Eingangs-Eigenschaften und Event-Eigenschaften in Ihren Nutzer:innen verwenden.

{% tabs local %}
{% tab Canvas-Entry-Eigenschaften %}

[Canvas-Entry-Eigenschaften]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) sind Eigenschaften für Canvase, die durch Aktionen oder die API getriggert werden. Beachten Sie, dass das Objekt `canvas_entry_properties` maximal 50 KB groß sein darf.

{% alert note %}
Speziell für In-App-Nachricht-Kanäle gilt: `canvas_entry_properties` kann nur in Canvas referenziert werden.
{% endalert %}

Sie können `canvas_entry_properties` in jedem Schritt von Messaging mit diesem Liquid-Format referenzieren: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Beachten Sie, dass es sich bei den Events um angepasste Events oder Kauf-Events handeln muss, um auf diese Weise verwendet werden zu können.

#### Anwendungsfall

{% raw %}
Angenommen, der Shop RetailApp erhält folgende Anfrage: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. 

RetailApp kann den Produktnamen (Schuhe) mit diesem Liquid in eine Nachricht einfügen: `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

RetailApp kann auch spezielle Nachrichten für verschiedene Eigenschaften von `product_name` in einem Canvas triggern, das Nutzer:innen anspricht, nachdem sie ein Kauf-Event ausgelöst haben. Sie können zum Beispiel unterschiedliche Nachrichten an Nutzer:innen, die Schuhe gekauft haben, und Nutzer:innen, die etwas anderes gekauft haben, senden, indem Sie das folgende Liquid in einen Messaging-Schritt einfügen.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Erweitern für Original Canvas Editor %}

Sie können Canvase nicht mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt ist nur zum Referenzieren verfügbar. Bei den Canvase, die mit dem Original-Editor erstellt wurden, können die Eingangs-Eigenschaften von Canvase nur im ersten vollständigen Schritt eines Canvas referenziert werden.

{% enddetails %}
{% endtab %}

{% tab Event-Eigenschaften %}

Event-Eigenschaften referenzieren auf die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können in Kampagnen mit aktionsbasierter Lieferung und Canvases verwendet werden.

{% alert important %}
Sie können `event_properties` nicht im ersten Nachrichten-Schritt Ihres Canvas verwenden. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen Aktionspfadschritt mit dem entsprechenden Event **vor dem** Nachrichtenschritt hinzufügen, der `event_properties` enthält.
{% endalert %}

In Canvas können angepasste Event- und Kauf-Event-Eigenschaften in Liquid in jedem Nachrichten-Schritt verwendet werden, der auf einen Aktions-Pfad-Schritt folgt. Stellen Sie sicher, dass Sie {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} verwenden, wenn Sie auf diese Event-Eigenschaften verweisen. DiDiese Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise in der Komponente „Nachricht“ verwendet werden zu können.

Im ersten Schritt der Nachricht, der einem Aktions-Pfad folgt, können Sie Event-Eigenschaften verwenden, die sich auf das in diesem Aktions-Pfad referenzierte Ereignis beziehen. Diese Event-Eigenschaften können jedoch nur verwendet werden, wenn der Nutzer:innen die Aktion tatsächlich durchgeführt hat (und nicht in die Gruppe Alle anderen einsortiert wurde). Zwischen diesem Aktionspfad und dem Nachrichtenschritt können Sie weitere Schritte einfügen (die selbst keine Aktionspfade oder Nachrichtenschritte sind).

{% details Erweitern für Original Canvas Editor %}

Sie können Canvase nicht mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt ist nur zum Referenzieren verfügbar. Im Original-Canvas-Editor können Event-Eigenschaften nicht in geplanten vollständigen Schritten verwendet werden. Sie können jedoch Event-Eigenschaften im ersten vollständigen Schritt eines aktionsbasierten Canvas verwenden, auch wenn der vollständige Schritt geplant ist.

{% enddetails %}

{% endtab %}
{% endtabs %}

Weitere Informationen und Beispiele finden Sie unter [Canvas-Eingangs-Eigenschaften und Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).