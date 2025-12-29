{% if include.section == "Differing audience size" %}

La taille de la population cible qui s'est affichée dans une campagne ou un Canvas peut différer de la [taille de l'audience atteignable pour un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation), même si vous ajoutez directement ce segment dans votre campagne ou votre Canvas sans filtre supplémentaire.
Cela peut se produire pour plusieurs raisons :

- Lorsqu'un groupe de contrôle global s'applique à une campagne ou à un Canvas, les utilisateurs de ce groupe de contrôle global sont exclus du décompte des utilisateurs joignables.
- La taille de la population cible d'une campagne ou d'un Canvas exclut les utilisateurs qui ne sont pas joignables par les différents canaux de messages ; le comportement diffère d'un canal à l'autre. Par exemple, l'audience atteignable pour une campagne ou un Canvas exclut les utilisateurs qui sont désabonnés, marqués comme spam (pour les e-mails) ou qui ont fait l'objet d'un échec provisoire d'envoi (pour les e-mails). Cependant, le segment lui-même n'exclut que les abonnements lorsqu'il indique le nombre estimé d'utilisateurs pouvant être joints par e-mail. 
- Braze n'envoie des messages SMS qu'aux utilisateurs faisant partie du groupe d'abonnement sélectionné. Par conséquent, la population ciblée par SMS pour une campagne ou un canvas exclura également tous les utilisateurs qui ne font pas partie du groupe d'abonnement sélectionné.

{% endif %}

{% if include.section == "Refresh settings" %}

Si vous n'avez pas besoin que votre extension soit actualisée à intervalles réguliers, vous pouvez l'enregistrer sans utiliser les paramètres d'actualisation, et Braze générera par défaut votre extension de segmentation en fonction de votre adhésion d'utilisateur à ce moment-là. Utilisez le comportement par défaut si vous ne souhaitez générer l'audience qu'une seule fois et la cibler ensuite avec une campagne ponctuelle.

Votre segmentation commencera toujours à être traitée après l'enregistrement initial. À chaque fois que votre segment est actualisé, Braze ré-exécute le segment et met à jour l'appartenance au segment pour refléter les utilisateurs de votre segment au moment de l'actualisation. Cela peut aider vos campagnes récurrentes à atteindre les utilisateurs les plus pertinents.

#### Mise en place d'une actualisation récurrente

Pour établir une planification récurrente en désignant des paramètres d'actualisation, sélectionnez **Activer l'actualisation**. L'option permettant d'actualiser les paramètres est disponible pour tous les types d'extensions de segments, y compris les segments SQL, les extensions de segments CDI et les extensions de segments basées sur des formulaires simples.

{% alert important %}
Pour optimiser la gestion de vos données, les paramètres d'actualisation sont automatiquement désactivés pour les extensions de segments non utilisées. Les extensions de segments sont considérées comme inutilisées lorsqu'elles sont :

- N'est pas utilisé dans des campagnes, des canevas ou des segments actifs ou inactifs (brouillons, arrêtés, archivés) ; ou
- N’a pas été modifiée depuis plus de 7 jours

Braze informera le contact de l'entreprise et le créateur de l'extension si ce paramètre est désactivé. L’option permettant de renouveler les extensions quotidiennement peut être réactivée à tout moment.
{% endalert %}

#### Sélectionner vos paramètres d'actualisation

![Intervalle d'actualisation Paramètres avec une fréquence d'actualisation hebdomadaire, une heure de début de 10 heures et le lundi sélectionné comme jour.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

Dans le panneau **Paramètres d'intervalle d'actualisation**, vous pouvez sélectionner la fréquence à laquelle cette extension de segmentation sera actualisée : toutes les heures, tous les jours, toutes les semaines ou tous les mois. Vous devrez également sélectionner l'heure spécifique (dans le fuseau horaire de votre entreprise) à laquelle l'actualisation doit avoir lieu, par exemple :

- Si votre campagne d'e-mail est envoyée tous les lundis à 11 heures, heure de la société, et que vous voulez vous assurer que votre segment est actualisé juste avant l'envoi, vous devriez choisir une planification d'actualisation hebdomadaire à 10 heures les lundis.
- Si vous souhaitez que votre segmentation soit actualisée tous les jours, sélectionnez la fréquence d'actualisation quotidienne, puis choisissez l'heure à laquelle l'actualisation doit avoir lieu.

{% alert note %}
La possibilité de définir une planification d'actualisation horaire n'est pas disponible pour les extensions de segments basées sur des formulaires (mais vous pouvez définir des planifications quotidiennes, hebdomadaires ou mensuelles).
{% endalert %}

#### Consommation de crédits et coûts supplémentaires

Étant donné que les actualisations réexécutent la requête de votre segment, chaque actualisation pour les segments SQL consommera des crédits de segment SQL, et chaque actualisation pour les extensions de segments CDI entraînera un coût au sein de votre entrepôt de données third-party.

{% alert note %}
L'actualisation des segments peut prendre jusqu'à 60 minutes en raison du temps de traitement des données. Les segments en cours d'actualisation auront un statut "En cours" dans votre liste d'extensions de segments. Cela a plusieurs implications :

- Pour terminer le traitement de votre segment avant une heure précise, choisissez une heure d'actualisation située 60 minutes plus tôt. 
- Il ne peut y avoir qu'une seule actualisation à la fois pour une extension de segments donnée. En cas de conflit où une nouvelle actualisation est lancée alors qu'une actualisation existante a déjà commencé à être traitée, Braze annulera la nouvelle demande d'actualisation et poursuivra le traitement en cours.
{% endalert %}

#### Critères de désactivation automatique des extensions périmées

Les actualisations planifiées sont automatiquement désactivées lorsqu'une extension de segments est périmée. Une extension de segments est périmée si elle répond aux critères suivants :

- Non utilisé dans des campagnes ou des canvas actifs
- Non utilisé dans un segment d'une campagne ou d'un canvas actifs.
- Non utilisé dans un segment où le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) est activé.
- N'a pas été modifié depuis plus de sept jours
- N'a pas été ajouté à une campagne ou à Canvas (y compris les brouillons), ou à un segment depuis plus de sept jours.

Si l'actualisation planifiée est désactivée pour une extension de segments, une notification l'indique pour cette extension.

![Une notification indiquant que "Les actualisations planifiées ont été désactivées pour cette extension car elle n'est pas utilisée dans des campagnes, des canevas ou des segments actifs". L'extension de segmentation a été désactivée le 23 février 2025 à 12h00."]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

Lorsque vous êtes prêt à utiliser une extension de segment périmée, passez en revue les paramètres d'actualisation, sélectionnez la planification d'actualisation qui correspond à votre cas d'utilisation, puis enregistrez toutes les modifications.

{% endif %}