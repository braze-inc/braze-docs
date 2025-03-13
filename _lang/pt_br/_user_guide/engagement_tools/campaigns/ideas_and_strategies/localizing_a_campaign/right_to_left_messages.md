---
nav\_title: Envio de mensagens da direita para a esquerda article\_title: Criando envios de mensagens da direita para a esquerda page\_order: 1 page\_type: reference description: "Esta página aborda as práticas recomendadas para o envio de mensagens no Braze que são lidas da direita para a esquerda."
---

# Criação de mensagens da direita para a esquerda

> A aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço (como Apple, Android e Google) as processam. Esta página aborda as práticas recomendadas para o envio de mensagens da direita para a esquerda, de modo que suas mensagens sejam exibidas com a maior precisão possível.

## Como funciona?

Há três áreas principais a serem consideradas ao criar uma mensagem da direita para a esquerda: - Como a mensagem aparece em seu dashboard do Braze - Como a mensagem aparece quando é entregue - O que acontece entre a criação e a entrega

Quando uma mensagem aparece no dispositivo de um usuário, sua aparência é determinada em grande parte pela forma como os provedores (como Apple e Microsoft) a tratam, o que depende das configurações de idioma do dispositivo. Por exemplo, uma mensagem em árabe terá uma aparência diferente se o dispositivo estiver configurado para inglês em vez de árabe. 

A Apple e o Android têm um controle significativo sobre como as mensagens são processadas, enquanto os provedores de serviço de e-mail (ESPs) têm algum controle. A personalização de e-mails em HTML no Braze pode ser mais flexível; no entanto, a mesma mensagem ainda pode ser renderizada de forma diferente em dispositivos diferentes com base nas configurações do usuário.

Embora o Braze tenha controle limitado sobre a aparência final das mensagens da direita para a esquerda, nosso objetivo é facilitar ao máximo os resultados finais precisos. Use as dicas e os truques a seguir como orientação ao criar mensagens da direita para a esquerda.

## Criação de uma mensagem da direita para a esquerda

A maneira mais comum de criar mensagens da direita para a esquerda no Braze é:

1. Crie uma mensagem da esquerda para a direita em um editor Braze.
2. Copie o texto da mensagem do Braze e, em seguida, use uma ferramenta de mensagem privada para localizá-lo em uma mensagem da direita para a esquerda.
3. Confirme se o alinhamento está formatado corretamente usando um processador de texto (como o Word).
- Você pode pular essa etapa se estiver criando uma mensagem de e-mail do tipo arrastar e soltar ou HTML. O editor de arrastar e soltar permite que você altere a direção do texto selecionando um botão, e o editor de HTML permite que você personalize o alinhamento da direita para a esquerda. <br><br>Menu do editor de arrastar e soltar do e-mail com botão para alternar o alinhamento do texto entre direita para esquerda e esquerda para direita]\[1]{: style="max-width:50%;"}

{: start="4"} 4. Cole o texto formatado no Braze.

### Comparação de mensagens da esquerda para a direita e da esquerda para a direita

Muitas vezes, é possível saber se você tem as configurações corretas da direita para a esquerda observando a pontuação. Na imagem à esquerda, o ponto de exclamação e o emoji estão no lado direito do texto, que é o início da frase nos idiomas da direita para a esquerda. Na imagem à direita, formatada da direita para a esquerda, a mensagem exibe corretamente os pontos de exclamação e o emoji no final das frases.

Comparação de duas mensagens em árabe para mostrar como as mensagens da direita para a esquerda e da esquerda para a direita aparecem.

## Considerações especiais para envios de mensagens da direita para a esquerda
 
### Notificações por push longas

O método de copiar e colar para mensagens push pode ser difícil de usar com notificações por push mais longas porque o conteúdo mais longo pode ser renderizado em várias linhas em um dispositivo móvel. Se você copiar o texto de sua mensagem de fora do Braze (como um documento do Word) e colá-lo diretamente no Braze, o alinhamento das frases e a colocação das palavras poderão ser alterados. Para evitar esse cenário, copie e cole em partes e adicione uma quebra de linha. Por exemplo, copie e cole as primeiras cinco palavras, adicione uma quebra de linha, copie as próximas cinco palavras, adicione uma quebra de linha e assim por diante.

As funções de visualização e teste foram criadas para mensagens da esquerda para a direita, portanto, as mensagens da direita para a esquerda não serão renderizadas corretamente na seção **Ver prévia e testar**, mas serão renderizadas corretamente nos dispositivos do usuário se as configurações estiverem definidas para isso. Sugerimos o envio de mensagens para você mesmo em um ambiente real para confirmar que elas são renderizadas corretamente com base nas configurações do dispositivo.

### Texto bidirecional

Muitos usuários que escrevem em idiomas da direita para a esquerda estão, na verdade, usando texto bidirecional: uma combinação de idiomas da esquerda para a direita e da direita para a esquerda. Por exemplo, um profissional de marketing pode enviar uma mensagem em hebraico com um nome de empresa em inglês. O Braze não pode lidar com a formatação de texto bidirecional. Duas maneiras de evitar problemas de formatação são evitar completamente o texto bidirecional ou separar o texto da esquerda para a direita do texto da direita para a esquerda usando quebras de linha. 

{% alert tip %} A formatação adequada do texto bidirecional é especialmente importante no envio de mensagens que incluem códigos promocionais; os códigos promocionais geralmente estão em um formato da esquerda para a direita porque os mesmos códigos podem ser usados em vários profissionais de marketing. Duas maneiras de acomodar códigos promocionais são usar uma imagem para o código promocional ou adicionar o código promocional no final da mensagem após uma quebra de linha. {% endalert %}

### Caracteres especiais, números e emojis

Caracteres especiais (como pontuação, símbolos matemáticos e moeda), números, marcadores e emojis podem "pular" ao criar mensagens da direita para a esquerda no Braze. Para contornar isso, escreva sua cópia com a formatação adequada em um processador de texto externo e, em seguida, cole a cópia no Braze. Também pode ser útil evitar colocar emojis no início do texto e, em vez disso, separá-los (e caracteres especiais e números) do texto com quebras de linha para evitar problemas de alinhamento.

### Envio de mensagens em árabe

Ao criar mensagens em árabe, use tamanhos de fonte significativamente maiores para obter a mesma legibilidade que obteria em outros idiomas. Sugerimos usar um tamanho de fonte cerca de 20% maior do que o tamanho normal para idiomas que usam o alfabeto latino ou romano. Isso ocorre porque as fontes árabes são pequenas para acomodar o espaço vertical ocupado pelos diacríticos (sinais de acentuação).

\[1]: {% image\_buster /assets/img/rtl\_button.png %} \[2]: {% image\_buster /assets/img/rtl\_comparison.png %}