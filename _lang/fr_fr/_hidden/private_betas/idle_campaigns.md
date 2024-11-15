---
nav_title: "Campagnes et canvas inactifs"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Campagnes et canvas inactifs

> Cet article de référence explique l'état d'inactivité des campagnes et des toiles et répond aux questions fréquemment posées.

{% alert note %}
En 2024, les canvas porteront la mention **Inactif** et seront arrêtés, de même que les campagnes. Lorsque les canvas sont inactifs ou arrêtés, ils suivent la logique décrite dans ce document.
{% endalert %}

Les campagnes et les canvas se voient attribuer un statut d'inactivité lorsqu'ils n'ont pas envoyé de messages ou n'ont pas saisi d'utilisateurs depuis un certain temps. Ces campagnes et toiles seront automatiquement arrêtées aux dates d'arrêt qui leur sont associées. Vous pouvez filtrer les campagnes et les toiles inactives pour vous aider à trier et à gérer votre liste de campagnes et de toiles.

## Campagnes inactives

De manière continue, les campagnes inactives qui répondent aux critères suivants seront arrêtées :
 
- Un envoi unique planifié a dépassé sa date d'envoi de sept jours.
- Une campagne planifiée ou basée sur des actions avec une date de fin est dépassée de sept jours.
- Une campagne sans date de fin qui n'a pas envoyé de messages depuis un an.

Pour les campagnes sans date de fin, si un message est envoyé ou si la campagne est mise à jour, le compte à rebours d'un an pour l'arrêt de la campagne sera réinitialisé. Lorsque les campagnes sont arrêtées, Braze en informe les clients dans leur tableau de bord et par e-mail.

Les campagnes seront arrêtées à la date d’arrêt par défaut la plus tardive et un jour après leur dernière date limite de conversion. Les envois qui résultent d'un gain ou d'une variante personnalisée sont traités comme des envois planifiés et seront interrompus sept jours après l'envoi du gain ou de la variante personnalisée. Toutes les campagnes seront arrêtées à 4 heures UTC chaque jour pour tous les utilisateurs de Braze.

Les cartes de contenu ne seront pas arrêtées avant leur date d'expiration et respecteront également les critères susmentionnés ainsi que la règle de la date limite de conversion.

Reportez-vous à ce tableau pour savoir comment maintenir une campagne active :

| Raison de l'inactivité                                                                              | Étapes pour rendre la campagne active                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Campagnes planifiées pour un envoi unique et dont la date d'envoi est dépassée de sept jours.                 | Planifier un envoi futur                            |
| Campagnes qui sont planifiées ou basées sur des actions, qui ont une date de fin, et dont celle-ci est dépassée de sept jours | Prolonger la date de fin                               |
| Campagnes sans date de fin qui n'ont pas envoyé de messages depuis un an.                                | Envoyer un message ou apporter des modifications à la campagne |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Canvas inactifs

Les toiles inutilisées qui répondent aux critères suivants seront arrêtées en permanence :

- Un envoi unique planifié a dépassé la date d'envoi et la durée maximale de plus de 7 jours.
- Un Canvas planifié ou basé sur une action avec une date de fin a dépassé sa date de fin et sa durée maximale de plus de 7 jours.
- Un canvas sans date finale n'a pas été saisi par les utilisateurs ou modifié depuis plus de 12 mois et sa durée maximale

Pour les canvas sans date finale, si un utilisateur est saisi ou si le Canvas est mis à jour, le compte à rebours d'un an pour l'arrêt du Canvas sera réinitialisé. Lorsque les canvas sont arrêtés, Braze en informe les clients dans leur tableau de bord et par e-mail.

La [durée maximale]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) d’un canvas est le temps le plus long qu'un utilisateur peut prendre pour compléter un canvas donné. Cette durée inclut les expirations des cartes de contenu et des messages in-app.

Reportez-vous à ce tableau pour savoir comment maintenir un canvas actif :

| Raison de l'inactivité                                                                                                  | Étapes pour rendre le canvas actif                     |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Canvas dont l'envoi est planifié une seule fois et dont la durée maximale, de sept jours après la date d'envoi, est dépassée                 | Planifier un envoi futur                          |
| Canvas qui sont planifiés ou basés sur des actions, qui ont une date de fin, et dont celle-ci est dépassée de sept jours, la durée maximale | Prolonger la date de fin                             |
| Les toiles sans date de fin qui n'ont pas envoyé de messages depuis un an.                                                      | Envoyez un message ou modifiez le canvas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

#### À quelles campagnes ou toiles cela s'applique-t-il ?

Cela s'appliquera aux campagnes et aux canvas qui répondent déjà aux critères énumérés précédemment, ainsi qu'aux campagnes et aux canvas qui répondront aux critères à l'avenir.

#### Comment savoir si une campagne ou un canvas est inactif ?

Les campagnes et les toiles inactives seront affichées dans les pages de la liste des campagnes et des toiles sous la catégorie **Inactif**. La date à laquelle la campagne ou le canvas sera arrêté est indiquée dans une colonne de la liste.

#### Que se passe-t-il si une campagne ou un canvas inactif est mis à jour ?

Si une campagne qui n'a pas envoyé de message ou un Canvas qui n'a pas saisi d'utilisateurs est mis à jour, le compte à rebours est réinitialisé.

#### Que se passe-t-il pour les campagnes qui n'ont pas envoyé de message depuis un an (ou les canvas qui n'ont pas enregistré d'utilisateurs depuis un an), mais qui ont une date finale dans le futur ?

Nous arrêterons ces campagnes et ces toiles sept jours après la date de fin.

#### Qui recevra des e-mails de notification concernant les campagnes arrêtées et les toiles ?

Par défaut, tous les utilisateurs disposant de droits d'administrateur sont abonnés aux notifications par e-mail concernant les campagnes et les toiles qui s'arrêtent automatiquement. Le créateur de la campagne ou du canvas sera toujours informé de son arrêt. Les utilisateurs peuvent gérer les préférences de notification par e-mail en allant dans **Paramètres de l'entreprise** > **Préférences de notification**, puis en ajoutant ou en supprimant des destinataires de la notification **Campagne arrêtée automatiquement** et de la notification **Toile arrêtée automatiquement.**

#### Comment fonctionne l'arrêt des cartes de contenu ?

Les cartes de contenu des campagnes ne seront pas arrêtées avant leur date d'expiration et la période tampon appropriée. Elles seront interrompues à la date la plus tardive entre la période tampon (correspondant au fait que la campagne est un envoi unique, a une date de fin ou n'a pas de date de fin) et la date limite d'expiration. 

Par exemple, si une carte de contenu expire le 1er avril, qu'elle est envoyée une seule fois et que la date limite de conversion est fixée à 10 jours, elle sera arrêtée le 12 avril (10 jours après la date limite de conversion, plus un jour). Si une carte de contenu expire le 1er avril, qu'elle est déclenchée par l'API et qu'elle n'a pas envoyé de messages depuis le 15 mars, elle expirera le 15 mars de l'année prochaine.

Les canvas sont uniquement arrêtés après l'arrêt des cartes de contenu, ce qui signifie que leur durée maximale est dépassée.

#### J'ai une expérience de drapeau de fonctionnalité dans mon Canvas. Une fois que mon indicateur de fonctionnalité est activé, le Canvas reste-t-il actif ?

Les toiles comportant des pas de drapeaux de fonctionnalité ne sont pas automatiquement arrêtées et ne deviennent pas inactives.

#### Pourquoi des campagnes inactives s'affichent-elles dans ma liste de campagnes alors que j'ai appliqué un filtre pour n'afficher que les campagnes actives ?

Les campagnes au ralenti sont considérées comme actives jusqu'à ce qu'elles soient arrêtées.

#### Une campagne peut-elle être considérée comme inactive alors qu'elle continue d'envoyer des notifications push ?

Non. Une campagne est considérée comme inactive lorsqu'elle n'envoie plus de messages. 