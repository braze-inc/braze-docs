---
nav_title: Vu
article_title: Vu
description: "Seen permet des expériences vidéo personnalisées à grande échelle, aidant les marques à susciter un plus grand engagement tout au long du parcours client."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Vu

> [Seen](https://seen.io) permet aux marques de créer et de proposer des expériences vidéo personnalisées à grande échelle. Avec Seen, vous pouvez concevoir une vidéo autour de vos données, la personnaliser à l'échelle dans le cloud, puis la distribuer là où elle fonctionne le mieux.
>
> L'intégration entre Braze et Seen vous permet d'envoyer les données des utilisateurs de Braze à Seen, de générer dynamiquement des vidéos personnalisées et de renvoyer les ressources vidéo, telles qu'une URL de lecteur unique et une vignette, dans Braze pour qu'elles soient utilisées dans les campagnes et Canvases.


## Cas d’utilisation

Seen prend en charge la réception/distribution automatisée et personnalisée de vidéos tout au long du cycle de vie du client, y compris :

- **Onboarding** : Accueillez les nouveaux utilisateurs avec des vidéos personnalisées en fonction de leur profil ou de leur contexte d'inscription.
- **Conversion et activation**: Renforcez les actions clés grâce à des messages vidéo contextuels.
- **Fidélisation et vente incitative**: Mettez en avant des offres personnalisées ou des jalons d'utilisation.
- Le **taux de reconquête et la prévention du désabonnement**: Réengagez les utilisateurs inactifs avec du contenu vidéo sur mesure.


## Conditions préalables

Avant de commencer, vous devez disposer des éléments suivants :

| Prérequis | Description |
|--------------|-------------|
| Vue Accès à la plate-forme | Vous avez besoin d'un abonnement à la plateforme Seen ou d'une campagne Seen active. Vous devez accéder aux paramètres de votre espace de travail pour récupérer votre ID d'espace de travail et générer un jeton API. |
| URL du webhook Braze pour la transformation des données | La transformation des données de Braze reformate les données entrantes de Seen afin qu'elles puissent être acceptées par l'endpoint /users/track de Braze. |
| Données des utilisateurs de Braze | La personnalisation des vidéos nécessite des données au niveau de l'utilisateur. Assurez-vous que les attributs pertinents sont disponibles dans Braze et que vous passez **braze_id** comme identifiant unique. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}




## Comment fonctionne Seen Journeys ?

Seen utilise [Journeys](https://docs.seen.io/journey) pour contrôler la manière dont les données entrantes sont traitées et dont les sorties vidéo sont générées.

Un parcours est un flux de travail configurable qui :
- reçoit des données de systèmes externes (tels que Braze)
- Applique des règles de logique et de personnalisation.
- Génère une vidéo et des ressources associées
- Renvoie une réponse configurable

Les voyages sont composés de **nœuds**, chacun ayant une fonction spécifique :

- **Nœud déclencheur**: Définit comment et quand un Journey démarre (pour les intégrations Braze, utilisez un déclencheur `On Create` ).
- **Nœud conditionnel**: Achemine les utilisateurs vers différents chemins logiques en fonction des valeurs des données.
- **Nœud du projet**: Applique une personnalisation dynamique de la vidéo en utilisant les données entrantes.
- **Nœud de joueur**: Génère une URL unique pour le lecteur vidéo
- **Nœud webhook**: Définit la charge utile de la réponse renvoyée à Braze.

Les réponses de Journey étant configurables, assurez-vous que les champs de sortie renvoyés par Seen correspondent aux attributs attendus par votre transformation de données Braze.


## Limite de débit
L'API Seen accepte jusqu'à 100 appels toutes les 10 secondes.


## Intégration

Dans cet exemple, Braze envoie les données de l'utilisateur à Seen pour générer une vidéo personnalisée. Seen renvoie ensuite une URL de lecteur vidéo et une URL de vignette uniques, qui sont stockées en tant qu'attributs personnalisés dans Braze en vue de leur utilisation dans l'envoi de messages.

Si vous avez plusieurs campagnes vidéo avec Seen, répétez le processus pour connecter Braze à toutes les campagnes vidéo.

### Étape 1 : Créez une campagne webhook pour envoyer des données à Seen

Créez une nouvelle [campagne webhook à]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) Braze.

Configurez le webhook comme suit :

- **URL du webhook** :  
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`  
  Trouvez votre ID d'espace de travail dans les paramètres de la plate-forme Seen.

- **Méthode HTTP**: POST
- **Corps de la requête** : Texte brut  
  Utilisez l'exemple suivant comme point de départ. Pour plus d'informations, reportez-vous à la [documentation de Seen sur la création de données.](https://docs.seen.io/create-data) 

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}
- **En-têtes de la requête**:
  - `Authorization` : Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > Générez un [jeton API](https://docs.seen.io/authorization) dans la plateforme Seen sous Paramètres de l'espace de travail. Vous pouvez contacter votre gestionnaire de la satisfaction client de Seen pour obtenir de l'aide.

- Pour tester le webhook avec un utilisateur, passez à l'onglet **Test.** 
- Après avoir confirmé que le test fonctionne comme prévu, terminez la configuration du webhook.


### Étape 2 : Configurer un parcours dans la plateforme Seen

Seen utilise [Journeys](https://docs.seen.io/journey) pour définir comment les données entrantes sont traitées, personnalisées et renvoyées à Braze.  
Chaque parcours est un flux de travail configurable composé de nœuds qui vous permettent de contrôler à la fois la logique de génération de la vidéo et le contenu de la réponse.

Pour configurer votre voyage :

1. Créez un nouveau parcours dans la plateforme Seen
2. Ajoutez un **nœud de déclencheur** et sélectionnez le déclencheur `On Create`.  
   Cela permet de s'assurer que le voyage commence lorsque Braze envoie des données à Seen. Créez et ajoutez toute logique de [segmentation](https://docs.seen.io/segments) dans votre espace de travail si nécessaire.
3. Créez votre logique en utilisant les nœuds suivants si nécessaire :
   - **Nœud conditionnel**: Acheminer les utilisateurs en fonction des valeurs des attributs (par exemple, le type de régime ou la région).
   - **Nœud du projet**: Appliquer la personnalisation dynamique des vidéos à l'aide des données entrantes.
   - **Nœud de joueur**: Générer une URL unique pour le lecteur vidéo
4. Ajoutez un **nœud webhook** pour définir la réponse renvoyée à Braze.

#### Exigences relatives à la réponse du nœud webhook

La charge utile de la réponse étant configurable, assurez-vous que les champs suivants sont renvoyés pour prendre en charge la transformation des données de Braze décrite à l'étape suivante :

| Champ | Description |
|------|-------------|
| `id` | Doit correspondre au site `braze_id` envoyé par Braze |
| `player_url` | URL unique pour le lecteur vidéo personnalisé |
| `email_thumbnail_url` | URL de la vignette vidéo générée |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si votre cas d'utilisation nécessite des attributs supplémentaires, incluez-les dans la réponse et mappez-les dans Braze.


### Étape 3 : Créer une transformation de données pour recevoir des données de Seen

Utilisez les transformations de données Braze pour ingérer la réponse Seen Journey et stocker les ressources vidéo sur le profil utilisateur.

1. Créez les [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) suivants dans Braze :
   - `player_url`
   - `email_thumbnail_url`
2. Naviguez vers **Paramètres des données** → **Transformation des données** et cliquez sur **Créer une transformation**.
3. Configurez la transformation :
   - **Démarrer de zéro**
   - **Destination** → POST : Suivi utilisateur
4. Partagez l'URL du webhook généré avec Seen, ou ajoutez-la directement au **nœud** Journey **Webhook**.
5. Utilisez le code de transformation suivant :

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6\. Envoyez une charge utile de test à l'endpoint fourni. Envoyez des données à la plateforme Seen pour exécuter votre Journey, ou envoyez la charge utile directement à Braze avec [Postman](https://www.postman.com/) ou un autre service similaire.
7\. Sélectionnez **Valider** pour vous assurer que tout fonctionne comme prévu.
8\. Sélectionnez **Enregistrer** et **activer**.