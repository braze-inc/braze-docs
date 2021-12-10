---
nav_title: Zendesk
article_title: Zendesk
page_order: 9
description: "Cet article décrit le partenariat entre Braze et Zendesk, une suite de support populaire qui vous permet d'utiliser des webhooks Braze qui peuvent synchroniser les données entre les deux plateformes."
alias: /fr/partners/zendesk/
page_type: partenaire
search_tag: Partenaire
---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) offre aux entreprises la possibilité d'avoir des conversations naturelles avec leurs clients par le biais du support omnichannel en utilisant les e-mails, webchat, voix ou applications de messagerie sociale. ZSS valorise le support à la clientèle par le suivi et la priorisation des interactions, permettant aux entreprises d'avoir une vision historique unifiée de leurs clients. Des outils puissants comme un système de billetterie simplifié permettent aux entreprises de toucher directement leurs clients avec une approche personnalisée.

Braze offre une intégration de serveur à serveur avec Zendesk, vous permettant d'utiliser les webhooks de Braze qui peuvent synchroniser les données de tickets entre Braze et Zendesk.

## Exigences

| Exigences                                                 | Origine | Accès                                                                                                    | Libellé                                                                                                                                                                                                                                                              |
| --------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Zendesk & Informations sur le compte               | Zendesk | https://`<your-zendesk-instance>`.zendesk.com/agent/admin                                          | Un compte Zendesk actif __avec les privilèges d'administrateur__ est requis pour utiliser l'intégration de Braze.<br><br>Le jeton API Zendesk est nécessaire pour pouvoir envoyer des requêtes depuis Braze vers le point de terminaison Zendesk Billet. |
| Identificateur commun entre Braze et Zendesk (Recommandé) | Brasero | Pour plus d'informations, consultez la documentation de notre [Cycle de vie][1] du profil d'utilisateur. | Un [identifiant commun](#common-identifier) entre Braze et Zendesk est recommandé.                                                                                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration de Braze et Zendesk
#### Créer des tickets Zendesk à partir de campagnes Braze / Canvases

L'intégration de Braze et Zendesk vous permet d'automatiser la création de tickets de support à Zendesk en raison de l'engagement de messages dans les voyages des utilisateurs au Brésil. Par exemple, après avoir implémenté et testé avec succès l'intégration, Braze peut créer un ticket de support à partir d'un utilisateur qui répond négativement à un message dans l'application avec la question « Apprécier notre application ? , permettant à votre équipe de support de contacter le client et de lui offrir de l'aide.

Complétez les étapes suivantes pour utiliser le canal de Webhook Braze pour envoyer des données à Zendesk.

### Étape 1 : Créer une campagne de webhook ou Canvas
<br>
{% tabs %}
{% tab Campaign %}

Pour créer un webhook, allez à la page **Campagnes** sur le tableau de bord de Braze, sous **Engagement**. <br>Dans le menu déroulant **Créer une campagne** , sélectionnez **Webhook** et nommez votre campagne.

{% endtab %}
{% tab Canvas %}

Pour créer un webhook, à partir d'un nouveau Canvas ou d'un Canvas existant, créez une étape complète ou un message dans le constructeur de Canvas . Ensuite, cliquez sur l'icône de message vert qui apparaît, puis sur **Webhook** à partir des options de message.

{% endtab %}
{% endtabs %}

### Étape 2 : Paramètres du Webhook
Pour configurer le webhook, définissez d'abord le type de contenu à JSON pour qu'il communique avec Zendesk, ainsi que l'ajouter à vos informations d'autorisation :

1. Créer une paire clé/valeur. Set `Content-Type` comme clé et sa valeur à `application/json`.<br><br>
2. Définir `Autorisation` comme une autre paire clé/valeur et sa valeur comme : <br />
{% raw %} `Basic {{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}<br><br>Remplacez `<email_address>` par votre adresse e-mail d'administrateur Zendesk et `<api_token>` avec le jeton API généré en suivant <a href="https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\" f-id=">ces instructions</a>. Veuillez noter que vous devez utiliser la syntaxe Liquid, c'est pourquoi l'adresse e-mail __et le jeton d'API doivent être entre accolades__ comme indiqué ci-dessous. <br><br>!\[zendesk_step1\]\[3\]{: style="max-width:70%;"}

### Étape 3 : URL du Webhook

Ensuite, dites à Braze où envoyer le webhook. Dans ce cas d'utilisation du ticket, l'URL du Webhook serait :

`<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`.

Des cas d'utilisation supplémentaires peuvent être gérés via [les API de support Zendesk][4], qui changerait le point de terminaison `/api/v2/` en conséquence à la fin de l'URL Webhook.

!\[zendesk_step2\]\[5\]{: style="max-width:70%;"}

### Étape 4 : bloc Webhook
Ensuite, définissez les détails du ticket comme le type, le sujet et le statut dans votre charge utile de webhook. Les détails du ticket sont extensibles et peuvent être personnalisés en fonction de l'API [Zendesk Ticket][6]. Pour commencer à remplir votre payload, définissez le corps de la requête à `Texte brut`, puis entrez les champs souhaités. Veuillez voir ci-dessous pour un exemple :

{% raw %}
```
{% assigner ticket_type = 'question/incident/task/problem' %} << Choisir un >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Votre message ici >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject": "{{ticket_subject}}",
"commentaire": { "body": "{{ticket_body}}" },
"priorité": "urgent",
"statut": "{{ ticket_status }}"
  }

```
{% endraw %}

Dans l’exemple, vous pouvez voir que la première partie de ce bloc assigne les variables nécessaires, ainsi que le type de ticket pour le reste de la charge utile. La deuxième partie contient les informations spécifiques pour le billet.

### Étape 5 : Testez votre intégration

Pour tester votre webhook, accédez à l'onglet Aperçu et appuyez sur `Envoyer le test`. Vous verrez alors si l'appel a été réussi. Enfin, vérifiez si le ticket a été créé sur le côté de Zendesk.

!\[zdfinal\]\[7\]

## Identifiant commun

Si vous avez un identifiant commun entre Braze et Zendesk, il serait préférable de l'utiliser comme le `requester_id`. Sinon, si ce n'est pas le cas, transmettez un ensemble d'attributs d'identification tels que le nom, l'adresse e-mail, le numéro de téléphone ou d'autres.
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %} [5]: {% image_buster /assets/img_archive/zendesk_step2.png %} [7]: {% image_buster /assets/img_archive/zdfinal.gif %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket