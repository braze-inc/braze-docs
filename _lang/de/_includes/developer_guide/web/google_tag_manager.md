## Über Google Tag Manager für das Internet {#google-tag-manager}

Mit dem Google Tag Manager (GTM) können Sie per Fernzugriff Tags auf Ihrer Website hinzufügen, entfernen und bearbeiten, ohne dass eine Freigabe des Produktionscodes oder technische Ressourcen erforderlich sind. Braze bietet die folgenden Templates für das Internet-SDK an:

|Tag-Typ|Anwendungsfall|
|--------|--------|
| Initialisierungs-Tag | Mit diesem Tag können Sie [das Braze Internet-SDK integrieren]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web), ohne den Code Ihrer Website ändern zu müssen.|
| Aktions-Tag | Mit diesem Tag können Sie [Content-Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [Nutzer:innen-Attribute festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) und [die Datenerfassung verwalten]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Angepasste Events mit GTM protokollieren

Sie können angepasste Events mit einem **Custom HTML**-Tag in GTM protokollieren. Dieser Ansatz nutzt den GTM [Data Layer](https://developers.google.com/tag-platform/tag-manager/datalayer), um Event-Daten von Ihrer Website an ein GTM-Tag zu übergeben, das das Braze Internet-SDK aufruft.

### 1. Schritt: Event in den Data Layer pushen

Pushen Sie in Ihrem Website-Code ein Event in den Data Layer, wo immer Sie das angepasste Event triggern möchten. Um beispielsweise ein angepasstes Event zu protokollieren, wenn ein Button angeklickt wird:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### 2. Schritt: Trigger in GTM erstellen

1. Gehen Sie in Ihrem GTM-Container zu **Triggers** und erstellen Sie einen neuen Trigger.
2. Setzen Sie den **Trigger Type** auf **Custom Event**.
3. Setzen Sie den **Event Name** auf denselben Wert, den Sie in den Data Layer gepusht haben (zum Beispiel `my_custom_event`).
4. Wählen Sie aus, wann der Trigger ausgelöst werden soll (zum Beispiel **All Custom Events**).

### 3. Schritt: Custom HTML-Tag erstellen

1. Gehen Sie in GTM zu **Tags** und erstellen Sie ein neues Tag.
2. Setzen Sie den **Tag Type** auf **Custom HTML**.
3. Fügen Sie im HTML-Feld Folgendes hinzu:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. Wählen Sie unter **Triggering** den Trigger aus, den Sie in Schritt 2 erstellt haben.
5. Speichern und veröffentlichen Sie Ihren Container.

Um Event-Eigenschaften einzubeziehen, übergeben Sie diese als zweites Argument:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Googles EU-Richtlinie zur Einwilligung der Nutzer:innen

{% alert important %}
Google aktualisiert seine [EU-Richtlinie zur Einwilligung der Nutzer:innen](https://www.google.com/about/company/user-consent-policy/) als Reaktion auf die Änderungen des [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), der seit dem 6. März 2024 in Kraft ist. Diese neue Änderung verlangt von Werbetreibenden, dass sie ihren Endnutzer:innen aus dem EWR und Großbritannien bestimmte Informationen offenlegen und die erforderlichen Einwilligungen von ihnen einholen. Mehr erfahren Sie in der folgenden Dokumentation.
{% endalert %}

Im Rahmen der EU-Richtlinie zur Einwilligung der Nutzer:innen von Google müssen die folgenden booleschen angepassten Attribute in Nutzerprofilen protokolliert werden:

- `$google_ad_user_data`
- `$google_ad_personalization`

Wenn Sie diese über die GTM-Integration festlegen, müssen Sie für angepasste Attribute ein Custom HTML-Tag erstellen. Im Folgenden finden Sie ein Beispiel dafür, wie Sie diese Werte als boolesche Datentypen (nicht als Strings) protokollieren:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Weitere Informationen finden Sie unter [Zielgruppen-Synchronisierung mit Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).