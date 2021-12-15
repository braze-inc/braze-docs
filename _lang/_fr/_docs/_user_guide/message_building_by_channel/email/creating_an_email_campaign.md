---
nav_title: Création d'une campagne d'email
article_title: Création d'une campagne d'email
page_order: 1
description: "Cet article de référence traite de la façon de créer une campagne d'email à l'aide de la plateforme Braze. Les meilleures pratiques sur la façon de composer vos messages, de prévisualiser votre contenu et de planifier votre campagne."
tool:
  - Campagnes
channel:
  - Email
---

# Création d'une campagne d'email

> Cet article traite de la façon de créer une campagne d'email en Brésil. Ici, nous aborderons les étapes et les meilleures pratiques sur la façon de composer votre message, de prévisualiser votre contenu et de planifier votre campagne.

Les messages électroniques sont parfaits pour diffuser du contenu à vos utilisateurs selon leurs conditions. Ce sont également d'excellents outils pour réengager les utilisateurs qui ont même désinstallé votre application. Envoyer des messages électroniques personnalisés et personnalisés améliorera l'expérience de vos utilisateurs et aidera vos utilisateurs à tirer le meilleur parti de votre application. Pour voir des exemples de campagnes de courriel, consultez notre [Études de cas](https://www.braze.com/customers).

{% alert tip %}
Si c'est la première fois que vous créez une campagne de courriel, nous vous recommandons vivement de consulter les cours LAB suivants :<br>

- [Courriel](https://lab.braze.com/messaging-channels-email)
- [Projet: Construire un programme de marketing par e-mail de base](https://lab.braze.com/project-build-a-basic-email-marketing-program)

{% endalert %}

## Étape 1 : Créer une nouvelle campagne

Sur la page **Campagnes** , cliquez sur **Créer une campagne** et sélectionnez **Envoyer** comme canal de messagerie. !\[Nouvelle page de campagne\]\[19\]

## Étape 2 : Sélectionnez votre expérience d'édition {#step-2-choose-your-template-and-compose-your-email}

À partir de l'assistant de campagne, nommez votre e-mail et fournissez une description facultative. Vous pouvez également assigner [tags][20] pour garder une trace des tactiques d'engagement.

{% alert tip %}
Les balises facilitent la recherche et la création de rapports à partir de vos campagnes. Par exemple, lorsque vous utilisez [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer par balises particulières.
{% endalert %}

Braze offre deux expériences d'édition lors de la création d'une campagne de messagerie, notre [Éditeur Glisser & Déposer]({{site.baseurl}}/dnd/) ou notre éditeur HTML standard. Cliquez sur la tuile appropriée pour sélectionner l'expérience d'édition que vous préférez. Une fois sélectionné, vous devez également sélectionner un modèle d'e-mail [HTML][10] existant ou [Glisser & Déposer][10] le modèle d'e-mail, [télécharger un modèle à partir d'un fichier][18] (éditeur HTML seulement), ou utiliser un modèle vierge.

!\[Création de courriel\]\[3\]

Une fois que vous aurez sélectionné votre modèle, vous verrez un aperçu de votre e-mail où vous pourrez rapidement aller à l'éditeur plein écran pour rédiger votre courriel. modifiez vos informations d'envoi et affichez les avertissements concernant la délivrabilité ou la conformité à la loi.

!\[Nouvelle vue d'ensemble des e-mails\]\[14\]

### Étape 2a: Ajouter des en-têtes de courriel

Les en-têtes de courriel contiennent des informations sur l'e-mail envoyé. Ces paires clé-valeur ont généralement des informations sur l'expéditeur, le destinataire, les protocoles d'authentification et contiennent des informations de routage de courriel. Braze ajoute automatiquement les informations d'en-tête nécessaires à la RFC pour que les e-mails soient envoyés à votre fournisseur de boîte de réception correctement.

Cependant, Braze vous offre la flexibilité nécessaire pour ajouter des en-têtes de courriel supplémentaires au besoin pour les cas d'utilisation avancés. Il y a quelques champs réservés que la plateforme Braze écrasera pendant l'envoi. Évitez d'utiliser les clés suivantes :

| Champs réservés                    |                 |            |
| ---------------------------------- | --------------- | ---------- |
| Cci                                | signature dkim- | Répondre à |
| CC                                 | A partir de     | Sujet      |
| Encodage Content-Transfer-Encodage | Version MIME    | À          |
| Type de contenu                    | Reçu            | x-sg-eid   |
| Signature DKIM                     | reçue           | x-sg-id    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Étape 2b: Prévisualiser et tester votre message

Une fois que vous avez fini de composer votre e-mail parfait, vous devez le tester avant de l'envoyer.

À partir du bas de l'écran d'aperçu, cliquez sur **Aperçu et Tester**. Ici vous pouvez prévisualiser comment votre e-mail apparaîtra dans la boîte de réception d'un client. Avec **Aperçu en tant qu'utilisateur** sélectionné, vous pouvez prévisualiser votre e-mail en tant qu'utilisateur aléatoire, sélectionner un utilisateur spécifique, ou créer un utilisateur personnalisé. Cela vous permet de tester que vos appels de contenu connecté et de personnalisation fonctionnent comme ils le devraient.

Vous pouvez également basculer entre les vues bureau, mobile et texte en clair pour avoir une idée de la façon dont votre message apparaîtra dans différents contextes.

Quand vous êtes prêt pour une vérification finale, sélectionnez **Test Send** et envoyez un message de test à vous-même ou à un groupe de testeurs de contenu pour vous assurer que votre e-mail s'affiche correctement sur une variété de périphériques et de clients de messagerie.

!\[Nouveau aperçu de courriel\]\[15\]

Si vous voyez des problèmes avec votre adresse e-mail ou si vous souhaitez apporter des modifications, cliquez sur **Modifier l'e-mail** pour retourner à l'éditeur.

{% alert tip %}
Les clients de messagerie qui prennent en charge le texte d'aperçu tirent toujours suffisamment de caractères pour remplir tout l'espace de texte d'aperçu disponible. Cependant, cela peut vous laisser dans des situations où le texte de l'aperçu est incomplet ou non optimisé. <br><br>Pour éviter cela, vous pouvez créer de l'espace blanc après le texte de prévisualisation de votre choix afin que les clients de messagerie ne tirent pas d'autres caractères ou textes distrayant dans l'enveloppe. Pour ce faire, ajoutez une chaîne de non-joints à largeur zéro (<unk>`&zwnj;`) et les espaces non cassés (`&nbsp;`) après le texte d'aperçu que vous voulez afficher. <br><br>Lorsqu'il est ajouté à la fin de votre texte d'aperçu dans la section de préen-tête, le morceau de code suivant ajoutera l'espace que vous cherchez:
```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
{% endalert %}

### Étape 2c: Vérifier les erreurs de courriel

L'éditeur appellera tous les problèmes qu'il attrape avec votre message avant de l'envoyer. Voici une liste d'erreurs qui sont comptabilisées dans notre éditeur :

- **Nom d'affichage** et **en-tête** non spécifiés entre eux.
- Adresses **de** et de **Répondre à** non valides.
- Dupliquer les clés **En-tête**.
- Problèmes de syntaxe des liquides.
- [Corps de courrier électronique de plus de 400kb; les corps sont fortement recommandés pour être plus petits que 102kb.][16]
- Emails avec un **corps ** vide** ou **sujet**.</li>
- E-mails sans lien de désinscription.
- Le courriel à partir duquel vous envoyez n'est pas en liste blanche, donc les envois seront très limités pour assurer la délivrabilité.</ul>

## Étape 3 : Planifiez votre campagne de messagerie

Vous pouvez planifier vos campagnes avec trois types de livraison:

- Planifié (envoi de votre campagne à une heure désignée)
- Action-Based (envoi lorsque vos utilisateurs effectuent des actions spécifiées)
- Déclenché par l'API (envoi selon une requête API)

{% tabs %}
{% tab Scheduled Delivery %}
La livraison planifiée vous permet de spécifier l'heure à laquelle le message doit être envoyé, soit immédiatement ou à un moment futur (vous pouvez également considérer l'heure locale dans votre programme). Vous pouvez également utiliser [le Timing Intelligent][21] pour envoyer le message lorsque l'utilisateur est le plus susceptible de s'engager. Braze effectue ce calcul en se basant sur une analyse statistique des interactions de l'utilisateur avec votre application.

Les messages peuvent également être configurés pour se reproduire quotidiennement, hebdomadaire (optionnellement sur certains jours), ou mensuellement.

Sauf si vous cochez **Autoriser les utilisateurs à être de nouveau éligibles pour recevoir la campagne**, chaque utilisateur ne recevra le contenu d'une campagne qu'une seule fois, et seuls les nouveaux utilisateurs qui satisfont aux critères recevront la campagne sur les livraisons subséquentes.

![Planifier]({% image_buster /assets/img_archive/schedule_new.png %}){: height="80%"" width="80%"}

{% endtab %}
{% tab Action-Based Delivery %}

La distribution par action vous permet de spécifier l'heure à laquelle un message sera envoyé après qu'un utilisateur prenne une action particulière (sélectionnée dans la liste déroulante **Nouvelle action de déclenchement**)

![Action]({% image_buster /assets/img_archive/action_delivery_new.png %}){: height="80%"" width="80%"}

{% endtab %}
{% tab API-Triggered Delivery %}

{% alert note %}
Lorsque l'action de déclenchement est définie à **Interagir avec la campagne**, sélectionner une option **Recevoir** car l'interaction provoquera votre nouvelle campagne dès que Braze marque la campagne sélectionnée comme envoyée, même si ce message rebondit ou échoue.
{% endalert %}

Consultez nos [terminaux déclenchés par l'API trouvés dans le Guide de l'API]({{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery) pour plus d'informations sur la livraison déclenchée par API.

{% endtab %}
{% endtabs %}

## Étape 4 : Choisissez les événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne, connue sous le nom d'événement de conversion [][22]. Vous pouvez spécifier l'une des actions suivantes en tant qu'événement de conversion :

- Ouvre l'application
- Fait un achat (peut être un achat générique ou un article spécifique)
- Effectue un événement spécifique personnalisé
- Ouvre l'email
- Clics email

Vous avez la possibilité d'autoriser jusqu'à une fenêtre de 30 jours au cours de laquelle une conversion sera comptée si l'utilisateur prend l'action spécifiée. Alors que Braze suit automatiquement l'ouverture et les clics pour votre campagne, vous pouvez définir l'événement de conversion à être quand un utilisateur ouvre ou clique sur une adresse e-mail pour profiter de la fonctionnalité [Sélection intelligente][13].

## Étape 5 : Choisissez votre segment cible

Ensuite, vous devez choisir le segment cible dans le menu déroulant. Vous recevrez automatiquement un instantané de ce à quoi ressemble la population de ce segment en ce moment, y compris le nombre d'utilisateurs dans ce segment sont accessibles par courriel. Gardez à l'esprit que l'adhésion exacte au segment est toujours calculée juste avant l'envoi du message.

!\[Target Segment\]\[5\]

Optionnellement, vous pouvez également choisir de limiter la livraison à un nombre spécifié d'utilisateurs dans le segment, ou permettre aux utilisateurs de recevoir le même message deux fois à la récurrence de la campagne.

### Campagnes multi-canaux avec email et push

Pour les campagnes multicanaux ciblant à la fois les canaux email et push, vous voudrez peut-être limiter votre campagne de sorte que seuls les utilisateurs qui sont explicitement inscrits recevront le message (excluant les utilisateurs abonnés ou désabonnés). Par exemple, dites que vous avez trois utilisateurs de différents statuts d'opt-in :

- **L'utilisateur A** est abonné à l'e-mail et est push activé. Cet utilisateur ne reçoit pas l'email mais recevra le push.
- **L'utilisateur B** est opté pour l'email mais n'est pas poussé activé. Cet utilisateur recevra l'email mais ne recevra pas le push.
- **L'utilisateur C** est opté pour l'email et est push activé. Cet utilisateur recevra à la fois l'email et le push.

Pour ce faire, sous **Résumé de l'audience**, sélectionnez pour envoyer cette campagne à "utilisateurs opted-in seulement". Cette option vous assurera que seuls les utilisateurs optés recevront votre courriel. et Braze enverra uniquement votre push aux utilisateurs qui sont activés par défaut.

{% alert important %}
Avec cette configuration, n'incluez aucun filtre dans l'étape **Utilisateurs cibles** qui limitent l'audience à un seul canal (e. ., `Push Activé = True` ou `Abonnement par courriel = Opted-In`).
{% endalert %}

## Étape 6 : Réviser et déployer

La page finale vous donnera un résumé de la campagne que vous venez de concevoir. Confirmez tous les détails pertinents et cliquez sur **Lancer la Campagne** pour l'activer pour l'envoi.

Maintenant, il suffit d'attendre que toutes les données se déroulent!

!\[Campagne de lancement\]\[6\]

## Rapports par e-mail

Braze vous fournit un rapport détaillé de chacune de vos campagnes de courriel. Naviguez vers l'onglet **Campagnes** sur votre tableau de bord et sélectionnez votre campagne désirée pour ouvrir la page **Détails**. Cette page est divisée en trois onglets :

- Analyses de campagne
- Rapport de rétention
- Rapport de l'entonnoir

### Analyses de la campagne

Sur la page **Analyses de campagne** , vous pouvez visualiser et analyser le succès de votre campagne dans un format organisé.

De plus, vous pouvez voir comment différents liens réussis dans une seule campagne de courriel utilisent des cartes thermiques. En dessous de la **performance par e-mail**, développez la liste déroulante **Total des clics** et cliquez sur **Voir la carte de chaleur** pour afficher une vue visuelle de votre e-mail qui montre la fréquence et l'emplacement globaux des clics dans la durée de vie de la campagne.

{% alert note %}
Les plages de dates ne sont pas prises en compte pour les cartes de chaleur des e-mails.
{% endalert %}

!\[Analyses de Courriel\]\[17\]

Lorsque vous regardez des clics pour votre variante, les clics reflètent des clics uniques. Lorsque vous développez chaque variation, les clics pour chaque lien dans la variation reflètent le total des clics (pas unique).

Pour des définitions détaillées des métriques sur cette page, consultez notre [Glossaire Analytiques E-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/analytics_glossary/).

{% alert note %}
Braze dédoublera les envois par adresse e-mail. Cependant, ne sont pas dédupliquées pour éviter l'illusion qu'un e-mail ouvert par un utilisateur avec plusieurs [profils d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/) sous une seule adresse e-mail ne serait compté que vers un seul profil d'utilisateur.
{% endalert %}

### Rapport de rétention

Sur la page du **Rapport de rétention** , vous pouvez exécuter divers rapports pour mesurer la rétention des utilisateurs qui ont effectué un événement de rétention sélectionné dans une campagne spécifique. [En savoir plus]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/).

### Rapport de l'entonnoir

Sur la page **Rapport d'entonnoir** , vous pouvez analyser les trajets que vos clients prennent après avoir reçu votre campagne. Si votre campagne utilise un groupe de contrôle ou plusieurs variantes, vous serez en mesure de comprendre comment les différentes variantes ont eu un impact sur l'entonnoir de conversion à un niveau plus granulaire, et optimiser sur la base de ces données. [En savoir plus]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/).
[3]: {% image_buster /assets/img_archive/choose_email_creation.png %} [5]: {% image_buster /assets/img_archive/targetsegment_email_new. ng %} [6]: {% image_buster /assets/img_archive/confirm_email.png %} [14]: {% image_buster /assets/img/email. ng %} [15]: {% image_buster /assets/img_archive/newEmailTest.png %} [17]: {% image_buster /assets/img_archive/email_click_results_heatmap. if %} [19]: {% image_buster /assets/img_archive/new_campaign_email.png %}

[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[13]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[18]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[21]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[22]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/
[22]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/