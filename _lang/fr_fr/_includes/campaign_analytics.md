## Analyse de campagne

Une fois que vous avez lancé votre campagne, vous pouvez revenir à la page des détails de cette campagne pour afficher les indicateurs clés. Accédez à la page des **campagnes** et sélectionnez votre campagne pour ouvrir la page des détails. Pour les cartes de contenu {% if include.channel == "Content Card" %} {% elsif include.channel == "email" %} e-mail {% elsif include.channel == "in-app message" %}messages in-app {% elsif include.channel == "push" %}messages push {% elsif include.channel == "SMS" %}messages SMS {% elsif include.channel == "whatsapp" %}messages WhatsApp {% elsif include.channel == "webhook" %}webhooks {% endif %}envoyés dans Canvas, reportez-vous à [Analytique Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/).

{% alert tip %}
Vous recherchez des définitions pour les termes et les indicateurs répertoriés dans votre rapport ? Consultez notre
  {% if include.channel == "email" %}[Glossaire analytique pour l’e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "Content Card" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/) et filtre par cartes de contenu
  {% elsif include.channel == "in-app message" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/) et filtrage par message in-app
  {% elsif include.channel == "push" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/) et filtre par Push
  {% elsif include.channel == "SMS" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/) et filtrage par SMS
  {% elsif include.channel == "whatsapp" %}[Glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/) et filtre par WhatsApp
  {% elsif include.channel == "webhook" %}[Report Metrics Glossaire]({{site.baseurl}}/user_guide/data/report_metrics/) et filtre par webhook{% endif %}.
{% endalert %}

À partir de l'onglet **Analyse/analytique de la campagne**, vous pouvez consulter vos rapports dans une série d'adjectifs. Vous pouvez voir plus ou moins que ceux énumérés dans les sections ci-dessous, mais chacun a son propre objectif utile.

### Détails de la campagne

Le panneau **Détails de la campagne** présente un aperçu de haut niveau de l'ensemble des performances de votre
  {% if include.channel == "Content Card" %}Carte de contenu.
  {% elsif include.channel == "email" %}e-mail.
  {% elsif include.channel == "in-app message" %}message in-app.
  {% elsif include.channel == "push" %}message push.
  {% elsif include.channel == "SMS" %}SMS.
  {% elsif include.channel == "whatsapp" %}messages WhatApp.
  {% elsif include.channel == "webhook" %}webhook.
  {% endif %}

Examinez ce panneau pour voir les indicateurs globaux tels que le nombre de messages envoyés au nombre de destinataires, le taux de conversion primaire et le chiffre d'affaires total généré par ce message. Vous pouvez également consulter les paramètres de livraison, d'audience et de conversion à partir de cette page.

{% if include.channel == "whatsapp" %}
{% alert note %}
Le canal WhatsApp comprend le taux de lecture. Cette mesure n'est fournie que pour les utilisateurs ayant activé les reçus de lecture, ce qui peut varier.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Panneau Détails de la campagne avec un aperçu des indicateurs utilisés pour déterminer les performances de la campagne.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "email" %}
![Panneau Détails de la campagne avec un aperçu des indicateurs utilisés pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Panneau Détails de la campagne avec un aperçu des indicateurs utilisés pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Panneau Détails de la campagne avec un aperçu des indicateurs utilisés pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Panneau Détails de la campagne avec un aperçu des indicateurs utilisés pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_iam.png %})

Dans Canvas, vous verrez les performances des messages in-app cartographiés sur le Canvas que vous avez créé. Vous pouvez utiliser le panneau de commande en haut de la page pour effacer les autres types de messages (canaux) et afficher uniquement les messages in-app dans votre Canvas.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "webhook" %}
![Panneau Détails de la campagne avec un aperçu des indicateurs utilisés pour déterminer les performances de la campagne.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### Groupes de contrôle {#cc-control-group}

Pour mesurer l'impact d'une carte de contenu individuelle, vous pouvez ajouter un [groupe de contrôle][2] à un test A/B. Le panneau supérieur **Détails de la campagne** n'inclut pas les indicateurs de la variante Groupe de contrôle.

{% elsif include.channel == "SMS" %}

#### Groupes de contrôle {#sms-control-group}

Pour mesurer l'impact d'un message SMS individuel, vous pouvez ajouter un [groupe de contrôle][2] à un test A/B. Le panneau supérieur **Détails de la campagne** n'inclut pas les indicateurs de la variante Groupe de contrôle.

{% elsif include.channel == "whatsapp" %}

#### Groupes de contrôle {#whatsapp-control-group}

Pour mesurer l'impact d'un message WhatsApp individuel, vous pouvez ajouter un [groupe de contrôle][2] à un test A/B. Le panneau supérieur **Détails de la campagne** n'inclut pas les indicateurs de la variante Groupe de contrôle.

{% elsif include.channel == "webhook" %}

#### Groupes de contrôle {#webhook-control-group}

Pour mesurer l'impact d'un message webhook individuel, vous pouvez ajouter un [groupe de contrôle][2] à un test A/B. Le panneau supérieur **Détails de la campagne** n'inclut pas les indicateurs de la variante Groupe de contrôle.

{% endif %}

#### modifications depuis la dernière consultation

Le nombre de mises à jour de la campagne par d'autres membres de votre équipe est suivi par l'indicateur *Changements depuis le dernier affichage* sur la page d'aperçu de la campagne. Sélectionnez **Modifications depuis la dernière consultation** pour afficher un journal des modifications apportées au nom de la campagne, à sa planification, à ses étiquettes, à son message, à son audience, à son statut d'approbation ou à la configuration de l'accès de l'équipe. Pour chaque mise à jour, vous pouvez voir qui a effectué la mise à jour et quand. Vous pouvez utiliser ce journal des modifications pour vérifier les changements apportés à votre campagne.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Performance de la carte de contenu

Le panneau " **Performance de la carte de contenu"** indique le niveau de performance de votre message en fonction de différents critères. Les indicateurs de ce volet varient en fonction de votre canal de communication choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal de communication.

![Analyse des performances des messages de carte de contenu]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### Performances des e-mails

Le tableau de bord des performances de **l'e-mail** indique le niveau de performance de votre message en fonction de différents critères. Les indicateurs de ce volet varient en fonction de votre canal de communication choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal de communication.

![Analyse des performances des messages e-mail]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### Performance des messages in-app

Le panneau de **performance des messages in-app** présente l'efficacité de votre message en fonction de différentes dimensions. Les indicateurs de ce volet varient en fonction de votre canal de communication choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal de communication.

![Analyse des performances des messages in-app]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Performances des notifications push

Le panneau " **Push Performance"** donne un aperçu de la performance de votre message en fonction de différents critères. Les indicateurs de ce volet varient en fonction de votre canal de communication choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal de communication.

![Analyse des performances des messages push]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### Performances des SMS

Le panneau " **Performance SMS"** indique le niveau de performance de votre message en fonction de différents critères. Les indicateurs de ce volet varient en fonction de votre canal de communication choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal de communication.

![Volet des performances des SMS/MMS qui comprend un tableau d'indicateurs pour un groupe de contrôle, la variante 1 et la variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "webhook" %}
### Performances des webhooks

Le tableau de bord des **performances des webhooks** donne un aperçu de l'efficacité de votre message en fonction de différents critères. Les indicateurs de ce volet varient en fonction de votre canal de communication choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal de communication.

![Panneau de performances du webhook comprenant un tableau d'indicateurs pour un groupe de contrôle et la variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### Performances WhatsApp

Le panneau **WhatsApp Performance** présente les performances de votre message en fonction de différents critères. Les indicateurs de ce volet varient en fonction de votre canal de communication choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal de communication.

![Panneau de performances de WhatsApp comprenant un tableau d'indicateurs pour la variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Si vous souhaitez simplifier votre vue, cliquez sur <i class="fas fa-plus"></i> **Add/Remove Columns (Ajouter/Supprimer des colonnes** ) et effacez les indicateurs que vous souhaitez. Par défaut, tous les indicateurs sont affichés.

{% if include.channel == "email" %}

#### Cartes thermiques

Grâce aux cartes thermiques, vous pouvez connaître le succès des différents liens d'une même campagne d'e-mailing. Dans la section **Analyse/analytique des messages**, accédez au panneau **Performance des e-mails.**  Sélectionnez **Aperçu et carte thermique** pour afficher un aperçu de votre campagne e-mail et la carte thermique. Vous pouvez également sélectionner le lien hypertexte dans le nom de la variante pour afficher la carte thermique.

Dans cette vue, vous pouvez utiliser la bascule **Afficher la carte thermique** pour afficher une vue visuelle de votre e-mail qui montre la fréquence globale et l'emplacement/localisation des clics au cours de la durée de vie de la campagne. Dans le panneau **Tableau des liens par nombre total de clics**, vous pouvez afficher tous les liens de votre campagne e-mail et les trier par nombre total de clics. Cela peut fournir des informations supplémentaires sur les endroits où vos utilisateurs naviguent. Pour enregistrer une copie de la carte thermique à des fins de référence, sélectionnez le bouton de téléchargement.

![Exemple de page de prévisualisation et de carte thermique comprenant une campagne d'e-mail et un panneau avec des exemples d'alias de liens avec leur nombre total de clics.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Images

Nous vous conseillons d'activer CORS pour vos URL d'images afin d'éviter que les images ne se cassent dans les aperçus et les exportations de cartes thermiques.

{% endif %}

{% if include.channel == "Content Card" %}

#### Métriques de la carte de contenu

Voici une description de certaines indicateurs clés que vous pouvez voir lors de l’examen des performances de vos messages. Pour obtenir les définitions complètes de tous les indicateurs des cartes de contenu, reportez-vous au [glossaire des indicateurs de rapport][1] et filtrez par cartes de contenu.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#messages-sent">Messages envoyés</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Messages Sent' %} <br><br>
                Ce montant est calculé différemment en fonction de ce que vous avez choisi pour
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">Création de cartes</a>:<br><br>
                <ul>
                    <li><b>Au moment du lancement ou de l'entrée d’étape :</b> Le nombre de cartes créées et disponibles pour être vues. Le fait que les utilisateurs aient consulté ou non la carte n’est pas comptabilisé.</li>
                    <li><b>À première vue :</b> Le nombre de cartes affichées aux utilisateurs.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impressions totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %} Ceci peut être incrémenté plusieurs fois pour le même utilisateur.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Impressions uniques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Ce compte</span> ne s'incrémente pas la deuxième fois qu'un utilisateur consulte une carte.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Destinataires uniques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %} <br><br> Étant donné qu'un spectateur peut être un destinataire unique chaque jour, vous devriez vous attendre à ce que ce chiffre soit plus élevé que celui des <i>impressions uniques.</i></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Clics uniques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Ceci inclut les clics sur les liens de désabonnement fournis par Braze.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-dismissals">Rejets uniques</a></td>
            <td>{% multi_lang_include metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
En matière de méthode d’enregistrement des impressions, il existe quelques différences entre Internet, Android et iOS. En règle générale, Braze enregistre une impression lorsqu'une carte est vue, c'est-à-dire après qu'un utilisateur a fait défiler son fil jusqu'à la carte de contenu spécifique.
{% endalert %}

#### Destinataires uniques et impressions uniques

Plusieurs indicateurs sont disponibles pour couvrir la visibilité de votre message. Il s'agit notamment des _messages envoyés_, des _destinataires uniques_ et des _impressions uniques_. En particulier, la différence entre les _destinataires uniques_ et les _impressions uniques_ peut prêter à confusion. Prenons quelques exemples de scénarios pour mieux comprendre ces indicateurs.

Supposons que vous consultiez une carte de contenu aujourd'hui, puis la même carte demain, et encore après-demain - vous serez compté comme _destinataire unique_ trois fois. Cependant, vous ne serez comptabilisé que pour une seule _impression unique_. Vous serez également inclus dans le nombre d' _envois de messages_, car la carte était disponible sur votre appareil.

Autre exemple, supposons que vous obteniez cinq _impressions uniques_ sur une campagne de cartes de contenu affichant 150 000 _messages envoyés_. Cela signifie que la carte a été mise à disposition (en arrière-plan) à une audience de 150 000 utilisateurs, mais que seuls cinq utilisateurs ont effectué toutes les étapes suivantes après l’envoi :

1. Ont démarré une session ou l’application a explicitement demandé une synchronisation des cartes de contenu (ou les deux)
2. Ont navigué dans la vue Carte de contenu
3. Le SDK a enregistré une impression et l’a consignée sur le serveur

Vos _messages envoyés_ se réfèrent aux cartes de contenu disponibles pour être vues, tandis que les _destinataires uniques_ se réfèrent aux cartes de contenu qui ont été effectivement vues.

{% elsif include.channel == "email" %}

#### Métriques des e-mails

Voici quelques indicateurs clés spécifiques aux e-mails que vous ne verrez pas dans d’autres canaux. Pour voir les définitions complètes de tous les indicateurs d'e-mail utilisés dans Braze, reportez-vous à notre [Glossaire d'analyse d'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Clics uniques</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Clicks' %} Ce suivi est effectué sur une période de sept jours pour les e-mails et mesuré par <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Cela inclut les clics sur les liens de désinscription fournis par Braze. Ce nombre doit être compris entre 5 et 10 %. Tout ce qui est supérieur à 10 % est exceptionnel !
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Ouvertures uniques</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Opens' %} Pour les e-mails, le suivi est effectué sur une période de 7 jours. Ce chiffre devrait se situer entre 30 et 40 %. Tout ce qui est supérieur à 40 % est exceptionnel !
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Taux de Click-to-Open</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Taux de courriers indésirables</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Spam' %} Si cet indicateur est supérieur à 0,08, cela peut être le signe que votre message est trop commercial ou que vous devriez reconsidérer vos méthodes de collecte d'adresses e-mail (de manière à n’envoyer des messages qu’aux destinataires intéressés par votre correspondance).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Désabonnés</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric= 'Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Autre ouverture</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Estimation des ouvertures réelles</a></td>
            <td class="no-split"> {% multi_lang_include metrics.md metric='Estimated Real Opens' %} Voir la section suivante pour plus de détails.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Ouverture automatique</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Rebonds</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Échec d'envoi définitif</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Échec provisoire de livraison</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Report</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Reports

On parle de report ou d'ajournement lorsqu'un e-mail n'a pas été livré immédiatement, mais que Braze relance l'e-mail jusqu'à 72 heures après cet échec temporaire de la réception/distribution afin de maximiser les chances de réussite avant l'arrêt des tentatives pour cette campagne spécifique. Les raisons habituelles de ces reports sont la limitation du débit du volume d'e-mails basée sur la réputation par le fournisseur de la boîte de réception, des problèmes temporaires de connectivité ou des erreurs de DNS.

Les _reports_ diffèrent des échecs provisoires _d'envoi_. Si aucun e-mail n'a été délivré avec succès pendant cette période de réessai, Braze enverra un événement d'échec provisoire d'envoi par tentative de campagne envoyée. Avant le 25 février 2025, ces tentatives étaient comptabilisées comme plusieurs échecs provisoires d'envoi pour une même campagne.

Notez que les _requêtes SQL_ ne sont actuellement disponibles qu'en utilisant les fonctionnalités de Braze Currents ou de Braze Snowflake (telles que Query Builder, SQL Segment, Snowflake Data Sharing). Si vous souhaitez l'inclure dans l'analyse/analytique des campagnes ou de Canvas, veuillez [nous faire part de vos commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

##### Taux d'ouverture réel estimé {#estimated-real-open-rate}

Cette statistique utilise un modèle analytique propriétaire créé par Braze pour reconstruire une estimation du taux d'ouverture unique de la campagne comme si les ouvertures automatiques n'existaient pas. Alors que nous recevons des étiquettes de *Machine Opens* sur certains événements d'ouverture de la part des expéditeurs d'e-mails (voir ci-dessus), ces étiquettes peuvent souvent étiqueter les ouvertures réelles comme des ouvertures réelles. En d'autres termes, les *autres ouvertures* sont probablement une sous-estimation des ouvertures réelles (par des utilisateurs réels). Au lieu de cela, Braze utilise les données de clics de chaque campagne pour déduire le taux d'ouverture du message par des humains réels. Cela permet de compenser les divers mécanismes d'ouverture des machines, y compris la protection de confidentialité dans Mail d'Apple.

Le _taux d'ouverture réel estimé_ est calculé 36 heures après le début de l'envoi de l'e-mail et est ensuite recalculé toutes les 24 heures. Si une campagne se répète, l'estimation est recalculée 36 heures après un nouvel envoi.

En règle générale, il faut environ 10 000 e-mails délivrés pour que la statistique soit calculée avec succès, bien que ce nombre puisse varier en fonction du taux de clics. Si la statistique ne peut pas être calculée, la colonne affiche "--".

###### Restrictions

Le taux d'ouverture réel estimé n'est disponible que dans les campagnes et n'est pas indiqué dans les événements actuels. Cet indicateur n'est calculé rétroactivement que pour les campagnes actives lancées avant le 14 novembre 2023.

{% elsif include.channel == "in-app message" %}

#### Métriques de message in-app

Voici quelques indicateurs clés de messages in-app que vous pouvez voir dans vos analyses. Pour consulter les définitions complètes de tous les indicateurs des messages in-app utilisés dans Braze, reportez-vous à notre [Glossaire des indicateurs de rapport][1].

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Clics sur le corps du message</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Clics Boutons 1</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Clics Boutons 2</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Impressions uniques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impressions totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversions (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Conversions totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Taux de conversion</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Fermer le message</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "push" %}

#### Métriques de notification push

Voici une description de certaines indicateurs clés que vous pouvez voir lors de l’examen des performances de vos messages. Pour obtenir les définitions complètes de tous les indicateurs de poussée, consultez le [glossaire des indicateurs de rapport][1] et filtrez par poussée.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Descriptif</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Rebonds</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %} Voir <a href="#bounced-push">Rebonds de notification push</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Ouvertures directes</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Ouvertures</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> La réception/distribution des notifications est assurée au mieux par les services de notification push d'Apple (APN). Cette action n’est pas destinée à fournir des données à votre application, mais seulement à informer l’utilisateur qu’il existe de nouvelles données disponibles. La distinction importante est que nous allons afficher le nombre de messages que nous avons délivrés avec succès aux APN, et pas nécessairement combien d’APN ont délivré des notifications avec succès aux appareils.

##### Suivi des désabonnements

Les désabonnements aux notifications push ne sont pas pris en compte en tant qu'indicateurs dans l'analyse de la campagne. Reportez-vous à la section [Suivi des désabonnements en mode push]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) pour savoir comment effectuer un suivi manuel de cette mesure.

##### Comprendre s'ouvre

Bien que les termes _ouvertures directes_ et _ouvertures influencées_ contiennent le mot « ouvertures », il s'agit en fait d'indicateurs différents. Les _ouvertures directes_ font référence à l'ouverture directe d'une notification push, comme indiqué dans le tableau ci-dessus. Les _ouvertures influencées_ font référence à l'ouverture d'une app, sans ouverture d'une notification push dans un délai spécifique après sa réception. Ainsi, les ouvertures _influencées_ font référence aux ouvertures de l'app, et non aux ouvertures des notifications push.

##### Pourquoi les envois push peuvent-ils dépasser le nombre de destinataires uniques ?

Le nombre d'_envois_ peut dépasser le nombre de _destinataires uniques_ pour les raisons suivantes :

- **La rééligibilité est en cours :** Lorsque la rééligibilité est activée dans les paramètres de votre campagne ou de votre canvas, les utilisateurs qui répondent aux critères de segmentation et de réception/distribution peuvent recevoir la même notification push plusieurs fois. Cela se traduit par un nombre plus élevé d'envois totaux.
- **Les utilisateurs disposent de plusieurs appareils :** Si la rééligibilité n'est pas activée, la différence peut s'expliquer par le fait que les utilisateurs ont plusieurs appareils associés à leur profil. Par exemple, un utilisateur peut avoir à la fois un smartphone et une tablette, et la notification push est envoyée à tous les appareils enregistrés. Chaque réception/distribution compte comme un envoi, mais un seul destinataire unique est enregistré.
- **Les utilisateurs sont affectés à plusieurs applications :** Si les utilisateurs sont associés à plusieurs apps (par exemple lorsqu'ils testent une nouvelle app), ils peuvent recevoir la même notification push sur chaque app. Cela contribue à augmenter le nombre d'envois.

##### Pourquoi les rebonds se produisent-ils ? {#bounced-push}

{% tabs %}
{% tab Service de notification push d'Apple %}

Les rebonds se produisent dans les services de notification push d'Apple (APN) lorsqu'une notification push tente d'être réception/distribution à un appareil sur lequel l'application prévue n'est pas installée. Les APN ont également le droit de modifier les jetons pour les appareils arbitrairement. Si vous essayez d’envoyer un message à un appareil d’utilisateur sur lequel le jeton de notification push a changé entre le moment où nous avons déjà enregistré son jeton (c.-à-d. au début de chaque session lorsque nous enregistrons un utilisateur pour un jeton de notification push) et le moment de l’envoi, il en résulte un rebond.

Si un utilisateur désactive la notification push dans les paramètres de l’appareil lors de la prochaine ouverture d’application, le SDK détecte que le push a été désactivé et informe Braze. À ce stade, nous allons mettre à jour l’état de l’opération push de Activé à Désactivé. Lorsqu’un utilisateur désactivé reçoit une campagne push avant d’avoir une nouvelle session, la campagne s’affiche avec succès et apparaît comme livrée. Il n’y aura pas de rebond de push pour cet utilisateur. Après une session ultérieure, lorsque vous essayez d’envoyer une notification push à l’utilisateur, Braze sait déjà si nous avons un jeton de premier plan, et donc aucune notification n’est envoyée.

Notez que les notifications push expirant avant la livraison ne sont pas considérées comme ayant échoué et ne seront pas enregistrées comme rebond.

{% endtab %}
{% tab Firebase Cloud Messaging %}

La messagerie cloud Firebase (FCM) peut être utilisée dans trois cas :

| Scénario | Descriptif |
| -- | -- |
| Applications désinstallées | Lorsqu’un message tente une livraison à un appareil et que l’application prévue est désinstallée sur cet appareil, le message est supprimé et l’ID d’enregistrement de l’appareil est invalidé. Toute future tentative d’envoi de message de l’appareil renvoie une erreur NotRegistered. |
| Application sauvegardée | Lorsqu’une application est sauvegardée, son ID d’enregistrement peut cesser d’être valide avant la restauration de l’application. Dans ce cas, FCM ne conservera plus l’ID d’enregistrement de l’application et l’application ne recevra plus de messages. Ainsi, les ID d'enregistrement ne doivent **pas** être enregistrés lors de la sauvegarde d'une application. |
| Application mise à jour | Lorsqu’une application est mise à jour, l’ID d’enregistrement de la version précédente peut ne plus fonctionner. Une application mise à jour doit donc remplacer son ID d’enregistrement existant. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### Métriques de messages SMS

Voici une description de certaines indicateurs clés que vous pouvez voir lors de l’examen des performances de vos messages. Pour obtenir les définitions complètes de tous les indicateurs SMS, consultez le [glossaire des indicateurs de rapport][1] et filtrez par SMS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Envoyé</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends-to-carrier">Envois à l’opérateur</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends to Carrier' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Échecs de réception</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Livraison confirmée</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rejets</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Désabonnement</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Aide</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Help' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Nombre total de clics</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Indicateurs de webhook

Voici quelques indicateurs clés de webhook qui peuvent apparaître dans vos analyses. Pour voir les définitions complètes de tous les indicateurs de webhook utilisés dans Braze, reportez-vous à notre [glossaire des indicateurs de rapport][1].

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Destinataires uniques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Envois</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Erreurs</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### Indicateurs WhatsApp

Voici quelques indicateurs clés de WhatsApp qui peuvent apparaître dans vos analyses. Pour consulter les définitions complètes de tous les indicateurs WhatsApp utilisés dans Braze, reportez-vous à notre [Glossaire des indicateurs de rapport.][1]

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Envois</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Réceptions</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Lectures</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Échecs</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Blocage de l'utilisateur final et indicateurs de reporting

D'autres indicateurs peuvent être consultés via le [tableau de bord du gestionnaire WhatsApp](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx), bien qu'une [confirmation de votre accès soit](https://www.facebook.com/business/help/218116047387456) nécessaire pour accéder à toutes les informations disponibles.

{% endif %}

### Performances historiques

Le panneau **Performances historiques** vous permet de visualiser les indicateurs du panneau **Performances des messages** sous la forme d'un graphique dans le temps. Utilisez les filtres en haut du volet pour modifier les statistiques et les canaux affichés dans le graphique. La plage temporelle de ce graphique reflète toujours la plage de temps spécifiée en haut de la page.

Pour obtenir une ventilation jour par jour, cliquez sur le menu hamburger <i class="fas fa-bars"></i> et sélectionnez **Télécharger CSV** pour recevoir une exportation CSV du rapport.

![Un graphique du volet Performances historiques avec des exemples de statistiques d’un e-mail de février 2021 à mai 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Si vous choisissez d'envoyer uniquement aux utilisateurs qui peuvent voir la dernière version de Braze des messages in-app (Génération 3), votre **audience cible** ne s'ajuste pas pour refléter votre choix.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Réponses à des mots-clés

Le panneau **Réponses par mot-clé** vous montre une chronologie des mots-clés entrants avec lesquels les utilisateurs ont répondu après avoir reçu votre message.  

![Panneau de réponses aux mots-clés SMS/MMS au niveau de la campagne qui comprend un graphique linéaire de la distribution des mots-clés dans le temps et une section Catégories de mots-clés avec des cases à cocher pour l'abonnement, l'exclusion, l'aide, l'autre, plus et l'accompagnement.]({% image_buster /assets/img/sms/keyword_responses.png %})

Ici, vous pouvez également consulter la répartition des réponses pour chaque catégorie de mots clés afin de déterminer les prochaines étapes du [reciblage]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) et de [création d’un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).

![Le tableau situé sous le graphique linéaire comporte des colonnes pour la catégorie de mots clés, la distribution des réponses et le reciblage, où vous avez la possibilité de créer une segmentation avec la catégorie de mots clés.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Détails de l'événement de conversion

Le panneau **Détails de l'événement de conversion** vous indique les performances de vos événements de conversion pour votre campagne. Pour plus d'informations, reportez-vous à la section [Événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results).

![Le panneau des détails de l'événement de conversion.]({% image_buster /assets/img/cc-conversion.png %})

### Corrélation de conversion

Le panneau **Corrélation de conversion** vous donne des informations sur les attributs et les comportements des utilisateurs qui favorisent ou entravent les résultats que vous avez définis pour les campagnes. Pour plus d'informations, consultez la section [Corrélation de conversion]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/).

![Le panneau de corrélation de conversion avec une analyse des attributs et du comportement de l'utilisateur à partir de l'événement de conversion principal - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "whatsapp" %}

### Analyses Meta

En plus des analyses/analytiques de Braze, des analyses au niveau des modèles sont accessibles dans le gestionnaire d'entreprise de WhatsApp. Pour plus d'informations, consultez la [documentation de Meta](https://www.facebook.com/business/help/218116047387456).

{% endif %}

{% if include.channel == "SMS" %}

### Événements SMS Currents

Comme pour les e-mails, Braze reçoit des événements au niveau utilisateur liés à un message SMS à mesure qu’il effectue son parcours à destination d’un utilisateur. Tout événement SMS entrant sera également envoyé en tant qu'événement Currents par le biais de l'événement [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events). Cela vous permet d'effectuer des actions supplémentaires ou des rapports sur les messages que vos utilisateurs envoient en dehors de la plateforme Braze.

{% alert note %}
Les messages entrants sont tronqués au-delà de 1 600 caractères.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Rapport de rétention

Les rapports de rétention indiquent les taux auxquels vos utilisateurs ont effectué un événement de rétention sélectionné sur les périodes dans une campagne ou un Canvas spécifique. Pour plus d'informations, reportez-vous aux [rapports de rétention]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

## Rapport d'entonnoir

Le rapport d’entonnoir offre un rapport visuel qui vous permet d’analyser les parcours de vos clients après la réception d’une campagne ou d’un Canvas. Si votre campagne ou votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous serez en mesure de comprendre comment les différentes variantes ont impacté le tunnel de conversion à un niveau plus précis et de l’optimiser en fonction de ces données.

Pour plus d'informations, reportez-vous aux [rapports d'entonnoirs]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

{% endif %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[2]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants
