---
nav_title: Zendesk
article_title: Zendesk
page_order: 9
description: "Cet article de référence présente le partenariat entre Braze et Zendesk, une suite d’assistance populaire qui vous permet d’utiliser des Webhooks de Braze pour synchroniser les données d’assistance entre les deux plateformes."
alias: /partners/zendesk/
page_type: partner
search_tag: Partenaire

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) permet aux entreprises d’avoir des conversations naturelles avec leurs clients à l’aide d’un support omnicanal utilisant les e-mails, un chat en ligne, la voix ou des applications de messageries sociales. Zendesk offre un système de cas d’assistance simplifié qui valorise le suivi et hiérarchise les interactions, ce qui permet aux entreprises d’avoir une vue historique et unifiée de leurs clients.

L’intégration serveur à serveur de Braze et Zendesk vous permet d’utiliser les Webhooks de Braze pour créer automatiquement des cas d’assistance dans Zendesk suite à l’engagement par message du parcours des utilisateurs dans Braze. Par exemple, après avoir mis en œuvre et testé une intégration, Braze peut créer un cas d’assistance pour un utilisateur qui a répondu négativement à un message in-app : « Vous aimez notre application ? » , permettant ainsi à votre équipe d’assistance de suivre le client.  

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Zendesk | Un [compte admin Zendesk](https://`<your-zendesk-instance>`.zendesk.com/agent/admin) est requis pour profiter de ce partenariat. |
| Jeton d’API Zendesk | Un [jeton d’API][2] Zendesk est nécessaire pour envoyer des requêtes de Braze vers l’endpoint des cas d’assistance Zendesk. |
| Identifiant commun (recommandé) | Un [identifiant commun](#common-identifier) entre Braze et Zendesk est recommandé. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer votre Webhook Braze
<br>
**Campagne**<br>Pour créer un Webhook, accédez à la page **Campaigns (Campagnes)** du tableau de bord de Braze, sous **Engagement**. Depuis le menu déroulant **Create Campaign (Créer une campagne)**, cliquez sur **Webhook** et nommez votre campagne.<br>
**Canvas**<br>Pour créer un Webhook à partir d’un nouveau Canvas ou d’un Canvas existant, créez une étape complète ou de message dans l’éditeur de Canvas. Ensuite, cliquez sur **Messages**, puis sélectionnez **Webhook** dans les options de message.

Dans votre Webhook, renseignez les champs suivants :
- **URL du webhook** : `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Corps de la demande** : Texte brut

D’autres cas d’utilisation peuvent être traités par les [API d’assistance Zendesk][4], ce qui changerait l’endpoint `/api/v2/` en conséquence à la fin de l’URL du Webhook.

#### En-têtes et méthode de requête

Zendesk nécessite un en-tête HTTP pour l’autorisation et une méthode HTTP. Dans l’onglet **Settings (Paramètres)**, remplacez le champ <email_address> par votre adresse e-mail administrateur Zendesk et <api_token> par votre jeton d’API Zendesk.

- **Méthode HTTP** : POST
- **En-têtes de requête** :
  - **Autorisation** : Basiques {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Type de contenu** : application/json

![][3]{: style="max-width:70%;"}

#### Corps de la demande

Définissez les détails du cas d’assistance comme le type, l’objet et le statut dans la charge de votre Webhook. Les détails du cas d’assistance sont extensibles et personnalisables avec l’[API d’assistance Zendesk][6]. Utilisez l’exemple suivant pour structurer votre charge utile et remplir les champs souhaités.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### Étape 2 : Prévisualiser votre demande

Votre texte brut indiquera automatiquement s’il s’agit d’une balise Braze.

Prévisualisez votre demande dans le volet **Preview (Prévisualiser)** ou accédez à l’onglet **Test** où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser votre propre test pour tester votre webhook.

Enfin, vérifiez si le cas d’assistance a été créé dans Zendesk.

## Identifiant commun

Si vous avez un identifiant commun entre Braze et Zendesk, il est recommandé de l’utiliser en tant qu’`requester_id` pour unifier les deux ensembles d’utilisateurs. Si vous ne disposez pas d’un identifiant commun, nous vous recommandons de transmettre un ensemble d’attributs d’identification tels que le nom, l’adresse e-mail, le numéro de téléphone ou autre.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[2]: https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %}
[4]: https://developer.zendesk.com/rest_api/docs/support/introduction
[5]: {% image_buster /assets/img_archive/zendesk_step2.png %}
[6]: https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket
[7]: {% image_buster /assets/img_archive/zdfinal.gif %}