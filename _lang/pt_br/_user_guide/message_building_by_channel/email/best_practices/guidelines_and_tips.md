---
nav_title: Diretrizes para envio de e-mail
article_title: Diretrizes para envio de e-mail
page_order: 1
page_type: reference
description: "Este artigo aborda dicas e truques gerais que você deve ter em mente ao criar campanhas de e-mail para vários casos de uso e tópicos."
channel: email

---

# Diretrizes para o envio de e-mail

> Ao criar sua campanha de mensagens, é importante ter em mente como o envio de mensagens por e-mail é recebido por seus vários usuários e prestadores de serviço de e-mail (ESPs). 

Aqui estão algumas dicas rápidas que você deve ter em mente ao criar seu conteúdo:

- Ao formatar seu e-mail, use folhas de estilo inline como CSS.
- Para usar um modelo de e-mail para as versões móvel e desktop, mantenha a largura abaixo de 500 pixels.
- As imagens carregadas para o modelo de e-mail devem ter menos de 5 MB. Os formatos compatíveis incluem PNG, JPEG e GIF.
- Não defina alturas e larguras para imagens, pois isso causará espaço em branco desnecessário em um e-mail degradado.
- `div` não devem ser usadas, pois a maioria dos clientes de e-mail não aceita seu uso. Em vez disso, use tabelas aninhadas.
- Evite usar JavaScript porque ele não funciona com nenhum ESP.
- A Braze melhora o tempo de carregamento usando um CDN global para hospedar todas as imagens de e-mail.

### Implementação de texto alternativo

Como os filtros de spam procuram tanto uma versão em HTML quanto em texto simples de uma mensagem, utilizar alternativas de texto simples é uma ótima maneira de reduzir sua pontuação de spam. Além disso, o texto alternativo `(alt="")` pode servir para complementar e, em alguns casos, substituir as imagens incluídas no corpo do e-mail que podem ter sido filtradas pelo provedor de e-mail do usuário. Os leitores de tela anunciam o texto alternativo para explicar as imagens, portanto, essa é uma oportunidade de usar linguagem simples para fornecer informações importantes sobre uma imagem.

### Validação de e-mail

{% alert important %}
A validação é usada para endereços de e-mail do dashboard, endereços de e-mail do usuário final (seus clientes) e endereços de origem e de resposta de uma mensagem de e-mail.
{% endalert %}

A validação de e-mail é feita quando o endereço de e-mail de um usuário foi atualizado ou está sendo importado para o Braze via API, upload de CSV, SDK ou modificado no dashboard. Note que seus endereços de e-mail não podem incluir espaços em branco e, se forem enviados usando a API, os espaços em branco resultarão em um erro 400.

Os endereços de e-mail direcionados por meio dos servidores Braze devem ser validados de acordo com os padrões [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822). O Braze não aceita determinados caracteres e os reconhece como inválidos. Se um e-mail for devolvido, a Braze o marcará como inválido e o status da inscrição não será alterado. 

{% details Caracteres não aceitos fora dos padrões RFC %}
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

### Configuração dos endereços de origem e de resposta

Ao definir seus endereços no campo "de", confira se o domínio de e-mail do campo "de" corresponde ao domínio de envio (como `marketing.yourdomain.com`). Não fazer isso pode resultar em desalinhamento de SPF e DKIM. Todos os e-mails de resposta podem ser definidos para seu domínio raiz.

{% alert note %}
A codificação Unicode não é compatível com os endereços "from".
{% endalert %}

### Verificação de detalhes HTML

Lembre-se de que algumas tags e atribuições HTML não são permitidas, pois podem permitir a execução de códigos maliciosos no navegador.

Confira as seguintes listas de tags e atribuições HTML que não são permitidas em seus e-mails:
{% details Expandir para tags HTML não permitidas %}
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

{% details Expandir para atribuições HTML não permitidas %}
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



