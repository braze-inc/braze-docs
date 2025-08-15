---
nav_title: Création d’un e-mail
article_title: Créer un e-mail avec du HTML personnalisé
page_order: 1
description: "Le présent article de référence explique comment créer un e-mail via la plateforme Braze. Vous trouverez ci-inclus les bonnes pratiques pour composer vos messages, prévisualiser votre contenu et planifier votre campagne ou Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# Créer un e-mail avec du HTML personnalisé

> Les messages électroniques sont parfaits pour fournir du contenu à vos utilisateurs selon leurs conditions. Ils sont également d’excellents outils pour réengager les utilisateurs, même ceux qui ont désinstallé votre application. Des e-mails personnalisés et adaptés améliorent l’expérience utilisateur et aident votre public à tirer le meilleur parti de votre application. 

Pour voir des exemples de campagnes par e-mail, consultez nos [études de cas](https://www.braze.com/customers). 

{% alert tip %}
Si c'est la première fois que vous créez une campagne e-mail, nous vous recommandons vivement de consulter ces cours d'apprentissage de Braze :<br><br>
- [Abonnements et autorisations par e-mail](https://learning.braze.com/messaging-channels-email)
- [Projet : Élaborer un programme marketing d’e-mail basique](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campagne %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **E-mail** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de certaines étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Pour plus d'informations sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier par étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape, si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai, au moment de l’envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.
{% endtab %}
{% endtabs %}

{% multi_lang_include drag_and_drop_access.md variable_name='email html editor' %}

## Étape 2 : Sélectionner votre expérience d’édition {#step-2-choose-your-template-and-compose-your-email}

Braze propose deux expériences d'édition lors de la création d'une campagne par e-mail : notre [éditeur par glisser-déposer]({{site.baseurl}}/dnd/) et notre éditeur HTML standard. Choisissez la tuile appropriée pour l'expérience de modification que vous préférez. 

![Choisissez entre l'éditeur par glisser-déposer, l'éditeur HTML ou les modèles pour l'édition de vos e-mails.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Vous pouvez ensuite sélectionner un [modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template) existant, [télécharger un modèle]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) à partir d'un fichier (éditeur HTML uniquement) ou utiliser un modèle vierge. 

{% alert tip %}
Nous vous recommandons de sélectionner une expérience d’édition par campagne par e-mail. Par exemple, choisissez l'éditeur **HTML classique** ou **l’éditeur de blocs** dans une même campagne d'e-mail plutôt que de passer d'un éditeur à l'autre.
{% endalert %}

## Étape 3 : Composez votre e-mail

Après avoir sélectionné votre modèle, vous verrez un aperçu de votre e-mail où vous pourrez passer directement à l'éditeur en plein écran pour rédiger votre e-mail, modifier vos informations d'envoi et voir les avertissements concernant la délivrabilité ou la conformité légale. Vous pouvez basculer entre les onglets HTML, classique, texte brut et [AMP]({{site.baseurl}}/user_guide/message_building_by_channel/email/amphtml/) pendant que vous rédigez. 

![Le bouton "Régénérer à partir de HTML".]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

La version en clair de votre e-mail sera toujours mise à jour automatiquement à partir de la version HTML jusqu'à ce qu'une modification de la version en clair soit détectée. Lorsqu'une modification est détectée, Braze ne met plus à jour le texte en clair, car nous supposons que vous avez apporté des modifications intentionnelles qui ne devraient pas être écrasées. Vous pouvez revenir à la synchronisation automatique dans l'onglet **Texte en clair** en sélectionnant l'icône **Régénérer à partir du HTML**, qui n'apparaît que si le texte en clair n'est pas synchronisé.

{% alert tip %}
Pour ajouter une dynamique dans un e-mail avec un aperçu précis, utilisez des GIF au lieu d'éléments nécessitant JavaScript, car la plupart des boîtes de réception ne prennent pas en charge JavaScript.
{% endalert %}

![Panneau de variantes d'e-mail pour la composition de votre e-mail.]({% image_buster /assets/img/email.png %}){: style="max-width:75%" }

{% alert important %}
Braze supprimera automatiquement les gestionnaires d’événements HTML référencés comme attributs. Cela modifiera le HTML, il est donc recommandé de revérifier l'e-mail une fois terminé. En savoir plus sur les [gestionnaires HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Besoin d’aide pour créer un texte d’exception ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez un nom ou une description du produit et l’IA générera un texte marketing semblant d’origine humaine pour une utilisation dans votre envoi de messages.

![Bouton Lancer l’IA de rédaction, situé dans l’onglet Corps du composeur d’e-mail.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Vous avez besoin d'aide pour rédiger des messages de droite à gauche dans des langues telles que l'arabe et l'hébreu ? Reportez-vous à la section [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) pour connaître les meilleures pratiques.

### Étape 3a : Ajoutez vos informations d'envoi

Après avoir terminé de concevoir et de créer votre message électronique, il est temps d'ajouter vos informations d'envoi dans la section **Paramètres d'envoi**.

1. Sous **Envoi d'informations**, sélectionnez un e-mail comme **Nom d'affichage + adresse de l'expéditeur**. Vous pouvez également personnaliser cela en sélectionnant **Personnaliser à partir du nom d'affichage + adresse**.
2. Sélectionnez un e-mail comme l'**adresse de réponse**. Vous pouvez également personnaliser ceci en sélectionnant **Personnaliser l'adresse de réponse**.
3. Ensuite, sélectionnez un e-mail comme **BCC Address** pour rendre votre e-mail visible à cette adresse.
4. Ajoutez une ligne d'objet à votre e-mail. Vous avez également la possibilité d’ajouter une accroche suivie d’un espace.

Les informations d'envoi que vous avez ajoutées sont renseignées dans un aperçu dans le panneau de droite. Ces informations peuvent également être mises à jour en allant dans **Réglages** > **Préférences e-mail** > **Configuration de l'envoi.**

#### Avancée

Sous **Paramètres d'envoi** > **Avancé**, vous pouvez activer le CSS en ligne et ajouter une personnalisation pour les en-têtes d'e-mail et les extras d'e-mail, ce qui vous permet d'envoyer des données supplémentaires à d'autres fournisseurs de services de messagerie.

##### En-têtes d’e-mail

Pour ajouter des en-têtes d'e-mail, sélectionnez **Ajouter un nouvel en-tête**. Les en-têtes d’e-mail contiennent des informations sur l’e-mail envoyé. Ces [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) contiennent généralement des informations sur l'expéditeur, le destinataire, les protocoles d'authentification et les informations de routage des e-mails. Braze ajoute automatiquement les informations d’en-tête requises par les RFC pour que les e-mails soient livrés correctement à votre fournisseur de messagerie.

Braze vous permet d'ajouter des en-têtes d'e-mail supplémentaires selon les besoins pour des cas d'utilisation avancés. Lors de l’envoi, la plate-forme Braze va écraser certains champs réservés. 

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

##### Ajout d’options d’e-mail

Les options d’e-mail vous permettent d'envoyer des données supplémentaires à d'autres fournisseurs de services d’e-mailing. Ceci n'est applicable que pour des cas d'utilisation avancés, vous ne devez donc utiliser les options d’e-mail que si votre entreprise a déjà mis cela en place.

Pour ajouter des e-mails supplémentaires, accédez aux **informations d'envoi** et sélectionnez **Ajouter un nouvel** e-mail supplémentaire.

{% alert warning %}
Le nombre total de paires clé-valeur ajoutées ne doit pas dépasser 1 Ko. Sinon, les messages seront annulés.
{% endalert %}

Les valeurs supplémentaires des e-mails ne sont pas publiées sur Currents ou Snowflake. Si vous souhaitez envoyer des métadonnées supplémentaires ou des valeurs dynamiques à Currents ou Snowflake, utilisez plutôt [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

### Étape 3b : Prévisualiser et tester votre message

Après avoir rédigé votre e-mail parfait, vous devez le tester avant de l’envoyer. En bas de l'écran d'aperçu, sélectionnez **Prévisualiser et tester**. 

Ici, vous pouvez visualiser la façon dont votre e-mail apparaîtra dans la boîte de réception d’un client. Si l'option **Prévisualiser en tant qu'utilisateur** est sélectionnée, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de tester que vos appels de contenu connecté et de personnalisation fonctionnent correctement. 

Ensuite, vous pouvez **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré.

Vous pouvez également basculer entre l’affichage mobile de bureau et de texte brut pour comprendre comment votre message apparaîtra dans différents contextes.

{% alert tip %}
Vous aimeriez savoir à quoi ressemblent vos e-mails pour vos utilisateurs en mode sombre ? Sélectionnez le **Aperçu en mode sombre** situé dans la section **Aperçu et test** (éditeur par glisser-déposer uniquement).
{% endalert %}

Lorsque vous êtes prêt pour une vérification finale, sélectionnez **Test Send** et envoyez un message de test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s'affiche correctement sur une variété d'appareils et de clients de messagerie.

![Testez l'option d'envoi et l'aperçu de l'exemple d'e-mail lors de la rédaction de votre e-mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si vous constatez des problèmes avec votre e-mail ou si vous souhaitez y apporter des modifications, sélectionnez **Modifier l'e-mail** pour revenir à l'éditeur.

{% alert tip %}
Les clients par e-mail qui prennent en charge la prévisualisation mettent toujours suffisamment de caractères pour remplir tout l’espace disponible pour le texte de prévisualisation. Cependant, cela peut entrainer des cas où le texte de prévisualisation est incomplet ou non optimisé.
<br><br>Pour éviter cela, vous pouvez créer un espace blanc après le texte de prévisualisation souhaité pour que les clients par e-mail n’ajoutent pas du texte ou des caractères non souhaités. Vous n’avez qu’à ajouter une chaîne d’antiliants sans chasse (`&zwnj;`) et d’espaces insécables (`&nbsp;`) après le texte que vous souhaitez afficher dans la prévisualisation. <br><br>Si vous l’ajoutez à la fin de votre texte de prévisualisation dans la section Accroche, le code suivant ajoutera l’espace vide que vous souhaitez pour l’éditeur HTML :<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
Pour l'éditeur de glisser-déposer, ajoutez uniquement les caractères non-joinants de largeur nulle (‌`&zwnj;`) sans le formatage `<div>` directement dans l'en-tête dans la section **Paramètres d'envoi**.

{% endalert %}

### Étape 3c : Vérifier les erreurs de courrier électronique

L’éditeur vous affichera les problèmes qu’il détecte dans votre message avant que vous ne l’envoyiez. Voici une liste d’erreurs prises en compte dans notre éditeur :

- **De Nom d'affichage** et **En-tête** non spécifiés ensemble
- Adresses **De** et **Répondre à** non valides
- Dupliquer les clés **En-tête**
- Problèmes de syntaxe Liquid
- Les corps d'e-mail de plus de 400 kb (il est fortement recommandé que les corps soient [inférieurs à 102 kb)]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size).
- E-mails avec un **corps** vide ou un **sujet** vide
- E-mails sans lien de désinscription
- L’adresse e-mail émettrice ne figure pas dans la liste d’autorisation (les envois seront fortement limités pour garantir la livrabilité)

## Étape 4 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campagne %}
Ensuite, construisez le reste de votre campagne ! Voir les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer votre campagne par e-mail.

#### Choisir un calendrier ou un déclencheur pour la livraison

Les e-mails peuvent être livrés en fonction d’une heure planifiée, d’une action ou d’un déclencheur API. Pour plus d'informations, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
Pour les campagnes déclenchées par l'API, lorsque l'action de déclenchement est définie sur **Interagir avec la campagne**, sélectionner une option **Recevoir** comme interaction fera en sorte que votre nouvelle campagne se déclenche dès que Braze marque la campagne sélectionnée comme envoyée, même si ce message est rejeté ou n'est pas livré.
{% endalert %}

Vous pouvez également définir la durée de la campagne, spécifier [Heures de silence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours), et définir des règles de [limitation de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour affiner votre audience. Vous verrez automatiquement un aperçu de la population approximative de ce segment à ce moment-là, y compris le nombre d’utilisateurs joignables par e-mail dans ce segment. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

Vous pouvez également choisir d'envoyer votre campagne uniquement aux utilisateurs qui ont un [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) spécifique, comme ceux qui sont abonnés et ont choisi de recevoir des e-mails.

Facultativement, vous pouvez également limiter la livraison à un nombre spécifié d’utilisateurs dans le segment, ou permettre aux utilisateurs de recevoir le même message deux fois dans le cadre d’une campagne récurrente.

##### Campagnes multicanales avec e-mail et notification push

Pour les campagnes multicanales avec e-mail et notifications push, vous pouvez limiter votre campagne pour que seuls les utilisateurs ayant explicitement consenti à recevoir des e-mails reçoivent le message (en excluant les utilisateurs abonnés et désabonnés). Par exemple, si vous avez trois utilisateurs avec un statut d’abonnement différent :

- L'**utilisateur A** est abonné à l'e-mail et dispose de la fonction "push". Cet utilisateur ne reçoit pas les e-mails, mais il recevra les notifications push.
- L'**utilisateur B** est abonné à l'e-mail mais n'est pas autorisé à utiliser la fonction "push". Cet utilisateur recevra les e-mails, mais pas les notifications push.
- **Utilisateur C** est abonné aux e-mails et les notifications push sont activées. Cet utilisateur recevra les e-mails et les notifications push.

Pour ce faire, sous **Résumé de l'audience**, sélectionnez d'envoyer cette campagne uniquement aux « utilisateurs ayant choisi de participer ». Cette option vérifiera que seuls les utilisateurs ayant opté pour recevront votre e-mail, et Braze n'enverra votre notification push qu'aux utilisateurs qui ont activé les notifications push par défaut.

{% alert important %}
Avec cette configuration, n'incluez pas de filtres dans l'étape **Audiences cibles** qui limitent l'audience à un seul canal (par exemple, `Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous pouvez spécifier l’une des actions suivantes en tant qu’événement de conversion :

- Ouvre l’application
- Effectue un achat (il peut s’agir d’un achat générique ou d’un article spécifique)
- Effectue un événement personnalisé spécifique
- Ouvre l’e-mail

Vous pouvez autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l’utilisateur effectue l’action spécifiée. Bien que Braze suive automatiquement les ouvertures et les clics pour votre campagne, vous souhaiterez peut-être définir l'événement de conversion lorsque un utilisateur ouvre ou clique sur une adresse e-mail pour profiter de [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Si vous ne l’avez pas déjà fait, complétez les sections restantes de vos composants Canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, mettre en œuvre des tests multivariés et la Sélection Intelligente, et plus encore, consultez l'étape [Construisez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.
{% endtab %}
{% endtabs %}

## Étape 5 : Revue et déploiement

La dernière section vous donnera un résumé de la campagne que vous venez de concevoir. Confirmez tous les détails pertinents et sélectionnez **Lancer des campagnes.** Maintenant, il est temps d'attendre que toutes les données arrivent ! 

Pour savoir comment vous pouvez accéder aux résultats de vos campagnes d'e-mail, consultez la rubrique [Rapports d'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)

