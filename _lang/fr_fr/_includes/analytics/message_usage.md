# Tableau de bord de l'utilisation des messages

> Le tableau de bord de l'utilisation des messages fournit des informations en libre-service sur l'utilisation de vos crédits SMS, RCS et WhatsApp pour une vue d'ensemble de l'utilisation historique et actuelle par rapport aux allocations contractuelles. Ces informations peuvent réduire votre confusion et vous aider à faire des ajustements pour prévenir les risques de dépassement.

Le tableau de bord de l'**utilisation des messages** est divisé en trois sections :
- [Aperçu de l'utilisation du crédit](#credit-usage-overview)
- [SMS/MMS](#smsmms) 
- [WhatsApp](#whatsapp)

Accédez au tableau de bord en sélectionnant **Paramètres** > **Facturation** > **Utilisation des messages**.

## Aperçu de l'utilisation des crédits de messages

L'**aperçu de l'utilisation des crédits de messages** donne un aperçu de l'utilisation de tous les canaux qui utilisent des crédits. Vous pouvez voir où vous en êtes par rapport à votre crédit global, et trouver des détails sur votre contrat actif et votre durée de contrat.

Cette page s'affiche si vous bénéficiez d'un contrat d'envoi de messages. Les canaux qui utilisent des crédits de messages sont indiqués dans l'**aperçu des contrats de crédits.**

{% alert note %}
Si vous avez acheté WhatsApp mais que vous n'avez pas de contrat de crédits de messages, vous verrez toujours la consommation de crédits pour WhatsApp car c'est ainsi que les anciens contrats WhatsApp sont facturés. Cela diffère des anciens SMS, qui ne consomment des crédits que lorsque vous avez souscrit un contrat de crédits de messages.
{% endalert %}

Les données de l'**aperçu de l'utilisation des crédits de messages** sont limitées à la période du contrat, qui est affichée dans l'**aperçu du contrat de crédits.** Vous ne pouvez pas filtrer sur une plage de dates en dehors de la **période des crédits**.

### Envoi de messages en cas de dépassement du contrat

Le graphique de l'**utilisation des crédits de messages sur le contrat** montre votre utilisation sur la période sélectionnée. La granularité de ce graphique dépend de l'horizon temporel que vous avez choisi. Exporter les options d'exportation en sélectionnant le menu dans le coin supérieur droit du graphique.

![Message Credits Usage Overview tableau de bord avec des sections pour l'utilisation des crédits, l'aperçu du contrat de crédit, et la consommation de crédit sur le contrat.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}){: style="max-width:70%;"}

## SMS, MMS et RCS

**SMS/MMS/RCS L'utilisation des crédits** montre la répartition de l'utilisation des canaux SMS, MMS et RCS. Les colonnes du tableau de données exigent généralement que vous ayez acheté des crédits de messages (bien que Braze prenne encore temporairement en charge les anciens modèles de facturation), et les colonnes **Taux de crédit** et **Crédits** indiquent le taux de pays respectif et les crédits consommés. En outre, les tuiles de haut niveau indiquent la consommation totale de SMS et, le cas échéant, de MMS pour la plage de dates sélectionnée.

Des filtres sont disponibles, vous permettant de filtrer par **pays** ou par type de SMS et RCS.

![SMS/MSS/RCS Crédits Utilisation avec des tuiles pour les données de haut niveau et une section pour la consommation par compte.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}){: style="max-width:70%;"}

Contrairement à l'**aperçu de l'utilisation des crédits de messages**, cette section contient les données historiques des périodes contractuelles précédentes. 

{% alert note %}
Il est possible de sélectionner une plage de dates contenant à la fois des utilisations sans crédits et des utilisations avec crédits de messages. Dans ce cas, la consommation qui s'est produite en dehors des crédits d'envoi de messages affichera `—` (null) dans les colonnes **Rapport de crédit** et **Crédits.**
{% endalert %}

![SMS/MMS/RCS Tableau d'utilisation des crédits avec des valeurs nulles.]({% image_buster /assets/img/app_settings/sms_table_null3.png %}){: style="max-width:70%;"}

## WhatsApp

L'**utilisation des crédits WhatsApp** montre la répartition de l'utilisation du canal WhatsApp. Les tuiles affichent l'utilisation totale du crédit WhatsApp, qui peut être décomposée dans la section **Utilisation par compte** en appliquant des filtres pour limiter les résultats du tableau de données à un espace de travail spécifique.

### Filtres

Vous pouvez filtrer vos données par :
- Pays
- Compte WhatsApp Business
- Espace de travail Braze
- Type de catégorie de conversation
- Région

![Utilisation des crédits WhatsApp avec une tuile pour le total des crédits consommés et un tableau d'utilisation par compte.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}){: style="max-width:70%;"}

## Choses à savoir

{% alert important %}
Les données présentées dans le tableau de bord de l' **utilisation des messages** se situent au niveau du contrat et ne se rapportent pas à une entreprise ou à un espace de travail particulier. Ces données reflètent l'utilisation de tous les espaces de travail de votre tableau de bord, et potentiellement de tous les tableaux de bord (si vous en avez plusieurs).
{% endalert %}

- Les données sous-jacentes sont fournies quotidiennement, les tableaux de données étant actualisés à 3 heures, 9 heures, 12 heures et 18 heures (heure de l'Est). 
- Braze suit la méthode d'arrondi standard : les chiffres sont arrondis au dixième le plus proche.