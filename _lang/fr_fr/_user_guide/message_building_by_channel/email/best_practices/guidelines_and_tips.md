---
nav_title: "Lignes directrices pour l'e-mail"
article_title: "Lignes directrices concernant l'e-mail"
page_order: 1
page_type: reference
description: "Cet article présente des conseils généraux et des astuces à garder à l'esprit lorsque vous créez des campagnes d'e-mail pour différents cas d'utilisation et sujets."
channel: email

---

# Lignes directrices pour l'e-mail

> Lorsque vous créez votre campagne d'e-mailing, il est important de garder à l'esprit la façon dont vos messages sont reçus par vos différents utilisateurs et fournisseurs de services d'e-mailing (ESP). 

Voici quelques conseils rapides à garder à l'esprit lorsque vous créez votre contenu :

- Lors de la mise en forme de votre e-mail, utilisez des feuilles de style en ligne (CSS).
- Pour utiliser un seul modèle d'e-mail pour les versions mobile et de bureau, veillez à ce que la largeur soit inférieure à 500 pixels.
- Les images téléchargées dans le modèle d'e-mail doivent être inférieures à 5 Mo. Les formats pris en charge sont PNG, JPEG et GIF.
- Ne définissez pas de hauteurs et de largeurs pour les images, car cela entraînerait des espaces blancs inutiles dans un e-mail dégradé.
- `div` ne doivent pas être utilisées car la plupart des clients d'e-mail ne les prennent pas en charge. Utilisez plutôt des tableaux imbriqués.
- Évitez d'utiliser JavaScript car il ne fonctionne avec aucun ESP.
- Braze améliore les temps de chargement en utilisant un réseau de diffusion de contenu global pour héberger toutes les images des e-mails.

### Mise en œuvre d'un texte alternatif

Étant donné que les filtres anti-spam recherchent à la fois une version HTML et une version en texte brut d'un message, l'utilisation d'alternatives en texte brut est un excellent moyen de réduire votre score anti-spam. En outre, le texte alternatif `(alt="")` peut servir à compléter et, dans certains cas, à remplacer les images incluses dans le corps de votre e-mail qui ont pu être filtrées par le fournisseur d'accès à l'e-mail de l'utilisateur. Les lecteurs d'écran annoncent un texte alt pour expliquer les images. C'est donc l'occasion d'utiliser un langage clair et simple pour fournir des informations clés sur une image.

### Validation de l'e-mail

{% alert important %}
La validation est utilisée pour les adresses e-mail du tableau de bord, les adresses e-mail des utilisateurs finaux (vos clients) et les adresses de départ et de destination d'un message e-mail.
{% endalert %}

La validation de l'e-mail est effectuée lorsque l'adresse e-mail d'un utilisateur a été mise à jour ou est importée dans Braze via l'API, le téléchargement CSV, le SDK ou modifiée dans le tableau de bord. Notez que vos adresses e-mail ne peuvent pas contenir d'espaces blancs et que si vous les envoyez à l'aide de l'API, les espaces blancs entraîneront une erreur 400.

Les adresses e-mail ciblées via les serveurs de Braze doivent être validées selon les normes [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822). Braze n'accepte pas certains caractères et les reconnaît comme invalides. Si un e-mail est rejeté, Braze marque l'e-mail comme invalide et le statut de l'abonnement n'est pas modifié. 

{% details Unaccepted characters outside of RFC standards %}
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

### Définition des adresses de départ et de destination des réponses

Lorsque vous définissez vos adresses "from", assurez-vous que votre domaine d'e-mail "from" correspond à votre domaine d'envoi (tel que `marketing.yourdomain.com`). Si vous ne le faites pas, vous risquez d'avoir un décalage entre SPF et DKIM. Tous les e-mails de réponse peuvent être définis sur votre domaine racine.

{% alert note %}
Le codage Unicode n'est pas pris en charge dans les adresses "from".
{% endalert %}

### Vérification des détails HTML

Gardez à l'esprit que certaines étiquettes et certains attributs HTML ne sont pas autorisés car ils peuvent potentiellement laisser un code malveillant s'exécuter dans le navigateur.

Consultez les listes suivantes pour connaître les tags et attributs HTML interdits dans vos e-mails :
{% details Expand for disallowed HTML tags %}
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

{% details Expand for disallowed HTML attributes %}
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



