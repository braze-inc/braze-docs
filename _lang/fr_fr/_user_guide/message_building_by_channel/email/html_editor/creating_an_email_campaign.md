---
nav_title: "Création d'un e-mail"
article_title: "Création d'un e-mail avec du HTML personnalisé"
page_order: 1
description: "Cet article de référence explique comment créer un e-mail à l'aide de la plateforme Braze. Vous y trouverez des bonnes pratiques sur la façon de composer vos messages, de prévisualiser votre contenu et de planifier votre campagne ou Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# Création d'un e-mail avec HTML personnalisé

> Les messages e-mail sont parfaits pour envoyer du contenu à vos utilisateurs selon leurs conditions. Ce sont également d'excellents outils pour réengager les utilisateurs qui ont peut-être même désinstallé votre appli. L'envoi de messages e-mail personnalisés et adaptés améliorera l'expérience sur l'application de vos utilisateurs, et les aidera à tirer le meilleur parti de votre appli. 

Pour voir des exemples de campagnes d'e-mail, consultez nos [études de cas.](https://www.braze.com/customers) 

{% alert tip %}
Si c'est la première fois que vous créez une campagne e-mail, nous vous recommandons vivement de consulter ces cours d'apprentissage de Braze :<br><br>
- [Abonnements et autorisations par e-mail](https://learning.braze.com/messaging-channels-email)
- [Projet : Créer un programme de base de marketing par e-mail](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé par le biais d'une campagne ou d'un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne.**
2. Sélectionnez **E-mail** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des étiquettes particulières.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Pour en savoir plus sur ce sujet, reportez-vous aux [tests multivariés et aux tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne seront similaires ou auront le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape dans le générateur de canvas. Donnez à votre démarche un nom clair et significatif.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape, si nécessaire. Vous pouvez encore affiner les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
5. Choisissez votre [comportement en matière d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.
{% endtab %}
{% endtabs %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Étape 2 : Sélectionnez votre expérience en matière de modification {#step-2-choose-your-template-and-compose-your-email}

Braze propose deux expériences d'édition lors de la création d'une campagne e-mail : notre [éditeur par glisser-déposer et]({{site.baseurl}}/dnd/) notre éditeur HTML standard. Choisissez la tuile appropriée pour l'expérience de modification que vous préférez. 

Choisissez entre l'éditeur par glisser-déposer, l'éditeur HTML ou les modèles pour l'édition de vos e-mails.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Vous pouvez ensuite sélectionner un [modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template) existant, [télécharger un modèle]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) à partir d'un fichier (éditeur HTML uniquement) ou utiliser un modèle vierge. 

{% alert tip %}
Nous vous recommandons de sélectionner une expérience de modification par campagne d'e-mail. Par exemple, choisissez l'**éditeur** **HTML Classic** ou **Block** dans une même campagne d'e-mail plutôt que de passer d'un éditeur à l'autre.
{% endalert %}

## Étape 3 : Composez votre e-mail

Après avoir sélectionné votre modèle, vous obtiendrez un aperçu de votre e-mail dans lequel vous pourrez passer directement à l'éditeur plein écran pour rédiger votre e-mail, modifier vos informations d'envoi et consulter les avertissements relatifs à la livrabilité ou à la conformité à la législation. Vous pouvez basculer entre les onglets HTML, classique, texte brut et [AMP]({{site.baseurl}}/user_guide/message_building_by_channel/email/amphtml/) pendant que vous rédigez. 

\![Le bouton "Régénérer à partir de HTML".]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

La version en clair de votre e-mail sera toujours mise à jour automatiquement à partir de la version HTML jusqu'à ce qu'une modification de la version en clair soit détectée. Lorsqu'une modification est détectée, Braze ne met plus à jour le texte en clair, car nous supposons que vous avez apporté des modifications intentionnelles qui ne devraient pas être écrasées. Vous pouvez revenir à la synchronisation automatique dans l'onglet **Texte en clair** en sélectionnant l'icône **Régénérer à partir du HTML**, qui n'apparaît que si le texte en clair n'est pas synchronisé.

{% alert tip %}
Pour ajouter du mouvement dans un e-mail avec un aperçu précis, utilisez des GIF au lieu d'éléments nécessitant JavaScript, car la plupart des boîtes de réception ne prennent pas en charge JavaScript.
{% endalert %}

!Panneau Variantes d'e-mail pour la composition de votre e-mail.]({% image_buster /assets/img/email.png %}){: style="max-width:75%" }

{% alert important %}
Braze supprimera automatiquement les gestionnaires d'événements HTML référencés en tant qu'attributs. Cette opération modifiera le code HTML, il est donc recommandé de revérifier l'e-mail une fois qu'elle est terminée. En savoir plus sur les [gestionnaires HTML.](https://www.w3schools.com/tags/ref_eventattributes.asp)
{% endalert %}

{% alert tip %}
Vous avez besoin d'aide pour créer un texte percutant ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez le nom ou la description d'un produit et l'intelligence artificielle générera un texte marketing de type humain à utiliser dans vos messages.

!Lancez le bouton de l'intelligence artificielle Copywriter, situé dans l'onglet Corps du compositeur d'e-mail.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Vous avez besoin d'aide pour rédiger des messages de droite à gauche dans des langues telles que l'arabe et l'hébreu ? Reportez-vous à la section [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) pour connaître les meilleures pratiques.

### Étape 3a : Ajoutez vos informations d'envoi

Une fois que vous avez fini de concevoir et de créer votre message e-mail, il est temps d'ajouter vos informations d'envoi dans la section **Paramètres d'envoi.** 

1. Sous **Informations sur l'envoi**, sélectionnez un e-mail comme **Nom d'affichage de l'expéditeur + adresse**. Vous pouvez également la personnaliser en sélectionnant **Personnaliser à partir de l'affichage du nom et de l'adresse.**
2. Sélectionnez un e-mail comme **adresse de réponse.** Vous pouvez également la personnaliser en sélectionnant **Personnaliser l'adresse de réponse.**
3. Ensuite, sélectionnez un e-mail comme **adresse CCI** pour que votre e-mail soit visible à cette adresse.
4. Ajoutez une ligne d'objet à votre e-mail. Vous pouvez également ajouter un accroche et un espace après l'accroche.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Un aperçu dans le panneau de droite s'affiche avec les informations d'envoi que vous avez ajoutées. Ces informations peuvent également être mises à jour en allant dans **Réglages** > **Préférences e-mail** > **Configuration de l'envoi.**

#### L'avancement

Sous **Paramètres d'envoi** > **Avancés**, vous pouvez activer le CSS en ligne et ajouter une personnalisation pour les en-têtes et les extras des e-mails, ce qui vous permet de renvoyer des données supplémentaires à d'autres fournisseurs de services d'e-mailing.

##### En-têtes d'e-mail

Pour ajouter des en-têtes d'e-mail, sélectionnez **Ajouter un nouvel en-tête**. Les en-têtes d'e-mail contiennent des informations sur l'e-mail envoyé. Ces [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) contiennent généralement des informations sur l'expéditeur, le destinataire, les protocoles d'authentification et les informations de routage des e-mails. Braze ajoute automatiquement les informations d'en-tête requises par le RFC pour que les e-mails soient correctement livrés à votre fournisseur de boîte de réception.

Braze vous offre la possibilité d'ajouter des en-têtes d'e-mail supplémentaires si nécessaire pour des cas d'utilisation avancés. Il existe quelques champs réservés que la plateforme Braze écrasera lors de l'envoi. 

Évitez d'utiliser les touches suivantes :

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
    <td>dkim-signature</td>
    <td>Répondre à</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>De</td>
    <td>Sujet</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>Pour</td>
  </tr>
  <tr>
    <td>Content-Type</td>
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

##### Ajout d'e-mails supplémentaires

Les extras d'e-mail vous permettent de renvoyer des données supplémentaires à d'autres fournisseurs de services d'e-mailing. Cette option ne s'applique qu'aux cas d'utilisation avancés ; vous ne devez donc utiliser les e-mails supplémentaires que si votre entreprise a déjà mis en place cette option.

Pour ajouter des e-mails supplémentaires, accédez aux **informations d'envoi** et sélectionnez **Ajouter un nouvel** e-mail supplémentaire.

{% alert warning %}
Le nombre total de paires clé-valeur ajoutées ne doit pas dépasser 1 Ko. Dans le cas contraire, les messages seront interrompus.
{% endalert %}

Les valeurs supplémentaires des e-mails ne sont pas publiées dans Currents ou Snowflake. Si vous souhaitez envoyer des métadonnées supplémentaires ou des valeurs dynamiques à Currents ou à Snowflake, utilisez l'option [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) à la place.

### Étape 3b : Prévisualisez et testez votre message

Une fois que vous avez fini de composer votre e-mail parfait, vous devez le tester avant de l'envoyer. En bas de l'écran d'aperçu, sélectionnez **Prévisualiser et tester**. 

Ici, vous pouvez prévisualiser la façon dont votre e-mail apparaîtra dans la boîte de réception d'un client. Si l'option **Prévisualiser en tant qu'utilisateur** est sélectionnée, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique ou créer un utilisateur personnalisé. Cela vous permet de tester que votre contenu connecté et vos appels de personnalisation fonctionnent comme il se doit. 

Ensuite, vous pouvez **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré.

Vous pouvez également passer de l'affichage sur ordinateur à l'affichage sur mobile et à l'affichage en texte clair pour avoir une idée de la façon dont votre message apparaîtra dans différents contextes.

{% alert tip %}
Curieux de savoir à quoi ressemble votre e-mail pour les utilisateurs en mode sombre ? Sélectionnez la bascule d'**aperçu du mode sombre** située dans la section **Aperçu et test** (éditeur par glisser-déposer uniquement).
{% endalert %}

Lorsque vous êtes prêt pour une dernière vérification, sélectionnez **Tester l'envoi** et envoyez un message test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s'affiche correctement sur une variété d'appareils et de clients de messagerie.

!Test de l'option d'envoi et aperçu de l'exemple d'e-mail lors de la composition de votre e-mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si vous constatez des problèmes avec votre e-mail ou si vous souhaitez y apporter des modifications, sélectionnez **Modifier l'e-mail** pour revenir à l'éditeur.

{% alert tip %}
Les clients e-mail qui prennent en charge le texte de prévisualisation insèrent toujours suffisamment de caractères pour remplir tout l'espace disponible pour le texte de prévisualisation. Cependant, vous pouvez vous retrouver dans des situations où le texte de l'aperçu est incomplet ou non optimisé.
<br><br>Pour éviter cela, vous pouvez créer un espace blanc après le texte de prévisualisation souhaité afin que les clients d'e-mail n'insèrent pas d'autres textes ou caractères distrayants dans le contenu de l'enveloppe. Pour ce faire, ajoutez une chaîne de non-joints de largeur nulle (`&zwnj;`) et d'espaces insécables (`&nbsp;`) après le texte de prévisualisation que vous souhaitez afficher. <br><br>Ajouté à la fin de votre texte d'aperçu dans la section accroche, le code suivant pour l'éditeur HTML ajoutera l'espace blanc que vous recherchez :<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
Pour l'éditeur glisser-déposer, ajoutez uniquement les non-jointeurs à largeur nulle (`&zwnj;`) sans le formatage `<div>` directement dans l'en-tête de la section **Paramètres d'accroche**.

{% endalert %}

### Étape 3c : Vérifier les erreurs d'e-mail

Le rédacteur signalera les problèmes qu'il détecte dans votre message avant que vous ne l'envoyiez. Voici une liste d'erreurs qui sont prises en compte dans notre éditeur :

- **A partir du Nom d'affichage** et de l'**En-tête** non spécifiés ensemble
- Adresses **"From** " et " **Reply-To"** non valides
- Duplication des clés d'**en-tête** 
- Problèmes de syntaxe des liquides
- Les corps d'e-mail de plus de 400 kb (il est fortement recommandé que les corps soient [inférieurs à 102 kb)]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size).
- E-mails dont le **corps** ou l'**objet** est vide
- Les e-mails sans lien de désinscription
- L'e-mail que vous envoyez n'est pas sur la liste des adresses autorisées (les envois seront fortement limités pour garantir la livrabilité).

## Étape 4 : Créez le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}
Ensuite, créez le reste de votre campagne ! Vous trouverez dans les sections suivantes de plus amples informations sur la manière d'utiliser au mieux nos outils pour créer votre campagne d'e-mailing.

#### Choisissez la planification ou le déclencheur de la réception/distribution

Les e-mails peuvent être délivrés en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
Pour les campagnes déclenchées par l'API, lorsque l'action de déclenchement est définie sur **Interagir avec la campagne**, la sélection d'une option **Recevoir** en tant qu'interaction entraînera le déclenchement de votre nouvelle campagne dès que Braze marquera la campagne sélectionnée comme envoyée, même si ce message rebondit ou ne parvient pas à être délivré.
{% endalert %}

Vous pouvez également définir la durée de la campagne, spécifier des [heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) et fixer des règles de [limitation de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisissez les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous obtiendrez automatiquement un aperçu de la population de ce segment à l'heure actuelle, y compris le nombre d'utilisateurs de ce segment qui peuvent être joints par e-mail. N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

Vous pouvez également choisir de n'envoyer votre campagne qu'aux utilisateurs qui ont un [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) spécifique, par exemple ceux qui sont abonnés et ont opté pour l'e-mail.

Vous pouvez également limiter la réception/distribution à un nombre déterminé d'utilisateurs au sein du segment, ou permettre aux utilisateurs de recevoir le même message deux fois lors d'une répétition de la campagne.

##### Campagnes multicanal avec e-mail et push

Pour les campagnes multicanal ciblant à la fois l'e-mail et les canaux push, vous pouvez limiter votre campagne de manière à ce que seuls les utilisateurs ayant explicitement opté pour le message le reçoivent (à l'exclusion des utilisateurs abonnés ou désabonnés). Par exemple, supposons que vous ayez trois utilisateurs ayant des statuts d'abonnement différents :

- L'**utilisateur A** est abonné à l'e-mail et dispose de la fonction "push". Cet utilisateur ne reçoit pas l'e-mail mais recevra le push.
- L'**utilisateur B** est abonné à l'e-mail mais n'est pas autorisé à utiliser la fonction "push". Cet utilisateur recevra l'e-mail mais ne recevra pas le push.
- L'**utilisateur C** est abonné à l'e-mail et dispose de la fonction "push". Cet utilisateur recevra à la fois l'e-mail et le push.

Pour ce faire, sous **Résumé de l'audience**, sélectionnez d'envoyer cette campagne aux "utilisateurs ayant opté pour l'abonnement uniquement". Cette option permet de vérifier que seuls les utilisateurs ayant opté pour l'abonnement recevront votre e-mail, et Braze n'enverra votre push qu'aux utilisateurs dont la fonction push est activée par défaut.

{% alert important %}
Avec cette configuration, n'incluez pas de filtres dans l'étape **Audiences cibles** qui limitent l'audience à un seul canal (par exemple, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

#### Choisissez des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous pouvez spécifier l'une des actions suivantes en tant qu'événement de conversion :

- Ouvre l'application
- Effectue un achat (il peut s'agir d'un achat générique ou d'un article spécifique)
- Exécution d'un événement personnalisé spécifique
- Ouvre l'e-mail

Vous pouvez autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée. Bien que Braze suive automatiquement les ouvertures et les clics pour votre campagne, vous pouvez définir l'événement de conversion comme étant le moment où un utilisateur ouvre ou clique sur une adresse e-mail afin de tirer parti de la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Si vous ne l'avez pas encore fait, complétez les sections restantes de vos composants Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.
{% endtab %}
{% endtabs %}

## Étape 5 : Examiner et déployer

La dernière section vous donnera un résumé de la campagne que vous venez de concevoir. Confirmez tous les détails pertinents et sélectionnez **Lancer des campagnes.** Maintenant, il est temps d'attendre que toutes les données arrivent ! 

Pour savoir comment vous pouvez accéder aux résultats de vos campagnes d'e-mail, consultez la rubrique [Rapports d'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)

