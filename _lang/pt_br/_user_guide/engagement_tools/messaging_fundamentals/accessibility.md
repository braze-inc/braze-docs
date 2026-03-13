---
nav_title: Acessibilidade
article_title: Crie mensagens acessíveis no Braze
page_order: 0.5
page_type: reference
description: "Este artigo de referência explica por que é importante considerar a acessibilidade em seu conteúdo de marketing e como você pode criar mensagens acessíveis no Braze."
---

# Crie mensagens acessíveis no Braze

> Entenda por que a acessibilidade é importante a ser considerada em seu conteúdo de marketing e como você pode criar mensagens acessíveis no Braze. Para mais orientações, confira nosso curso [Fundamentos de Mensagens Acessíveis](https://learning.braze.com/accessible-messaging-foundations) no Braze Learning.

O conteúdo de marketing que exclui pessoas com deficiência, mesmo que não intencionalmente, pode impedir que milhões de pessoas interajam com sua marca. A acessibilidade no marketing é sobre permitir que todos experimentem seu marketing, entendam sua comunicação e tenham a oportunidade de investir ou se tornar fã de seu produto, serviço ou marca. 

Ao criar o envio de mensagens, reserve um tempo extra para considerar como tornar seus designs acessíveis a todos os clientes.

{% alert important %}
Este conteúdo é destinado a orientações gerais e não garante conformidade com padrões de acessibilidade, como o WCAG. O Braze oferece ferramentas que suportam a criação de mensagens mais acessíveis, mas é sua responsabilidade garantir que seu conteúdo final atenda a quaisquer requisitos aplicáveis. A acessibilidade é um tópico complexo com muitas partes móveis. Muitas empresas trabalham com especialistas ou consultores em acessibilidade para garantir que seu conteúdo, design e práticas de desenvolvimento atendam às necessidades de todos os usuários.
{% endalert %}

## Acessibilidade no Braze

Apoiar a comunicação acessível significa estar aberto, curioso e disposto a aprender. No Braze, nos preocupamos em ajudar as pessoas a se conectarem—e sabemos que fazer espaço para todos é parte de fazer isso bem. A acessibilidade não é algo que consideramos "pronto" e acolhemos a chance de continuar aprendendo.

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
- Aproximadamente 10-20% da população global é considerada neurodivergente (veja [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Cerca de 1 em cada 100 crianças tem autismo em todo o mundo (consulte a [OMS](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Melhores práticas

Criar conteúdo acessível não precisa ser esmagador. Pequenas escolhas pensativas podem fazer uma grande diferença. Esta seção apresenta dicas práticas que ajudam mais pessoas a ler, navegar e interagir com suas mensagens com sucesso. Seja ajustando seu texto, estilizando seus botões ou adicionando texto alternativo às imagens, cada ajuste se soma a uma experiência mais inclusiva. Vamos nos aprofundar.

### Conteúdo

#### Estrutura e fluxo

Vamos começar com a base. Quando seu conteúdo tem uma estrutura clara, é mais fácil para todos acompanharem—especialmente para pessoas que dependem de leitores de tela ou navegação por teclado.

- **Divida seu conteúdo em seções:** Usar cabeçalhos, marcadores e listas ajuda as pessoas a entender e escanear rapidamente seu conteúdo—mesmo quando estão com pressa. 
- **Não pule níveis de cabeçalho:** Os cabeçalhos dão estrutura ao seu conteúdo, ajudando os leitores a entender rapidamente como as seções se relacionam entre si. Quando você pula níveis de cabeçalho (por exemplo, pulando diretamente de um H2 para um H4), você quebra essa estrutura lógica. Isso torna mais difícil para os usuários, especialmente aqueles que usam leitores de tela, navegar e entender sua mensagem claramente. Sempre siga uma hierarquia lógica e sequencial de cabeçalhos (H1 para H2 para H3, e assim por diante) para garantir que seu conteúdo permaneça organizado, acessível e fácil para todos acompanharem.

#### Legibilidade

Uma vez que sua estrutura esteja em vigor, o próximo passo é garantir que suas palavras sejam realmente fáceis de ler. Isso significa manter as coisas simples, escaneáveis e confortáveis para ler em diferentes dispositivos e necessidades dos usuários.

- **Escreva frases curtas e claras:** Frases curtas são fáceis para todos entenderem, especialmente para pessoas que usam leitores de tela ou que têm dificuldade em processar informações complexas. Escreva para um nível de leitura da sétima série dos Estados Unidos. Você pode usar recursos como o [Hemingway App](https://hemingwayapp.com/) para verificar o nível de leitura do seu texto.
- **Escolha tamanhos de fonte e espaçamento legíveis:** Texto que é muito pequeno pode ser difícil de ler—especialmente em dispositivos móveis. Use pelo menos 14px para o texto do corpo. Faça os cabeçalhos maiores para que os usuários possam ver claramente a diferença. Espaçamento extra entre linhas (cerca de 1,5 altura da linha) e parágrafos melhora a legibilidade, especialmente para pessoas com necessidades visuais ou cognitivas.
- **Evite texto justificado:** Texto justificado cria espaçamento desigual entre as palavras, dificultando a leitura para pessoas com dislexia ou deficiências cognitivas. Considere fazer conteúdo que se ajuste a mais de duas linhas alinhado à esquerda para idiomas da esquerda para a direita ou alinhado à direita para [idiomas da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages).
- **Use texto em negrito, itálico e maiúsculas com moderação:** Enfatizar texto demais dificulta a leitura—especialmente para pessoas com dislexia ou deficiências visuais. Mantenha simples.

#### Clareza e usabilidade

Finalmente, vamos falar sobre os detalhes mais sutis—as coisas que ajudam os usuários não apenas a ver seu conteúdo, mas a entendê-lo e interagir com ele. 

- **Rotule claramente links e botões:** Certifique-se de que seu [link](#links) e [botão](#buttons) expliquem claramente o que acontece a seguir. Isso ajuda as pessoas que usam leitores de tela ou navegam com um teclado a saber o que esperar.
- **Evite símbolos e emojis:** Caracteres especiais e emojis podem tornar seu conteúdo divertido, mas podem ser confusos quando lidos por leitores de tela. Use-os com moderação e certifique-se de que não substituam texto claro e descritivo.
- **Teste para truncamento:** Sempre teste sua cópia [enviando uma mensagem de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) para um dispositivo para garantir que o texto não esteja truncado. Se sua mensagem estiver sendo cortada, isso prejudica tanto você quanto seu público, pois impede que seu conteúdo chegue até eles.

### Botões

Use **botões** para indicar uma ação, como enviar um formulário ou tocar em um carrossel. Se você estiver navegando para uma nova URL, considere usar um [link](#links) em vez disso.

#### Escreva texto claro e orientado para a ação

Semelhante ao texto do link, os rótulos dos botões devem descrever claramente a ação. Texto de botão eficaz é específico e orientado para a ação. Por exemplo, "Enviar Pedido" diz claramente aos usuários o que acontecerá quando clicarem, enquanto simplesmente "Enviar" pode ser ambíguo. Cada rótulo deve descrever precisamente sua ação pretendida, para que leitores de tela e todos os usuários possam entender e prever facilmente o resultado ao interagir com seus botões.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bom texto de botão <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Texto de botão ruim <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Enviar Pedido"</td>
      <td>"Enviar"</td>
    </tr>
    <tr>
      <td>"Criar Conta"</td>
      <td>"Inscrever-se"</td>
    </tr>
    <tr>
      <td>"Baixar Nosso Folheto"</td>
      <td>"Baixar"</td>
    </tr>
    <tr>
      <td>"Ver Detalhes do Produto"</td>
      <td>"Saiba Mais"</td>
    </tr>
    <tr>
      <td>"Inscrever-se para Atualizações"</td>
      <td>"Inscrever-se"</td>
    </tr>
  </tbody>
</table>

Mantenha o texto do botão conciso para evitar truncamento. Se o texto de um botão for muito longo, pode ser cortado com uma reticência em vez de ser quebrado.

#### Use contraste de cor suficiente

O texto do botão deve ser fácil de ler contra a cor de fundo do botão. Verifique se o texto do seu botão atende aos mínimos de contraste WCAG 2.2 AA [mínimos de contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html):

- 4.5:1 de relação de contraste para texto de tamanho normal (a maioria dos botões)
- relação de contraste 3:1 para texto grande (geralmente acima de 18pt)

Alto contraste ajuda os botões a permanecerem legíveis e clicáveis para todos, incluindo usuários com deficiências visuais ou aqueles que visualizam sua mensagem em ambientes desafiadores. Para mais orientações, veja a seção [Contraste de cores](#color-contrast).

#### Facilite o toque nos botões

Certifique-se de que seus botões (e links) sejam grandes o suficiente e espaçados adequadamente para usuários em dispositivos móveis. Alvos de toque pequenos ou aglomerados [pode ser frustrante ou impossível para usuários com deficiências motoras interagir com eles.  

### Links

Use links para navegação, como direcionar os usuários para uma página externa.

#### Escreva texto descritivo para links

Escreva um texto de link que descreva claramente para onde o link levará o usuário. Os usuários de leitores de tela costumam pular de um link para outro como forma de folhear o conteúdo, portanto, certifique-se de que o texto do link seja independente. Evite frases como "clique aqui", "mais" e "clique para obter detalhes", pois elas são ambíguas quando lidas fora do contexto.

Por exemplo, considere como você pode escrever um link para visualizar um boletim meteorológico.

| Ruim  | Melhor | Melhor |
| --- | --- | --- | 
| Clique aqui | Clique aqui para acessar a previsão do tempo de hoje | Tempo de hoje |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Como em todo conteúdo, seja direto e use o mínimo possível de palavras adicionais.

#### Evite estilizar links como botões

Os editores de arrastar e soltar do Braze geram HTML semântico por padrão, então os links não são estilizados como botões lá. No entanto, se você estiver trabalhando com [HTML personalizado](#custom-html) ou fazendo alterações no nível do código, tenha isso em mente:

- **Links (`<a>`)** respondem à tecla <kbd>Enter</kbd>.
- **Botões (`<button>`)** respondem tanto à tecla <kbd>Enter</kbd> quanto à tecla <kbd>Espaço</kbd>.

Estilizar um link para parecer um botão pode confundir pessoas que navegam com um teclado—elas podem tentar pressionar <kbd>Espaço</kbd> e esperar que funcione.

Use o elemento certo para a ação:

- Use `<button>` para ações, como enviar um formulário ou abrir um modal.
- Use `<a>` para navegação, como vincular a outra página ou arquivo.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Alvos de toque

Alvos de toque são qualquer parte da sua mensagem que os usuários tocam para realizar uma ação, como botões, links ou ícones. Esses elementos precisam ser grandes o suficiente e espaçados adequadamente para que as pessoas possam tocá-los facilmente, especialmente em dispositivos móveis.

Quando os alvos de toque são muito pequenos ou muito próximos, pode ser frustrante ou impossível para usuários com desafios de mobilidade ou destreza interagir com sua mensagem. Melhorar isso pode ajudar a reduzir erros e criar uma experiência mais fluida para todos.

Aqui está o que você deve ter em mente:
- **Use um tamanho de alvo de toque adequado.** Aposte em um tamanho mínimo de alvo de toque de 44 x 44 pixels. Isso está alinhado com as diretrizes WCAG 2.2 para [alvos de toque](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) e padrões comuns de usabilidade móvel.
- **Dê espaço para cada alvo.** Se os alvos de toque estiverem muito próximos—como links empilhados ou botões agrupados—pode ser fácil errar ou tocar no errado. Adicione espaçamento ou preenchimento entre os elementos para evitar isso.
- **Não confie apenas em visuais.** Mesmo ícones pequenos podem ser tornados mais utilizáveis com preenchimento extra, permitindo que atendam aos requisitos de tamanho mínimo sem alterar o layout.
- **Prévia em dispositivos móveis.** Teste sua mensagem em diferentes tamanhos de tela e certifique-se de que os elementos interativos sejam fáceis de usar.

Melhorar os alvos de toque é uma das maneiras mais eficazes de tornar sua mensagem mais acessível em dispositivos móveis—e é uma boa experiência do usuário para todos.

### Imagens

#### Forneça texto alternativo

Texto alternativo (texto alt) é uma descrição curta do conteúdo ou função de uma imagem que leitores de tela e outras tecnologias assistivas fornecem aos usuários. Para cada imagem significativa, escreva um texto alt descritivo para que os usuários que não conseguem ver os visuais ainda entendam sua mensagem ou chamada à ação. 

#### Evite imagens de texto

Sempre que possível, evite colocar texto dentro de imagens—leitores de tela não conseguem ler texto baseado em imagem, e os usuários não conseguem ajustar facilmente o tamanho ou a cor da fonte para melhor visibilidade. Considere estas dicas:

- **Remova texto onde puder:** Mova qualquer texto descritivo ou promocional da imagem para um campo de texto em sua mensagem. Dessa forma, os usuários podem redimensioná-lo ou mudar a cor conforme necessário usando seu dispositivo ou preferências do navegador.
- **Teste de legibilidade e contraste:** Se você precisar manter o texto na imagem, siga as melhores práticas de [contraste de cores](#color-contrast) e use uma [fonte de grande escala](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Isso significa que o texto deve ter pelo menos 18 pontos (cerca de 24 pixels) para texto não negrito ou 14 pontos (cerca de 18 pixels) se for negrito. Usar esses tamanhos ajuda o texto a permanecer legível sem forçar os usuários a dar zoom, e melhora o contraste e a legibilidade geral do conteúdo. Teste para confirmar se ainda é legível em telas menores.
- **Forneça texto alternativo:** Para texto essencial que deve permanecer na imagem, inclua texto alternativo descrevendo as palavras.

Quando as imagens contêm texto que não pode ser editado, os usuários com deficiências visuais perdem a flexibilidade de fazer ajustes de leitura. Ao separar o texto das imagens, você ajuda mais usuários a ler e interagir com sua mensagem confortavelmente.

#### Dicas para escrever texto alternativo

- [Descreva o que realmente está na imagem](#tip-1)
- [Mantenha-o curto, mas específico](#tip-2)
- [Evite “imagem de” ou “foto de”](#tip-3) 
- [Refletir o texto que aparece na imagem](#tip-4)
- [Fique no contexto relevante—sem jargão de marketing extra](#tip-5)
- [Considere o propósito da imagem](#tip-6)

##### Descreva o que realmente está na imagem {#tip-1}

Usuários de leitores de tela dependem de texto alternativo para entender o conteúdo ou a função de uma imagem. Evite jargões de marketing genéricos que não correspondem ao que é mostrado visualmente.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Maus exemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mulher sorridente vestindo uma jaqueta jeans azul, segurando uma sacola de compras."</td>
      <td>"Hora de se mimar!" (Sem menção ao que realmente está na imagem)</td>
    </tr>
    <tr>
      <td>"Homem vestindo uma camiseta preta, encostado em uma bicicleta em uma rua da cidade."</td>
      <td>"Abrace sua melhor vida agora!" (Ignora a bicicleta e o cenário da cidade)</td>
    </tr>
    <tr>
      <td>"Prédio de apartamentos azul com uma placa de 'Para Alugar' na frente."</td>
      <td>"A chave para um amanhã melhor!" (Não reflete o apartamento ou a placa)</td>
    </tr>
  </tbody>
</table>

##### Mantenha curto, mas específico {#tip-2}

Texto alternativo conciso facilita o processamento para os usuários. Inclua detalhes suficientes para transmitir o propósito, mas evite qualquer enrolação. Como regra geral, mantenha o texto alternativo com 125 caracteres ou menos. Se algo mais do que uma breve frase ou sentença for necessário, considere usar um dos [métodos de descrição longa](https://www.w3.org/WAI/tutorials/images/complex/) do W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Maus exemplos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Tênis de corrida vermelhos em um fundo branco"</td>
      <td>"Tênis de corrida que são extremamente confortáveis e perfeitos para seu estilo de vida ativo em um tom vibrante de vermelho." (Muito longo e cheio de enrolação promocional)</td>
    </tr>
    <tr>
      <td>"Quatro laptops em um suporte de exibição"</td>
      <td>"Descubra o impulsionador de produtividade definitivo que redefine como você trabalha todos os dias, de todas as maneiras imagináveis." (Não descreve o que realmente está sendo mostrado)</td>
    </tr>
    <tr>
      <td>"Grupo de amigos comendo sorvete em um dia ensolarado"</td>
      <td>"Capture a pura felicidade com o doce mais gostoso—a vida é melhor com nossa marca de sorvete!" (Muito abstrato e focado na marca)</td>
    </tr>
  </tbody>
</table>

##### Evite "imagem de" ou "foto de" {#tip-3}

Leitores de tela já anunciam uma imagem. Vá direto para descrever o assunto.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Maus exemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mesa posta para brunch com panquecas, frutas e café."</td>
      <td>"Imagem de uma mesa posta para brunch"</td>
    </tr>
    <tr>
      <td>"Outdoor na estrada com texto em destaque 'Grande Abertura'"</td>
      <td>"Foto de um outdoor ao lado da estrada"</td>
    </tr>
    <tr>
      <td>"Paisagem montanhosa coberta de neve ao pôr do sol"</td>
      <td>"Foto de neve e montanhas"</td>
    </tr>
  </tbody>
</table>

##### Refletir o texto que aparece na imagem {#tip-4}

Se uma imagem incluir texto essencial, coloque essa informação no texto alternativo para que os usuários não percam.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Maus exemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Banner com a frase ‘Promoção de Verão—50% de desconto em toda a moda praia.'"</td>
      <td>"Banner promovendo uma venda." (Não menciona o desconto real)</td>
    </tr>
    <tr>
      <td>"Logo com o texto ‘Café Toscana' em fonte cursiva"</td>
      <td>"Imagem do logo de um café." (Não inclui o texto ‘Café Toscana')</td>
    </tr>
    <tr>
      <td>"Anúncio de ‘Ingressos para o Concerto Disponíveis Agora—Começa em 5 de Junho'"</td>
      <td>"Anúncio de concerto." (Sem detalhes do evento)</td>
    </tr>
  </tbody>
</table>

##### Mantenha-se no contexto relevante—sem jargões de marketing extras {#tip-5}

Não encha o texto alternativo com termos de SEO ou chamadas para ação que não estejam diretamente relacionadas à imagem. Forneça valor para aqueles que não podem ver a imagem.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Maus exemplos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Laptop mostrando o gráfico de análise do dashboard do Braze"</td>
      <td>"Aumente as conversões e dispare o ROI com a melhor plataforma do mundo!" (Adiciona linguagem de marketing desnecessária)</td>
    </tr>
    <tr>
      <td>"Conjunto de pátio no quintal com quatro cadeiras e uma mesa de vidro"</td>
      <td>"Organize uma incrível festa de verão para todos os seus amigos e familiares agora!" (Descreve um cenário, não a imagem)</td>
    </tr>
    <tr>
      <td>"Celular exibindo um aplicativo de previsão do tempo com 75°F visível"</td>
      <td>"Experimente inovações em tempo real no rastreamento do clima que são revolucionárias" (Não reflete o que está visivelmente mostrado)</td>
    </tr>
  </tbody>
</table>

##### Considere o propósito da imagem {#tip-6}

Se uma imagem estiver funcionando como um link ou chamada para ação, descreva a ação pretendida ("Comprar", "Link para", "Inscrever-se"), não apenas o rótulo ou produto mostrado.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Maus exemplos <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Compre a Coleção de Outono"</td>
      <td>"Coleção de Outono" (Falta a ação pretendida)</td>
    </tr>
    <tr>
      <td>"Link para eBook gratuito"</td>
      <td>"eBook gratuito" (Não deixa claro que é um link)</td>
    </tr>
    <tr>
      <td>"Inscreva-se na lista de e-mails"</td>
      <td>"Lista de e-mails" (Não descreve o que o usuário pode fazer)</td>
    </tr>
  </tbody>
</table>

Se a imagem não tiver um propósito, deixe isso claro também. Imagens decorativas, como logotipos, devem ter uma tag alt vazia (`alt=""`) para que leitores de tela saibam pular o anúncio. Sem isso, geralmente o nome do arquivo da imagem é lido em vez disso.

### Vídeos

Vídeos são envolventes, mas se não forem acessíveis, você corre o risco de excluir parte do seu público. Use as seguintes dicas para tornar seu conteúdo de vídeo mais inclusivo:

- [Fornecer legendas ocultas](#closed-captions)
- [Fornecer controles de reprodução](#playback-controls)
- [Evitar reprodução automática](#no-auto-play)
- [Evitar conteúdo piscante ou com estroboscópio](#no-seizures)

#### Fornecer legendas fechadas {#closed-captions}

Inclua legendas fechadas com seus vídeos para que os usuários possam acompanhar o diálogo, os efeitos sonoros e outros conteúdos de áudio. As legendas ajudam:

- Pessoas surdas ou com dificuldades auditivas
- Espectadores assistindo em um ambiente sem som
- Falantes não nativos que preferem ler junto

As legendas fechadas podem ser ativadas ou desativadas, permitindo que os usuários escolham o que funciona melhor para eles.

{% multi_lang_include accessibility/video.md %}

#### Fornecer controles de reprodução {#playback-controls}

Certifique-se de que seu vídeo incorporado inclua controles de reprodução acessíveis—como reproduzir, pausar, silenciar e buscar—para que os usuários possam interagir com ele da maneira que funciona melhor para eles.

#### Evitar reprodução automática {#no-auto-play}

Sempre que possível, evite configurar vídeos para reproduzir automaticamente. A reprodução automática pode ser desconcertante ou desorientadora para:

- Usuários que dependem de leitores de tela ou navegação por teclado
- Pessoas com sensibilidade ao movimento
- Qualquer um em um ambiente silencioso (como um local de trabalho ou ambiente noturno)

Deixe os usuários escolherem quando reproduzir um vídeo, incluindo controles claros.

#### Evitar conteúdo piscante ou com estroboscópio {#no-seizures}

Não inclua vídeos com efeitos de piscar ou estroboscópicos, especialmente em alta frequência. Esses podem disparar convulsões em usuários com epilepsia fotossensível e causar desconforto para outros.

### Contraste de cores

Um contraste de cor suficiente ajuda a garantir que suas mensagens sejam fáceis de ler para todos, incluindo pessoas com baixa visão ou aquelas que visualizam seu conteúdo em condições brilhantes ou desafiadoras. Busque por razões de contraste que atendam aos requisitos de nível AA da [WCAG 2.2](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Razão de contraste de 4.5:1 para texto normal (pense em texto do corpo, botões e links)
- Razão de contraste de 3:1 para texto grande (pense em cabeçalhos e rótulos maiores)

Você pode testar suas escolhas de cores usando a [Ferramenta de Verificação de Contraste WebAim](https://webaim.org/resources/contrastchecker/).

{% multi_lang_include accessibility/color.md %}

### HTML personalizado

Se você usar algum HTML personalizado em seu envio de mensagens:

- Use [HTML semântico](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Isso significa usar os elementos HTML corretos para a finalidade pretendida, em vez de estilizar um elemento para que se pareça com outro. A maioria dos elementos HTML tem seu próprio suporte de acessibilidade incorporado.
- Defina o [atributo](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) `lang` dentro do seu HTML para identificar o idioma em que seu conteúdo está escrito. Os leitores de tela usam diferentes bibliotecas de sons para cada idioma com base na pronúncia e nas características desse idioma. Se isso não for especificado, um leitor de tela assume que o conteúdo está escrito no idioma padrão que o usuário escolheu ao configurar o leitor de tela. Se a mensagem não estiver realmente no idioma padrão, o leitor de tela pode não pronunciar a mensagem corretamente. 

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Ao usar o editor de arrastar e soltar de e-mail, o valor do idioma para o e-mail pode ser definido acessando a guia **Configurações** e selecionando o valor de idioma apropriado.
{% endalert %}

- Use [atributos ARIA](#aria-attributes) para fornecer contexto extra. Esses atributos fornecem informações adicionais para tecnologias assistivas, ajudando a esclarecer o papel, estado ou propriedades de elementos de UI que podem ser, de outra forma, pouco claros. 

### Atributos ARIA

Quando você estiver usando código personalizado nos editores Braze, pode usar Aplicativos da Internet Ricos Acessíveis ([ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)) para fornecer suporte extra de acessibilidade para usuários que dependem de tecnologia assistiva. Os papéis e atributos ARIA ajudam os leitores de tela a interpretar seu conteúdo de forma mais clara, especialmente quando você está usando elementos que não transmitem significado por si só (como `<div>` ou `<span>`).

{% alert important %}
Embora o ARIA seja projetado para tornar o conteúdo da web mais acessível, se usado incorretamente, pode fazer mais mal do que bem. ARIA não substitui HTML semântico, ele o complementa—portanto, use ARIA apenas quando elementos HTML nativos não atenderem às suas necessidades.
{% endalert %}

Aqui estão alguns exemplos que são especialmente úteis em contextos de envio de mensagens:

- [aria-label](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentation"](#rolepresentation)
- [aria-live="polite"](#aria-livepolite)

#### aria-label

`aria-label` adiciona um nome acessível a elementos que não têm texto visível. Se você estiver usando um ícone sem texto (como uma lixeira ou “X” para fechar), alguém que usa um leitor de tela não saberá o que ele faz—exceto se você rotulá-lo. `aria-label` dá uma voz a esse ícone.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby

`aria-labelledby` conecta um elemento a algo que já tem um rótulo visível. Então, se você tiver um banner ou região que deve ser lida em voz alta com um título, você pode usar `aria-labelledby` para dizer à tecnologia assistiva: “Ei, use aquele cabeçalho ali para nomear esta parte.”

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true"

`aria-hidden="true"` oculta coisas de leitores de tela.  É útil para texto ou visuais que não transmitem um significado importante—como um brilho, marca de seleção ou emoji usado puramente para estilo.

Isso mantém a experiência mais limpa para usuários de leitores de tela, que de outra forma poderiam ouvir conteúdo redundante ou confuso. Também é útil para ocultar coisas como conteúdo de acordeão fora da tela que ainda não foi expandido.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

Em geral, é melhor usar `alt=""` para [imagens decorativas](#images) e ícones em vez de `aria-hidden="true"`. Embora HTML semântico seja amplamente suportado por todos os leitores de tela e software assistivo, o suporte a ARIA varia. Mesmo que você use `aria-hidden`, ainda deve incluir um atributo alt vazio.

#### role="presentation"

`role="presentation"` diz à tecnologia assistiva para ignorar elementos apenas de layout, como tabelas de design. Por exemplo, os e-mails costumam usar tabelas apenas para alinhar as coisas. Sem esse papel, os leitores de tela podem assumir que seu layout é uma tabela de dados e começar a ler números de linhas e colunas.  

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

E-mails criados no editor de arrastar e soltar têm elementos de apresentação automaticamente marcados com o atributo ARIA `role="presentation"`.

#### aria-live="polite"

`aria-live="polite"` anuncia atualizações quando o conteúdo muda sem necessidade de interação do usuário. Use-o quando você exibir atualizações dinâmicas dentro de uma mensagem, como sucessos, erros ou outras notificações.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Teste de acessibilidade automatizado

Para ajudar você a identificar e corrigir problemas de acessibilidade cedo, a Braze oferece testes de acessibilidade automatizados nas seguintes áreas:

- [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) para e-mails
- [Scanner de acessibilidade]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=in-app%20message#accessibility-scanner) para mensagens criadas usando nosso editor de HTML (por exemplo, mensagens HTML no aplicativo, Blocos de Conteúdo HTML, [rodapés de e-mail personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer), [páginas de aceitação de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-opt-in-page) e [páginas de cancelamento de inscrição de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-unsubscribe-page)).

Esses testes verificam sua mensagem em relação às Diretrizes de Acessibilidade para Conteúdo da Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) - um conjunto de padrões técnicos reconhecidos internacionalmente para conteúdo acessível. Quaisquer problemas que possam ser detectados automaticamente são sinalizados e categorizados por gravidade para ajudar você a priorizar.

{% alert note %}
Inbox Vision funciona tanto para e-mails HTML quanto para e-mails de arrastar e soltar. O scanner só funciona em conteúdo criado com o editor de HTML.
{% endalert %}

### O que os testes automatizados podem e não podem detectar

Os testes de acessibilidade automatizados são um ótimo ponto de partida - mas não conseguem detectar tudo. Alguns problemas precisam de um toque humano para serem avaliados corretamente, especialmente quando o contexto ou o design visual desempenham um papel na experiência do usuário com seu e-mail.

Você pode ver alguns problemas marcados como **Precisa de revisão**. Esses são casos em que o verificador não consegue dizer com certeza se algo é um problema de acessibilidade. Quando isso acontece, recomendamos revisar manualmente.

Alguns exemplos do que ferramentas automatizadas não conseguem detectar de forma confiável incluem:

- Se a ordem de foco dos elementos interativos segue uma sequência lógica
- Se o conteúdo é totalmente operável com um teclado, sem exigir um mouse
- Se o texto alternativo descreve de forma significativa uma imagem
- Se os cabeçalhos são usados corretamente para organizar o conteúdo
- Se os links e botões estão claramente rotulados e são fáceis de entender
- Se os alvos de toque são grandes o suficiente e espaçados adequadamente
- Se o texto em imagens de fundo atende aos requisitos de contraste de cor
- Se as instruções ou rótulos são claros e úteis para todos os usuários

Essas limitações não são exclusivas do Braze—são comuns a todas as ferramentas automatizadas de acessibilidade. Verificações automatizadas não conseguem imitar toda tecnologia assistiva, leitor de tela ou necessidade do usuário. É por isso que a acessibilidade não é uma verificação única—é uma prática contínua.

Mesmo que sua mensagem passe por todas as verificações automatizadas, ainda é importante:

- Revisar cuidadosamente os problemas sinalizados, especialmente aqueles rotulados como **Necessita revisão**.
- Testar manualmente sempre que possível, especialmente para padrões de layout e interação.
- Usar ferramentas como leitores de tela, navegação apenas com teclado e zoom do navegador para simular diferentes necessidades de acesso.

Ao combinar testes automatizados com uma revisão manual cuidadosa, você identificará mais problemas potenciais e criará campanhas mais inclusivas e utilizáveis para cada destinatário.
