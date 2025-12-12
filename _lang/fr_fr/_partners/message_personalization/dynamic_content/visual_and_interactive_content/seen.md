---
nav_title: SEEN
article_title: SEEN
description: "Cet article de référence présente le partenariat entre Braze et SEEN, une plateforme permettant de concevoir des vidéos personnalisées pour accroître l'engagement tout au long du parcours client."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# SEEN

> [SEEN](https://seen.io/) est une plateforme vidéo de personnalisation qui permet aux entreprises de créer et de créer des vidéos autour de leurs clients afin de leur offrir une expérience plus engageante. Avec SEEN, vous pouvez concevoir une vidéo autour de vos données, la personnaliser à l'échelle dans le cloud, puis la distribuer là où elle fonctionne le mieux.

## Cas d’utilisation

SEEN offre une personnalisation vidéo automatisée tout au long du parcours client. Les utilisations courantes sont l'onboarding, la fidélisation, les inscriptions et la conversion, ainsi que le taux de reconquête et l'anti-churn.

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis          | Descriptif                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Une campagne SEEN   | Une campagne SEEN est nécessaire pour bénéficier de ce partenariat.                                                                     |
| Source des données   | Vous devrez envoyer des données à SEEN pour personnaliser vos vidéos. Assurez-vous que vous disposez de toutes les données pertinentes dans Braze et que vous transmettez des données avec **braze_id** comme identifiant. |
| URL du webhook Braze pour la transformation des données   | La transformation des données de Braze sera utilisée pour reformater les données entrantes de SEEN afin qu'elles puissent être acceptées par l'endpoint /users/track de Braze. |

## Limite de débit

L'API SEEN accepte actuellement 1 000 appels par heure.

## Intégration de SEEN à Braze

Dans l'exemple suivant, nous envoyons les données des utilisateurs à SEEN pour la génération de vidéos, et nous renvoyons à Braze un lien unique vers la page d'atterrissage et une vignette unique et personnalisée pour la distribution. Cet exemple utilise un webhook POST pour envoyer des données à SEEN, et une transformation de données pour recevoir les données en retour à Braze. Si vous avez plusieurs campagnes vidéo avec SEEN, répétez le processus pour connecter Braze à toutes les campagnes vidéo.

{% alert tip %}
En cas d'expérience client, contactez votre gestionnaire satisfaction client SEEN pour obtenir de l'aide.
{% endalert %}

### Étape 1 : Créez une campagne webhook

Créez une nouvelle [campagne webhook à]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) Braze. Donnez un nom à votre campagne, puis reportez-vous au tableau suivant pour composer votre webhook :

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Champ</strong></th>
      <th><strong>Détails</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>URL du webhook</strong></td>
      <td>Utilisez l'URL webhook suivante. Vous recevrez votre <code>campaign_slug</code> de SEEN pour appeler l'endpoint correct.<br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td><strong>Méthode HTTP</strong></td>
      <td>Utilisez le <code>POST</code> méthode.</td>
    </tr>
    <tr>
      <td><strong>Corps de la demande</strong></td>
      <td>Saisissez le corps de votre demande dans un texte brut similaire à ce qui suit.<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>Pour plus d'informations, voir <a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">SEEN API.</a></td>
    </tr>
    <tr>
      <td><strong>En-têtes de requête</strong></td>
      <td>Utilisez les informations suivantes pour remplir les en-têtes de vos demandes :<br>- <strong>Autorisation :</strong> <code>Token {token}</code><br>- <strong>Type de contenu :</strong> <code>application/json</code><br><br>Vous recevrez votre jeton d'authentification de la part de SEEN.</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez maintenant tester le webhook avec un utilisateur en passant à l'onglet **Test.** 

Si tout fonctionne comme prévu, passez à Braze, puis réglez le taux d'envoi de la campagne sur 10 **messages par minute**. De cette façon, vous ne dépasserez pas la limite de débit de la SEEN, qui est de 1 000 appels par heure.

### Étape 2 : Créer une transformation des données

1. Créez de nouveaux champs d'[attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) pour `landing_page_url` et `email_thumbnail_url`. Ce sont les deux attributs que nous utiliserons dans cet exemple.
2. Ouvrez [Transformation de données]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) sous **Paramètres des données**, et sélectionnez **Créer une transformation**.
3. Donnez un nom à votre transformation, puis choisissez **Start from scratch** et définissez **Destination** sur **POST : Suivez les utilisateurs**.
4. Sélectionnez **Partager l'URL de votre webhook avec SEEN**.
5. Vous pouvez utiliser le code ci-dessous comme point de départ de la transformation :

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.customer_id,
      "_update_existing_only": true,
      "landing_page_url": payload.landing_page_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```
{% alert note %}
Si vous souhaitez inclure d'autres données, veillez à les inclure également. N'oubliez pas de discuter également avec le SEEN afin que le payload du rappel comprenne tous les champs nécessaires.
{% endalert %}

{: start="6"}
6\. Envoyez une charge utile de test à l'endpoint fourni. Si vous souhaitez utiliser la charge utile de rappel définie dans la [documentation SEEN](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp), vous pouvez l'envoyer vous-même avec [Postman](https://www.postman.com/) ou un autre service similaire :

```json
{
        "customer_id": "101",
        "campaign_slug": "onboarding",
        "landing_page_url": "your.subdomain.com/v/12345",
        "video_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/output.m3u8",
        "thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/thumbnail.jpg",
        "email_thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/email_thumbnail.jpg"
       
}
```

{: start="7"}
7\. Sélectionnez **Valider** pour vous assurer que tout fonctionne comme prévu.
8\. Sélectionnez **Enregistrer** et **activer**.
