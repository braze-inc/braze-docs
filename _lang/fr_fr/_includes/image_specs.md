{% if include.variable_name == "image behavior" %}


| Disposition | Comportement |
| --- | --- |
| Image et texte | Les images hautes ou étroites sont réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
| Image uniquement | Le message sera redimensionné pour s’adapter à la plupart des tailles d'image. |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "payload size" %}

Nous recommandons les tailles de charge utile suivantes :

| Système d'envoi de messages | Charge utile recommandée |
| --- | --- |
| iOS (avant iOS 8) | 0,256 Ko |
| iOS (après iOS 8) | 2 Ko |
| Android (FCM) | 4 Ko |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

Les messages in-app modaux sont conçus pour s’adapter le mieux possible aux proportions de l’appareil, tout en restant fidèle à la taille et aux rapports de l’image ou du texte de votre choix pour votre message.

Bien qu'il n'y ait pas de limite au nombre de caractères de texte que vous pouvez inclure dans un message in-app (ainsi que dans les boutons, le titre, le corps principal et autres), nous modérons le nombre de caractères de texte que vous utilisez. Un texte trop long obligera les utilisateurs à développer et à faire défiler le message.

Tous les messages in-app ont une taille d'image recommandée de 500 Ko, une taille d'image maximale de 5 Mo, et prennent en charge les types de fichiers PNG, JPEG et GIF.

{% tabs %}
{% tab Portrait %}

| Type | Rapport hauteur/largeur | Qualité de l’image | Remarques |
| --- | --- | --- | --- |
| Portrait plein écran avec texte | 6:5 | Haute résolution 1200 x 1000 px <br>Résolution minimale 600 x 500 px | L’image peut être rognée de tous les côtés, mais elle occupera toujours la moitié supérieure de la fenêtre. |
| Portrait plein écran (image seule, avec ou sans boutons) | 3:5 | Haute résolution 1200 x 2000 px <br> Résolution minimale 600 x 1000 px | Sur les appareils grand format, l’image peut être rognée sur les bords gauche et droit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Paysage %}

| Type | Rapport hauteur/largeur | Qualité de l’image | Remarques |
| --- | --- | --- | --- |
| Paysage plein écran avec texte | 10:3 | Haute résolution 2000 x 600 px <br>Résolution minimale 1000 x 300 px | L’image peut être rognée de tous les côtés, mais elle occupera toujours la moitié supérieure de la fenêtre. |
| Paysage plein écran (image seule, avec ou sans boutons) | 5:3 | Haute résolution 2000 x 600 px <br> Résolution minimale 1000 x 600 px | Sur les appareils grand format, l’image peut être rognée sur les bords gauche et droit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Contextuel %}

| Type | Rapport hauteur/largeur | Qualité de l’image | Remarques |
| --- | --- | --- | --- |
| Fenêtre contextuelle | 1:1 | Haute résolution 150 x 150 px <br> Résolution minimale 50 x 50 px | Les images de différents rapports hauteur/largeur seront insérées dans un conteneur d’images carré, sans rognage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Fenêtre modale %}

| Type | Rapport hauteur/largeur | Qualité de l’image | Remarques |
| --- | --- | --- | --- |
| Modale (image seulement) | 1:1 | Résolution maximale recommandée : 1200 x 2000 px <br> Résolution minimale : 600 x 600 px | Le message sera redimensionné pour s’adapter à la plupart des tailles d'image. La résolution maximale recommandée a un rapport hauteur/largeur de 3:5, ce qui peut ne pas donner des résultats optimaux. Bien que les images plus grandes soient utilisables, elles peuvent entraîner des temps de chargement plus longs. <br> Le rapport hauteur/largeur idéal pour les images est de 1:1\. Le non-respect de ce rapport peut déclencher un avertissement lors du téléchargement. Cet avertissement est une suggestion pour de meilleurs résultats et n'empêche pas le téléchargement d'images plus grandes. |
| Fenêtre modale avec texte | 29:10 | Haute résolution 1450 x 500 px <br> Résolution minimale 600 x 205 px | Les images hautes seront réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Type de message | Longueur maximale du message | Longueur maximale du titre |
| --- | --- | --- |
| Écran de verrouillage iOS | 175 caractères | 43 caractères |
| Notification iOS | 175 caractères | 43 caractères |
| Alerte en bannière iOS | 85 caractères | 43 caractères |
| Écran de verrouillage Android | 49 caractères | 43 caractères |
| Tiroir de notification Android | 597 caractères | 43 caractères |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

La taille recommandée pour toutes les images push est de 500 KB.

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Type d’image</th>
      <th>Rapport hauteur/largeur</th>
      <th>Pixels maximums</th>
      <th>Taille maximale de l'image</th>
      <th>Types de fichier</th>
      <th>Remarques</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (recommandé)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>À compter du mois de janvier 2020, les notifications push enrichies pour iOS peuvent gérer des images de 1 038 x1 038 px tant que leur taille est inférieure à 10 Mo, mais nous recommandons d’utiliser des fichiers aussi petits que possible. En pratique, l’envoi de fichiers volumineux peut entraîner une surcharge inutile du réseau et rendre les échecs de téléchargement plus courants.<br><br>Pour plus d'informations, consultez la rubrique <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">Notifications enrichies pour iOS</a>.</td>
    </tr>
    <tr>
      <td>Icône push Android</td>
      <td>1:1</td>
      <td>N/A</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Image de notification élargie sous Android</td>
      <td>2:1</td>
      <td><b>Petites :</b><br>512 x 256<br><br><b>Intermédiaire :</b><br>1024 x 512<br><br><b>Grandes :</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td>Utilisé dans les <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">notifications riches d'Android</a>.</td>
    </tr>
    <tr>
      <td>Image d'inclinaison Android</td>
      <td>3:2</td>
      <td>N/A</td>
      <td>S.O.</td>
      <td>PNG, JPEG</td>
      <td>Pour plus de détails, consultez la section <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Notifications push d’images insérées pour Android</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 role="presentation"}

{% endif %}

{% if include.variable_name == "email" %}

| Type d'e-mail | Propriétés maximales recommandées |
| --- | --- | 
| Texte uniquement | 25 KB |
| Texte avec images | 60 KB |
| Largeur de l'e-mail | 600 px |
{: .reset-td-br-1 .reset-td-br-2}

| Spécifications des images | Propriétés maximales recommandées |
| --- | --- | 
| Taille | 5 MB |
| Largeur | En-tête : 600 px<br>Corps : 480 px |
| Types de fichier | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2}

| Spécifications du texte | Propriétés maximales recommandées |
| --- | --- | 
| Longueur de la ligne d'objet | 35 caractères<br>6 à 10 mots |
| `"From: Name"` longueur | 25 caractères |
| Longueur du pré-en-tête | 85 caractères |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "content cards" %}

| Type de carte | Rapport hauteur/largeur     | Qualité de l’image       |
| --------- | ---------------- | ------------------- |
| Classique   | Format 1:1 | 60 x 60 px        |
| Avec légende | Format 4:3 | Largeur minimale de 600 px |
| Bannière    | N'importe quel rapport hauteur/largeur | Largeur minimale de 600 px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Pour plus d'informations, reportez-vous aux [informations créatives des cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

{% endif %}
