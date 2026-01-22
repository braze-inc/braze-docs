## À propos de Google Tag Manager pour le Web {#google-tag-manager}

Google Tag Manager (GTM) vous permet d'ajouter, de supprimer et de modifier à distance des tags sur votre site web sans nécessiter de code de production ni de ressources d'ingénierie. Braze propose les modèles suivants pour le SDK Web :

|Type d'étiquette|Cas d’utilisation|
|--------|--------|
| Étiquette d'initialisation | Cette étiquette vous permet d'[intégrer le SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sans avoir à modifier le code de votre site.|
| Étiquette d'action | Cette étiquette vous permet de [créer des cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), de [définir les paramètres de l'utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) et de [gérer la collecte des données]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Règles de consentement des utilisateurs de Google dans l'UE

{% alert important %}
Google met à jour ses [règles de consentement des utilisateurs de l'Union européenne](https://www.google.com/about/company/user-consent-policy/) en réponse aux changements apportés à la [loi sur les marchés numériques (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), en vigueur à partir du 6 mars 2024. Ce nouveau changement oblige les annonceurs à divulguer certaines informations à leurs utilisateurs finaux de l'EEE et du Royaume-Uni, et à obtenir d'eux les consentements nécessaires. Consultez la documentation suivante pour en savoir plus.
{% endalert %}

Dans le cadre de la politique de consentement de l'utilisateur de l'UE de Google, les attributs personnalisés booléens suivants doivent être enregistrés dans les profils utilisateurs :

- `$google_ad_user_data`
- `$google_ad_personalization`

Si vous les définissez via l'intégration GTM, les attributs personnalisés nécessitent la création d'une balise HTML personnalisée. L'exemple suivant montre comment enregistrer ces valeurs en tant que types de données booléennes (et non en tant que chaînes de caractères) :

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Pour plus d'informations, reportez-vous à la section [Synchronisation de l'audience avec Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).
