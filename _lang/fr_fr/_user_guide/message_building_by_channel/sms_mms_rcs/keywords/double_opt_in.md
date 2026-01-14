---
nav_title: Double abonnement
article_title: Double abonnement
description: "Cet article de référence couvre la fonctionnalité de double opt-in et explique comment activer la fonctionnalité, sélectionner des mots-clés d'opt-in et des messages de réponse, et entrer les utilisateurs dans le flux de travail de double opt-in par le biais des mises à jour d'abonnement qui se produisent dans l'API REST, le SDK et les mises à jour du centre de préférences."
page_type: reference
page_order: 2
channel:
  - SMS
  - MMS
  - RCS
---

# Double abonnement

> La fonctionnalité de double abonnement vous permet d'exiger des utilisateurs qu'ils confirment explicitement leur intention d'abonnement avant de pouvoir recevoir des messages SMS, MMS ou RCS. Cela vous permet de vous concentrer sur les utilisateurs qui sont susceptibles d'être engagés ou qui sont engagés dans le canal, et de respecter les meilleures pratiques en matière de conformité.

Lorsque le double abonnement est activé, les utilisateurs reçoivent un message leur demandant leur consentement explicite avant de pouvoir recevoir des messages de vos campagnes ou de vos toiles. 

Bien qu'il ne s'agisse pas d'une exigence explicite du Telephone Consumer Protection Act de 1991 (TCPA), Braze vous recommande de configurer le double abonnement pour confirmer que les utilisateurs sont conscients et consentent à faire partie de votre programme SMS, MMS ou RCS. Pour plus d'informations sur la conformité, consultez la rubrique [Lois, réglementations et prévention des abus pour les SMS, MMS et RCS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)

## Flux de travail à double abonnement (double opt-in)

Le double abonnement vous permet d'obtenir un consentement explicite par le biais de campagnes d'abonnement entrantes et sortantes.

### Sortie

Lorsqu'un utilisateur fournit son numéro de téléphone, il reçoit un message lui demandant son consentement.

Capture d'écran d'un message SMS sortant contenant le texte de la marque : "Bienvenue dans les mises à jour de texte de la marque ! 1 msg par semaine pour les dernières offres. Répondez Y pour vous abonner.", les utilisateurs répondant par "Y", et la marque répondant par "Merci ! Vous êtes maintenant abonné aux alertes de BRAND. Voici un code promo SMS10 pour 10% de réduction sur votre premier achat !"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Inbound

Lorsqu'un utilisateur envoie un message contenant un mot-clé d'abonnement, il reçoit un message lui demandant son consentement.

Capture d'écran d'un message SMS entrant dans lequel un utilisateur envoie "JOIN" et reçoit la réponse "Reply Y to confirm you want to JOIN our SMS program". 3msg/semaine, envoyez un SMS à STOP à tout moment, puis renvoyez le message "Y".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Permettre le double abonnement

Pour activer le double abonnement, accédez au tableau **Mots clés globaux** dans le groupe d'abonnement concerné et cliquez sur **Modifier** dans la **catégorie Mot clé avec option d'abonnement.** Ensuite, sélectionnez votre méthode d'abonnement**(Opt-In** ou **Double Opt-In**). En sélectionnant **Double abonnement**, la page s'agrandit et affiche des [champs configurables](#configurable-fields) supplémentaires.

La section Méthode d'abonnement propose deux méthodes d'abonnement au choix : L'abonnement et le double abonnement.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Champs configurables {#configurable-fields}

| Catégorie   |    Domaines    | Description   
| ----------- |----------- |---------------- 
| Demande d'abonnement | Mots clés | Il s'agit des mots-clés qu'un utilisateur peut saisir pour indiquer son intention d'abonnement. `START` est un mot-clé obligatoire. Cette demande d'abonnement sera également envoyée à l'utilisateur lorsque le statut de son abonnement est mis à jour par les sources répertoriées dans la section [Sources d'abonnement](#subscription-sources).
| | Envoi de messages | Il s'agit de la réponse initiale qu'un utilisateur recevra après avoir envoyé un mot-clé d'abonnement (par exemple, "Répondez à Y pour confirmer que vous souhaitez recevoir des messages de ce numéro. Msg&Data Des tarifs peuvent être appliqués." )
| Confirmation du double abonnement | Mots clés | Il s'agit des mots-clés avec lesquels un utilisateur peut répondre pour confirmer son intention d'abonnement. Au moins un mot-clé est requis. Ces mots-clés doivent être spécifiés dans le champ **Message de réponse à la demande d'abonnement.** 
| | Envoi de messages | Il s'agit de la réponse de confirmation qu'un utilisateur recevra après avoir explicitement confirmé son abonnement et qu'il peut désormais recevoir des messages. Le statut du groupe d'abonnement de l'utilisateur sera défini sur `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsqu'un utilisateur reçoit une demande d'abonnement, il dispose de 30 jours pour confirmer son intention d'abonnement. Si un utilisateur souhaite s'abonner après la période de 30 jours, il doit envoyer un mot-clé d'opt-in par SMS pour relancer le processus de double opt-in.

Les champs configurables comportent deux sections, Demande d'abonnement et Confirmation d'abonnement, chacune comportant les champs Mots clés et Message de réponse.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Statut du groupe d'abonnement

Ce n'est qu'une fois que l'utilisateur a terminé le processus de double abonnement que le [statut du groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) est mis à jour et devient `Subscribed`. Si l'utilisateur commence le flux de travail mais ne le termine pas, il reste sur `Unsubscribed` et ne peut pas recevoir de messages de ce groupe d'abonnement.

Les utilisateurs peuvent également être entrés dans le flux de travail à double abonnement s'ils sont [abonnés à partir d'autres sources]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (par exemple, API REST, SDK).

## Sources d'abonnement {#subscription-sources}

Les utilisateurs peuvent également entrer dans le flux de travail du double abonnement par le biais de mises à jour d'abonnement qui se produisent en dehors des messages entrants. Ces sources comprennent les mises à jour de l'API REST, du SDK et du centre de préférences. Lorsqu'un utilisateur entre dans le processus de double abonnement par le biais de ces sources, il reçoit le **message de réponse à l'invitation à l'abonnement.**

Chaque source d'abonnement a un comportement différent en matière d'inscription, comme le décrit le tableau suivant.

Source    | Comportement en matière d'abonnement double (Double Opt-In)   
----------- | -----------
SDK | Les utilisateurs entreront automatiquement dans le flux de travail du double abonnement lorsqu'ils s'abonnent via le SDK de Braze.
API REST | Les utilisateurs peuvent être introduits dans le flux de travail lorsque l'état de l'abonnement est défini par `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` et que le paramètre facultatif `use_double_opt_in_logic` est transmis en tant que `true` (par exemple, [{"subscription_group_id": "subscription_group_identifier", "subscription_state": "abonné", "use_double_opt_in_logic": true}]). Si ce paramètre est omis, les utilisateurs ne seront pas pris en compte dans le processus de double abonnement.
Shopify | Les utilisateurs ne seront pas entrés dans le flux de travail du double abonnement lorsque leur statut d'abonnement est défini par notre intégration Shopify.
Import d'utilisateurs | Les utilisateurs ne seront pas pris en compte dans le processus de double abonnement lorsque leur statut d'abonnement est défini par l'importation d'utilisateurs.
[Centre de préférences]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Les utilisateurs entreront automatiquement dans le processus de double abonnement lorsqu'ils s'abonneront par l'intermédiaire d'un centre de préférences.
Étape de mise à jour de l'utilisateur | Les utilisateurs peuvent être pris en compte dans le flux de travail à double abonnement lorsque leur statut d'abonnement est défini par l'étape Mise à jour de l'utilisateur et que le paramètre facultatif `use_double_opt_in_logic` est transmis en tant que `true`. Si ce paramètre est omis, les utilisateurs ne seront pas pris en compte dans le processus de double abonnement.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Prise en charge multilingue
Pour les messages entrants, le double abonnement est pris en charge pour toutes les langues définies dans le groupe d'abonnement. Cela signifie que vous pouvez définir vos réponses automatiques dans différentes langues et que Braze enverra la réponse automatique associée à une langue spécifique lorsqu'un mot-clé correspondant est reçu.

Les utilisateurs qui entrent dans le flux de travail du double abonnement par le biais de mises à jour d'abonnement qui se produisent en dehors des messages entrants (par exemple, SDK, REST API, Shopify) ne recevront que les mots-clés anglais.

