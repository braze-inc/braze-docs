---
nav_title: "Campagnes inactives"
permalink: "/idle_campaigns/"
hidden: true
layout: dev_guide
---

# Campagnes inactives

> Cet article de référence explique le statut d’inactivité des campagnes et fournit des réponses aux questions fréquemment posées.

Lorsqu’une campagne n’envoie plus de messages, Braze lui attribue un statut inactif pour vous aider à trier et gérer votre liste de campagnes. En utilisant ce nouveau filtre, vous pouvez filtrer vos campagnes et voir lesquelles seront automatiquement arrêtées et la date d’arrêt associée. De manière continue, les campagnes inactives qui répondent aux critères suivants seront arrêtées :
 
- Les campagnes par événement et planifiées avec des dates de fin, sept jours après la date de fin
- Les campagnes ponctuelles planifiées, sept jours après la date d’envoi 
- Les campagnes par événement et planifiées sans date de fin qui n’ont pas envoyé de messages pendant un an
- Les campagnes déclenchées par API qui n’ont pas envoyées de messages pendant un an

Les campagnes seront arrêtées à la date d’arrêt par défaut la plus tardive et un jour après leur dernière date limite de conversion. Les envois résultant d’une variante gagnante ou personnalisée sont considérés comme des envois planifiés et seront arrêtés sept jours après l’envoi de la variante gagnante ou personnalisée. Toutes les campagnes seront arrêtées à 4 h UTC chaque jour, pour tous les utilisateurs de Braze.

Pour les campagnes récurrentes sans dates de fin, si un message est envoyé ou si la campagne est mise à jour, le compte à rebours d’un an avant d’arrêter la campagne sera réinitialisé. Lorsque les campagnes sont arrêtées, Braze informe les clients dans leur tableau de bord et par e-mail. Si vous souhaitez qu’une de vos campagnes inactives reste active, relancez-la, puis mettez à jour la date de fin de la campagne. Pour les campagnes inactives sans dates de fin, vous pouvez effectuer n’importe quelle modification pour maintenir la campagne active.

## Foire aux questions

#### À quelles campagnes cela s’applique-t-il ?

Cela s’appliquera aux campagnes qui répondent déjà aux critères précédemment énumérés, ainsi qu’à celles qui y répondront à l’avenir.

#### Comment savoir si une campagne est inactive ?

Les campagnes inactives seront affichées dans la liste des campagnes, dans la catégorie **Idle (Inactive)**. La date à laquelle la campagne sera arrêtée est indiquée à côté de chaque campagne. Les campagnes avec des dates de fin et des envois ponctuels deviendront inactives pendant sept jours avant leur arrêt automatique. Les campagnes qui n’ont pas envoyé de message pendant 11 mois deviendront inactives pendant un mois avant leur arrêt automatique. 

#### Que se passe-t-il si une campagne inactive est mise à jour ?

Si une campagne qui n’a pas envoyé de message est mise à jour, le compte à rebours de 12 mois sera réinitialisé. 

#### Qu’advient-il des campagnes qui n’ont pas envoyé de message pendant un an, mais qui ont une date de fin dans le futur ?

Nous arrêterons cette campagne sept jours après la date de fin.

#### Comment puis-je maintenir une campagne inactive active ?

Pour qu’une campagne ne soit plus inactive et s’assurer qu’elle reste active, mettez-la à jour afin qu’elle ne réponde pas aux critères d’inactivité ci-dessus. Consultez ce tableau pour connaître les étapes à suivre pour activer les campagnes inactives, en fonction de votre cas d’utilisation.

| Raison du statut de campagne inactive | Étapes pour rendre la campagne active |
| --- | --- |
| Les campagnes par événement avec des dates de fin, sept jours après la date de fin | Prolonger la date de fin |
| Les campagnes planifiées avec des dates de fin, sept jours après la date de fin | Prolonger la date de fin |
| Campagnes d'envoi uniques planifiées avec des dates de fin sept jours après la date de fin | Planifier un envoi futur |
| Les campagnes par événement (sans date de fin) qui n’ont pas envoyées de messages pendant un an | Envoyer un message ou apporter des modifications à la campagne | 
| Les campagnes planifiées (sans date de fin) qui n’ont pas envoyées de messages pendant un an | Envoyer un message ou apporter des modifications à la campagne | 
| Les campagnes déclenchées par API qui n’ont pas envoyées de messages pendant un an | Envoyer un message ou apporter des modifications à la campagne |
| Les campagnes seront arrêtées selon le critère de statut inactif le plus tardif et un jour après leur dernière date limite de conversion | Mettre à jour le critère ci-dessus ou prolonger la date limite de conversion, en fonction de ce qui se produit plus tard |
| Les envois résultant d’une variante gagnante ou personnalisée sont considérées comme des envois planifiés et seront désactivés sept jours après l’envoi de la variante gagnante ou personnalisée | Mettre à jour le moment où la variante sera envoyée vers une date ultérieure |
{: .reset-td-br-1 .reset-td-br-2}

#### Que se passe-t-il si je désire continuer à exécuter une campagne qui n’a pas envoyé de message ni été modifiée depuis plus de 12 mois ?

Pour continuer à exécuter une campagne inactive, relancez-la. Dans ce cas, le compte à rebours de 12 mois sera réinitialisé. 

#### Que se passe-t-il si je désire continuer à exécuter une campagne dont la date de fin est dépassée ?

Pour relancer une campagne dont la date de fin est dépassée, mettez à jour la date de fin de la campagne à la date souhaitée. 

#### Qui recevra des notifications par e-mail concernant les campagnes arrêtées ?

Par défaut, tous les utilisateurs disposant d’autorisations d’administrateur sont inscrits aux notifications par e-mail concernant les campagnes s’arrêtant automatiquement. Le créateur de la campagne sera toujours informé lors de son arrêt. Les utilisateurs peuvent gérer les préférences de notification par e-mail en allant dans **Company Settings > Notification Preferences (Paramètres de la société > Préférences de notification)**, puis en ajoutant ou en supprimant des destinataires de la notification **Campaign Automatically Stopped (Campagne arrêtée automatiquement)**.

#### Une action est-elle requise ?

Aucune action supplémentaire n’est requise. Veuillez contacter votre gestionnaire du succès des clients Braze si vous avez des questions.
