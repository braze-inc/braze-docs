---
nav_title: Autres niveaux
article_title: Autres niveaux
alias: /partners/otherlevels/
description: "Cet article couvre l'intégration entre OtherLevels Experience Platform et Braze."
page_type: partner
search_tag: OtherLevels

---

# Autres niveaux

> La plateforme [OtherLevels](https://www.otherlevels.com/) Experience Platform utilise la GenAI pour transformer la façon dont les marques de sport, les éditeurs et les opérateurs se connectent à leurs clients en transformant le contenu traditionnel en expériences vidéo et rich media personnalisées à l'échelle de la marque.

*Cette intégration est maintenue par OtherLevels.*

## Aperçu

L'intégration entre Braze et OtherLevels vous permet de créer des vidéos GenAI personnalisées par le biais d'appels API à la plateforme d'expérience OtherLevels, puis d'envoyer ces vidéos à vos utilisateurs sous forme de vidéos push iOS par le biais du [contenu connecté de Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/).

Offrez à vos utilisateurs une meilleure expérience grâce aux expériences alimentées par l'intelligence artificielle d'OtherLevels. Transformez le contenu existant et celui de tiers en vidéo et en média enrichi hautement évolutifs pour des audiences qui consomment déjà le contenu différemment et réagissent fortement aux expériences contextuellement personnalisées.

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte OtherLevels   | Un compte OtherLevels est nécessaire pour profiter de ce partenariat.                                                                     |
| Une clé de l'API REST de Braze  | Une clé API REST de Braze avec des autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cette intégration nécessite d'appeler l'API OtherLevels Experience Platform dans le cadre du processus de génération de vidéos avant que les messages puissent être envoyés à vos utilisateurs depuis Braze. Des exemples cURL sont fournis dans cette documentation, mais nous recommandons d'utiliser des clients API tels que Postman pour automatiser les appels API.

## Cas d’utilisation

Utilisez les vidéos GenAI créées avec la plateforme OtherLevels Experience pour :
- Créez de meilleures expériences pour les propriétaires et les ligues sportives, l'engagement des supporters, les paris sportifs, l'iGaming et les loteries.
- Amplifiez votre marketing client en transformant les contenus textuels en médias enrichis et en vidéos, créant ainsi des expériences humaines et engageantes.
- Améliorez les résultats de l'acquisition à la fidélisation en étendant, et non en réoutillant, votre intégration existante à Braze.

## Intégration de la plateforme d'expérience OtherLevels

### Étape 1 : Appelez l'API de la plateforme d'expérience OtherLevels pour générer une vidéo. {#step-1}

La première étape de l'intégration consiste à appeler l'API de la plateforme d'expérience OtherLevels pour générer une nouvelle vidéo. Notez que la génération de vidéo n'est pas instantanée. En fonction de la longueur et de la complexité de la vidéo, la création du contenu peut prendre jusqu'à une demi-heure. Planifiez les horaires de vos messages et les appels à l'API en conséquence, de sorte que les appels à l'API pour générer des vidéos soient effectués suffisamment à l'avance pour que l'envoi de vos messages Braze soit programmé.

{% alert important %}
La requête suivante utilise cURL. Pour une gestion plus efficace des demandes d'API, nous vous recommandons d'utiliser un client d'API tel que Postman.
{% endalert %}

Reportez-vous à l'exemple suivant pour savoir comment structurer votre appel à l'API. Pour plus d'informations sur la personnalisation des spécificités de la vidéo et la structuration de votre appel d'API, reportez-vous à la section [Personnaliser la vidéo GenAI](#customizing-the-genai-video).

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

Remplacez les éléments suivants :

| Marque substitutive          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | Une clé de projet OtherLevels vous sera fournie lorsque vous disposerez d'un compte OtherLevels.                                                                     |
| `BACKGROUND_IMAGE_URL`  | Une URL HTTPS pour l'arrière-plan de la vidéo. |
| `INSERT_TITLE` | Le titre de la vidéo. Il s'agit d'une référence interne qui ne sera pas affichée dans la vidéo.                                                 |
| `TALENT_TEMPLATE` | A ID du modèle de talent. OtherLevels travaillera avec vous lors de l'ouverture du compte pour créer un talent (avatar). Vous recevrez un ou plusieurs ID de talents qui pourront être utilisés.                                                 |
| `TALENT_MODEL` | A Talent Model ID. OtherLevels travaillera avec vous lors de l'ouverture du compte pour créer un talent (avatar). Vous recevrez un ou plusieurs modèles de talents qui peuvent être utilisés.                                                 |
| `INSERT_SCRIPT` | Le texte exact que vous souhaitez que le talent prononce pendant la vidéo.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Dans le cadre de la réponse API, OtherLevels renverra une charge utile JSON indiquant un appel API réussi. Le JSON contiendra un `recipe_id` unique pour identifier la vidéo générée. Le site `recipe_id` sera nécessaire à l'étape suivante.

Voici un exemple de réponse de l'API :

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### Étape 2 : Définir le site `recipe_id` comme attribut personnalisé

L'adresse `recipe_id` que vous avez reçue à l'[étape 1](#step-1) est maintenant définie comme attribut personnalisé de Braze pour le ou les utilisateurs auxquels vous souhaitez envoyer les vidéos.

Selon votre cas d'utilisation, vous pouvez avoir généré une seule vidéo destinée à une large audience, auquel cas cette même adresse `recipe_id` peut être définie pour plusieurs utilisateurs. Vous pouvez également avoir généré plusieurs vidéos uniques, chacune ciblant un utilisateur différent. Dans ce cas, chaque utilisateur doit avoir son site `recipe_id` personnalisé défini en tant qu'attribut personnalisé de Braze.

{% alert important %}
La requête suivante utilise cURL. Pour une gestion plus efficace des demandes d'API, nous vous recommandons d'utiliser un client d'API tel que Postman.
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

Remplacez les éléments suivants :

| Marque substitutive             | Description                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | L'URL de l'endpoint REST de Braze de votre instance Braze actuelle. Pour plus d'informations, reportez-vous aux [clés API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Votre clé API REST de Braze avec l'autorisation `users.track`.                                                                                                                                      |
| `USER_ID`              | L'ID de l'utilisateur qui recevra cette vidéo. Pour plus d'exemples d'identifiants pouvant être utilisés, reportez-vous à [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users).                                                                                                                                                  |
| `RECIPE_ID`       | Le site `recipe_id` reçu de la réponse de l'API OtherLevels à l'[étape 1.](#step-1)                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Étape 3 : Envoi par le biais du contenu connecté de Braze

Pour envoyer les vidéos GenAI sous forme d'envois de messages push iOS à vos utilisateurs, procédez comme suit :

1. Créez une campagne de notification push pour Braze iOS.
2. Lors de la composition de votre campagne, accédez à la section **Ressources** et collez la syntaxe de contenu connecté suivante dans le champ **Ajouter à partir de l'URL**.

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

Remplacez ensuite `OTHERLEVELS_PROJECT_KEY` par la clé de projet fournie par OtherLevels.

{: start="3"}
3\. Dans le menu déroulant du **format de fichier URL**, sélectionnez **MP4**.
4\. Configurez le reste de la campagne (contenu du message, planification de l'envoi et audience cible) en fonction de vos préférences.

![Exemples de ressources pour le contenu connecté.]({% image_buster /assets/img/otherlevels/1.png %})

## Personnaliser la vidéo GenAI

### Taille et attributs de la vidéo

L'arrière-plan vidéo peut être spécifié à l'aide de la touche `bg_image`.

| Paramètre             | Description                  |
|-------------------------|----------------------------|
| `url`    | URL HTTPS pour l'image d'arrière-plan. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

La taille de l'arrière-plan vidéo peut être spécifiée à l'aide de la touche `resize_image`. Nous recommandons que l'image d'arrière-plan ait la même taille que celle configurée ici.

| Paramètre             | Description                  |
|-------------------------|----------------------------|
| `width`    | Largeur de l'image d'arrière-plan, avec des options pour les modes portrait et paysage. |
| `height`     | Hauteur de l'image d'arrière-plan, avec des options pour les modes portrait et paysage.                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Les options de superposition vidéo peuvent être spécifiées dans la clé `image_video_overlay`.

| Paramètre             | Description                  |
|-------------------------|----------------------------|
| `width`    | Largeur de la superposition, avec des options pour les modes portrait et paysage. |
| `height`         | Hauteur de la superposition, avec des options pour les modes portrait et paysage.                                              |
| `color`              | Couleur de l'incrustation spécifiée en RVB avec la vidéo de transparence.                                                                   |
| `y_pos`       | Décalage de l'axe Y par rapport au centre.                                                              |
| `x_pos`    | Décalage de l'axe X par rapport au centre. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Talent et scénario

Dans le cadre du provisionnement, OtherLevels travaillera avec vous pour générer un ou plusieurs talents (parfois appelés avatars) à utiliser dans vos vidéos. En fonction de votre cas d'utilisation et de votre marque, cela peut se faire sous la forme d'un de vos ambassadeurs de marque existants ou d'une création unique.

Après leur création, vous recevrez des ID `TALENT_TEMPLATE` et `TALENT_MODEL` utilisables avec notre API. 

Le modèle vocal utilisé pour traiter les scripts d'entrée fonctionne mieux lorsqu'il fournit un script naturel qu'un humain lirait. Dans la plupart des cas, vous n'avez pas besoin de ponctuation supplémentaire pour guider manuellement le script. Toutefois, nous vous recommandons de tester tous vos scripts avant de les envoyer à une audience réelle. La vitesse à laquelle le talent lit le script peut être spécifiée dans la touche `talking_talent_speed`.

| Paramètre             | Description                  |
|-------------------------|----------------------------|
| `speed`    | Spécifiez la vitesse à laquelle le talent lira le script. Par exemple, `1.5`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Considérations supplémentaires

- Seule la plateforme de notification push d'iOS prend en charge nativement les médias vidéo. Les notifications push Android ne prennent pas en charge les vidéos de manière native, cette intégration ne peut donc être utilisée qu'avec votre audience iOS.
- Lorsqu'ils reçoivent des notifications push vidéo sur les appareils iOS, les utilisateurs doivent appuyer sur la notification push et la maintenir enfoncée pour que la vidéo se charge et soit lue. Il s'agit d'un comportement standard sur la plateforme iOS, qui ne peut pas être personnalisé.