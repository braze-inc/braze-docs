---
nav_title: YouTube em HTML
article_title: YouTube em mensagens no app em HTML para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Este artigo de referência aborda como adicionar vídeos do YouTube em mensagens no app em HTML para seu aplicativo Android ou FireOS."
channel:
  - in-app messages

---

# YouTube em HTML

> O YouTube e outros conteúdos em HTML5 podem ser reproduzidos em mensagens no app em HTML. Isso requer que a aceleração de hardware seja ativada na atividade em que a mensagem no app está sendo exibida; consulte o [guia do desenvolvedor do Android](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) para obter mais detalhes. A aceleração de hardware está disponível apenas nas versões 11 e posteriores da API do Android.

A seguir, um exemplo de um vídeo do YouTube incorporado em um trecho de HTML:

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI">
        </iframe>
    </div>
</body>
```

