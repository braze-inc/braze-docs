---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Cet article de référence présente le partenariat entre Braze et Inkit qui vous permet de gagner du temps en automatisant vos campagnes de publipostage et de ramener les clients hors ligne en ligne."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com) et Braze permettent aux entreprises de générer et de distribuer des documents en toute sécurité, aussi bien sous forme numérique que par publipostage.

_Cette intégration est maintenue par Inkit._

## À propos de l'intégration

L'intégration entre Braze et Inkit vous permet de générer des documents et de les envoyer directement aux utilisateurs de Braze grâce aux webhooks de Braze.

## Conditions préalables

|Condition| Description|
| ---| ---|
|Compte Inkit | Un [compte Inkit](https://www.inkit.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé API Inkit<br><br>`<INKIT_API_TOKEN>` | Cette clé se trouve sur votre [tableau de bord Inkit](https://app.inkit.io/#/account/integrations) sous l'onglet **Développement** et vous permettra de connecter vos comptes Braze et Inkit.|
| ID du modèle Inkit<br><br>`<INKIT_TEMPLATE_ID>` | Après avoir créé un modèle, vous pouvez copier l'ID du modèle à partir de l'onglet **Modèles** pour l'utiliser dans votre modèle dans Braze.<br><br>Par exemple, vous pouvez créer un modèle appelé `invoice_template` dans l'environnement Inkit avec l'ID de modèle : `tmpl_3bDScFl9cwr3OAVR1RSdEC`.
| En-tête HTTP | L'en-tête HTTP fait partie de la requête API que vous envoyez de Braze à Inkit. Vous devez y inclure votre clé API Inkit pour authentifier et autoriser les appels à l'API Inkit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration

### Étape 1 : Créer un modèle Inkit

Sur la plateforme Inkit, créez un modèle à utiliser dans votre campagne Braze en HTML, Word, PowerPoint, Excel ou PDF. Consultez la [documentation d'Inkit](https://docs.inkit.com/docs/create-a-template) pour en savoir plus.

### Étape 2 : Créez votre modèle de webhook Braze à Braze

Pour créer un modèle de webhook Inkit à utiliser dans de futures campagnes ou Canvases, naviguez vers **Modèles** > **Modèles de webhook** dans la plateforme Braze. 

Si vous souhaitez créer une campagne webhook Inkit unique ou utiliser un modèle existant, sélectionnez **Webhook** à Braze lors de la création d'une nouvelle campagne.

![Une sélection de modèles de webhook prédéfinis disponibles dans l'onglet Modèles de webhook de la section Modèles et médias.]({% image_buster /assets/img/inkit-webhook-template.png %})

Une fois que vous avez sélectionné le modèle de webhook Inkit, vous devriez voir ce qui suit :
- **URL du webhook** : Blanc
- **Corps de la requête** : Texte brut

Dans le champ URL du webhook, vous devez [créer](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) et saisir une URL de webhook Inkit.

![Code du corps de la requête et URL du webhook affichés dans l'onglet de composition du générateur webhook Braze.]({% image_buster /assets/img/inkit-integration.png %})

#### En-têtes et méthode de la requête

Inkit a besoin d’un paramètre `HTTP Header` pour l'autorisation, y compris pour votre clé API Inkit encodée en base 64. Ce qui suit sera déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres**, vous devez remplacer le `<INKIT_API_TOKEN>` par votre clé API Inkit.

{% raw %}
- **Méthode HTTP**: POST
- **En-tête de la requête** :
  - **Autorisation**: De base `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Corps de la requête

Veillez à ce que votre liquide corresponde aux attributs personnalisés appropriés associés aux champs obligatoires et facultatifs suivants. Vous pouvez également ajouter des champs de données personnalisés à toute requête.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Étape 3 : Prévisualiser votre requête

Votre texte brut sera automatiquement mis en évidence s'il s'agit d'une balise Braze applicable. Les valeurs `street`, `unit`,`state` et `zip` doivent être définies en tant qu’[attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) pour envoyer ce webhook.

Prévisualisez votre requête dans le panneau **Aperçu** ou accédez à l'onglet **Test**, où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}


