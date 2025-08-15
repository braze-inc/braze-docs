---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et MyPostcard, qui vous permet d'utiliser le publipostage comme un canal supplémentaire pour votre flux de travail CRM."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard][1], une application mondiale de cartes postales de premier plan, vous permet d'exécuter des campagnes de publipostage en toute simplicité, offrant un moyen fluide et rentable d'entrer en contact avec vos clients. 

Utilisez l'intégration de MyPostcard et de Braze pour envoyer sans effort des mailings imprimés à vos clients.

## Conditions préalables

| Condition                      | Description                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Compte MyPostcard B2B           | L'inscription à MyPostcard est nécessaire pour profiter de cette intégration.                                          |
| Clé API B2B et informations d'identification        | Vous trouverez votre clé API et les informations d'identification dans l'outil d'administration de MyPostcard B2B.                                         |
| Approbation de la campagne B2B de MyPostcard | Pour profiter de cette intégration, vous devez implémenter une campagne de publipostage dans l'outil MyPostcard B2B. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Cas d’utilisation

Pour améliorer vos campagnes de publipostage, il est essentiel d'aller au-delà des envois de masse traditionnels et d'intégrer le courrier imprimé de façon fluide/sans heurts dans vos flux de travail. Cette approche vous permet d'atteindre des clients personnalisés qui se sont désabonnés de vos bulletins d'information par e-mail ou dont les e-mails sont marqués comme étant des spams. Avec MyPostcard, vous pouvez envoyer sans effort des campagnes de publipostage directement via Braze.

- Créez des flux de travail intuitifs dans Braze, en intégrant le courrier imprimé comme un nouveau canal puissant, sans aucune expertise technique.
- Libérez le potentiel des mailings imprimés personnalisés en quelques étapes simples.
- Bénéficiez d'une mise en œuvre simple qui s'accompagne d'une assistance personnalisée de la part d'une équipe dédiée.

## Intégration

Pour intégrer MyPostcard, [connectez-vous ou inscrivez-vous][2] et créez votre première campagne pour l'utiliser via les [webhooks de Braze][3].

### Étape 1 : Créez votre modèle de webhook Braze à Braze

Créez un modèle de webhook MyPostcard à utiliser dans de futures campagnes ou Canvases en naviguant vers **Modèles** > **Modèles de webhook à** Braze dans la plateforme Braze.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), allez dans **Engagement** > **Modèles et médias** > **Modèles de webhook.**
{% endalert %}

Si vous souhaitez créer une campagne webhook MyPostcard ponctuelle ou utiliser un modèle existant, sélectionnez **Webhook** à Braze lors de la création d'une nouvelle campagne. Remplissez les champs suivants :

| Champ         | Description                                               |
|---------------|-----------------------------------------------------------|
| **URL du webhook** | L'URL du webhook telle qu'elle apparaît dans l'outil d'administration B2B.             |
| **Corps de la demande** | Texte brut (format JSON trouvé dans l'outil d'administration B2B).        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Méthode de requête et en-têtes

MyPostcard exige qu'une méthode HTTP ainsi que les en-têtes HTTP suivants soient inclus dans le modèle.

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Champ</strong></th>
      <th><strong>Détails</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Méthode HTTP</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Nom d’utilisateur</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Mot de passe</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Type de contenu</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Corps de la demande

Copiez le corps de la demande affiché dans l'outil d'administration B2B, puis remplissez les marqueurs substitutifs avec du contenu en utilisant les étiquettes de personnalisation Liquid.

![Onglet Compose affichant le corps JSON et les informations relatives au webhook.][4]

### Étape 2 : Prévisualiser votre requête

Ensuite, prévisualisez votre demande dans le panneau **Aperçu** ou allez dans l'onglet **Test**, où vous pouvez choisir un utilisateur aléatoire, un utilisateur existant ou créer un utilisateur personnalisé pour tester votre webhook. N'oubliez pas d'enregistrer votre modèle avant de quitter la page !

![Testez l'onglet webhook avec différents champs pour valider la mise en œuvre.][5]

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}

[1]: https://www.mypostcard.com
[2]: https://www.mypostcard.com/b2b/admin/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks
[4]: {% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %}
[5]: {% image_buster /assets/img/mypostcard/mypostcard_test.jpg %}
