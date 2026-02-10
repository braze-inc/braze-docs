---
nav_title: Acessibilidade
article_title: Crie envios de mensagens acessíveis no Braze
page_order: 0.5
page_type: reference
description: "Este artigo de referência explica por que é importante considerar a acessibilidade em seu conteúdo de marketing e como você pode criar mensagens acessíveis no Braze."
---

# Crie mensagens acessíveis no Braze

> Entenda por que é importante considerar a acessibilidade em seu conteúdo de marketing e como você pode criar mensagens acessíveis no Braze. Para obter mais orientações, confira nosso curso [Fundamentos do Envio de Mensagens Acessíveis](https://learning.braze.com/accessible-messaging-foundations) no Braze Learning.

O conteúdo de marketing que exclui pessoas com deficiência, mesmo que não intencionalmente, pode impedir que milhões de pessoas interajam com sua marca. A acessibilidade no marketing consiste em capacitar todos a experimentar seu marketing, entender sua comunicação e ter a oportunidade de investir em seu produto, serviço ou marca ou de se tornar um fã deles. 

Ao criar o envio de mensagens, reserve um tempo extra para considerar como tornar seus designs acessíveis a todos os clientes.

{% alert important %}
Este conteúdo é destinado à orientação geral e não garante a conformidade com os padrões de acessibilidade, como as WCAG. O Braze oferece ferramentas que dão suporte à criação de mensagens mais acessíveis, mas é sua responsabilidade garantir que o conteúdo final atenda a todos os requisitos aplicáveis. A acessibilidade é um tópico complexo com muitas partes móveis. Muitas empresas trabalham com especialistas ou consultores em acessibilidade para garantir que suas práticas de conteúdo, design e desenvolvimento atendam às necessidades de todos os usuários.
{% endalert %}

## Acessibilidade no Braze

Apoiar a comunicação acessível significa manter-se aberto, curioso e disposto a aprender. No Braze, nos preocupamos em ajudar as pessoas a se conectarem - e sabemos que abrir espaço para todos faz parte de fazer isso bem. A acessibilidade não é algo que consideramos "pronto", e agradecemos a chance de continuar aprendendo.

{% multi_lang_include accessibility/feedback.md %}

## Áreas de deficiência a serem consideradas

*Esta seção foi parcialmente adaptada de [W3C: Habilidades e barreiras diversas](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visual %}

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

{% endtab %}
{% tab Hearing %}

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

{% endtab %}
{% tab Physical %}

As deficiências físicas podem incluir fraqueza e limitações de controle ou sensação muscular, distúrbios nas articulações, dor que impede o movimento e membros ausentes.

Esses usuários dependem do suporte do teclado para ativar a funcionalidade (mesmo que não estejam usando um teclado padrão). Para interagir com seu conteúdo, esses usuários precisam:

- Grandes áreas clicáveis
- Tempo suficiente para concluir as tarefas
- Indicadores visíveis do foco atual
- Mecanismos para pular blocos de conteúdo, como cabeçalhos de página ou barras de navegação

{% alert note %}
Quase 2 milhões de pessoas nos EUA vivem com perda de membros (consulte [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

{% endtab %}
{% tab Cognitive %}

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
- Cerca de 10 a 20% da população global é considerada neurodivergente (consulte [a Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Cerca de 1 em cada 100 crianças tem autismo em todo o mundo (consulte a [OMS](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Melhores práticas

A criação de conteúdo acessível não precisa ser uma tarefa árdua. Escolhas pequenas e bem pensadas podem fazer uma grande diferença. Esta seção apresenta dicas práticas que ajudam mais pessoas a ler, navegar e interagir com sucesso com suas mensagens. Seja ajustando seu texto, estilizando seus botões ou adicionando texto alternativo às imagens, cada ajuste contribui para uma experiência mais inclusiva. Vamos nos aprofundar.

### Conteúdo

#### Estrutura e fluxo

Vamos começar com a base. Quando o seu conteúdo tem uma estrutura clara, é mais fácil para todos acompanharem, especialmente as pessoas que dependem de leitores de tela ou de navegação pelo teclado.

- **Divida seu conteúdo em seções:** O uso de títulos, marcadores e listas ajuda as pessoas a entenderem e examinarem rapidamente seu conteúdo, mesmo quando estão com pressa. 
- **Não pule os níveis de cabeçalho:** Os títulos estruturam o conteúdo, ajudando os leitores a entender rapidamente como as seções se relacionam entre si. Quando você pula os níveis de cabeçalho (por exemplo, pular diretamente de um H2 para um H4), você quebra essa estrutura lógica. Isso torna mais difícil para os usuários, especialmente os que usam leitores de tela, navegar e entender claramente a sua mensagem. Siga sempre uma hierarquia lógica e sequencial de títulos (H1 a H2 a H3 e assim por diante) para garantir que seu conteúdo permaneça organizado, acessível e fácil de ser seguido por todos.

#### Legibilidade

Uma vez que sua estrutura esteja pronta, a próxima etapa é garantir que suas palavras sejam realmente fáceis de ler. Isso significa manter as coisas simples, digitalizáveis e confortáveis para leitura em todos os dispositivos e necessidades do usuário.

- **Escreva frases curtas e claras:** Frases curtas são fáceis de serem entendidas por todos, especialmente por pessoas que usam leitores de tela ou que têm dificuldade para processar informações complexas. Escreva para um nível de leitura da sétima série dos Estados Unidos. Você pode usar recursos como o [Hemingway App](https://hemingwayapp.com/) para verificar o nível de leitura do seu texto.
- **Escolha tamanhos de fonte e espaçamento legíveis:** O texto muito pequeno pode ser difícil de ler, especialmente em celulares. Use pelo menos 14px para o texto do corpo. Faça títulos maiores para que os usuários possam ver claramente a diferença. O espaçamento extra entre linhas (cerca de 1,5 de altura de linha) e parágrafos melhora a legibilidade, especialmente para pessoas com necessidades visuais ou cognitivas.
- **Evite texto justificado:** O texto justificado cria um espaçamento desigual entre as palavras, dificultando a leitura para pessoas com dislexia ou deficiências cognitivas. Considere a possibilidade de alinhar à esquerda o conteúdo que se estende por mais de duas linhas nos idiomas da esquerda para a direita ou à direita nos [idiomas da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages).
- **Use texto em negrito, itálico e caixa alta com moderação:** Enfatizar muito o texto dificulta a leitura, especialmente para pessoas com dislexia ou deficiências visuais. Mantenha a simplicidade.

#### Clareza e usabilidade

Por fim, vamos falar sobre os detalhes mais finos - os aspectos que ajudam os usuários não apenas a ver seu conteúdo, mas a entender e interagir com ele. 

- **Identifique claramente os links e botões:** Certifique-se de que o texto do [link](#links) e do [botão](#buttons) explique claramente o que acontecerá em seguida. Isso ajuda as pessoas que usam leitores de tela ou que navegam com um teclado a saber o que esperar.
- **Acesse com calma os símbolos e emojis:** Caracteres especiais e emojis podem tornar seu conteúdo divertido, mas podem ser confusos quando lidos por leitores de tela. Use-as com moderação e certifique-se de que elas não substituam um texto claro e descritivo.
- **Teste de truncamento:** Sempre teste sua cópia [enviando uma mensagem de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) para um dispositivo para garantir que o texto não esteja truncado. Se sua mensagem estiver sendo cortada, isso prejudica você e seu público, pois impede que seu conteúdo chegue até eles.

### Botões

Use **botões** para indicar uma ação, como o envio de um formulário ou a reprodução de um carrossel. Se estiver navegando para um novo URL, considere usar um [link](#links).

#### Escreva textos claros e orientados para a ação

Assim como o texto do link, os rótulos dos botões devem descrever claramente a ação. O texto eficaz do botão é específico e orientado para a ação. Por exemplo, "Submit Order" informa claramente aos usuários o que acontecerá quando eles clicarem, enquanto simplesmente "Submit" pode ser ambíguo. Cada rótulo deve descrever com precisão a ação pretendida, para que os leitores de tela e todos os usuários possam entender e prever facilmente o resultado ao interagir com os botões.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bom texto de botão <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Texto ruim do botão <span aria-hidden="true">🚫</span>.
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Enviar pedido"</td>
      <td>"Enviar"</td>
    </tr>
    <tr>
      <td>"Criar conta"</td>
      <td>"Inscreva-se"</td>
    </tr>
    <tr>
      <td>"Baixe nosso folheto</td>
      <td>"Baixar"</td>
    </tr>
    <tr>
      <td>"Exibir detalhes do produto"</td>
      <td>"Saiba mais"</td>
    </tr>
    <tr>
      <td>"Assinar para receber atualizações"</td>
      <td>"Assinar"</td>
    </tr>
  </tbody>
</table>

Mantenha o texto do botão conciso para evitar o truncamento. Se o texto de um botão for muito longo, ele poderá ser cortado com reticências em vez de ser envolvido.

#### Use contraste de cores suficiente

O texto do botão deve ser fácil de ler em relação à cor de fundo do botão. Verifique se o texto do botão atende aos [requisitos mínimos de contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) AA das WCAG 2.2:

- Taxa de contraste de 4,5:1 para texto de tamanho normal (a maioria dos botões)
- Taxa de contraste de 3:1 para textos grandes (normalmente acima de 18pt)

O alto contraste ajuda os botões a permanecerem legíveis e clicáveis para todos, inclusive para usuários com deficiências visuais ou para aqueles que visualizam a sua mensagem em ambientes desafiadores. Para obter mais orientações, consulte a seção [Contraste de cores](#color-contrast).

#### Torne os botões fáceis de tocar

Certifique-se de que seus botões (e links) sejam grandes o suficiente e tenham espaçamento suficiente para usuários de dispositivos móveis. [Alvos de toque](#touch-targets) pequenos ou lotados podem ser frustrantes ou impossíveis de serem interagidos por usuários com deficiências motoras.  

### Links

Use links para navegação, como direcionar os usuários para uma página externa.

#### Escreva um texto descritivo para o link

Escreva um texto de link que descreva claramente para onde o link levará o usuário. Os usuários de leitores de tela costumam pular de um link para outro como forma de folhear o conteúdo, portanto, certifique-se de que o texto do link seja independente. Evite frases como "clique aqui", "mais" e "clique para obter detalhes", pois elas são ambíguas quando lidas fora do contexto.

Por exemplo, considere como você pode escrever um link para visualizar um boletim meteorológico.

| Ruim  | Melhor | Melhor |
| --- | --- | --- | 
| Clique aqui | Clique aqui para acessar a previsão do tempo de hoje | Tempo de hoje |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Como em todo conteúdo, seja direto e use o mínimo possível de palavras adicionais.

#### Evite estilizar links como botões

Os editores de arrastar e soltar do Braze produzem HTML semântico por padrão, portanto, os links não são estilizados como botões. No entanto, se estiver trabalhando com [HTML personalizado](#custom-html) ou fazendo alterações no nível do código, tenha isso em mente:

- **Os links (`<a>`** ) respondem à tecla <kbd>Enter</kbd>.
- **Os botões (`<button>`** ) respondem às teclas <kbd>Enter</kbd> e <kbd>Espaço</kbd>.

A estilização de um link para que se pareça com um botão pode confundir as pessoas que navegam com um teclado - elas podem tentar pressionar <kbd>Espaço</kbd> e esperar que funcione.

Use o elemento certo para a ação:

- Use `<button>` para ações, como o envio de um formulário ou a abertura de um modal.
- Use o endereço `<a>` para navegação, como um link para outra página ou arquivo.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Alvos de toque

Os direcionamentos de toque são qualquer parte da sua mensagem em que os usuários tocam para realizar uma ação, como botões, links ou ícones. Esses elementos precisam ser grandes e espaçados o suficiente para que as pessoas possam tocá-los facilmente, especialmente em dispositivos móveis.

Quando os direcionamentos de toque são muito pequenos ou muito próximos uns dos outros, pode ser frustrante ou impossível para os usuários com dificuldades de mobilidade ou destreza interagirem com a mensagem. Melhorar isso pode ajudar a reduzir erros e criar uma experiência mais tranquila para todos.

Veja a seguir o que você deve ter em mente:
- **Use o tamanho adequado do direcionamento de toque.** Procure obter um tamanho mínimo de alvo de toque de 44 x 44 pixels. Isso se alinha com as diretrizes WCAG 2.2 para [direcionamentos de toque](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) e padrões comuns de usabilidade móvel.
- **Dê espaço para cada direcionamento.** Se os alvos de toque estiverem muito próximos uns dos outros - como links empilhados ou botões bem agrupados - pode ser fácil perder ou tocar no alvo errado. Adicione espaçamento ou preenchimento entre os elementos para evitar isso.
- **Não dependa apenas de recursos visuais.** Até mesmo ícones pequenos podem se tornar mais úteis com preenchimento extra, permitindo que eles atendam aos requisitos de tamanho mínimo sem alterar o layout.
- **Pré-visualização no celular.** Teste sua mensagem em diferentes tamanhos de tela e certifique-se de que os elementos interativos sejam fáceis de usar.

Melhorar os direcionamentos de toque é uma das maneiras mais eficazes de tornar sua mensagem mais acessível no celular - e é uma boa experiência do usuário para todos.

### Imagens

#### Fornecer texto alternativo

O texto alternativo (alt text) é uma breve descrição do conteúdo ou da função de uma imagem que os leitores de tela e outras tecnologias de assistência fornecem aos usuários. Para cada imagem significativa, escreva um texto alternativo descritivo para que os usuários que não puderem ver os recursos visuais ainda entendam sua mensagem ou chamada para ação. 

#### Evite imagens de texto

Sempre que possível, evite colocar texto dentro de imagens - os leitores de tela não conseguem ler textos baseados em imagens, e os usuários não podem ajustar facilmente o tamanho ou a cor da fonte para melhorar a visibilidade. Considere estas dicas:

- **Remova o texto onde for possível:** Em vez disso, mova qualquer texto descritivo ou promocional da imagem para um campo de texto em sua mensagem. Dessa forma, os usuários podem redimensioná-lo ou recolori-lo conforme necessário, usando as preferências do dispositivo ou do navegador.
- **Teste a legibilidade e o contraste:** Se você precisar manter o texto na imagem, siga as práticas recomendadas [de contraste de cores](#color-contrast) e use uma [fonte de grande escala](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Isso significa que o texto deve ter pelo menos 18 pontos (cerca de 24 pixels) para texto sem negrito ou 14 pontos (cerca de 18 pixels) se estiver em negrito. O uso desses tamanhos ajuda o texto a permanecer legível sem forçar os usuários a aumentar o zoom, além de melhorar o contraste geral e a legibilidade do conteúdo. Teste para confirmar se ainda é legível em telas menores.
- **Forneça texto alternativo:** Para o texto essencial que deve permanecer na imagem, inclua um texto alternativo que descreva as palavras.

Quando as imagens contêm texto que não pode ser editado, os usuários com deficiências visuais perdem a flexibilidade de fazer ajustes de leitura. Ao separar o texto das imagens, você ajuda mais usuários a ler e interagir com sua mensagem confortavelmente.

#### Dicas para escrever texto alternativo

- [Descreva o que está de fato na imagem](#tip-1)
- [Seja breve, mas específico](#tip-2)
- [Evite "imagem de" ou "foto de"](#tip-3) 
- [Refletir o texto que aparece na imagem](#tip-4)
- [Atenha-se ao contexto relevante - sem jargões extras de marketing](#tip-5)
- [Considere o objetivo da imagem](#tip-6)

##### Descreva o que está de fato na imagem {#tip-1}

Os usuários de leitores de tela dependem do texto alternativo para entender o conteúdo ou a função de uma imagem. Evite "discurso de marketing" genérico que não corresponda ao que está sendo mostrado visualmente.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Exemplos ruins <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mulher sorridente vestindo uma jaqueta jeans azul, segurando uma sacola de compras."</td>
      <td>"Time to treat yourself!" (Não há menção do que está de fato na imagem)</td>
    </tr>
    <tr>
      <td>"Homem vestindo uma camiseta preta, apoiado em uma bicicleta em uma rua da cidade."</td>
      <td>"Abrace sua melhor vida agora!" (Ignora o cenário da bicicleta e da cidade)</td>
    </tr>
    <tr>
      <td>"Prédio de apartamentos azul com um letreiro 'Aluga-se' na frente."</td>
      <td>"A chave para um amanhã melhor!" (Não reflete o apartamento ou o login)</td>
    </tr>
  </tbody>
</table>

##### Seja breve, mas específico {#tip-2}

O texto alternativo conciso facilita o processamento pelos usuários. Inclua detalhes suficientes para transmitir o objetivo, mas não inclua nada de mais. Como regra geral, mantenha o texto alternativo com 125 caracteres ou menos. Se for necessário algo mais do que uma breve frase ou sentença, considere usar um dos [métodos de descrição longa](https://www.w3.org/WAI/tutorials/images/complex/) do W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Exemplos ruins <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Tênis de corrida vermelho em um fundo branco"</td>
      <td>"Tênis de corrida que são extremamente confortáveis e perfeitos para seu estilo de vida ativo em um tom vibrante de vermelho." (Muito longo e cheio de informações promocionais)</td>
    </tr>
    <tr>
      <td>"Quatro laptops em um suporte de exibição"</td>
      <td>"Descubra o maior impulsionador de produtividade que redefine a forma como você trabalha todos os dias, de todas as maneiras imagináveis." (Não descreve o que é realmente mostrado)</td>
    </tr>
    <tr>
      <td>"Grupo de amigos tomando sorvete em um dia ensolarado"</td>
      <td>"Capture a felicidade pura com a guloseima mais doce - a vida é melhor com nossa marca de sorvete!" (Muito abstrato e focado na marca)</td>
    </tr>
  </tbody>
</table>

##### Evite "imagem de" ou "foto de" {#tip-3}

Os leitores de tela já anunciam uma imagem. Vá direto para a descrição do assunto.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Exemplos ruins <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mesa preparada para o brunch com panquecas, frutas e café."</td>
      <td>"Imagem de uma mesa posta para um brunch"</td>
    </tr>
    <tr>
      <td>"Outdoor de beira de estrada com texto em negrito 'Grand Opening'"</td>
      <td>"Foto de um outdoor na beira de uma estrada"</td>
    </tr>
    <tr>
      <td>"Paisagem de montanha nevada ao pôr do sol"</td>
      <td>"Foto de neve e montanhas"</td>
    </tr>
  </tbody>
</table>

##### Refletir o texto que aparece na imagem {#tip-4}

Se uma imagem incluir um texto essencial, coloque essa informação no texto alternativo para que os usuários não a percam.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Exemplos ruins <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Banner dizendo 'Promoção de verão - 50% de desconto em todos os trajes de banho'."</td>
      <td>"Banner promovendo uma venda." (Não menciona o desconto real)</td>
    </tr>
    <tr>
      <td>"Logotipo com o texto 'Café Toscana' em fonte script"</td>
      <td>"Imagem do logotipo de uma cafeteria." (Não inclui o texto 'Café Toscana')</td>
    </tr>
    <tr>
      <td>"Anúncio anunciando 'Ingressos para shows disponíveis agora - a partir de 5 de junho'"</td>
      <td>"Anúncio de concerto." (Sem detalhes do evento)</td>
    </tr>
  </tbody>
</table>

##### Atenha-se ao contexto relevante - sem jargões extras de marketing {#tip-5}

Não preencha o texto alternativo com termos de SEO ou chamadas para ação não diretamente relacionadas à imagem. Forneça valor para aqueles que não podem ver a imagem.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Exemplos ruins <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Laptop mostrando o gráfico de análise de dados do dashboard do Braze"</td>
      <td>"Aumente as conversões e dispare o ROI com a melhor plataforma do mundo!" (Adiciona linguagem de marketing desnecessária)</td>
    </tr>
    <tr>
      <td>"Conjunto para pátio de quintal com quatro cadeiras e uma mesa de vidro"</td>
      <td>"Organize uma festa de verão incrível para todos os seus amigos e familiares agora!" (Descreve um cenário, não a imagem)</td>
    </tr>
    <tr>
      <td>"Telefone celular exibindo um app de previsão do tempo com 75°F à vista"</td>
      <td>"Experimente inovações em tempo real no rastreamento do clima que é um divisor de águas" (Não reflete o que é mostrado visivelmente)</td>
    </tr>
  </tbody>
</table>

##### Considere o objetivo da imagem {#tip-6}

Se uma imagem estiver funcionando como um link ou uma chamada para ação, descreva a ação pretendida ("Comprar", "Link para", "Inscreva-se"), não apenas o rótulo ou o produto mostrado.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Exemplos ruins <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Compre a coleção de outono"</td>
      <td>"Coleção de outono" (ação não planejada)</td>
    </tr>
    <tr>
      <td>"Link para o e-book gratuito"</td>
      <td>"Free e-book" (não deixa claro que se trata de um link)</td>
    </tr>
    <tr>
      <td>"Inscreva-se na lista de discussão"</td>
      <td>"Mailing list" (Não descreve o que o usuário pode fazer)</td>
    </tr>
  </tbody>
</table>

Se a imagem não tiver uma finalidade, informe isso também. Imagens decorativas, como logotipos, devem ter uma tag alt vazia (`alt=""`) para que os leitores de tela saibam que não devem anunciá-las. Sem ele, geralmente o nome do arquivo de imagem é lido.

### Vídeos

Os vídeos são engajadores, mas se não forem acessíveis, você corre o risco de excluir parte do seu público. Use as dicas a seguir para tornar seu conteúdo de vídeo mais inclusivo:

- [Fornecer legendas ocultas](#closed-captions)
- [Fornecer controles de reprodução](#playback-controls)
- [Evite a reprodução automática](#no-auto-play)
- [Evite conteúdo piscante ou estroboscópico](#no-seizures)

#### Fornecer legendas ocultas {#closed-captions}

Inclua legendas ocultas em seus vídeos para que os usuários possam acompanhar o diálogo, os efeitos sonoros e outros conteúdos de áudio. As legendas ajudam:

- Pessoas surdas ou com deficiência auditiva
- Telespectadores assistindo em um ambiente sem som
- Falantes não nativos que preferem ler junto

As legendas ocultas podem ser ativadas ou desativadas, permitindo que os usuários escolham o que funciona melhor para eles.

{% multi_lang_include accessibility/video.md %}

#### Fornecer controles de reprodução {#playback-controls}

Certifique-se de que o vídeo incorporado inclua controles de reprodução acessíveis, como reproduzir, pausar, silenciar e buscar, para que os usuários possam interagir com ele da maneira que for melhor para eles.

#### Evite a reprodução automática {#no-auto-play}

Sempre que possível, evite configurar os vídeos para serem reproduzidos automaticamente. A reprodução automática pode ser chocante ou desorientadora para os usuários:

- Usuários que dependem de leitores de tela ou navegação por teclado
- Pessoas com sensibilidade ao movimento
- Qualquer pessoa em um ambiente silencioso (como um local de trabalho ou um ambiente noturno)

Permita que os usuários escolham quando reproduzir um vídeo, incluindo controles claros.

#### Evite conteúdo piscante ou estroboscópico {#no-seizures}

Não inclua vídeos com efeitos intermitentes ou estroboscópicos, especialmente em alta frequência. Eles podem disparar convulsões em usuários com epilepsia fotossensível e causar desconforto em outros.

### Contraste de cores

Um contraste de cores suficiente ajuda a garantir que suas mensagens sejam fáceis de ler para todos, inclusive para as pessoas com baixa visão ou para aquelas que visualizam seu conteúdo em condições de luminosidade ou desafiadoras. Procure obter taxas de contraste que atendam aos [requisitos de nível AA das WCAG 2.2](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Taxa de contraste de 4,5:1 para texto normal (pense no corpo do texto, botões e links)
- Taxa de contraste de 3:1 para textos grandes (como cabeçalhos e rótulos maiores)

Você pode testar suas escolhas de cores usando a [ferramenta de verificação de contraste do WebAim](https://webaim.org/resources/contrastchecker/).

{% multi_lang_include accessibility/color.md %}

### HTML personalizado

Se você usar algum HTML personalizado em seu envio de mensagens:

- Use [HTML semântico](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Isso significa usar os elementos HTML corretos para a finalidade pretendida, em vez de estilizar um elemento para que se pareça com outro. A maioria dos elementos HTML tem seu próprio suporte de acessibilidade incorporado.
- Defina a [atribuição`lang` ](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) em seu HTML para identificar o idioma em que seu conteúdo está. Os leitores de tela usam diferentes bibliotecas de sons para cada idioma com base na pronúncia e nas características desse idioma. Se isso não for especificado, um leitor de tela assumirá que o conteúdo está escrito no idioma padrão que o usuário escolheu ao configurar o leitor de tela. Se a mensagem não estiver realmente no idioma padrão, o leitor de tela poderá não pronunciá-la corretamente. 

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Ao usar o editor de arrastar e soltar e-mail, o valor do idioma do e-mail pode ser definido na guia **Configurações** e selecionando o valor de idioma apropriado.
{% endalert %}

- Use [atribuições ARIA](#aria-attributes) para fornecer contexto extra. Essas atribuições fornecem informações adicionais às tecnologias assistivas, ajudando a esclarecer a função, o estado ou as propriedades dos elementos da interface do usuário que, de outra forma, poderiam não estar claros. 

### Atribuições ARIA

Ao usar código personalizado nos editores do Braze, você pode usar o[ARIA (](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)Accessible Rich Internet Applications) para fornecer suporte extra de acessibilidade para usuários que dependem de tecnologia assistiva. As funções e atribuições ARIA ajudam os leitores de tela a interpretar seu conteúdo com mais clareza, especialmente quando se usa elementos que não transmitem significado por si só (como `<div>` ou `<span>`).

{% alert important %}
Embora o ARIA tenha sido projetado para tornar o conteúdo da Web mais acessível, se usado incorretamente, ele pode causar mais danos do que benefícios. O ARIA não substitui o HTML semântico, ele o complementa - portanto, use o ARIA somente quando os elementos HTML nativos não atenderem às suas necessidades.
{% endalert %}

Aqui estão alguns exemplos que são especialmente úteis em contextos de envio de mensagens:

- [rótulo aria](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentation"](#rolepresentation)
- [aria-live="polite" (educado)](#aria-livepolite)

#### rótulo aria

`aria-label` adiciona um nome acessível a elementos que não têm texto visível. Se você estiver usando um ícone sem texto (como uma lixeira ou um "X" para fechar), alguém que usa um leitor de tela não saberá o que ele faz, a menos que você o rotule. `aria-label` dá voz a esse ícone.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby

`aria-labelledby` conecta um elemento a algo que já tem um rótulo visível. Portanto, se você tiver um banner ou uma região que deva ser lida em voz alta com um título, poderá usar o site `aria-labelledby` para informar à tecnologia assistiva: "Ei, use aquele título ali para nomear esta parte".

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true"

`aria-hidden="true"` oculta coisas dos leitores de tela.  É útil para textos ou recursos visuais que não transmitem um significado importante, como um brilho, uma marca de seleção ou um emoji usado apenas por estilo.

Isso mantém a experiência mais limpa para os usuários de leitores de tela, que, de outra forma, poderiam ouvir conteúdo redundante ou confuso. Também é útil para ocultar coisas como conteúdo de acordeão fora da tela que ainda não foi expandido.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

Em geral, é melhor usar `alt=""` para [imagens](#images) e ícones [decorativos](#images) em vez de `aria-hidden="true"`. Embora o HTML semântico seja amplamente suportado por todos os leitores de tela e softwares de assistência, o suporte ao ARIA varia. Mesmo se você usar `aria-hidden`, deverá incluir uma atribuição alt vazia.

#### role="presentation"

`role="presentation"` diz à tecnologia assistiva para ignorar elementos somente de layout, como tabelas de design. Por exemplo, os e-mails geralmente usam tabelas apenas para alinhar as coisas. Sem essa função, os leitores de tela podem presumir que o layout é uma tabela de dados e começar a ler os números das linhas e colunas.  

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

Os e-mails criados no editor de arrastar e soltar têm elementos de apresentação marcados automaticamente com o atributo ARIA `role="presentation"`.

#### aria-live="polite" (educado)

`aria-live="polite"` anuncia atualizações quando o conteúdo é alterado sem a necessidade de interação do usuário. Use-o quando exibir atualizações dinâmicas em uma mensagem, como sucessos, erros ou outras notificações.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Teste automatizado de acessibilidade

Para ajudá-lo a identificar e corrigir problemas de acessibilidade com antecedência, o Braze oferece testes automatizados de acessibilidade nas seguintes áreas:

- [Visão da caixa de entrada]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) para e-mails
- [Verificador de acessibilidade]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=in-app%20message#accessibility-scanner) para mensagens criadas usando nosso editor de HTML (por exemplo, mensagens no app em HTML, blocos de conteúdo em HTML, [rodapés de e-mail personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer), [páginas de aceitação de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-opt-in-page) e [páginas de cancelamento de inscrição de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-unsubscribe-page)).

Esses testes verificam sua mensagem em relação ao padrão[WCAG (](https://www.w3.org/WAI/standards-guidelines/wcag/)Web Content Accessibility Guidelines) - um conjunto de padrões técnicos internacionalmente reconhecidos para conteúdo acessível. Todos os problemas que podem ser detectados automaticamente são sinalizados e categorizados por gravidade para ajudá-lo a priorizar.

{% alert note %}
O Inbox Vision funciona tanto para e-mails em HTML quanto para e-mails do tipo arrastar e soltar. O scanner só é executado em conteúdo criado com o editor de HTML.
{% endalert %}

### O que os testes automatizados podem e não podem detectar

Os testes automatizados de acessibilidade são um ótimo ponto de partida, mas não conseguem detectar tudo. Alguns problemas precisam de um toque humano para serem avaliados adequadamente, especialmente quando o contexto ou o design visual desempenha um papel na forma como os usuários experimentam seu e-mail.

Você poderá ver alguns problemas marcados como **Precisa de revisão**. Esses são casos em que o verificador não pode dizer com certeza se algo é um problema de acessibilidade. Quando isso acontecer, recomendamos revisá-lo manualmente.

Alguns exemplos do que as ferramentas automatizadas não conseguem detectar de forma confiável incluem:

- Se a ordem de foco dos elementos interativos seguir uma sequência lógica
- Se o conteúdo for totalmente operável com um teclado, sem a necessidade de um mouse
- Se o texto alternativo descrever uma imagem de forma significativa
- Se os títulos forem usados adequadamente para organizar o conteúdo
- Se os links e botões estiverem claramente identificados e forem fáceis de entender
- Se os alvos de toque forem grandes o suficiente e espaçados adequadamente
- Se o texto em imagens de fundo atender aos requisitos de contraste de cores
- Se as instruções ou rótulos são claros e úteis para todos os usuários

Essas limitações não são exclusivas do Braze - elas são comuns a todas as ferramentas de acessibilidade automatizadas. As verificações automatizadas não podem imitar todas as tecnologias assistivas, leitores de tela ou necessidades do usuário. É por isso que a acessibilidade não é uma verificação única - é uma prática contínua.

Mesmo que sua mensagem seja aprovada em todas as verificações automáticas, ainda assim é importante:

- Analise cuidadosamente os problemas sinalizados, especialmente aqueles marcados como **Precisa de revisão**.
- Faça testes manuais sempre que possível, especialmente para padrões de layout e interação.
- Use ferramentas como leitores de tela, navegação somente com teclado e zoom do navegador para simular diferentes necessidades de acesso.

Ao combinar testes automatizados com uma revisão manual cuidadosa, você detectará mais problemas em potencial e criará campanhas mais inclusivas e úteis para todos os destinatários.
