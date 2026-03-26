## À propos de Google Tag Manager pour le Web {#google-tag-manager}

Google Tag Manager (GTM) vous permet d'ajouter, de supprimer et de modifier à distance des étiquettes sur votre site web, sans nécessiter de mise en production ni de ressources techniques. Braze propose les modèles suivants pour le SDK Web :

|Type d'étiquette|Cas d'utilisation|
|--------|--------|
| Étiquette d'initialisation | Cette étiquette vous permet d'[intégrer le SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sans avoir à modifier le code de votre site.|
| Étiquette d'action | Cette étiquette vous permet de [créer des cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), de [définir les attributs utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) et de [gérer la collecte des données]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Enregistrer des événements personnalisés avec GTM

Vous pouvez enregistrer des événements personnalisés à l'aide d'une étiquette **Custom HTML** dans GTM. Cette approche utilise la [couche de données](https://developers.google.com/tag-platform/tag-manager/datalayer) GTM pour transmettre les données d'événement de votre site vers une étiquette GTM qui appelle le SDK Web de Braze.

### Étape 1 : Envoyer l'événement vers la couche de données

Dans le code de votre site, envoyez un événement vers la couche de données à chaque endroit où vous souhaitez déclencher l'événement personnalisé. Par exemple, pour enregistrer un événement personnalisé lorsqu'un bouton est cliqué :

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Étape 2 : Créer un déclencheur dans GTM

1. Dans votre conteneur GTM, accédez à **Triggers** et créez un nouveau déclencheur.
2. Définissez le **Trigger Type** sur **Custom Event**.
3. Définissez le **Event Name** sur la même valeur que celle envoyée à la couche de données (par exemple, `my_custom_event`).
4. Choisissez quand le déclencheur doit se déclencher (par exemple, **All Custom Events**).

### Étape 3 : Créer une étiquette Custom HTML

1. Dans GTM, accédez à **Tags** et créez une nouvelle étiquette.
2. Définissez le **Tag Type** sur **Custom HTML**.
3. Dans le champ HTML, ajoutez le code suivant :

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. Sous **Triggering**, sélectionnez le déclencheur que vous avez créé à l'étape 2.
5. Enregistrez et publiez votre conteneur.

Pour inclure des propriétés d'événement, transmettez-les en tant que second argument :

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Règles de consentement des utilisateurs de Google dans l'UE

{% alert important %}
Google met à jour ses [règles de consentement des utilisateurs de l'Union européenne](https://www.google.com/about/company/user-consent-policy/) en réponse aux changements apportés à la [loi sur les marchés numériques (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), en vigueur depuis le 6 mars 2024. Ce changement oblige les annonceurs à divulguer certaines informations à leurs utilisateurs finaux de l'EEE et du Royaume-Uni, et à obtenir les consentements nécessaires. Consultez la documentation suivante pour en savoir plus.
{% endalert %}

Dans le cadre des règles de consentement des utilisateurs de l'UE de Google, les attributs personnalisés booléens suivants doivent être enregistrés dans les profils utilisateurs :

- `$google_ad_user_data`
- `$google_ad_personalization`

Si vous les définissez via l'intégration GTM, les attributs personnalisés nécessitent la création d'une étiquette HTML personnalisée. L'exemple suivant montre comment enregistrer ces valeurs en tant que types de données booléennes (et non en tant que chaînes de caractères) :

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Pour plus d'informations, reportez-vous à la section [Synchronisation de l'audience avec Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).