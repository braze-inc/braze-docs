---
nav_title: Lob
article_title: Lob
alias: /fr/partners/lob/
description: "Cet article décrit le partenariat entre Braze et Lob.com, qui vous permet d'envoyer du courrier direct comme des lettres, des cartes postales et des chèques par courrier."
page_type: partenaire
search_tag: Partenaire
---

# Lob

> [Lob.com][38] est un service en ligne qui vous permet d'envoyer du courrier direct à vos utilisateurs.

L'intégration de Braze et Lob tire parti des webhooks de Braze et de l'API Lob pour envoyer des courriers comme des lettres, des cartes postales et des vérifications par courrier.

## Pré-requis

| Exigences        | Libellé                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| Compte Lob       | Un compte Lob est requis pour profiter de ce partenariat.                                                          |
| Clé de l'API Lob | Vous pouvez trouver la clé de l'API Lob dans la section des paramètres sous votre nom dans le tableau de bord Lob. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Sélectionnez le point de terminaison de Lob

L'URL HTTP à demander dans le webhook est différente pour chaque action que vous pouvez faire à Lob. Dans l'exemple suivant, nous utilisons le point de terminaison de l'API postcards `https://api.lob.com/v1/postcards`. Visitez la [liste complète de points de terminaison][39] pour sélectionner le point de terminaison approprié à votre cas d'utilisation.

!\[Points de terminaison\]\[37\]

### Étape 2 : Créez votre modèle de webhook Braze

Créer un modèle de webhook Lob à utiliser dans de futures campagnes ou Canvases, accédez à la section **Modèles & Médias** de la plateforme Braze. Si vous souhaitez créer une campagne de webhook Lob unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle Webhook, remplissez les champs suivants :
- **URL du Webhook**: `<LOB_API_ENDPOINT>`
- **Corps de la requête**: Texte brut

#### En-têtes de requête et méthode

Lob nécessite un en-tête HTTP pour être autorisé et une méthode HTTP. Les éléments suivants seront déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres** , vous devez remplacer le `<LOB_API_KEY>` par votre clé API Lob. Cette clé doit inclure un ":" directement après la clé et être encodée en base 64.

- **Méthode HTTP**: POST
- **En-têtes de la requête**:
  - **Autorisation**: Basique `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

!\[Aperçu de la Lobe\]\[35\]

#### Corps de la requête

Ce qui suit est un exemple de corps de requête pour le point de terminaison des cartes postales de Lob. Alors que ce corps de requête est fourni dans le modèle de base Lob en Brésil, Si vous souhaitez utiliser d'autres terminaux, vous devez ajuster vos champs Liquid en conséquence.

```json
{% raw %}"description": "Carte postale démo",
"pour": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"{% endraw %}
```

### Étape 3 : Aperçu de votre demande

À ce stade, votre campagne devrait être prête à être testée et envoyée. Vérifiez le tableau de bord Lob et les journaux de messages d'erreur de la console du développeur Braze si vous rencontrez des erreurs. Par exemple, l'erreur suivante a été causée par un en-tête d'authentification mal formaté.

!\[Message du journal d'erreur\]\[36\]

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page! <br>Les modèles de webhook mis à jour peuvent être trouvés dans la liste **Modèles de Webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}
[33]: {% image_buster /assets/img_archive/lob_api_key.png %} [34]: {% image_buster /assets/img_archive/lob_success_response.png %} [35]: {% image_buster /assets/img_archive/lob_full_request. ng %} [36]: {% image_buster /assets/img_archive/error_log.png %} [37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}

[38]: https://lob.com
[39]: https://lob.com/docs#intro
