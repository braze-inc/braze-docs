---
nav_title: Inkit
article_title: Inkit
alias: /fr/partners/inkit/
description: "Cet article décrit le partenariat entre Braze et Inkit, qui vous permet de gagner du temps et des efforts en automatisant vos campagnes de publipostage et en ramenant vos clients hors ligne en ligne."
page_type: partenaire
search_tag: Partenaire
---

# Inkit

> [Inkit][1] vous permet de joindre et de communiquer avec vos clients en leur fournissant des campagnes de messagerie directe automatisées et personnalisées, rendre des documents sans papier à l'échelle et valider les adresses postales des clients.

L'intégration de Braze et Inkit vous permet d'envoyer du courrier Inkit aux utilisateurs de Braze via les webhooks de Braze.

## Pré-requis

| Exigences                                                       | Libellé                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Inkit                                                    | Un [compte Inkit](https://console.liftigniter.com/login) est requis pour profiter de ce partenariat.                                                                                                                                                                                      |
| Inkit API key<br><br>`<INKIT_API_TOKEN>`      | Cette clé se trouve sur votre [Tableau de bord Inkit](https://app.inkit.io/#/account/integrations) vous permettra de connecter vos comptes Braze et Inkit.                                                                                                                                |
| Modèle de kit ID<br><br>`<INKIT_TEMPLATE_ID>` | Cette clé se trouve dans l'URL de chaque modèle, vous permettant d'envoyer votre modèle en Brésil. <br><br>Par exemple, dans l'URL `https://app.inkit.io/#/templates/design/bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`, l'ID du modèle est `bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`. |
| En-tête HTTP                                                    | Trouvé sur votre compte Inkit, vous allez combiner cela avec votre clé API Inkit pour autoriser la connexion comme une paire clé-valeur dans votre modèle Braze.                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Créer un modèle Inkit

Sur la plate-forme Inkit, créez un modèle à utiliser dans votre campagne Braze. Consultez la [documentation Inkit](https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration) sur ce partenariat pour en savoir plus.

### Étape 2 : Créez votre modèle de webhook Braze

Créer un modèle de webhook Inkit à utiliser dans de futures campagnes ou Canvases, accédez à la section **Modèles & Médias** de la plateforme Braze. Si vous souhaitez créer une campagne de webhook Inkit unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

!\[Modèle de webhook Inkit\]\[7\]

Une fois que vous avez sélectionné le modèle de webhook Inkit, vous devriez voir ce qui suit :
- **URL du Webhook**: `https://internal.inkit.io/integrations/webhook`
- **Corps de la requête**: Texte brut

!\[Inkit intégration\]\[5\]

#### En-têtes de requête et méthode

Inkit nécessite un `en-tête HTTP` pour être autorisé qui inclut votre clé API Inkit encodée en base 64. Les éléments suivants seront déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres** , vous devez remplacer la `<INKIT_API_TOKEN>` par votre clé API Inkit.

{% raw %}
- **Méthode HTTP**: POST
- **En-tête de la requête**:
  - **Autorisation**: Basique `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Corps de la requête**: application/json
{% endraw %}

#### Corps de la requête

Assurez-vous que votre Liquid correspond aux attributs personnalisés appropriés associés aux champs obligatoires et facultatifs listés ci-dessous. Vous pouvez également ajouter des champs de données personnalisés à n'importe quelle requête.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "compagnie": "{{custom_attribute.${company_name}}}",
  "téléphone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Étape 3 : Aperçu de votre demande

Votre texte brut sera automatiquement mis en surbrillance s'il s'agit d'une balise Braze applicable. `rue`, `unité`, `état`, et `zip` doivent être configurés comme [attributs personnalisés][3] pour envoyer ce Webhook.

Prévisualisez votre demande dans le panneau de gauche ou accédez à l’onglet `Test` où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page! <br>Les modèles de webhook mis à jour peuvent être trouvés dans la liste **Modèles de Webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}
[5]: {% image_buster /assets/img/inkit-integration.png %} [7]: {% image_buster /assets/img/inkit-webhook-template.png %}

[1]: https://www.inkit.com
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes