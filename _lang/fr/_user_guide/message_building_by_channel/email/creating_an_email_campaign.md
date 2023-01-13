---
nav_title: Création d’un e-mail
article_title: Création d’un e-mail
page_order: 1
description: "Le présent article de référence explique comment créer un e-mail via la plateforme Braze. Vous trouverez ci-inclus les meilleures pratiques pour composer vos messages, prévisualiser votre contenu et planifier votre campagne ou Canvas."
tool:
  - Campagnes
channel:
  - E-mail
  
---

# Création d’une campagne d’e-mail

> Le présent article explique comment créer une campagne par e-mail dans Braze. Nous allons voir ici les étapes et les meilleures pratiques pour composer votre message, prévisualiser votre contenu et planifier votre campagne.

Les messages électroniques sont parfaits pour fournir du contenu à vos utilisateurs selon leurs conditions. Ils sont également d’excellents outils pour réengager les utilisateurs, même ceux qui ont désinstallé votre application. Des e-mails personnalisés et adaptés améliorent l’expérience utilisateur et aident votre public à tirer le meilleur parti de votre application. Pour voir des exemples de campagnes par e-mail, consultez nos [Études de cas](https://www.braze.com/customers). 

{% alert tip %}
Si c’est la première fois que vous créez une campagne par e-mail, nous vous recommandons vivement de consulter les cours suivants de Braze Learning :<br>

- [E-mail](https://learning.braze.com/messaging-channels-email)
- [Project: Élaborer un programme marketing d’e-mail basique](https://learning.braze.com/project-build-a-basic-email-marketing-program)

{% endalert %}

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campaign %}
**Étapes :**

1. Sur la page **Campaign (Campagne)**, cliquez sur <i class="fas fa-plus"></i>**Create Campaign (Créer une campagne)**
2. Sélectionnez **E-mail**, ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel Campaign (Campagne multicanale)**.
3. Donnez un nom clair et significatif à votre campagne.
4. Si nécessaire, ajoutez des [Équipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) et des [Tags.]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)
   * Les tags facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [Créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer les éléments en fonction de tags spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Pour plus d’informations sur ce sujet, consultez [Tests A/B et Tests multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant (Copier à partir de la variante)** dans le menu déroulant **Add Variant (Ajouter une variante)**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l’aide de l’Assistant Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre public pour cette étape, si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options de public seront vérifiées après le délai, au moment de l’envoi des messages.
5. Choisissez votre [comportement d’avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de messagerie que vous souhaitez associer à votre message.
{% endtab %}
{% endtabs %}

## Étape 2 : Sélectionnez votre expérience de modification {#step-2-choose-your-template-and-compose-your-email}

Braze offre deux expériences d’édition lors de la création d’une campagne d’e-mail : [l’Éditeur Drag & Drop]({{site.baseurl}}/dnd/) et l’éditeur HTML standard. Cliquez sur la vignette appropriée pour sélectionner l’expérience de modification que vous préférez. 

![Choix entre l’Éditeur Drag & Drop ou l’éditeur HTML pour votre expérience de modification des e-mails.][3]{: style="max-width:75%" }

Ensuite, vous pouvez sélectionner un [modèle d’e-mail ][10]existant, [charger un modèle][18] à partir d’un fichier (dans Éditeur HTML uniquement), ou utiliser un modèle vide. 

{% alert tip %}
Nous vous recommandons de sélectionner une expérience d’édition par campagne par e-mail. Par exemple, choisissez l’éditeur HTML Classic ou Block dans une campagne par e-mail unique plutôt que de basculer entre les éditeurs.
{% endalert %}

## Étape 3 : Composez votre e-mail

Après avoir sélectionné votre modèle, vous verrez un aperçu de votre e-mail où vous pourrez rapidement basculer sur l’éditeur en plein écran pour rédiger votre e-mail, modifier vos informations d’envoi et afficher les avertissements concernant la délivrabilité ou la conformité par rapport aux lois. 

Vous rédigez votre e-mail dans l’Éditeur Drag & Drop ? Reportez-vous à la section [Présentation de l’Éditeur Drag & Drop]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/) pour vous aider à composer votre e-mail. 

![Tableau des variantes d’e-mail pour composer votre e-mail.][14]{: style="max-width:75%" }

{% alert tip %}
Vous avez besoin d’aide pour créer un message génial ? Essayez [l’Assistant de Rédaction basé sur l’IA]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/). Entrez le nom ou la description d’un produit et l’IA générera un message marketing qui semble rédigé par un humain et que vous pourrez utiliser pour votre campagne.

![Utilisez le bouton AI Copywriter (Rédacteur IA) . sur l’onglet Body (Corps) du composeur d’e-mail.]{% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

### Étape 3a : Ajouter des en-têtes d’e-mail

Pour ajouter des en-têtes d’e-mail, cliquez sur **Edit Sending Info (Modifier les informations d’envoi)** et sélectionnez **Add New Header (Ajouter un nouvel en-tête)**.

Les en-têtes d’e-mail contiennent des informations sur l’e-mail envoyé. Ces [paires clé-valeur ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) contiennent généralement des informations sur l’expéditeur, le destinataire, les protocoles d’authentification ainsi que des informations de routage d’e-mail. Braze ajoute automatiquement les informations d’en-tête requises par les RFC pour que les e-mails soient livrés correctement à votre fournisseur de messagerie.

Cependant, Braze vous permet d’ajouter si nécessaire des en-têtes d’e-mails supplémentaires pour des cas d’utilisation avancés. Lors de l’envoi, la plate-forme Braze va écraser certains champs réservés. 

Évitez d’utiliser les touches suivantes :

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table id="reserved-fields">
<thead>
  <tr>
    <th>Champs réservés</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>CCI</td>
    <td>Signature DKIM</td>
    <td>Répondre à</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>De</td>
    <td>Objet</td>
  </tr>
  <tr>
    <td>Contenu-Transfert-Encodage</td>
    <td>Version MIME</td>
    <td>A</td>
  </tr>
  <tr>
    <td>Type de contenu</td>
    <td>Reçu</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>Signature DKIM</td>
    <td>reçu</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

### Étape 3b : Prévisualiser et tester votre message

Après avoir rédigé votre e-mail parfait, vous devez le tester avant de l’envoyer.

En bas de l’écran d’aperçu, cliquez sur **Preview and Test (Aperçu et test)**. Ici, vous pouvez voir comment votre e-mail apparaîtra dans la boîte de réception d’un client. Quand vous sélectionnez **Prévisualiser en tant qu’utilisateur**, vous pouvez prévisualiser votre e-mail en tant qu’utilisateur aléatoire, mais aussi sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de tester que vos appels de contenu connectés et de personnalisation fonctionnent comme ils le devraient.

Vous pouvez également basculer entre les vues PC, mobile et texte brut pour voir comment votre message apparaîtra dans différents contextes.

Lorsque vous êtes prêt pour une vérification finale, sélectionnez ** Test Send (Envoi d’un Test)** pour envoyer un message test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s’affiche correctement sur les divers appareils et clients par e-mail.

![Option d’envoi de test et exemple de prévisualisation du message lors de la composition d’un e-mail.][15]

Si vous rencontrez des problèmes avec votre e-mail ou si vous souhaitez apporter des modifications, cliquez sur **Edit Email (Modifier l’e-mail)** pour revenir à l’éditeur.

{% alert tip %}
Les clients par e-mail qui prennent en charge la prévisualisation mettent toujours suffisamment de caractères pour remplir tout l’espace disponible pour le texte de prévisualisation. Cependant, cela peut entrainer des cas où le texte de prévisualisation est incomplet ou non optimisé.
<br><br>Pour éviter cela, vous pouvez créer un espace blanc après le texte de prévisualisation souhaité pour que les clients par e-mail n’ajoutent pas du texte ou des caractères non souhaités. Vous n’avez qu’à ajouter une chaîne d’antiliants sans chasse (`&zwnj;`) et d’espaces insécables (`&nbsp;`) après le texte que vous souhaitez afficher dans la prévisualisation. <br><br>Si vous l’ajoutez à la fin de votre texte de prévisualisation dans la section Accroche, le code suivant ajoutera l’espace vide que vous souhaitez :<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

{% endalert %}

### Étape 3c : Vérifier les erreurs dans l’e-mail

L’éditeur vous affichera les problèmes qu’il détecte dans votre message avant que vous ne l’envoyiez. Voici une liste d’erreurs qui peuvent être détectées dans notre éditeur :

- **Nom d’affichage « De »** et **En-tête** non spécifiés ensemble
- Adresses **De** et **Répondre à** invalides
- Clés **d’en-tête** dupliquées
- Problèmes de syntaxe Liquid
- Corps d’e-mail de plus de 400 Ko (il est fortement recommandé que les corps des messages fassent [moins de 102 Ko][16])
- E-mails avec **Corps** ou **Sujet** vide
- E-mails sans lien de désinscription
- L’adresse e-mail émettrice n’est pas whitelistée (les envois seront fortement limités pour garantir la délivrabilité)

## Étape 4 : Créez le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campaign %}
Ensuite, construisez le reste de votre campagne ! Consultez les sections suivantes pour plus d’informations sur l’utilisation optimale de nos outils pour créer votre campagne par e-mail.

#### Choisir un calendrier ou un déclencheur pour la livraison

Les e-mails peuvent être livrés en fonction d’un calendrier, d’une action ou d’un déclencheur API. Pour en savoir plus, consultez la section [Planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
Pour les campagnes déclenchées par l’API, lorsque l’action de déclenchement est définie sur **Interact With Campaign (Interagir avec la campagne)**, la sélection de l’option**Recevoir** en tant qu’interaction déclenchera votre campagne dès que Braze marque la campagne sélectionnée comme étant envoyée, même si le message est rejeté ou non livré.
{% endalert %}

Vous pouvez également définir la durée de la campagne, des [Heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours), et spécifier des [limites de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler vos utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour préciser votre public. Vous verrez automatiquement un aperçu de la population approximative de ce segment à ce moment-là, y compris le nombre d’utilisateurs joignables par e-mail dans ce segment. Gardez à l’esprit que l’appartenance précise à un segment est toujours calculée juste avant l’envoi du message.

Vous pouvez également choisir d’envoyer votre campagne uniquement aux utilisateurs qui ont un [statut d’abonnement ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) spécifique, comme ceux qui sont inscrits et qui ont accepté de recevoir les e-mails.

Facultativement, vous pouvez également limiter la livraison à un nombre spécifié d’utilisateurs dans le segment, ou permettre aux utilisateurs de recevoir le même message deux fois dans le cadre d’une campagne récurrente.

##### Campagnes multicanales avec e-mail et notification push

Pour les campagnes multicanales avec e-mail et notifications push, vous pouvez limiter votre campagne pour que seuls les utilisateurs ayant explicitement consenti à recevoir des e-mails reçoivent le message (en excluant les utilisateurs abonnés et désabonnés). Par exemple, si vous avez trois utilisateurs avec un statut d’abonnement différent :

- **L’utilisateur A** est abonné aux e-mails et la notification push est activée. Cet utilisateur ne reçoit pas les e-mails, mais il recevra les notifications push.
- L’**utilisateur B** a consenti explicitement aux e-mails, mais la notification push n’est pas activée. Cet utilisateur recevra les e-mails, mais pas les notifications push.
- L’**utilisateur C** a consenti explicitement aux e-mails et la notification push est activée. Cet utilisateur recevra les e-mails et les notifications push.

Pour ce faire, sous **Audience Summary (Synthèse du public)**, sélectionnez pour envoyer cette campagne uniquement aux « utilisateurs ayant explicitement consenti ». Cette option garantira que seuls les utilisateurs abonnés recevront vos e-mails et Braze enverra uniquement vos notifications push aux utilisateurs pour lesquels la notification push est activée par défaut.

{% alert important %}
Avec cette configuration, n’incluez pas de filtres dans l’étape **Utilisateurs cible** qui limitent l’audience à un seul canal (par ex. `Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre à quelle fréquence les utilisateurs effectuent des actions spécifiques ([événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)) après avoir reçu une campagne. Vous pouvez spécifier l’une des actions suivantes en tant qu’événement de conversion :

- Ouvre l’application
- Effectue un achat (il peut s’agir d’un achat générique ou d’un article spécifique)
- Effectue un événement personnalisé spécifique
- Ouvre l’e-mail

Vous pouvez autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l’utilisateur effectue l’action spécifiée. Même si Braze suit automatiquement les ouvertures et les clics de votre campagne, vous pouvez néanmoins définir un Événement de conversion lorsque l’utilisateur ouvre ou clique sur une adresse e-mail pour tirer parti de la fonctionnalité de[ Sélection Intelligente de Braze]({{site.baseurl}}/user_guide/intelligence/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre Canvas Step. Pour plus d’informations sur la mise en place du reste de votre Canvas, la mise en œuvre d’un test multivarié et d’une sélection intelligente, etc. consultez la section [Construire votre Canvas Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.
{% endtab %}
{% endtabs %}

## Étape 5 : Revue et déploiement

La dernière page affiche un résumé de la campagne que vous venez de concevoir. Confirmez tous les détails pertinents et cliquez sur **Launch Campaign (Lancer la Campagne)** pour l’activer.

Maintenant, il suffit d’attendre que toutes les données arrivent ! Ensuite, consultez [Email reporting (Rapports sur l’e-mail)]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) pour voir comment accéder aux résultats de vos campagnes d’emailing.

[3]: {% image_buster /assets/img_archive/choose_email_creation.png %}
[5]: {% image_buster /assets/img_archive/targetsegment_email_new.png %}
[6]: {% image_buster /assets/img_archive/confirm_email.png %}
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[13]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[14]: {% image_buster /assets/img/email.png %}
[15]: {% image_buster /assets/img_archive/newEmailTest.png %}
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size
[17]: {% image_buster /assets/img_archive/email_click_results_heatmap.gif %}
[18]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/
[19]: {% image_buster /assets/img_archive/new_campaign_email.png %}
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[21]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[22]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/