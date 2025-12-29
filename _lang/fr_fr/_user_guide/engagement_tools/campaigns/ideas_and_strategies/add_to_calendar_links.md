---
nav_title: Liens vers le calendrier
article_title: Liens vers le calendrier
page_order: 1
page_type: tutorial
description: "Cet article explique comment inclure un lien d'ajout au calendrier dans vos campagnes d'e-mailing."
channel: email

---

# Liens vers le calendrier

> Lorsque vous faites la promotion d'un événement, d'une vente ou d'un rendez-vous, vous pouvez aider les utilisateurs à enregistrer facilement l'événement dans leur calendrier en ajoutant un lien "Ajouter au calendrier" à vos e-mails.

Pour ce faire, rédigez votre e-mail et déterminez l'emplacement de vos liens. Ajoutez ensuite deux options : une pour le calendrier Google et une pour les autres calendriers (tels que iCal ou Outlook). Par exemple, "Ajouter au calendrier Google" et "Ajouter à iCal ou Outlook".

!Dialogue de lien lors de l'ajout d'un lien dans le tableau de bord. L'onglet "Informations sur le lien" est sélectionné et le texte est défini sur "Ajouter au calendrier Google".]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## Format de l'URL

Ajoutez l'URL suivante à vos liens, en remplaçant les marqueurs substitutifs. La seule différence entre ces deux URL est que Google Calendar a besoin d'un paramètre supplémentaire : `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Remplacez les éléments suivants :

- `EVENT_SUBJECT`: Titre de l'événement
- `EVENT_LOCATION`: Emplacement/localisation de l'événement
- `START_TIME`: L'heure de début de l'événement au format ISO 8601 (AAAA-MM-JJTHH:MM:SSZ) en UTC
- `END_TIME`: L'heure de fin de l'événement au format ISO 8601 (AAAA-MM-JJTHH:MM:SSZ) en UTC
- `EVENT_DESCRIPTION`: Description de l'événement

Remplacez les espaces par le code d'échappement HTML `%20`. Par exemple, le sujet de "Meet Braze" serait "Meet%20Braze".

Voici un exemple d'URL "Ajouter au calendrier Google" :

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Paramètres supplémentaires

Les paramètres suivants sont facultatifs et peuvent être utilisés pour définir des aspects supplémentaires d'un événement.

- **Nom de l'organisateur :** `&organizer=name`
- **Joignez l'URL de l'événement :** `&attach=http://www.example.com/`
- **Durée :** `duration=30M` comme alternative à l'heure de fin de l'événement (dtend), spécifiez une durée comme 1H ou 30M
- **Heure de l'alarme de rappel, en minutes :** `&reminder=15`
- **Manifestation toute la journée :** `&allday=1`
- **UID :** paramètre facultatif permettant de coder en dur l'identifiant unique de l'événement, ce qui permet à certaines applications de calendrier de mettre à jour l'événement au fil du temps. La chaîne de caractères @ics.agical.io est automatiquement ajoutée à la valeur.

Vous pouvez également ajouter des paramètres supplémentaires pour les événements récurrents :
- **Événements hebdomadaires :** `&recur=weekly`
- **Événements mensuels :** `&recur=monthly`
- **Fin de la récurrence :** `&recuruntil=END_DATE` où `END_DATE` est la date et l'heure de la fin de la récurrence au format ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC.

## Comportement du lien

Lorsqu'un utilisateur clique sur le lien, les calendriers transforment automatiquement les horodatages UTC dans les URL pour refléter le fuseau horaire de l'utilisateur défini dans son calendrier.

Par exemple, si vous ouvrez le lien "Ajouter à Google Calendar" et que votre calendrier est réglé sur CST, l'heure de l'événement sera pré-remplie en fonction de ce que 15h UTC est en CST (10h).

### Calendrier Google

Lorsque vous cliquez dessus, Google Agenda s'ouvre dans un nouvel onglet ou une nouvelle fenêtre avec les détails de l'événement pré-remplis dans l'invitation et prêts à être enregistrés par l'utilisateur. Cela se produit à la fois sur les téléphones mobiles et les ordinateurs de bureau.

\![Dialogue de Google Calendar pour ajouter un événement avec les détails de l'événement ajoutés et prêts à être enregistrés.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal ou Outlook

Lorsque vous cliquez sur le bureau, un fichier ICS est téléchargé. L'utilisateur doit ensuite ouvrir le fichier ICS, qui ouvrira iCal ou Outlook et invitera l'utilisateur à ajouter l'événement à son calendrier.

\![Calendrier iCal avec une boîte de dialogue pour l'ajout d'un nouvel événement, qui invite l'utilisateur à sélectionner un calendrier et à confirmer.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

\![Calendrier iCal avec l'événement ajouté.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

Sur mobile, les utilisateurs doivent appuyer sur le lien et le maintenir enfoncé, ce qui les invite à l'ajouter à leur calendrier.

\![iOS pop-up lorsque vous appuyez et maintenez sur un lien de calendrier, qui comprend un bouton pour "Ajouter au calendrier".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Pour plus d'informations, reportez-vous à
* [Créer des événements pour le calendrier Google](https://developers.google.com/calendar/api/guides/create-events)
* [Créer un lien Ajouter au calendrier dans un message e-mail](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)


