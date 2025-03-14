---
nav\_title : Listes de suppression article\_title : Listes de suppression page\_order : 2.5 page\_type : référence outil : Description des segments : "Cette page explique comment utiliser les listes de suppression pour spécifier les utilisateurs qui ne doivent jamais recevoir vos messages."

---

# Listes de suppression

> Les listes de suppression spécifient les groupes d'utilisateurs qui ne recevront jamais de messages. Les administrateurs peuvent créer des listes de suppression dynamiques avec des filtres de segmentation pour restreindre un groupe d'utilisateurs de la même manière que vous le feriez pour la segmentation.

{% alert important %} Les listes de suppression sont actuellement en version bêta. Si vous souhaitez participer à cette version bêta, contactez votre gestionnaire satisfaction client. Pendant la phase bêta, les fonctionnalités peuvent changer, et vous pouvez avoir jusqu'à cinq listes de suppression actives à la fois, mais faites savoir à votre gestionnaire satisfaction client si vous avez besoin de plus. {% endalert %}

## Fonctionnement

Les listes de suppression sont dynamiques et s'appliquent automatiquement à certaines formes d'envoi de messages, mais vous pouvez définir des exceptions pour certaines étiquettes. Si les étiquettes d'exception que vous avez sélectionnées sont utilisées dans une campagne ou un canvas, cette liste de suppression ne s'appliquera pas à cette campagne ou à ce canvas. Les messages provenant de campagnes ou de Canvases avec des étiquettes d'exception atteindront toujours tous les utilisateurs de la liste de suppression qui font partie de vos segments de ciblage.

### Messages non concernés par les listes de suppression

Dans le cadre de la version bêta, les listes de suppression ne s'appliqueront pas aux types de messages suivants (en d'autres termes, les utilisateurs des listes de suppression recevront **toujours** des messages appartenant aux éléments suivants) : - Drapeaux de fonctionnalité - Cas d'utilisation transactionnels - Campagnes API - Campagnes déclenchées par l'API - Canevas déclenchés par l'API - Campagnes déclenchées par l'API de Braze`(/messages` et `/send`).

Vous n'avez pas besoin d'ajouter une étiquette d'exception pour ces cas d'utilisation, car les listes de suppression ne s'y appliquent pas automatiquement. Pour exclure un groupe d'utilisateurs d'un message dans le cadre de ces cas d'utilisation, vous devez créer un segment de ciblage qui exclut ces utilisateurs.

{% alert important %} Pendant la phase bêta, nous recueillons les commentaires des clients afin d'améliorer notre produit. Informez votre gestionnaire de satisfaction client si vous envisagez d'appliquer des listes de suppression à des cas d'utilisation transactionnels. {% endalert %}

### Canaux concernés par les listes de suppression

Les listes de suppression sont dynamiques et s'appliqueront automatiquement à tous les canaux suivants (sauf si la campagne ou le Canvas contient une étiquette d'exception) : - SMS - Email - Push - Messages in-app - Carte de contenu - Bannière - SMS/MMS - Webhook - WhatsApp - LINE.

## Mise en place de listes de suppression

Les listes de suppression pouvant avoir un impact significatif sur les messages que vous envoyez, seuls les administrateurs peuvent modifier, enregistrer, activer et désactiver les listes de suppression (tous les utilisateurs peuvent consulter les listes de suppression).

1. Allez dans **Audience** > **Listes de suppression**.<br><br>La page "Listes de suppression" avec une liste de trois listes de suppression]\[1].<br><br>
2. Sélectionnez **Créer une liste de suppression** et ajoutez un nom.<br><br>\![Une fenêtre intitulée "Créer une liste de suppression" avec un champ pour saisir un nom.]\[2]{ : style="max-width:80% ;"}<br><br>
3. Utilisez des filtres de segmentation pour identifier les utilisateurs de vos listes de suppression. Vous devez en sélectionner au moins un.

{% alert important %} Bien que le processus de configuration semble similaire à la [création de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), une liste de suppression est un groupe d'utilisateurs auxquels vous ne souhaitez **pas** envoyer de messages, quelle que soit leur appartenance à un segment. {% endalert %}

\![Un générateur de liste de suppression avec un filtre pour les utilisateurs qui ont ouvert un e-mail il y a plus de 90 jours]\[3].

{ : start="4"} 4. Déterminez si vous souhaitez des exceptions basées sur les étiquettes en cochant la case située sous le nom de votre segment (reportez-vous à la section [Fonctionnement](#how-it-works) pour plus d'informations), puis ajoutez les étiquettes des campagnes ou des canevas que les utilisateurs de cette liste de suppression doivent continuer à recevoir. <br><br>En d'autres termes, si vous ajoutez l'étiquette d'exception "Confirmation d'expédition", les utilisateurs de votre liste de suppression seront exclus de tous les messages, à l'exception de ceux qui utilisent l'étiquette "Confirmation d'expédition".<br><br>La section "Détails de la liste d'expédition" avec une étiquette d'exception appelée "Confirmation d'expédition"]\[4].<br><br>
5\. Enregistrez ou activez votre liste de suppression. - Lorsque vous enregistrez, votre liste de suppression est sauvegardée mais n'est pas activée, ce qui signifie qu'elle n'entre pas en vigueur. Votre liste de suppression restera inactive jusqu'à ce que vous l'activiez, et les listes de suppression inactives n'auront pas d'impact sur l'envoi des messages (les utilisateurs ne seront pas exclus des messages). - Lorsque vous l'activerez, votre liste de suppression sera enregistrée et entrera immédiatement en vigueur, ce qui signifie que les utilisateurs de votre liste de suppression seront immédiatement exclus des campagnes ou des canevas (sauf ceux qui contiennent une étiquette d'exception).

{% alert note %} Seuls les administrateurs peuvent enregistrer ou activer des listes de suppression. Vous pouvez avoir jusqu'à cinq listes de suppression actives à la fois dans la version bêta. {% endalert %}

Vous pouvez désactiver ou archiver les listes de suppression lorsque vous n'en avez plus besoin. - Pour désactiver une liste de suppression, sélectionnez une liste de suppression active, puis cliquez sur **Désactiver**. Les listes de suppression désactivées peuvent être réactivées ultérieurement. - Pour archiver, faites-le à partir de la page **Listes de suppression.** 

## Utilisation de la liste de suppression

### Pour les campagnes

La section "Listes de suppression" comporte une liste de suppression active, intitulée "Faibles scores de santé marketing"]\[5].

Si un utilisateur figure dans une liste de suppression, il ne recevra pas de campagne pour laquelle cette liste de suppression s'applique. Reportez-vous à la section [Messages non concernés par les listes de suppression](#messages-not-affected-by-suppression-lists) pour connaître les cas où une liste de suppression ne s'applique pas.

#### Vérification des listes de suppression appliquées

Pour vérifier l'utilisation des listes de suppression dans une campagne, accédez à la section **Liste de suppression de** la page **Audience cible** pour voir quelles listes de suppression sont appliquées à cette campagne.

### Pour les toiles

Si un utilisateur fait partie d'une liste de suppression, il pourra toujours entrer dans le Canvas mais ne pourra pas recevoir d'étapes du message dans le Canvas. Lorsqu'ils avancent à une étape du message, ils quittent le Canvas. Toutefois, un utilisateur figurant sur une liste de suppression peut toujours recevoir des envois autres que des messages avant un envoi de messages. 

#### Empêcher les segments d'entrer dans un canvas

Pour qu'un segment ne **soit** pas saisi dans un canvas, vous pouvez configurer les paramètres de ciblage de ce canvas de manière à exclure ce segment en suivant les étapes suivantes :

1. Créez une segmentation en utilisant les mêmes filtres et critères que votre liste de supression.
2. À l'étape **Cible**, utilisez le filtre **Adhésion au segment** pour cibler les utilisateurs qui ne sont pas inclus dans votre segment.

Par exemple, supposons que vous ayez un canvas avec une liste de suppression appliquée. Le canvas comporte une étape de mise à jour de l'utilisateur suivie d'une étape d'envoi de messages. Dans ce scénario, les utilisateurs de la liste de suppression entrent dans le canvas, passent par l'étape de mise à jour de l'utilisateur (où l'utilisateur peut être mis à jour, en fonction de la configuration de cette étape), puis sortent à l'étape du message (à ce moment-là, l'utilisateur est inclus dans les indicateurs "Sorti"). 

#### Vérification des listes de suppression appliquées

Pour vérifier l'utilisation des listes de suppression dans un canvas, accédez à la section **Liste de suppression de** la page **Audience ciblée** pour voir quelles listes de suppression sont appliquées à ce canvas. Vous pouvez également consulter les listes de suppression appliquées dans l'étape **Résumé**.

\[1] : {% image\_buster /assets/img/suppression\_lists\_home.png %} \[2] : {% image\_buster /assets/img/create\_suppression\_list.png %} \[3] : {% image\_buster /assets/img/suppression\_list\_filters.png %} \[4] : {% image\_buster /assets/img/exception\_tags.png %} \[5] : {% image\_buster /assets/img/active\_suppression\_list.png %}
