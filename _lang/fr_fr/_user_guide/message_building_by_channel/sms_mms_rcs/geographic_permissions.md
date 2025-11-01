---
nav_title: "Autorisations géographiques"
article_title: Autorisations géographiques
description: "Cet article traite de la liste des pays autorisés pour les autorisations géographiques, qui vous permet de choisir les pays auxquels les SMS, MMS et RCS peuvent être envoyés."
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# Autorisations géographiques

> Les autorisations géographiques renforcent la sécurité et protègent contre le trafic frauduleux de SMS, MMS et RCS en appliquant des contrôles sur les pays auxquels vous pouvez envoyer des messages. Vous pouvez spécifier une liste de pays autorisés pour vous assurer que les messages SMS, MMS et RCS ne sont envoyés qu'aux régions approuvées. Seuls les administrateurs peuvent modifier la liste des pays autorisés. Les utilisateurs non administrateurs ont accès à une version en lecture seule de la liste d'autorisations qui indique les pays vers lesquels un groupe d'abonnement peut envoyer des messages.

Si vous êtes administrateur, vous pouvez configurer les pays qui figurent sur la liste des pays autorisés. La liste des pays autorisés est configurée au niveau du [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/). Vous pouvez y accéder en allant dans **Audience** > **Abonnements** et en sélectionnant un groupe d'abonnement SMS, MMS ou RCS. La liste d'autorisation se trouve sous la rubrique " **Autorisations géographiques"**.

!La section modifiable des autorisations géographiques par SMS pour un administrateur ayant plusieurs pays sélectionnés dans la "Liste des pays autorisés".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Sélection des pays

Ajoutez des pays à la liste des pays autorisés à l'aide de la liste déroulante. Les pays les plus courants en matière de SMS et de RCS sont indiqués en haut de la page, les autres étant indiqués en dessous. Vous pouvez également rechercher des pays en tapant dans le champ de texte.

\![La liste déroulante "Country allowlist" avec les pays les plus courants s'affiche en haut.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Supprimez les pays précédemment sélectionnés en décochant les cases correspondantes.

### Enregistrer vos modifications

Les modifications prendront effet après que vous aurez sélectionné **Enregistrer.** En supprimant des pays de votre liste d'autorisation, vous empêcherez l'envoi de tous les messages SMS, MMS et RCS vers des numéros situés dans ces pays.

\![Modale d'avertissement confirmant les pays qui seront supprimés de la liste d'autorisation.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Pays à haut risque

Certains pays présentent un risque plus élevé de pompage du trafic SMS et RCS. Ces pays sont signalés par une étiquette " **High Risk** " dans la liste déroulante des pays.

\![La liste déroulante des pays avec l'Azerbaïdjan ayant une étiquette "Risque élevé".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Si vous autorisez l'envoi dans ces pays, vous devez d'abord reconnaître le risque que cela comporte avant que le pays ne soit ajouté à votre liste d'autorisation.

{% alert note %}
Limitez les pays de votre liste d'autorisation à ceux qui sont nécessaires pour répondre aux besoins de votre entreprise. Vous minimiserez ainsi le risque de trafic frauduleux. Pour plus d'informations sur la prévention du pompage de trafic par SMS, consultez les [FAQ sur la fraude par pompage de trafic par SMS.]({{site.baseurl}}/sms_traffic_pumping_fraud/)
{% endalert %}

## Visibilité des envois bloqués

Les tentatives d'envoi vers des pays qui ne figurent pas sur votre liste d'autorisation seront interrompues. Les messages interrompus seront consignés dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) et dans l'[événement d'engagement aux messages interrompus par SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

Les messages interrompus en raison d'envois bloqués s'affichent comme des **erreurs de message interrompu** et comportent le message "Le numéro de téléphone du destinataire se trouve dans un pays bloqué".

\![Journal d'abandon montrant plusieurs envois de SMS qui ont été bloqués parce que le numéro de téléphone se trouve dans un pays bloqué.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

