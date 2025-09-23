---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Cet article de référence présente le partenariat entre Braze et Lob.com, qui vous permet d'envoyer des publipostages tels que des lettres, des cartes postales et des chèques par la poste."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com][38] est un service en ligne qui vous permet d'envoyer un publipostage à vos utilisateurs.

L'intégration Braze et Lob exploite les webhooks Braze et l'API Lob pour envoyer des courriers tels que des lettres, des cartes postales et des chèques par la poste.  

## Conditions préalables

|Condition| Description|
| ---| ---|
|Compte Lob | Un compte Lob est nécessaire pour bénéficier de ce partenariat. |
| Clé API de Lob | Votre clé API de Lob se trouve dans la section des paramètres, sous votre nom, dans le tableau de bord de Lob. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Sélectionnez l'endpoint de Lob

L'URL HTTP à demander dans le webhook est différente pour chaque action que vous pouvez effectuer sur Lob. Dans l'exemple suivant, nous utilisons l'endpoint de l'API d’envoi de cartes postales `https://api.lob.com/v1/postcards`. Consultez la [liste complète des endpoints]][39] pour sélectionner l'endpoint qui convient à votre cas d'utilisation. 

| Point d'extrémité de l'API | Endpoints disponibles |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/addresses<br>/v1/addresses/{id}<br>/v1/verify<br>/v1/postcards<br>/v1/postcards/{id}<br>/v1/letter<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/areas<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routes<br>/v1/countries<br>/v1/states|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 2 : Créez votre modèle de webhook Braze à Braze

Pour créer un modèle de webhook Lob à utiliser dans de futures campagnes ou Canvases, naviguez vers **Modèles** > **Modèles de webhook** dans la plateforme Braze. 

Si vous souhaitez réaliser une campagne webhook à Braze unique ou utiliser un modèle existant, sélectionnez **Webhook** à Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle de webhook, remplissez les champs suivants :
- **URL de webhook** : `<LOB_API_ENDPOINT>`
- **Corps de la requête** : Texte brut

#### En-têtes de requête et méthode

Lob nécessite un en-tête HTTP pour l'autorisation et une méthode HTTP. Ce qui suit sera déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres**, vous devez remplacer le `<LOB_API_KEY>` par votre clé API Lob. Cette clé doit comporter un " : " directement après la clé et être codée en base 64. 

- **Méthode HTTP** : POST
- **En-têtes de la requête** :
  - **Autorisation**: De base `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Code du corps de la requête et URL du webhook affichés dans l'onglet de composition du générateur de webhook Braze.][35]

#### Corps de la requête

Voici un exemple de corps de requête pour l'endpoint Lob postcards. Bien que ce corps de requête soit fourni dans le modèle de base Lob de Braze, si vous souhaitez utiliser d'autres endpoints, vous devez ajuster vos champs Liquid en conséquence.

```json
{% raw %}"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"{% endraw %}
```

### Étape 3 : Prévisualisez votre requête

À ce stade, votre campagne devrait être prête à être testée et envoyée. Consultez le tableau de bord de Lob et les journaux des messages d'erreur de la console de développement de Braze si vous rencontrez des erreurs. Par exemple, l'erreur suivante a été provoquée par un en-tête d'authentification mal formaté. 

![Un journal des erreurs indiquant l'heure, le nom de l'application, le canal et le message d'erreur. Le message d'erreur contient l’alerte u message et le code d'état.][36]

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
Il y a [38]: https://lob.com
Il y a [39]: https://lob.com/docs#intro
Il y a [40]: https://lob.com/docs#auth
