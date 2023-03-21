---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Cet article de référence présente le partenariat entre Braze et Lob.com, qui vous permet d’envoyer des publipostages tels que des lettres, des cartes postales et des chèques par le biais du courrier."
page_type: partner
search_tag: Partenaire

---

# Lob

> [Lob.com][38] est un service en ligne qui vous permet d’envoyer directement des publipostages à vos utilisateurs.

L’intégration de Braze et Lob exploite les webhooks de Braze et de l’API de Lob pour envoyer des lettres, des cartes postales et des chèques par courrier postal.  

## Conditions préalables

|Condition| Description|
| ---| ---|
|Compte Lob | Un compte Lob est requis pour profiter de ce partenariat. |
| Clé d’API Lob | Vous pouvez trouver la clé d’API Lob sous la section des paramètres sous votre nom dans le tableau de bord de Lob. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Sélectionner l’endpoint Lob

L’URL HTTP à demander dans le webhook est différente selon l’action demandée à Lob. L’exemple suivant décrit l’utilisation de l’endpoint de l’API de carte postale`https://api.lob.com/v1/postcards`. Reportez-vous à la [liste complète des endpoints][39] pour sélectionner le plus approprié pour votre scénario. 

| endpoint de l’API | Endpoints disponibles |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/addresses<br>/v1/addresses/{id}<br>/v1/verify<br>/v1/postcards<br>/v1/postcards/{id}<br>/v1/letter<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/areas<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routes<br>/v1/countries<br>/v1/states|
{: .reset-td-br-1 .reset-td-br-2}

### Étape 2 : Créer votre modèle de webhook Braze

Pour créer un modèle de webhook Lob à utiliser dans les campagnes ou les Canvas futurs, accédez à la section **Templates & Media (Modèles et médias)** dans la plateforme Braze. Si vous souhaitez créer une campagne de webhook Lob unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.

Dans votre nouveau modèle de webhook, renseignez les champs suivants :
- **URL du webhook** : `<LOB_API_ENDPOINT>`
- **Corps de la demande** : Texte brut

#### En-têtes et méthode de la requête

Lob nécessite un en-tête HTTP pour l’autorisation et une méthode HTTP. Les éléments suivants seront déjà inclus dans le modèle comme paire clé-valeur, mais dans l’onglet **Settings (Paramètres)**, vous devez remplacer le `<LOB_API_KEY>` avec votre clé d’API Lob. Cette clé doit inclure le caractère « : » directement après la clé et être encodée dans la base 64. 

- **Méthode HTTP** : POST
- **En-têtes de requête** :
  - **Autorisation** : Basiques `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Type de contenu** : application/json

![Code du corps de la demande et URL du webhook affichés dans l’onglet de composition du constructeur de webhooks dans Braze.][35]

#### Corps de la demande

Voici un exemple de corps de demande pour l’endpoint cartes postales de Lob. Bien que ce corps de demande soit fourni dans le modèle de base de Lob dans Braze, si vous souhaitez utiliser d’autres endpoints, vous devez ajuster vos champs Liquid en conséquence.

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

### Étape 3 : Prévisualiser votre demande

À ce stade, votre campagne doit être prête à être testée et envoyée. Vérifiez le tableau de bord de Lob et les journaux des messages d’erreur de la Developer Console de Braze si vous rencontrez des erreurs. Par exemple, l’erreur suivante a été causée par un en-tête d’authentification mal formaté. 

![Journal d’erreur indiquant l’heure, le nom de l’application, le canal et le message d’erreur. Le message d’erreur inclut l’alerte de message et le code d’état.][36]

{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Saved Webhook Templates (Modèles de webhooks enregistrés)** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
[38]: https://lob.com
[39]: https://lob.com/docs#intro
[40]: https://lob.com/docs#auth
