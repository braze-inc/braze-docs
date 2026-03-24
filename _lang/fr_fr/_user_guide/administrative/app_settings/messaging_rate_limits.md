---
nav_title: Limites de débit d'envoi de messages de l'espace de travail
article_title: Limites de débit d'envoi de messages de l'espace de travail
alias: /workspace_messaging_rate_limits/
page_type: reference
description: "Cet article de référence décrit les limites de débit d'envoi de messages de l'espace de travail et leur fonctionnement avec vos messages."
page_order: 10
---

# Limites de débit d'envoi de messages de l'espace de travail

> Utilisez les limites de débit d'envoi de messages de l'espace de travail pour réguler le rythme de distribution de vos messages sortants depuis votre plateforme, afin de vous assurer que vos utilisateurs reçoivent bien les messages dont ils ont besoin.

{% alert important %}
Les limites de débit d'envoi de messages de l'espace de travail sont déployées progressivement. Il est possible que ces paramètres ne soient pas encore visibles dans votre tableau de bord.
{% endalert %}

## Fonctionnement

Les limites de débit d'envoi de messages de l'espace de travail s'appliquent à l'ensemble des messages envoyés dans votre espace de travail. En définissant et en optimisant une limite de débit au niveau de l'espace de travail, vous pouvez mieux contrôler le trafic sortant de vos messages Braze, évitant ainsi d'éventuels pics de demande susceptibles d'affecter les performances du serveur.
{% alert note %}
Gardez à l'esprit que les messages envoyés via les endpoints API d'envoi de messages tels que `/messages/send` et `/messages/schedule/create` sont également comptabilisés et soumis aux limites de débit d'envoi de messages de l'espace de travail.
{% endalert %}
Le nombre total de messages envoyés par minute ne dépasse pas les limites de débit configurées pour l'espace de travail. Il n'y a pas d'ordre particulier déterminant quelles campagnes sont distribuées dans les premières minutes par rapport aux minutes suivantes.

Par exemple, supposons que vous ayez une limite de débit d'envoi de messages de l'espace de travail de 100 000 messages par minute, et que les messages suivants soient tous en cours de traitement à 12 h :

| Campagne   | Nombre de messages | Heure d'envoi |
|------------|--------------------|---------------|
| Campagne 1 | 100 000            | 12 h          |
| Campagne 2 | 100 000            | 12 h          |
| Campagne 3 | 100 000            | 12 h          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Les messages sont distribués sur un intervalle de 3 minutes.

Les messages sont traités en parallèle. Une fois traités, ils sont planifiés de manière à respecter la limite de débit d'envoi de messages de l'espace de travail selon le principe du premier arrivé, premier servi. Cela signifie que dans l'exemple ci-dessus, les messages envoyés chaque minute sont un mélange variable des campagnes 1, 2 et 3, totalisant 100 000.

![Exemple de distribution des messages pour les trois campagnes.]({% image_buster /assets/img/workspace_messaging_rate_limits2.png %})

Prenons l'exemple suivant avec une limite de débit d'envoi de messages de l'espace de travail de 100 000 messages par minute, et les messages suivants configurés :

| Campagne   | Nombre de messages | Heure d'envoi |
|------------|--------------------|---------------|
| Campagne 1 | 1 000 000          | 9 h           |
| Campagne 2 | 1 000 000          | 9 h 05        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Voici le calendrier de distribution prévu et les messages envoyés par minute :

- La campagne 1 serait planifiée de 9 h à 9 h 10, avec 100 000 messages envoyés par minute.
- La campagne 2 serait planifiée pour être distribuée 5 minutes après son heure de distribution initiale, soit de 9 h 10 à 9 h 20, avec 100 000 messages envoyés par minute.

![Exemple de distribution des messages par minute pour les deux campagnes.]({% image_buster /assets/img/workspace_messaging_rate_limits1.png %})

{% alert note %}
Après avoir défini la limite de débit d'envoi de messages de l'espace de travail, vous pouvez l'augmenter. Cependant, tous les messages déjà traités avant l'augmentation utilisent la limite précédemment définie.
{% endalert %}

## Définir la limite de débit d'envoi de messages de votre espace de travail

1. Dans le tableau de bord de Braze, accédez à **Paramètres** > **Paramètres de l'espace de travail** > **Limites de débit d'envoi de messages de l'espace de travail**.
2. Sélectionnez **+ Ajouter une limite de débit**, puis sélectionnez un canal de communication.
3. Pour **Messages par minute**, saisissez la limite de débit.
4. Sélectionnez **Enregistrer**.

## Bon à savoir

La limite de débit s'applique à la distribution, c'est-à-dire au début de la tentative d'envoi du message. Lorsque le temps nécessaire pour finaliser l'envoi varie, le nombre d'envois terminés peut légèrement dépasser la limite de débit sur certaines minutes. Sur la durée, le nombre d'envois par minute se stabilise en moyenne à un niveau ne dépassant pas la limite de débit.

Lorsqu'une campagne ou un canvas possède sa propre limite de débit et qu'une limite de débit au niveau de l'espace de travail s'applique également, les deux sont appliquées. Par exemple, si une campagne a une limite de débit de 500 000 mais qu'en raison des limites de débit de l'espace de travail, elle ne peut envoyer que 100 000 messages par minute à ce moment-là, c'est la limite de débit de l'espace de travail qui prend effet.

Braze essaie de répartir uniformément la distribution des messages tout au long de la minute, mais ne peut pas le garantir. Par exemple, si vous avez une campagne avec une limite de débit de 500 000 messages par minute, nous essaierons de répartir les 500 000 messages uniformément sur la minute (environ 8 400 messages par seconde), mais il peut y avoir des variations dans le débit par seconde.

Notez que vous pouvez toujours définir des limites de débit individuelles dans vos campagnes et Canvas. Celles-ci sont appliquées indépendamment des limites de débit d'envoi de messages de l'espace de travail.

### Messages non inclus dans les limites de débit d'envoi de messages de l'espace de travail

- Les messages envoyés via les [campagnes d'e-mails transactionnels]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) ne sont pas inclus dans les limites de débit d'envoi de messages de l'espace de travail. Cela signifie qu'ils sont soumis à leur propre limite de débit et ne sont pas comptabilisés dans les limites de débit d'envoi de messages de l'espace de travail définies.
- Les messages envoyés aux [groupes initiateurs]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab#seed-groups) et les [envois de test]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages) ne sont pas inclus dans les limites de débit d'envoi de messages de l'espace de travail. Cela signifie qu'ils ne sont pas soumis à une limite de débit et ne sont pas comptabilisés dans les limites de débit d'envoi de messages de l'espace de travail définies.
- Les réponses automatiques SMS ne sont pas incluses dans les limites de débit d'envoi de messages de l'espace de travail. Cela signifie qu'elles ne sont pas soumises à une limite de débit et ne sont pas comptabilisées dans les limites de débit d'envoi de messages de l'espace de travail définies.