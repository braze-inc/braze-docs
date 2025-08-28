---
nav_title: Tableau de bord de conversions
article_title: Tableau de bord de conversions
alias: "/conversions_dashboard_v2/"
description: "Le tableau de bord de conversions vous permet d’analyser les conversions entre les campagnes, les Canvas et les canaux en utilisant des méthodes d’attribution différentes."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# Tableau de bord de conversions

> Le tableau de bord des conversions analyse les conversions entre les campagnes, les Canvas et les canaux, en utilisant diverses [méthodes d'attribution](#attribution-methods). Lorsque vous mesurez vos conversions, vous pouvez spécifier la période, l’événement de conversion et la fenêtre de conversion.

## Mettre en place votre rapport

Pour configurer votre tableau de bord des conversions :

1. Sélectionnez **Analyse** > **Conversions**.
2. Sélectionnez une **plage de dates** pour votre rapport, de 90 jours maximum.
3. Sélectionnez les campagnes ou les toiles (ou les deux) à analyser. 
   - (facultatif) Filtrez les campagnes et les toiles en sélectionnant une étiquette.  
4. Sélectionnez le **(s) canal(aux)** à analyser pour vos messages.
5. Sélectionnez une **Ventilation par** couche pour afficher différentes dimensions de données, par exemple par variante, étape du canvas, pays ou langue.
6. (Facultatif) Si vous souhaitez calculer les conversions d'un événement qui n'a pas été configuré en tant qu'événement de conversion sur la campagne ou le Canvas, activez l'option [Utiliser des événements personnalisés.](#using-custom-events)
7. Choisissez une [méthode d'attribution](#attribution-methods) pour analyser les messages sélectionnés.

{% alert note %}
Si vous analysez les conversions pour plusieurs canaux, votre **méthode d'attribution** sera par défaut l' **Attribution de la dernière touche.**
{% endalert %}

{:start="8"}
8\. Sélectionnez **Créer** pour exécuter le/un rapport.

Une fois la page chargée, sélectionnez un **événement de conversion** pour filtrer le rapport sur les données de conversion. Les sélections disponibles incluront les événements qui ont été préconfigurés sur les toiles et les campagnes. Si vous avez sélectionné un événement personnalisé lors de la création de votre rapport (étape 6), cette option n'est pas disponible.

### Utilisation d'événements personnalisés

Pour que les indicateurs d'événements personnalisés apparaissent sur le tableau de bord des conversions, vous devez avoir un événement de conversion et un événement d'entrée dans le canvas dans la plage de dates spécifiée sur la page. 

Pour calculer les conversions d'un événement qui n'a pas été configuré comme événement de conversion sur la campagne ou le Canvas, sélectionnez un événement personnalisé spécifique à utiliser comme événement de conversion. 

1. Lors de la configuration de votre rapport, activez l'option **Utiliser des événements personnalisés**.
2. Sélectionnez un événement personnalisé à utiliser comme événement de conversion.
3. Sélectionnez la fenêtre de conversion dans laquelle l'événement aurait dû se produire pour être considéré comme une conversion.

{% alert note %}
Si vous sélectionnez un événement personnalisé, vous ne verrez pas la liste déroulante des **événements de conversion** sur la page et vous devrez exécuter à nouveau le rapport pour afficher les conversions pour différents événements personnalisés.
{% endalert %}

## Comprendre votre rapport

Votre rapport est divisé en trois sections :

- [Détails de la conversion](#conversion-details)
- [Tunnel de conversion](#conversion-funnel)
- [Évolution des conversions](#conversions-over-time)

### Détails de la conversion

Le tableau des détails de la conversion présente toujours une colonne pour les *destinataires* et une autre pour les *conversions* (taux et total). Les deux autres colonnes du tableau qui apparaissent dépendent des options que vous avez sélectionnées lors de la configuration de votre rapport. 

![Tableau des détails de la conversion indiquant Touches comme méthode d'attribution pour les colonnes trois et quatre.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

Le tableau suivant décrit les indicateurs possibles.

| Indicateurs métriques | Description |
| --- | --- |
| Destinataires | Nombre d'utilisateurs ayant reçu un message par l'intermédiaire du canal sélectionné au cours de la période couverte par le rapport. |
| Taux de conversion (destinataires) | Calculé selon la formule : (Nombre de conversions) / (Nombre de destinataires) |
| Méthode d'attribution | Défini par la [méthode d'attribution](#attribution-methods) que vous avez sélectionnée lors de la création du rapport. Pour l'attribution de la dernière touche ou si plusieurs canaux sont sélectionnés, elle apparaît sous forme de [touches.](#terms-to-know) |
| Taux de conversion (méthode d'attribution) | Défini par la [méthode d'attribution](#attribution-methods) que vous avez sélectionnée lors de la création du rapport. Si plusieurs canaux sont sélectionnés, l'attributut par défaut est celui de la dernière touche. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si vous avez sélectionné des détails de ventilation pour les campagnes ou les toiles lors de l'implémentation [de votre rapport](#setting-up-your-report) (étape 5), vous pouvez cliquer sur <i class="fas fa-angle-down"></i> pour développer le tableau.

### Tunnel de conversion

Ce diagramme à barres montre les chiffres absolus pour chaque [événement d'engagement]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) en fonction du canal sélectionné. Le nombre de conversions sera défini en fonction de la méthode d'attribution sélectionnée.

Par défaut, toutes les campagnes et toiles sélectionnées sont affichées. Pour désélectionner une campagne ou un canvas, sélectionnez le nom de la campagne ou du canvas que vous souhaitez exclure. Pour plus de détails sur l'événement de fiançailles, vous pouvez survoler chaque barre.

Pour télécharger les données de la série temporelle, sélectionnez une option de téléchargement : PNG, JPEG, PDF, SVG ou CSV.

{% alert note %}
Ce graphique n'affiche les données que pour un seul canal à la fois. Utilisez le menu déroulant **Canal** sur le graphique pour sélectionner un seul canal.
{% endalert %}

![Graphique de l'entonnoir des conversions pour deux campagnes d'e-mail montrant des résultats similaires pour les e-mails délivrés, les e-mails ouverts, les e-mails cliqués et les conversions.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Évolution des conversions

Ce graphique chronologique comprend une représentation des conversions par campagne ou Canvas au fil du temps. Par défaut, toutes les campagnes et toiles sélectionnées sont affichées. Pour désélectionner une campagne ou un canvas, cliquez sur le nom de la campagne ou du canvas que vous souhaitez exclure.

Pour télécharger les données de la série chronologique, sélectionnez <i class="fas fa-bars"></i>, puis choisissez votre option de téléchargement. Les options disponibles sont PNG, JPEG, PDF, SVG ou CSV.

![Graphique des conversions dans le temps pour deux campagnes d'e-mail, montrant les conversions par jour.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Méthodes d'attribution

| Méthode d'attribution | Définition | Calcul du taux | Options spécifiques au canal |
| --- | --- | --- | --- |
| Lors d’une réception | Nombre total de conversions survenues après la réception du message | Calculé comme suit : (conversions uniques reçues) / (destinataires uniques). | {::nomarkdown}<ul><li>Lors de la réception d’un e-mail</li><li>Lors de la réception/distribution du SMS</li></ul>{:/} |
| Lors d’un envoi | Nombre total de conversions survenues après l'envoi du message | Calculé comme suit : (conversions d'envois uniques) / (destinataires uniques). | {::nomarkdown}<ul><li>Lors de l’envoi d’une notification push</li><li>Lors de l’envoi d’une carte de contenu</li><li>Lors de l’envoi d’un SMS</li></ul>{:/} |
| Lors d’une ouverture | Nombre total de conversions survenues après l'ouverture du message | Calculé comme suit : (conversions uniques ouvertes) / (destinataires uniques). | {::nomarkdown}<ul><li>Lors de l’ouverture d’un e-mail</li><li>Lors de l’ouverture d’une notification push</li></ul>{:/} |
| Lors d’un clic | Nombre total de conversions qui se sont produites clic de message | Calculé comme suit : (conversions par clics uniques) / (destinataires uniques). | {::nomarkdown}<ul><li>Lors d’un clic sur un e-mail</li><li>Après avoir cliqué sur la carte de contenu</li><li>Lors d’un clic sur un message in-app</li></ul>{:/} |
| Lors d’une impression | Nombre total de conversions qui ont eu lieu après une impression | Calculé comme suit : (conversions d'impressions uniques) / (destinataires uniques). | {::nomarkdown}<ul><li>Lors de l’impression d’un message in-app</li><li>Lors de l'impression de la carte de contenu</li></ul>{:/} |
| Lors du dernier contact | Les conversions qui accordent tout le crédit au dernier message touché ou cliqué pendant la fenêtre de conversion. | Calculé comme suit : (nombre de touches) / (destinataires uniques) | L'attribution de la dernière touche est automatiquement sélectionnée si plusieurs canaux sont ajoutés au rapport.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Termes à connaître

| Terme | Définition |
| --- | --- |
| Toucher | Une interaction physique ou un point de contact avec un message.<br><br>Les touches peuvent inclure :<br>{::nomarkdown}<ul><li>Clics sur e-mails</li><li>Ouverture de notification push</li><li>Carte de contenu cliquée</li><li>Clic sur le in-app Message</li><li>SMS Click</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
