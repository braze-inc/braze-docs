## Über Google Tag Manager für Internet {#google-tag-manager}

Mit dem Google Tag Manager (GTM) können Sie per Fernzugriff Tags auf Ihrer Website hinzufügen, entfernen und bearbeiten, ohne dass eine Freigabe des Produktionscodes oder technische Ressourcen erforderlich sind. Braze bietet die folgenden Templates für das Internet SDK an:

|Tag Typ|Anwendungsfall|
|--------|--------|
| Tag der Initialisierung | Mit diesem Tag können Sie [das Web Braze SDK integrieren]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web), ohne dass Sie den Code Ihrer Website ändern müssen.|
| Aktion Tag | Mit diesem Tag können Sie [Content-Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [Nutzer-Attribute festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) und [die Datenerfassung verwalten]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Googles EU-Richtlinie zur Zustimmung der Nutzer:in

{% alert important %}
Google aktualisiert seine [EU-Zustimmungsrichtlinie](https://www.google.com/about/company/user-consent-policy/) als Reaktion auf die Änderungen des [Digital Markets Act (DMA](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)), der ab dem 6\. März 2024 in Kraft tritt. Diese neue Änderung verlangt von den Werbetreibenden, dass sie ihren Endnutzern aus dem EWR und dem Vereinigten Königreich bestimmte Informationen offenlegen und die erforderlichen Einwilligungen von ihnen einholen. Weitere Informationen finden Sie in der folgenden Dokumentation.
{% endalert %}

Im Rahmen der EU-Zustimmungsrichtlinie von Google müssen die folgenden booleschen benutzerdefinierten Attribute in Nutzerprofilen protokolliert werden:

- `$google_ad_user_data`
- `$google_ad_personalization`

Wenn Sie diese über die GTM-Integration einstellen, müssen Sie für benutzerdefinierte Attribute ein benutzerdefiniertes HTML-Tag erstellen. Im Folgenden finden Sie ein Beispiel dafür, wie Sie diese Daten als boolesche Datentypen (nicht als Strings) protokollieren:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Weitere Informationen finden Sie unter [Zielgruppen-Synchronisierung mit Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).
