---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre a biblioteca de mídia
page_order: 5
page_type: FAQ
tool: Media
description: "Este artigo fornece respostas a perguntas frequentes sobre a biblioteca de mídia na Braze."

---

# Perguntas frequentes

> Esta página fornece respostas a perguntas frequentes sobre a biblioteca de mídia na Braze.

### Há limites de armazenamento para imagens na biblioteca de mídia?

Não, não há limites de armazenamento para ativos na biblioteca de mídia. No entanto, há limites de tamanho para ativos (máximo de 5 MB).

### Existem datas de expiração para ativos que passaram por upload?

Não, os ativos enviados para a biblioteca de mídia serão mantidos durante toda a duração do seu contrato com a Braze.

### Posso fazer upload de ativos de vídeo?

Não, a biblioteca de mídia não é compatível com arquivos de vídeo. Recomendamos que você os hospede externamente ou em uma plataforma como o YouTube.

### Posso cortar todos os tipos de imagem?

Não, a biblioteca de mídia não é compatível com o corte de imagens GIF.

### Como faço para cortar uma imagem existente?

É possível recortar uma imagem existente selecionando a imagem na biblioteca de mídia e clicando em **Crop & Save New Image**. 

![Prévia da imagem da biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Em seguida, você será redirecionado para um criador de cortes, onde poderá selecionar o tipo de proporção e editar o nome da nova imagem. Quando você selecionar **Save**, a nova imagem poderá ser usada.

![Janela para cortar e salvar a imagem da biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Minha imagem continua expirando quando tento fazer upload. O que posso fazer?

Isso pode acontecer por vários motivos, mas uma solução comum é certificar-se de que sua imagem esteja otimizada antes de tentar fazer upload. Isso significa passar sua imagem por um otimizador de imagens, como o [ImageOptim](https://imageoptim.com/mac).

Além disso, se sua imagem foi criada no Photoshop (ou em um software semelhante) e tem muitas camadas, mesclar e reduzir o número de camadas também pode ajudar.

### Vejo um "Erro inesperado" ao fazer upload de uma imagem, mesmo ela tendo menos de 5 MB e estando em um formato compatível. O que há de errado?

Isso pode acontecer por dois motivos principais:

1. **Metadados inválidos no arquivo:** O software que a Braze usa para processar imagens pode rejeitar arquivos com metadados inválidos ou incompatíveis. Em alguns casos, o arquivo também pode ser processado de uma forma que ultrapasse o limite de 5 MB. Tente usar uma imagem diferente (por exemplo, reexporte ou salve novamente a imagem no seu editor de imagens) ou uma imagem de outra origem.
2. **Caracteres especiais no nome do arquivo:** Nomes de arquivo que contêm caracteres especiais (como `&` ou `%`) podem causar falha no upload. Renomeie o arquivo para usar apenas letras, números, hifens ou underscores e tente fazer upload novamente.

### Por que não posso fazer upload de qualquer imagem que eu queira nos criadores de push?

Isso ocorre porque a maioria dos criadores tem restrições quanto ao tamanho da proporção da imagem permitida.