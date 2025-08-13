---
nav_title: Recommandations pour les e-mails
article_title: Recommandations pour les e-mails
page_order: 1
page_type: reference
description: "Le présent article couvre les conseils généraux et les astuces à garder en tête lorsque vous créez des campagnes par e-mail pour différents cas d’utilisation et différents sujets."
channel: email

---

# Recommandations pour les e-mails

> Lorsque vous créez votre campagne par e-mail, il est important de garder à l’esprit comment vos messages vont être reçus par vos divers utilisateurs et par les ESP (fournisseurs de services d'e-mail). 

Voici quelques conseils rapides à garder à l’esprit en construisant votre contenu :

- Lors du formatage de votre e-mail, utilisez les feuilles de style inline en tant que CSS.
- Pour utiliser un modèle d’e-mail sur mobile et PC en même temps, spécifiez une largeur inférieure à 500 pixels.
- Les images chargées dans le modèle d'e-mail doivent être inférieures à 5 Mo. Les formats pris en charge incluent PNG, JPEG et GIF.
- Ne définissez pas de hauteurs et de largeurs pour les images, car cela générera un espace blanc inutile dans un e-mail dégradé.
- Les balises `div` ne doivent pas être utilisées car la plupart des clients e-mail ne les prennent pas en charge. Utilisez plutôt des tables imbriquées.
- Évitez d’utiliser Javascript parce qu’il ne fonctionne avec aucun ESP.
- Braze améliore les temps de chargement en utilisant un CDN global pour héberger toutes les images des e-mails.

### Utiliser du texte alternatif

Comme les filtres anti-spam surveillent à la fois la version HTML et la version texte brut d’un message, l’utilisation d’alternatives en texte brut est un excellent moyen de réduire votre score de spam. De plus, le texte alternatif `(alt="")` peut compléter, voire remplacer les images incluses dans le corps de votre e-mail, qui peuvent avoir été filtrées et supprimées par le fournisseur d’e-mail d’un utilisateur. Les lecteurs d’écran dévoilent le texte alternatif pour expliquer les images. C’est donc l’occasion d’utiliser un langage simple pour fournir des informations clés sur une image.

### Validation de l’e-mail

{% alert important %}
La validation est utilisée pour les adresses e-mail du tableau de bord, les adresses e-mail de l’utilisateur final (vos clients), ainsi que les adresses de réponse et de réponse effectuées par e-mail.
{% endalert %}

La validation de l'email est effectuée lorsqu'une adresse email utilisateur a été mise à jour ou est importée dans Braze via l'API, le téléchargement CSV, le SDK ou modifiée dans le tableau de bord. Prenez en compte le fait que les adresses e-mail ne peuvent pas comprendre d’espace et que, si elles sont envoyées à l’aide de l’API, les espaces entraîneront une erreur 400.

Les adresses e-mail ciblées via les serveurs Braze doivent être validées selon les normes [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822), Braze n'accepte pas certains caractères et les reconnaît comme invalides. Si un e-mail est renvoyé, Braze marque l’adresse e-mail comme non valide et le statut d’abonnement n’est pas modifié. 

{% details Caractères non acceptés en dehors des normes RFC %}
- *
- /
- ?
- !
- $
- #
- %
- ^
- &
- (
- )
- {
- }
- [
- ]
- ~
- , 
{% enddetails %}

### Définir les adresses « De » et « Répondre à »

Lorsque vous définissez vos adresses d’expéditeur, assurez-vous que votre domaine d’e-mail « De » correspond à votre domaine d’envoi (par exemple, `marketing.yourdomain.com`). Le non-respect de cette consigne peut entraîner un mauvais alignement SPF et DKIM. Tous les e-mails de réponse peuvent être définis dans votre domaine racine.

{% alert note %}
Le codage Unicode n'est pas pris en charge dans les adresses "from".
{% endalert %}

### Vérification des détails HTML

N’oubliez pas que certaines balises et attributs HTML ne sont pas autorisés car ils peuvent potentiellement permettre d’exécuter du code malveillant dans le navigateur.

Consultez les listes suivantes pour voir les balises et les attributs HTML qui ne sont pas autorisés dans vos e-mails :
{% details Développer pour les balises HTML non autorisées %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `<iframe>`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details Développer pour les attributs HTML non autorisés %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}



