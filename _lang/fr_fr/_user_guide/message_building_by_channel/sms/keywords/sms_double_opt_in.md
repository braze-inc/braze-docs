---
nav_title: Double opt-in SMS
article_title: Double opt-in SMS
description: "Cet article de référence couvre la fonctionnalité de double opt-in par SMS, et explique comment activer la fonctionnalité, sélectionner les mots-clés d'opt-in et les messages de réponse, et entrer les utilisateurs dans le flux de travail de double opt-in par SMS via les mises à jour d'abonnement qui se produisent dans les mises à jour de l'API REST, du SDK et du centre de préférences."
page_type: reference
page_order: 2
channel:
  - SMS
---

# Double abonnement aux SMS

> La fonctionnalité de double opt-in par SMS vous permet d'exiger que les utilisateurs confirment explicitement leur intention de s'inscrire avant de pouvoir recevoir des messages SMS. Ceci vous aide à concentrer votre attention sur les utilisateurs qui sont susceptibles d'être engagés ou qui sont engagés avec les SMS.

Lorsque la double acceptation par SMS est activée, les utilisateurs reçoivent un message SMS leur demandant leur consentement explicite avant de pouvoir être contactés par vos campagnes ou Canvases. 

Bien que cela ne soit pas une exigence explicite de la loi sur la protection des consommateurs par téléphone de 1991 (TCPA), Braze recommande de configurer une double acceptation par SMS pour confirmer que les utilisateurs sont conscients et consentent à faire partie de votre programme SMS. Pour plus d'informations sur la conformité SMS, consultez les [lois, réglementations et prévention des abus en matière de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

## Flux de travail du double abonnement aux SMS

Les utilisateurs peuvent donner leur consentement explicite par le biais de messages SMS sortants ou entrants.

### Double abonnement par SMS sortant

Lorsqu'un utilisateur fournit son numéro de téléphone, il reçoit un message SMS qui demande son consentement.

![Capture d'écran du SMS sortant avec le texte de la marque « Bienvenue dans les infos de MARQUE par SMS ! » 1 msg par semaine pour recevoir les nouvelles offres. Répondez O pour vous abonner. », les utilisateurs répondant « O », et la marque répondant « Merci ! Vous êtes maintenant inscrit aux alertes de la MARQUE. Voici un code promo SMS10 pour bénéficier de 10 % de réduction sur votre premier achat ! »][2]{:style="max-width:40%;"}

### Double opt-in SMS entrant

Lorsqu'un utilisateur envoie un SMS contenant un mot-clé d'abonnement, il reçoit un SMS demandant son consentement.

![Capture d'écran d'un message SMS entrant où un utilisateur envoie "JOIN" et reçoit la réponse "Répondez Y pour confirmer que vous souhaitez REJOINDRE notre programme SMS." 3 msg/semaine, envoyer STOP à tout moment pour ARRÊTER, puis renvoie « O ».][1]{:style="max-width:40%;"}

## Activation de la double acceptation par SMS

Pour activer la double acceptation par SMS, accédez à la table **SMS Global Keywords** dans le groupe d'abonnement applicable, et cliquez sur **Editer** dans la **Catégorie de mot-clé d'acceptation**. Ensuite, sélectionnez votre méthode d'adhésion (**Opt-In** ou **Double Opt-In**). Sélectionner **Double Opt-In** développera la page pour afficher des [champs configurables supplémentaires](#configurable-fields).

![La section Méthode d'abonnement propose deux méthodes d'abonnement au choix : Abonnement et Double abonnement.][3]{:style="max-width:50%;"}

### Champs configurables {#configurable-fields}

| Catégorie   |    Champs    | Description   
| ----------- |----------- |---------------- 
| Demande d’abonnement | Mots-clés | Ce sont les mots-clés qu'un utilisateur peut envoyer par SMS pour indiquer son intention de s'inscrire. `START` est un mot-clé obligatoire. Cette invite d'adhésion sera également envoyée à l'utilisateur lorsque son statut d'abonnement sera mis à jour par les sources répertoriées dans la section [Sources d'abonnement](#subscription-sources).
| | Message de réponse | Ceci est la réponse initiale qu'un utilisateur recevra après avoir envoyé un mot-clé d'adhésion (par exemple, « Répondez Y pour confirmer que vous souhaitez recevoir des messages de ce numéro. » Des frais de messagerie et de données peuvent s'appliquer.
| Confirmation d’abonnement double | Mots-clés | Il s’agit des mots-clés qu'un utilisateur peut renvoyer pour confirmer son intention de s'abonner. Au moins un mot-clé est requis. Ces mots-clés doivent être spécifiés dans le champ **Message de réponse à l'invite d'adhésion**.
| | Message de réponse | Ceci est la réponse de confirmation qu'un utilisateur recevra après avoir explicitement confirmé son abonnement, indiquant qu’il peut désormais recevoir des SMS. Le statut du groupe d'abonnement de l'utilisateur sera défini sur `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsqu'un utilisateur reçoit une demande d'abonnement, il dispose de 30 jours pour confirmer son intention d'abonnement. Si un utilisateur souhaite s'abonner après cette période de 30 jours, il doit envoyer un mot-clé d'abonnement par SMS pour recommencer le processus de double abonnement.

![Les champs configurables comportent deux sections, Demande d'abonnement et Confirmation d’abonnement double, chacune avec les champs Mots-clés et Message de réponse.][4]

## Statut du groupe d'abonnement

Ce n'est qu'après que l'utilisateur a complété le flux de travail de double abonnement aux SMS que son [statut de groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) est mis à jour sur `Subscribed`. Si l'utilisateur commence le flux de travail mais ne le termine pas, il reste `Unsubscribed` et ne peut pas recevoir de messages SMS de ce groupe d'abonnement.

Les utilisateurs peuvent également être inscrits dans le flux de travail de double acceptation par SMS s'ils sont [abonnés à partir d'autres sources]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (par exemple, REST API, SDK).

## Sources d'abonnement {#subscription-sources}

Les utilisateurs peuvent également entrer dans le flux de travail de double acceptation par SMS via des mises à jour d'abonnement qui se produisent en dehors des messages SMS entrants. Ces sources incluent des mises à jour de l'API REST, du SDK et du centre de préférences. Lorsque un utilisateur entre dans le flux de travail de double abonnement aux SMS via ces sources, il reçoit le **message de réponse de demande d’abonnement**.

Chaque source d'abonnement a un comportement d'inscription différent, comme décrit dans le tableau suivant.

Source    | Comportement d'inscription à double confirmation   
----------- | -----------
SDK | Lorsqu’ils s’abonnent via le SDK Braze, les utilisateurs entrent automatiquement dans le flux de travail de double abonnement aux SMS.
API REST | Les utilisateurs peuvent être intégrés dans le flux de travail lorsque le statut de l'abonnement est défini via `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` et que le paramètre optionnel `use_double_opt_in_logic` est passé comme `true` (par exemple, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Si ce paramètre est omis, les utilisateurs ne seront pas inscrits dans le flux de travail de double opt-in par SMS.
Shopify | Les utilisateurs ne seront pas inscrits dans le flux de travail de double acceptation par SMS lorsque leur statut d'abonnement est défini par notre intégration Shopify.
Importation d’utilisateurs | Les utilisateurs ne seront pas inscrits dans le flux de travail de double acceptation par SMS lorsque leur statut d'abonnement est défini par l'importation d'utilisateurs.
[Centre de préférences]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Les utilisateurs entreront automatiquement dans le flux de travail de double acceptation par SMS lorsqu'ils s'abonneront via un centre de préférences.
Étape de mise à jour de l’utilisateur | Les utilisateurs peuvent être intégrés dans le flux de travail de double acceptation par SMS lorsque leur statut d'abonnement est défini via l'étape de mise à jour de l'utilisateur et que le paramètre facultatif `use_double_opt_in_logic` est passé comme `true`. Si ce paramètre est omis, les utilisateurs ne seront pas inscrits dans le flux de travail de double opt-in par SMS.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Prise en charge multilingue
Pour les messages entrants, le double opt-in par SMS est pris en charge pour toutes les langues définies dans le groupe d'abonnement. Cela signifie que vous pouvez définir vos réponses automatiques dans différentes langues et Braze enverra la réponse automatique associée à une langue spécifique lorsqu'un mot-clé correspondant est reçu.

Les utilisateurs qui entrent dans le flux de travail de double acceptation par SMS via des mises à jour d'abonnement qui se produisent en dehors des messages entrants (par exemple, SDK, API REST, Shopify) ne recevront que les mots-clés en anglais.

[1]: {% image_buster /assets/img/double_opt_in_inbound.png %}
[2]: {% image_buster /assets/img/double_opt_in_outbound.png %}
[3]: {% image_buster /assets/img/double_opt_in_method.png %}
[4]: {% image_buster /assets/img/double_opt_in_fields.png %}
