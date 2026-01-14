---
nav_title: Mensagens da direita para a esquerda
article_title: Criando mensagens da direita para a esquerda
page_order: 1
alias: /right_to_left_messages/
page_type: reference
description: "Esta página aborda as práticas recomendadas para a criação de mensagens no Braze que são lidas da direita para a esquerda."
---

# Criação de mensagens da direita para a esquerda

> A aparência final das mensagens da direita para a esquerda depende muito de como os provedores de serviços (como Apple, Android e Google) as processam. Esta página aborda as práticas recomendadas para a criação de mensagens da direita para a esquerda, de modo que suas mensagens sejam exibidas com a maior precisão possível.

## Aparência da mensagem

Ao criar uma mensagem da direita para a esquerda, tenha em mente o seguinte:

- **Aparência no painel de controle do Braze:** Quando uma mensagem aparece no dispositivo de um usuário, sua aparência é amplamente determinada pelo sistema operacional e pelas configurações de idioma do dispositivo, o que significa que o que você vê no painel nem sempre é 100% preciso.
- **Aparência no dispositivo:** A Apple e o Android têm um controle significativo sobre como as mensagens são processadas, enquanto os provedores de serviços de e-mail (ESPs) têm algum controle. A personalização de e-mail em HTML no Braze pode ser mais flexível; no entanto, a mesma mensagem ainda pode ser renderizada de forma diferente em dispositivos diferentes com base nas configurações do usuário.

Além disso, verifique a pontuação e os emojis para determinar se sua mensagem está sendo renderizada de forma padrão ou da direita para a esquerda.

| Renderização ocidental padrão | Renderização da direita para a esquerda |
|------------------|------------------------|
| Exibe o ponto de exclamação e o emoji no **final** das frases. | Exibe o ponto de exclamação e o emoji no **início** da frase. |
| \![Um exemplo de mensagens padrão da direita para a esquerda.]({% image_buster /assets/img/right-to-left/standard.png %}) | \![Um exemplo de mensagens da esquerda para a direita.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Criação de uma mensagem da direita para a esquerda

Para criar sua mensagem da direita para a esquerda no Braze:

1. Escreva sua mensagem padrão no editor do Braze.
2. Copie o texto da mensagem do Braze e, em seguida, use uma ferramenta de localização para convertê-lo em uma mensagem da direita para a esquerda.
3. Cole sua mensagem convertida de volta no Braze.
4. Verifique a formatação e o alinhamento do texto. Se estiver criando uma mensagem de e-mail HTML ou do tipo arrastar e soltar, você poderá fazer isso no compositor. Caso contrário, você precisará usar um processador de texto separado.<br><br>\![Menu do editor de arrastar e soltar do e-mail com botão para alternar o alinhamento do texto entre direita para esquerda e esquerda para direita.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Considerações
 
### Notificações push longas

O método de copiar e colar para mensagens push pode ser difícil de usar com notificações push mais longas porque o conteúdo mais longo pode ser renderizado em várias linhas em um dispositivo móvel. Se você copiar o texto da mensagem de fora do Braze (como um documento do Word) e colá-lo diretamente no Braze, o alinhamento das frases e a colocação das palavras poderão ser alterados. Para evitar esse cenário, copie e cole em partes e adicione uma quebra de linha. Por exemplo, copie e cole as primeiras cinco palavras, adicione uma quebra de linha, copie as próximas cinco palavras, adicione uma quebra de linha e assim por diante.

As funções de visualização e teste são criadas para mensagens da esquerda para a direita, portanto, as mensagens da direita para a esquerda não serão renderizadas corretamente na seção **Preview & Test**, mas serão renderizadas corretamente nos dispositivos do usuário se as configurações estiverem definidas para isso. Sugerimos que você envie mensagens para si mesmo em um ambiente real para confirmar que elas são renderizadas corretamente com base nas configurações do dispositivo.

### Texto bidirecional

Muitos usuários que escrevem em idiomas da direita para a esquerda estão, na verdade, usando texto bidirecional: uma combinação de idiomas da esquerda para a direita e da direita para a esquerda. Por exemplo, um profissional de marketing pode enviar uma mensagem em hebraico com um nome de empresa em inglês. O Braze não consegue lidar com a formatação de texto bidirecional. Duas maneiras de evitar problemas de formatação são evitar completamente o texto bidirecional ou separar o texto da esquerda para a direita do texto da direita para a esquerda usando quebras de linha. 

{% alert tip %}
A formatação adequada do texto bidirecional é especialmente importante na elaboração de mensagens que incluem códigos promocionais; os códigos promocionais geralmente estão em um formato da esquerda para a direita porque os mesmos códigos podem ser usados em vários mercados. Duas maneiras de acomodar códigos promocionais são usar uma imagem para o código promocional ou adicionar o código promocional no final da mensagem após uma quebra de linha.
{% endalert %}

### Caracteres especiais, números e emojis

Caracteres especiais (como pontuação, símbolos matemáticos e moeda), números, marcadores e emojis podem "pular" ao criar mensagens da direita para a esquerda no Braze. Para contornar isso, escreva sua cópia com a formatação adequada em um processador de texto externo e, em seguida, cole a cópia no Braze. Também pode ser útil evitar colocar emojis no início do texto e, em vez disso, separá-los (e caracteres especiais e números) do texto com quebras de linha para evitar problemas de alinhamento.

### Mensagens em árabe

Ao redigir mensagens em árabe, use tamanhos de fonte significativamente maiores para obter a mesma legibilidade que obteria em outros idiomas. Sugerimos usar um tamanho de fonte cerca de 20% maior do que o tamanho usual para idiomas que usam o alfabeto latino ou romano. Isso ocorre porque as fontes árabes são pequenas para acomodar o espaço vertical ocupado pelos diacríticos (sinais de acentuação).
