---
nav_title: "Autorisations géographiques des SMS"
article_title: Autorisations géographiques des SMS
description: "Cet article traite de la liste des pays autorisés pour les autorisations géographiques de SMS, qui vous permet de choisir les pays auxquels les SMS peuvent être envoyés."
page_order: 4.5
page_type: reference
channel:
  - SMS
alias: "/sms_geographic_permissions/"
  
---

# Autorisations géographiques des SMS

> Les autorisations géographiques pour les SMS renforcent la sécurité et protègent contre le trafic frauduleux de SMS en appliquant des contrôles sur les pays auxquels vous pouvez envoyer des messages SMS. Vous pouvez spécifier une liste de pays autorisés pour vous assurer que les messages SMS ne sont envoyés qu'aux régions approuvées. Seuls les administrateurs peuvent modifier la liste des pays autorisés. Les utilisateurs non administrateurs ont accès à une version en lecture seule de la liste d'autorisations qui indique les pays vers lesquels un groupe d'abonnement peut envoyer des messages.

![La section SMS Geographic Permissions en lecture seule pour un utilisateur non-administrateur dont les États-Unis et le Royaume-Uni ont été sélectionnés dans la "Country allowlist".][6]{: style="max-width:80%;"}

## Configuration de la liste des pays autorisés pour les SMS

Si vous êtes administrateur, vous pouvez configurer les pays qui figurent sur la liste des pays autorisés. La liste des pays autorisés est configurée au niveau du [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/). Vous pouvez y accéder en allant dans **Audience** > **Abonnements** et en sélectionnant un groupe d'abonnement SMS. La liste d'autorisation se trouve sous **SMS Geographic Permissions.**

![La section modifiable des autorisations géographiques par SMS pour un administrateur dont l'Australie, le Canada et les États-Unis ont été sélectionnés dans la "liste des pays autorisés".][1]{: style="max-width:80%;"}

### Sélection des pays

Ajoutez des pays à la liste des pays autorisés à l'aide de la liste déroulante. Les pays les plus courants pour les SMS sont indiqués en haut de la page, les autres étant indiqués en dessous. Vous pouvez également rechercher des pays en tapant dans le champ de texte.

![Liste déroulante « Liste des pays autorisés » avec les pays les plus courants affichés en haut.][2]{: style="max-width:80%;"}

Supprimez les pays précédemment sélectionnés en décochant les cases correspondantes.

### Enregistrer vos modifications

Les modifications prendront effet une fois que vous aurez sélectionné **Enregistrer**. En supprimant des pays de votre liste d'autorisation, vous empêcherez l'envoi de tous les messages SMS et MMS vers des numéros situés dans ces pays.

![Fenêtre modale confirmant les pays qui seront supprimés de la liste d'autorisation.][3]{: style="max-width:70%;"}

## Pays à haut risque

Certains pays présentent un risque plus élevé de pompage par SMS. Ces pays sont signalés par une étiquette " **High Risk** " dans la liste déroulante des pays.

![Le pays en bas, l'Azerbaïdjan, classé « à haut risque ».][4]{: style="max-width:80%;"}

Si vous autorisez l'envoi dans ces pays, vous devez d'abord reconnaître le risque que cela comporte avant que le pays ne soit ajouté à votre liste d'autorisation.

{% alert note %}
Limitez les pays de votre liste d'autorisation aux seuls pays nécessaires pour répondre aux besoins de votre entreprise. Vous minimiserez ainsi le risque de trafic frauduleux. Pour plus d'informations sur la prévention du pompage de trafic par SMS, consultez les [FAQ sur la fraude par pompage de trafic par SMS.]({{site.baseurl}}/sms_traffic_pumping_fraud/)
{% endalert %}

## Visibilité des envois bloqués

Les tentatives d'envoi vers des pays qui ne figurent pas sur votre liste d'autorisation seront interrompues. Les messages interrompus seront consignés dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) et dans l'[événement d'engagement aux messages interrompus par SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

Les messages interrompus en raison d'envois bloqués s'affichent à l'adresse `Abort_Type = "blocked_recipient_country"` et le journal d'interruption indique en détail le pays bloqué.

![Journal d'annulation indiquant le type d'annulation (abort_type of blocked_recipient_country) et les initiales du pays du numéro de téléphone bloqué.][5]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/high_risk.png %}
[5]: {% image_buster /assets/img/sms/abort_log.png %}
[6]: {% image_buster /assets/img/sms/sms_geographic_permissions_read_only.png %}