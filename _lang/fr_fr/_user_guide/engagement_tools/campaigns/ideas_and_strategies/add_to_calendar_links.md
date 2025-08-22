---
nav_title: Liens d’ajout au calendrier
article_title: Liens d’ajout au calendrier
page_order: 1
page_type: tutorial
description: "Cet article décrit la manière d’intégrer un lien d’ajout au calendrier dans vos campagnes par e-mail."
channel: email

---

# Liens d’ajout au calendrier

> Lorsque vous mettez un événement en avant, tel qu’une vente ou un rendez-vous, vous pouvez aider vos utilisateurs à l’enregistrer facilement dans leur calendrier en ajoutant u lien « Ajouter au calendrier » dans vos e-mails.

Pour ce faire, rédigez votre e-mail et déterminez où vous voulez mettre vos liens. Ajoutez ensuite deux options : une vers Google Agenda et une vers d’autres calendriers (tels que iCal ou Outlook). Par exemple, « Ajouter à Google Agenda » et « Ajouter à iCal ou Outlook ».

![Dialogue du lien en ajoutant un lien dans le tableau de bord. L'onglet "Informations sur le lien" est sélectionné et le texte est défini sur "Ajouter au calendrier Google".]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## Format d’URL

Ajoutez l’URL suivante à vos liens en remplaçant les marques substitutives. La seule différence entre ces deux URL est que Google Agenda nécessite un paramètre supplémentaire : `&format=gcal`.

{% tabs %}
{% tab Calendrier Google %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal ou Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Remplacez les éléments suivants :

- `EVENT_SUBJECT` : Titre de l’événement
- `EVENT_LOCATION` : Emplacement de l’événement
- `START_TIME` : Le début de l’événement au format ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC
- `END_TIME` : La fin de l’événement au format ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC
- `EVENT_DESCRIPTION` : Description de l’événement

Remplacez tous les espaces avec le code d’échappement HTML `%20`. Par exemple, un sujet du type « Rencontrez Braze » serait « Rencontrez%20Braze ».

Voici un exemple d’une URL « Ajouter à Google Agenda » :

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Paramètres supplémentaires

Les paramètres suivants sont facultatifs et peuvent être utilisés pour définir des aspects supplémentaires d’un événement.

- **Nom de l'organisateur :** `&organizer=name`
- **Joindre l'URL de l'événement :** `&attach=http://www.example.com/`
- **Durée :** `duration=30M`, comme alternative à l'heure de fin de l'événement (dtend), spécifiez une durée comme 1H ou 30M
- **Heure de l'alarme de rappel, en minutes :** `&reminder=15`
- **Événement sur toute la journée :** `&allday=1`
- **UID :** paramètre facultatif permettant de coder en dur l’identifiant unique de l’événement, ce qui permet à certaines applications de calendrier de mettre à jour l’événement au fil du temps. La chaîne de caractères @ics.agical.io est automatiquement ajoutée à la valeur.

Vous également pouvez ajouter des paramètres supplémentaires pour les événements récurrents :
- **Événements hebdomadaires :** `&recur=weekly`
- **Événements mensuels :** `&recur=monthly`
- **Fin de la récurrence :** `&recuruntil=END_DATE` où `END_DATE` est la date et l'heure de la fin de la récurrence au format ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC.

## Comportement du lien

Lorsqu’un utilisateur clique sur le lien, les calendriers transforment automatiquement les horodatages UTC dans les URL pour prendre en compte le fuseau horaire de l’utilisateur défini dans leur calendrier.

Par exemple, si vous ouvre le lien d’illustration « Ajouter à Google Agenda » et que votre calendrier est paramétré en UTC, l’heure de l’événement se remplira en fonction de ce que représente 15 h UTC en CST (10 h).

### Google Agenda

Lorsque vous cliquez dessus, Google Agenda s'ouvre dans un nouvel onglet ou une nouvelle fenêtre avec les détails de l'événement pré-remplis dans l'invitation et prêts à être enregistrés par l'utilisateur. Ceci se produit sur mobile et ordinateur.

![Boîte de dialogue de Google Calendar pour ajouter un événement avec les détails de l'événement ajoutés et prêts à être enregistrés.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal ou Outlook

Lorsqu’il est cliqué sur un ordinateur, un fichier ICS est téléchargé. L’utilisateur doit alors ouvrir le fichier ICS ce qui ouvrira iCal ou Outlook et demandera à l’utilisateur d’ajouter l’événement à leur calendrier.

![Calendrier iCal avec une boîte de dialogue pour l'ajout d'un nouvel événement, qui invite l'utilisateur à sélectionner un calendrier et à confirmer.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![Calendrier iCal avec l'événement ajouté.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

Sur un mobile, les utilisateurs doivent appuyer et maintenir le lien, ce qui leur demande de l’ajouter dans leur calendrier.

![Fenêtre contextuelle d'iOS lorsque vous appuyez sur un lien de calendrier et le maintenez enfoncé, qui comprend un bouton pour "Ajouter au calendrier".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Pour plus d'informations, reportez-vous à :
* [Créer des événements pour le calendrier Google](https://developers.google.com/calendar/api/guides/create-events)
* [Créer un lien Ajouter au calendrier dans un message e-mail](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)


