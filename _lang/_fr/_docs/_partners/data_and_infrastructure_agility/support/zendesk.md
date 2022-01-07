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

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) offre aux entreprises la possibilité d'avoir des conversations naturelles avec leurs clients par le biais du support omnichannel en utilisant les e-mails, webchat, voix ou applications de messagerie sociale. Zendesk propose un système de billetterie simplifié qui valorise le suivi et la priorisation des interactions, permettant aux entreprises d'avoir une vision historique unifiée de leurs clients.

L'intégration entre serveurs de Braze et Zendesk vous permet d'utiliser les webhooks de Braze pour automatiser la création de tickets de support à Zendesk en raison de l'engagement de messages dans les voyages des utilisateurs au Brésil. Par exemple, après avoir implémenté et testé avec succès une intégration, Braze peut créer un ticket de support à partir d'un utilisateur répondant négativement à une "Appréciation de notre application ? message dans l'application, permettant à votre équipe d'assistance de suivre avec le client.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Zendesk                  | Un compte administrateur [Zendesk](https://<code><your-zendesk-instance></code>.zendesk.com/agent/admin) est requis pour profiter de ce partenariat.                                                                              |
| Zendesk API token               | Un jeton API <a href="https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\" f-id=">Zendesk</a> est requis pour envoyer des requêtes depuis Braze vers le point de terminaison du ticket Zendesk. |
| Identifiant commun (recommandé) | Un [identifiant commun](#common-identifier) entre Braze et Zendesk est recommandé.                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créez votre webhook Braze
<br>
**Campagne**<br>Pour créer un webhook, allez sur la page **Campagnes** du tableau de bord de Braze, sous **Engagement**. Dans le menu déroulant **Créer une campagne** , sélectionnez **Webhook** et nommez votre campagne.<br> **Toile**<br>Pour créer un webhook, à partir d'un nouveau Canvas ou d'un Canvas existant, créez une étape complète ou un message dans le constructeur de Canvas . Ensuite, cliquez sur l'icône de message vert qui apparaît, puis sur **Webhook** à partir des options de message.

Dans votre Webhook, remplissez les champs suivants :
- **URL du Webhook**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Corps de la requête**: Texte brut

Des cas d'utilisation supplémentaires peuvent être gérés via [les API de support Zendesk][4], qui changerait le point de terminaison `/api/v2/` en conséquence à la fin de l'URL Webhook.

#### En-tête et méthode de la requête

Zendesk nécessite un en-tête HTTP pour être autorisé et une méthode HTTP. Dans l'onglet **Paramètres** , remplacez le <email_address> avec votre email d'administration Zendesk et <api_token> avec votre jeton API Zendesk.

- **Méthode HTTP**: POST
- **En-têtes de la requête**:
  - **Autorisation**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

!\[Zendesk HTTP header and method\]\[3\]{: style="max-width:70%;"}

#### Corps de la requête

Définissez les détails du ticket comme le type, le sujet et le statut dans votre charge utile de webhook. Les détails du ticket sont extensibles et personnalisés en fonction de l'API [Zendesk][6]. Utilisez l'exemple suivant pour structurer votre charge utile et entrer les champs souhaités.

{% raw %}
```json
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

### Étape 2 : Aperçu de votre demande

Votre texte brut sera automatiquement mis en surbrillance s'il s'agit d'une balise Braze applicable.

Prévisualisez votre demande dans le panneau de gauche ou accédez à l’onglet **Test** où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

Enfin, vérifiez si le ticket a été créé sur le côté de Zendesk.

## Identifiant commun

Si vous avez un identifiant commun entre Braze et Zendesk, il est recommandé d'utiliser ceci comme le `requester_id`, cela aidera à unifier les deux ensembles d'utilisateurs. Sinon, si ce n'est pas le cas, nous vous recommandons de passer un ensemble d'attributs d'identification tels que le nom, l'adresse e-mail, le numéro de téléphone ou autres.
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %} [5]: {% image_buster /assets/img_archive/zendesk_step2.png %} [7]: {% image_buster /assets/img_archive/zdfinal.gif %}

[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket