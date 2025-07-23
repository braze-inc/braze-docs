---
nav_title: Criação de envios de mensagens acessíveis
article_title: Criação de mensagens acessíveis no Braze
page_order: 3.5
page_type: reference
description: "Este artigo de referência explica por que é importante considerar a acessibilidade em seu conteúdo de marketing e como você pode criar mensagens acessíveis no Braze."
---

# Criação de mensagens acessíveis no Braze

> O conteúdo de marketing que exclui pessoas com deficiência, mesmo que não intencionalmente, pode impedir que milhões de pessoas interajam com sua marca. Acessibilidade em marketing significa facilitar a experiência de todos com seu marketing, receber e entender sua comunicação e ter a oportunidade de investir ou se tornar um fã de seu produto, serviço ou marca. Ao criar o envio de mensagens, reserve um tempo extra para considerar como tornar seus designs acessíveis a todos os clientes.

## Por que a acessibilidade é importante

- **Melhor usabilidade:** A acessibilidade o incentiva a pensar na usabilidade do seu app ou site porque você está pensando em como o usuário interage com o seu conteúdo. Isso significa que a acessibilidade geralmente melhora a experiência on-line de todos os usuários, não apenas daqueles com deficiência.
- **Ampliar o alcance no mercado:** O mercado global de pessoas com deficiência é de mais de 1 bilhão de pessoas, com um poder de compra de quase US$ 7 trilhões.
   > "O mercado de pessoas com deficiência é grande e está crescendo à medida que a população global envelhece. No Reino Unido, onde o grande mercado de deficientes é conhecido como Purple Pound, as pessoas com deficiência e suas famílias gastam pelo menos £249 bilhões todos os anos. Nos EUA, o gasto discricionário anual de pessoas com deficiência é superior a US$ 200 bilhões. A estimativa global do mercado de deficiências é de quase US$ 7 trilhões."<br>*Fonte: [W3C](https://www.w3.org/WAI/business-case/)*
- **Minimizar o risco legal:** Muitos países têm leis que exigem acessibilidade digital.

## Áreas de deficiência a serem consideradas

*Esta seção foi parcialmente adaptada de [W3C: Habilidades e barreiras diversas](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

### Visual

As deficiências visuais podem variar de perda de visão leve ou moderada em um ou ambos os olhos até perda substancial ou completa da visão em ambos os olhos. Algumas pessoas têm sensibilidade reduzida ou ausente a determinadas cores ou sensibilidade aumentada a cores brilhantes.

Para interagir com seu conteúdo, esses usuários precisam ter a capacidade de:

- Ampliar ou reduzir o tamanho do texto e das imagens
- Personalize as configurações de fontes, cores e espaçamento
- Ouça a síntese de texto para fala do conteúdo (ou seja, use um leitor de tela)
- Ouça as descrições em áudio do vídeo
- Ler textos usando Braille atualizável

{% alert note %}
- Em todo o mundo, pelo menos 2,2 bilhões de pessoas têm deficiência visual para perto ou para longe (consulte a [OMS](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment))
- Cerca de 1 em cada 12 homens e 1 em cada 200 mulheres têm algum grau de deficiência de visão de cores, com uma estimativa de 300 milhões de pessoas no mundo (consulte o [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/))
{% endalert %}

### Audição

As deficiências auditivas podem incluir deficiência auditiva leve a moderada em um ou ambos os ouvidos. Até mesmo a perda parcial da audição pode ser problemática em relação ao conteúdo de áudio.

Para entender seu conteúdo, esses usuários dependem de:

- Transcrições e legendas de conteúdo de áudio
- Reprodutores de mídia que exibem legendas e oferecem opções para ajustar o tamanho do texto e as cores das legendas
- Opções para parar, pausar e ajustar o volume do conteúdo de áudio (independentemente do volume do sistema)
- Áudio de primeiro plano de alta qualidade que é claramente distinguível de qualquer ruído de fundo

{% alert note %}
- Uma em cada oito pessoas nos Estados Unidos (13%, ou 30 milhões) com 12 anos ou mais tem perda auditiva em ambos os ouvidos, com base em exames auditivos padrão
- Aproximadamente 15% dos adultos americanos (37,5 milhões) com 18 anos ou mais relatam algum problema de audição (consulte o [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

### Físico

As deficiências físicas podem incluir fraqueza e limitações de controle ou sensação muscular, distúrbios nas articulações, dor que impede o movimento e membros ausentes.

Esses usuários dependem do suporte do teclado para ativar a funcionalidade (mesmo que não estejam usando um teclado padrão). Para interagir com seu conteúdo, esses usuários precisam:

- Grandes áreas clicáveis
- Tempo suficiente para concluir as tarefas
- Indicadores visíveis do foco atual
- Mecanismos para pular blocos de conteúdo, como cabeçalhos de página ou barras de navegação

{% alert note %}
Quase 2 milhões de pessoas nos EUA vivem com perda de membros (consulte [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

### Cognitivo

As deficiências cognitivas, de aprendizagem e neurológicas envolvem neurodiversidade e distúrbios neurológicos, bem como distúrbios comportamentais e de integridade mental que não são necessariamente neurológicos. Eles podem afetar qualquer parte do sistema nervoso e afetar a capacidade das pessoas de ouvir, mover-se, ver, falar e entender as informações.

Dependendo das necessidades individuais, esses usuários contam com:

- Conteúdo claramente estruturado
- Rotulagem consistente de formulários, botões e outros conteúdos
- Direcionamento previsível de links e interação geral
- Diferentes maneiras de navegar, como menus e barras de pesquisa
- Configurações para desativar conteúdo piscante, intermitente ou que cause distração de outra forma
- Texto mais simples que é apoiado por imagens


{% alert note %}
- Uma em cada cinco pessoas nos Estados Unidos tem problemas de aprendizado e atenção (consulte [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Cerca de 10 a 20% da população global é considerada neurodivergente (consulte a [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Cerca de 1 em cada 100 crianças tem autismo em todo o mundo (consulte a [OMS](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

## Práticas recomendadas

### Conteúdo

- Mantenha seu conteúdo dentro da marca, mas use linguagem simples. Escreva para um nível de leitura da sétima série dos Estados Unidos. Você pode usar recursos como o [Hemingway App](https://hemingwayapp.com/) para verificar o nível de leitura do seu texto.
- Estruture seu conteúdo de forma lógica e certifique-se de que os títulos sigam a hierarquia correta. Não pule os níveis de cabeçalho.
- Evite texto alinhado ao centro para partes longas de conteúdo. Isso pode ser difícil de ler para usuários com deficiências cognitivas ou de aprendizado. O conteúdo que se estende por mais de duas linhas deve ser alinhado à esquerda.
- Use fontes sans-serif, que são mais fáceis de ler em dispositivos digitais.
- Sempre teste sua cópia [enviando uma mensagem de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) para um dispositivo para garantir que o texto não esteja truncado. Se sua mensagem estiver sendo cortada, isso prejudica você e o usuário, pois impede que seu conteúdo chegue aos usuários.

### Links

Use links para navegação, como direcionar os usuários para uma página externa.

{% alert tip %}
Se você quiser algo que pareça e funcione como um botão, tente sempre usar um botão real em vez de estilizar um link como um botão. Os links e os botões podem parecer iguais para os usuários comuns - eles podem passar o mouse sobre o link ou o botão e clicar neles com o mouse -, mas os botões e os links têm controles diferentes (por exemplo, os botões podem ser ativados pressionando a tecla <kbd>Espaço</kbd> ou a tecla <kbd>Enter</kbd>, mas os links só podem ser ativados com a tecla <kbd>Enter</kbd>), o que pode gerar confusão se você estilizar um link como um botão.
{% endalert %}

Escreva um texto de link que descreva claramente para onde o link levará o usuário. Os usuários de leitores de tela costumam pular de um link para outro como forma de folhear o conteúdo, portanto, certifique-se de que o texto do link seja independente. Evite frases como "clique aqui", "mais" e "clique para obter detalhes", pois elas são ambíguas quando lidas fora do contexto.

Por exemplo, considere como você pode escrever um link para visualizar um boletim meteorológico.

| Ruim  | Melhor | Melhor |
| --- | --- | --- | 
| Clique aqui | Clique aqui para acessar a previsão do tempo de hoje | Tempo de hoje |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Como em todo conteúdo, seja direto e use o mínimo possível de palavras adicionais.

### Botões

Use botões para ações clicáveis, como o envio de um formulário ou a reprodução de um carrossel.

Semelhante ao texto do link, escreva o texto do botão que descreva claramente a ação que ocorrerá quando o usuário pressioná-lo (por exemplo, "Leia a story completa" em vez de "Leia mais"). Teste para garantir que o texto do botão não seja muito longo. Se o botão não puder exibir todo o texto, ele será truncado com reticências, em vez de o texto ser colocado em uma nova linha.

### Imagens

Alguns usuários não conseguem ver as imagens em seu conteúdo de marketing. Sem considerar a acessibilidade, as imagens podem se tornar uma barreira para que todos os usuários recebam o mesmo conteúdo.

#### Texto alternativo

O texto alternativo é uma breve descrição do conteúdo da imagem que os leitores de tela e outras tecnologias assistivas fornecem aos seus usuários.

- Para cada imagem, escreva um texto alternativo que forneça as informações ou a função da imagem.
- Se a imagem for [decorativa](https://www.w3.org/WAI/tutorials/images/decorative/) (não acrescenta nada ao conteúdo), use uma atribuição alt vazia (`alt=""`).
- Não use a palavra "foto" ou "imagem" em seu texto alternativo.

#### Imagens de texto

Evite usar imagens de texto, pois os leitores de tela não conseguem ler o texto contido em uma imagem. As imagens de texto também não são bem redimensionadas e não podem ser personalizadas de acordo com as necessidades e preferências do usuário. Com o texto real, os usuários podem personalizar itens como cor e contraste e redimensionar o texto sem perder a qualidade. Quando as imagens de texto são ampliadas, elas ficam pixeladas e com qualidade inferior, dificultando a leitura.

### Vídeos

Forneça legendas ocultas para vídeos. Eles ajudam as pessoas com perda de visão, as que estão assistindo em um local barulhento e as que falam um idioma diferente do idioma do vídeo.

### Contraste de cores

Ter um contraste de cores suficiente pode ser uma vitória rápida para a acessibilidade. A relação de contraste entre as cores do primeiro plano (texto) e do plano de fundo deve estar em conformidade com os [requisitos de nível AA das WCAG 2.1](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Taxa de contraste de 4.5:1 para texto normal (texto do corpo, botões e links)
- Taxa de contraste de 3:1 para textos grandes (como cabeçalhos)

Você pode usar a [ferramenta de verificação de contraste do WebAim](https://webaim.org/resources/contrastchecker/) para verificar se o texto está legível em relação às cores de fundo.

### Formulários

**Corte os formulários mais longos em seções menores** <br>Para reduzir a carga cognitiva, divida formulários longos em seções menores. Isso é conhecido como chunking, um padrão de divulgação progressiva usado para tornar as informações mais fáceis de serem consumidas. Isso beneficia todos os usuários, mas é especialmente útil para pessoas com deficiências cognitivas.

**Não oculte conteúdo importante em dicas de ferramentas ou em outros estados de foco** <br>O conteúdo contido em estados de foco é menos detectável e compatível com dispositivos móveis, e os usuários de ampliadores de tela terão dificuldade para visualizar o conteúdo que só está disponível ao passar o mouse.

**Evitar o bloqueio de caracteres inválidos nos campos** <br>Não impeça que determinados tipos de caracteres sejam inseridos em campos de formulário. É melhor permitir que os usuários insiram o que quiserem e, em seguida, fornecer uma mensagem de erro sobre o que está errado. O bloqueio da entrada do teclado representa um problema específico para os usuários de tecnologia assistiva, pois eles dependem muito da validação em linha para determinar se preencheram o formulário corretamente.

**Escreva mensagens de erro claras** <br>Uma boa mensagem de erro é composta de três partes: o que aconteceu, o que deu errado e como pode ser corrigido. O envio de mensagens de erro deve ser claro e fácil de entender. Tente falar em uma linguagem simples. Não há necessidade de um jargão sofisticado.
<br>

### HTML personalizado

Se você usar algum HTML personalizado em seu envio de mensagens:

- Use [HTML semântico](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Isso significa usar os elementos HTML corretos para a finalidade pretendida, em vez de estilizar um elemento para que se pareça com outro. A maioria dos elementos HTML tem seu próprio suporte de acessibilidade incorporado.
- Defina a atribuição de idioma em seu HTML para identificar o idioma em que seu conteúdo está. Os leitores de tela usam diferentes bibliotecas de sons para cada idioma com base na pronúncia e nas características desse idioma. Se o idioma for especificado, os leitores de tela poderão alternar automaticamente entre as bibliotecas de idiomas, conforme necessário. Por exemplo:

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

