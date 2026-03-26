---
nav_title: Guia de estilo do Braze Docs
article_title: Guia de estilo do Braze Docs
description: "Guia de estilo de escrita para o Braze Docs."
page_order: 0
noindex: true
---

# Guia de estilo do Braze Docs

## Guia de estilo de escrita

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

### Diretrizes gerais {#general-guidelines}

#### Voz e tom {#voice-and-tone}

A voz da marca Braze é inteligente, conversacional e direta. Somos uma voz humana em um mundo de jargões tecnológicos; oferecemos clareza e orientação a qualquer pessoa interessada na arte do engajamento do cliente; e evitamos jargões em favor de uma linguagem concisa que é tão fácil de entender quanto poderosa.

Para alinhar essa voz de marca em nossa escrita e edição, usamos três diretrizes de voz: **direta, empoderadora** e **humana**.

##### Direta

Estruture sua escrita de forma clara e facilite para as pessoas encontrarem as informações de que precisam.

* Explique coisas complicadas de forma simples.
* Seja conciso.
* Use linguagem consistente para recursos e ações.

###### Diretrizes

✅ Use recursos visuais para ajudar a esclarecer assuntos complexos. <br>
**Exemplo:** A imagem do ciclo de vida do perfil de usuário no [artigo Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) ajuda a ilustrar um conceito complicado.

✅ Crie uma hierarquia de informações clara. <br>
**Exemplo:** "Esta é uma visão geral de como o conteúdo é gerenciado no Braze Docs. Para saber mais sobre um tópico específico, escolha a página dedicada ao tópico na navegação."

✅ Elimine jargões e siglas sempre que possível. Se não for possível, defina-os. <br>
**Exemplo:** "O Short Messaging Service (SMS) é usado para enviar e receber mensagens de texto curtas."

##### Empoderadora

Qual problema você está tentando resolver com sua escrita? Mantenha esse problema em mente ao criar qualquer conteúdo.

* Explique o "porquê" e o "como" para dar aos usuários a confiança para agir.
* Seja específico ao explicar benefícios e seja claro sobre o que é e o que não é possível.
* Ofereça conselhos práticos e incentivo sincero.

###### Diretrizes

✅ Facilite encontrar o caminho ideal. <br>
**Exemplo:** "Quando você interrompe um Canvas, o seguinte se aplica: 1. Os usuários são impedidos de entrar no Canvas. 2. Nenhuma mensagem adicional é enviada, independentemente de onde o usuário esteja no fluxo. 3. **Exceção:** Canvases de e-mail não param imediatamente."

✅ Forneça exemplos, casos de uso e modelos que simplifiquem ou elevem o trabalho do usuário. <br>
**Exemplo:** "`IInAppMessageManagerListener` também inclui métodos delegados para cliques na própria mensagem ou em um dos botões. Um caso de uso comum seria interceptar uma mensagem quando um botão ou mensagem é clicado para processamento adicional."

##### Humana

A escrita informativa é inerentemente seca — queremos que os leitores se concentrem no conteúdo, não na entrega. Ainda assim, podemos escrever de uma forma que ajude nossos leitores a processar as informações que estão consumindo e torne mais provável que internalizem o conhecimento. Seja humano, deixe sua personalidade aparecer e seja memorável.

* Busque um tom conversacional em vez de formal.
* Foque no usuário; respeite sua situação e estado emocional.
* Centralize ativamente a experiência humana, não o estado da máquina.

###### Diretrizes

✅ Aplique o tom e os recursos da marca de forma cuidadosa. <br>
**Exemplo:** "Integrar com a Braze é um processo que vale a pena. Mas você é inteligente. Você está aqui. Claramente, você já sabe disso."

✅ Aplique as [melhores práticas de acessibilidade](#accessibility) tanto para conteúdo visual quanto verbal. <br>
**Exemplo:** Substituir expressões idiomáticas como "out-of-the-box" por "padrão" torna seu texto mais acessível para falantes de inglês como segunda língua.

✅ Forneça suporte consistente ao longo da jornada do usuário. <br>
**Exemplo:** Use o framework Diátaxis para garantir que você está atendendo às necessidades de diferentes usuários em diferentes momentos.

#### Acessibilidade {#accessibility}

A Braze busca oferecer uma experiência inclusiva. Use as diretrizes a seguir para garantir que seu conteúdo de aprendizado seja acessível para as [1 bilhão de pessoas](https://www.who.int/en/news-room/fact-sheets/detail/disability-and-health) com necessidades de acessibilidade.

##### Geral

* Evite linguagem tendenciosa ou capacitista. Para mais informações, consulte a seção sobre [Linguagem inclusiva](#inclusive-language).
* Use um [leitor de tela](https://support.apple.com/guide/mac-help/use-accessibility-features-mh35884/mac) para testar seu conteúdo.
* Não use um [e comercial](#ampersands) (&) no lugar de "e", a menos que esteja referenciando elementos da interface que usam e comercial.

##### Linguagem e formatação

* Use [linguagem simples](https://www.plainlanguage.gov/guidelines/).
* Coloque as informações mais importantes no início das seções. Use o modelo jornalístico da [pirâmide invertida](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)).
* Quebre blocos de texto para ajudar os leitores a escanear informações. Use parágrafos, [listas](#lists), [alertas](#callouts-and-alerts) e [imagens](#figures-and-other-images) para melhorar a legibilidade.
* [Escreva frases e parágrafos curtos](https://www.usability.gov/how-to-and-tools/methods/writing-for-the-web.html). Como regra geral, busque no máximo 20 palavras por frase e cinco frases por parágrafo.
* Evite usar siglas e frases em latim, pois podem ser difíceis de traduzir. Em vez disso, use palavras ou frases simples.

##### Títulos

* Use [títulos e cabeçalhos](#headings-and-titles) únicos, descritivos e claros.
* Use um h1 para títulos de página.
* Não pule níveis de título. Um h3 deve seguir um h2, e assim por diante.

##### Links

* Não use textos de link como "Saiba mais", "aqui" ou "este documento". Para mais frases a evitar, consulte a seção [Escrevendo links](#writing-links).
* Evite colocar dois links consecutivos em uma frase. Coloque um caractere ou palavra entre eles para separá-los.
* [Links para download de arquivos](#links-for-file-download) devem indicar que clicar no link faz o download do arquivo, bem como o tipo de arquivo (PDF, CSV, etc.)
* Se não estiver claro pelo contexto, links para seções no mesmo documento devem usar uma [frase padrão](#structuring-links) indicando essa ação.

##### Imagens, vídeos e GIFs

* Forneça [texto alternativo](#alt-text) para cada imagem que resuma as informações apresentadas na imagem.
* Não use imagens como a única forma de mostrar informações. Sempre forneça os passos, conteúdo ou outros detalhes apresentados na imagem no texto ao redor.
* Não use imagens de saída de terminal, exemplos de código ou texto. Em vez disso, use texto real.
* Forneça legendas para conteúdo em vídeo.
* Não use elementos piscantes em vídeos ou GIFs.

##### Tabelas {#tables-1}

* Sempre use uma frase introdutória para descrever o propósito da tabela.
* Evite tabelas no meio de uma lista, especialmente uma lista de passos.

#### Público global {#global-audience}

Escrevemos nosso conteúdo de aprendizado em inglês americano. No entanto, a Braze é uma marca global e, como tal, escrevemos para um público global. Use as diretrizes a seguir para garantir que os clientes entendam sua escrita mesmo quando o inglês não é sua primeira língua.

1. **Escreva pensando na localização:**
  * Formate [datas e horários](#dates-and-times) de formas não ambíguas.
  * Não coloque sobreposições de texto em imagens, pois esse texto não pode ser traduzido.
  * Evite [gírias e expressões idiomáticas](#slang-and-idioms).
  * Forneça contexto. Não presuma que o leitor sabe do que você está falando.
2. **Escreva frases curtas e precisas:**
  * Use [linguagem simples](https://www.plainlanguage.gov/guidelines/).
  * Defina [abreviações](#abbreviations).
  * Evite [pronomes ambíguos](#ambiguous-pronouns). Se um pronome puder ser ambíguo, substitua-o pelo substantivo apropriado.
3. **Seja consistente:**
  * Use o mesmo termo para um conceito em todas as menções do termo, incluindo a mesma capitalização e formatação de texto.
  * Escreva frases na ordem sujeito + verbo + objeto.
  * Se as instruções dependem de uma condição ser atendida, coloque a cláusula condicional primeiro. Para mais informações, consulte [ordem das cláusulas](#clause-order).
4. **Seja inclusivo:**
  * Use [linguagem inclusiva](#inclusive-language).
  * Use [nomes de exemplo](#example-names) diversos.
  * Evite humor culturalmente específico.

#### Linguagem inclusiva {#inclusive-language}

Podemos ser uma empresa B2B, mas as pessoas estão no centro do que fazemos, e a nossa é uma marca global. Sempre que nos referimos a uma pessoa em nosso conteúdo, somos cuidadosos em ser inclusivos e atenciosos. Em caso de dúvida, consulte esta seção ou [The Diversity Style Guide](https://www.diversitystyleguide.com/).

##### Idade

A menos que seja relevante para sua escrita, não se refira à idade de um sujeito. Não use qualificadores como "jovem" ou "velho" para descrever qualquer sujeito ou público.

Se você está representando uma faixa etária, seja descritivo e específico como "Geração Z" em vez de "juventude". Não use descritores vagos como "idade universitária" quando poderia dizer "estudantes universitários".

##### Cor

Evite incluir termos de cor em sua escrita, a menos que seja absolutamente necessário, e se necessário, inclua texto explicativo.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Pressione ✅ Salvar.</td><td style="width: 50%;">Pressione o ícone verde Salvar.</td></tr>
<tr><td style="width: 50%;">Pressione o ícone de marca de verificação verde.</td><td style="width: 50%;">Pressione o ícone verde ao lado do botão vermelho Cancelar.</td></tr>
<tr><td style="width: 50%;">Pressione o ícone verde.</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

Não dependa da cor como único indicador para elementos interativos. Por exemplo, sublinhe links ao passar o mouse ou marque um campo obrigatório com um asterisco.

Evite depender exclusivamente de verde e vermelho para indicadores de "bom" e "ruim" (ou, mais frequentemente, "faça" e "não faça"). O daltonismo vermelho/verde é o tipo mais comum de daltonismo. Se você usar cor para comunicar o que fazer e o que não fazer, certifique-se de incluir também outros textos ou símbolos para transmitir o mesmo ponto.

##### Linguagem condescendente {#condescending-language}

Ao escrever instruções ou detalhar passos para o leitor seguir, evite usar palavras ou frases como:

* simples, como "Criar uma campanha é simples."
* simplesmente, como "...simplesmente adicione X em Y"
* apenas, como "...apenas instale X"
* "É fácil"

Se alguém tiver dificuldade com os passos ou instruções, seus descritores casuais podem parecer condescendentes. Você também pode excluir involuntariamente pessoas da sua documentação que interpretam isso como um indicador de que não são habilidosas o suficiente para seguir suas instruções.

##### Clientes versus consumidores

Ao se referir aos usuários da empresa e seus consumidores, use os seguintes termos adequadamente:

* **Clientes:** Marcas com as quais trabalhamos. Nunca se refira aos nossos clientes como "clients".
 * **Usuários da empresa:** No contexto da documentação, quando é importante distinguir entre usuários da plataforma e os usuários finais que recebem mensagens de marketing, use "usuários da empresa".
* **Consumidores:** Clientes de uma marca com a qual trabalhamos.
* **Usuários:** Geralmente reservado para uma estatística específica que depende de métricas de "usuário" (como "retenção de usuários"). Ao se referir a "usuários" em nosso conteúdo, primeiro tente ser mais específico. Pense em compradores, consumidores, pacientes, jogadores.

##### Departamentos e equipes

Capitalize os nomes de departamentos ou equipes. Não capitalize "equipe" ou "departamento".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Marketing, Business Intelligence equipe de Produto</td><td style="width: 50%;">marketing, business intelligence Equipe de Produto</td></tr>
<tr><td style="width: 50%;">departamento de Receita</td><td style="width: 50%;">Departamento de Receita</td></tr>
</tbody>
</table>
{:/}

##### Deficiência

Não se refira à deficiência de uma pessoa, a menos que seja especificamente relevante para sua escrita. Nesse caso, seja atencioso e pergunte se o sujeito prefere linguagem centrada na identidade ou centrada na pessoa. Ao se referir a um sujeito com deficiência, não use termos como "deficiente" de forma pejorativa.

Linguagem capacitista inclui palavras ou frases como "louco", "insano", "cego para" ou "fazer vista grossa", "aleijado", "burro" e outras. Escolha palavras alternativas dependendo do contexto.

##### Doença

Ao descrever uma doença, evite palavras como "sofrer", "lutar" ou "vítima". Busque ser neutro e objetivo.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Ela foi diagnosticada com câncer.</td></tr>
<tr><td style="width: 100%;">Eles vivem com HIV.</td></tr>
<tr><td style="width: 100%;">Ele se recuperou do AVC.</td></tr>
</tbody>
</table>
{:/}


##### Inclusividade no conteúdo

Destaque e represente uma comunidade diversa. Seja atencioso e inclusivo ao envolver nossos clientes, palestrantes, especialistas do setor e membros da equipe da Braze.

##### Cargos

Quando se trata de cargos, nos desviamos do estilo AP. Em todos os casos, capitalizamos cargos ao nos referir a alguém especificamente.

###### Cargo com nome da empresa

Capitalize cargos formais quando vierem antes ou depois do nome de uma pessoa. Formatamos de três maneiras:

1. **[Cargo Formal]** na **[Nome da Empresa]** + **[Nome Completo]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Creative Director na PantsLabyrinth David Bowie</td><td style="width: 50%;">creative director na PantsLabyrinth David Bowie</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Nome Completo]** + vírgula + **[Cargo Formal]** na **[Nome da Empresa]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">David Bowie, Creative Director na PantsLabyrinth</td><td style="width: 50%;">David Bowie, creative director na PantsLabyrinth</td></tr>
</tbody>
</table>
{:/}

{: start="3"}
3. **[Nome da Empresa]** + **[Cargo Formal]** + **[Nome Completo]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">PantsLabyrinth Creative Director David Bowie</td><td style="width: 50%;">PantsLabyrinth creative director David Bowie</td></tr>
</tbody>
</table>
{:/}

###### Cargo sem nome da empresa

Ao se referir a uma pessoa específica pelo cargo formal, capitalize o cargo formal e o nome assim:

1. **[Cargo Formal]** + **[Nome Completo]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CEO Robin Fenty</td><td style="width: 50%;">Chief executive officer Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Cargo Formal]** + vírgula + **[Nome Completo]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">SVP, Product, Robin Fenty</td><td style="width: 50%;">senior vice president, product, Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

###### Outros

Cargos formais são "na [EMPRESA]." Fundadores e Cofundadores são "da [EMPRESA]." Cargos formais e ocupações por si só não precisam ser capitalizados.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Escrevi para o chief data officer deles.</td><td style="width: 50%;">Escrevi para o Chief Data Officer deles</td></tr>
<tr><td style="width: 50%;">Conversamos com vários analistas de business intelligence.</td><td style="width: 50%;">Conversamos com vários Analistas de Business Intelligence.</td></tr>
<tr><td style="width: 50%;">Entre em contato com seu gerente de conta da Braze.</td><td style="width: 50%;">Escrevi para o Chief Data Officer deles Entre em contato com seu Gerente de Conta da Braze.</td></tr>
</tbody>
</table>
{:/}

Siga cargos neutros em termos de gênero, a menos que o gênero já tenha sido estabelecido.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">vendedor(a)</td><td style="width: 50%;">vendedor/vendedora</td></tr>
</tbody>
</table>
{:/}

Abrevie cargos quando apropriado, como VP ou SVP, se é assim que a pessoa se refere ao seu cargo. Em caso de espaço de texto limitado, abreviações padrão (VP, SVP, Sr. ou Jr.) são aceitáveis.

##### Gênero

Não faça suposições sobre o gênero das pessoas. Pergunte aos sujeitos que aparecem em seu conteúdo como se identificam.

Ao se referir a membros da comunidade, "queer" é aceitável. "Gay" não é. Você pode se referir a um grupo de pessoas como "LGBTQ". Não use isso para descrever um indivíduo.

Ao se dirigir a grupos de pessoas em seu conteúdo, evite atribuir gênero ao seu público (exemplo: "OK, meninas!"). Use expressões neutras em termos de gênero (exemplo: "Vamos lá, pessoal!").

"Eles/elas/deles/delas" é sempre aceitável como pronome singular ou plural em todo o nosso conteúdo.

##### Saúde mental

Saúde mental e doenças cobrem uma ampla gama de condições. A menos que seja relevante para o que você está escrevendo, não se refira à saúde mental de uma pessoa. Evite palavras e frases estigmatizantes. Não use termos médicos coloquialmente (exemplo: "O estado deprimente das coisas...").

##### Nomes

Na primeira vez que mencionar uma pessoa, use seu primeiro nome e nome completo. A partir daí, use o primeiro ou último nome ao se referir a ela.

##### Pronomes

Para informações sobre o uso apropriado de pronomes, consulte a seção de Linguagem e Gramática sobre [Pronomes](#pronouns).

##### Raça, religião e etnia

Não se refira à raça, religião ou etnia de uma pessoa, a menos que seja relevante para o que você está escrevendo. Em textos onde raça ou etnia são fatores, pergunte ao sujeito como se identifica.

Não use hífen para indicar dupla herança ou religião. Em vez disso, use um espaço.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Muslim American</td><td style="width: 50%;">Muslim-American</td></tr>
<tr><td style="width: 50%;">Cuban American</td><td style="width: 50%;">Cuban-american</td></tr>
</tbody>
</table>
{:/}

Capitalize os nomes próprios de etnias, nacionalidades, povos e tribos.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cambodian</td><td style="width: 50%;">cambodian</td></tr>
<tr><td style="width: 50%;">Black Americans</td><td style="width: 50%;">black Americans</td></tr>
</tbody>
</table>
{:/}

Capitalize os nomes de religiões ou termos religiosos.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Bahá'í Faith</td><td style="width: 50%;">bahá'í faith</td></tr>
<tr><td style="width: 50%;">Buddhist</td><td style="width: 50%;">buddhist</td></tr>
</tbody>
</table>
{:/}

Não se aproprie de palavras ou expressões que pertencem ao Inglês Vernáculo Afro-Americano (on fleek, bae, lit, woke).

Não se aproprie de palavras ou expressões específicas de povos indígenas (exemplo: spirit animal, powwow).

#### Fontes de terceiros {#third-party-sources}

Nunca copie conteúdo de outros sites, pois isso pode violar direitos autorais. O conteúdo pode ser tanto texto quanto imagens.

Em vez de copiar ou citar sites de terceiros, parafraseie o conteúdo ou forneça um link para o site de terceiros para mais informações. Para mais informações, consulte [Links para outros sites](#links-to-other-sites).

### Linguagem e gramática {#language-and-grammar}

Manter-se alinhado com a gramática e mecânica acordadas nos ajuda a manter nossa escrita clara e consistente. Esta seção cobre o que tentamos seguir em nossa documentação técnica, salvo indicação em contrário.

#### Abreviações {#abbreviations}

Abreviações, como siglas, iniciais e palavras encurtadas, podem prejudicar nossa clareza, voz e SEO.

Embora algumas abreviações sejam amplamente compreendidas, outras não são bem conhecidas ou são familiares apenas para um grupo específico de clientes. Use seu melhor julgamento e, como regra geral, não é necessário expandir uma abreviação se ela estiver listada no [American Heritage Dictionary](https://ahdictionary.com/).

Se uma abreviação não for bem conhecida, expanda-a na primeira menção, seguida da abreviação entre parênteses. Para todas as menções subsequentes do termo, use a abreviação.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Expanda abreviações incomuns na primeira menção</em></th><th style="width: 50%;">Não faça: <em>Expandir abreviações comuns</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Top-level domain (TLD)</td><td style="width: 50%;">Portable Document Format (PDF)</td></tr>
<tr><td style="width: 50%;">Universally unique identifier (UUID)</td><td style="width: 50%;">Universal Serial Bus (USB)</td></tr>
</tbody>
</table>
{:/}


Trate abreviações como palavras regulares ao torná-las plurais e não adicione apóstrofo — por exemplo, APIs e SDKs. O mesmo vale para qual artigo (um ou uma) você usa — observe como a abreviação é pronunciada. Quando uma abreviação começa com um som de vogal, use "um/uma"; para sons de consoante, use "um/uma".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça: <em>Use artigos dependendo de como a abreviação é pronunciada, não escrita</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">um ISP</td></tr>
<tr><td style="width: 100%;">uma DLL</td></tr>
<tr><td style="width: 100%;">um site HTML</td></tr>
<tr><td style="width: 100%;">um arquivo CSV</td></tr>
</tbody>
</table>
{:/}

#### Voz ativa {#active-voice}

Usamos a voz ativa na Braze sempre que possível. A voz ativa é nosso padrão ouro. Evite a voz passiva, na qual pode ser difícil determinar quem ou o que está realizando uma ação específica.

Para verificar se sua frase está na voz passiva, insira "por alguém" após o verbo. Se a frase fizer sentido — provavelmente está na voz passiva.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use voz ativa</em></th><th style="width: 50%;">Não faça: <em>Usar voz passiva, se possível</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">A Braze conecta consumidores às marcas que amam.</td><td style="width: 50%;">Os consumidores são conectados às marcas que amam.</td></tr>
<tr><td style="width: 50%;">A Braze exige que os colaboradores mantenham seus endereços atualizados.</td><td style="width: 50%;">Os colaboradores são obrigados a manter seus endereços atualizados.</td></tr>
<tr><td style="width: 50%;">Administradores da empresa podem configurar requisitos de autenticação para fazer login na Braze.</td><td style="width: 50%;">Os requisitos de autenticação para fazer login na Braze podem ser configurados por administradores da empresa.</td></tr>
</tbody>
</table>
{:/}

##### Exceções

É aceitável usar a voz passiva nos seguintes casos:

* Para minimizar a ênfase em um sujeito, geralmente para evitar culpar o leitor:
  - **Faça:** Dois erros foram encontrados no e-mail.
  - **Não faça:** Você criou dois erros no e-mail.
* Se saber quem é responsável pela ação não é importante:
  - **Faça:** Este artigo foi atualizado pela última vez em dezembro de 2020.

#### Artigos {#articles}

Use os artigos "um", "uma" e "o/a" para tornar sua escrita clara e auxiliar na tradução. Use "o/a" antes de um substantivo singular ou plural específico, e "um/uma" antes de um substantivo singular não específico.

Para determinar se você deve usar "um" ou "uma", observe o gênero do substantivo que segue. As mesmas diretrizes se aplicam a [Abreviações](#abbreviations).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça: <em>Use artigos dependendo do gênero do substantivo.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">uma hora</td></tr>
<tr><td style="width: 100%;">um minuto</td></tr>
<tr><td style="width: 100%;">um artigo de FAQ</td></tr>
<tr><td style="width: 100%;">um curso LAB</td></tr>
</tbody>
</table>
{:/}

#### Pronomes {#pronouns}

##### Pronomes pessoais

Use pronomes de segunda pessoa (você) sempre que possível.

Não se refira aos clientes da Braze como "usuário" em textos voltados ao público externo; em vez disso, fale diretamente com o leitor usando "você". Para se referir aos clientes dos nossos clientes, use "seus consumidores" ou, se a situação se relacionar a estatísticas de usuários, "seus usuários".

Evite pronomes de primeira pessoa (eu, nós, nosso) exceto nos seguintes casos:

* Entradas em FAQs. Por exemplo, "Como faço para redefinir minha senha?".
* Usar "nós" para se referir à Braze como organização.
 * Se não estiver claro a quem "nós" se refere, primeiro mencione a Braze pelo nome e depois use "nós" nas menções subsequentes.

##### Pronomes neutros em termos de gênero

Use os pronomes que seus sujeitos usam. Se houver qualquer incerteza, use formas neutras em termos de gênero. Não use "ele/ela" como alternativa.

Só use pronomes com gênero (ele/ela, dele/dela) se a pessoa a quem você está se referindo for realmente desse gênero.

##### Pronomes ambíguos {#ambiguous-pronouns}

Pronomes substituem substantivos. A palavra à qual um pronome se refere é chamada de antecedente. Ao escrever instruções ou material de aprendizado, certifique-se de fazer referências claras entre um pronome e seu antecedente. Isso pode exigir repetir sujeitos para tornar o significado claro.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Garanta que um pronome referencie claramente seu antecedente</em></th><th style="width: 50%;">Não faça: <em>Usar referências pronominais ambíguas</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Se você digitar texto no campo, o texto não muda.</td><td style="width: 50%;">Se você digitar texto no campo, ele não muda.</td></tr>
<tr><td style="width: 50%;">Ela disse a Sarah que a resposta de Sarah estava incorreta.</td><td style="width: 50%;">Ela disse a Sarah que sua resposta estava incorreta.</td></tr>
<tr><td style="width: 50%;">Você não pode editar uma campanha arquivada. Desarquive uma campanha para editá-la.</td><td style="width: 50%;">Você não pode editar uma campanha arquivada. Desarquive-a para editá-la.</td></tr>
</tbody>
</table>
{:/}

##### Pronomes opcionais

Para adicionar clareza à sua escrita e auxiliar na localização, use pronomes como "que", "o qual" e "quem".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use "que", "o qual" e "quem" para adicionar clareza.</em></th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Clique com o botão direito no link que você deseja abrir.</td><td style="width: 50%;">Clique com o botão direito no link você deseja abrir.</td></tr>
<tr><td style="width: 50%;">A partir daqui, você pode escolher qual coorte do Tinyclues deseja incluir.</td><td style="width: 50%;">A partir daqui, você pode escolher uma coorte do Tinyclues que deseja incluir.</td></tr>
</tbody>
</table>
{:/}

#### Capitalização {#capitalization}

Evite capitalização desnecessária. Na maioria dos casos, use capitalização de frase. A capitalização de título só deve ser usada para nomes próprios ou nomes de recursos.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use minúsculas para escrever URLs de sites e endereços de e-mail</em></th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">www.braze.com/docs</td><td style="width: 50%;">www.Braze.com/docs</td></tr>
<tr><td style="width: 50%;">sample@email.com</td><td style="width: 50%;">SAMPLE@EMAIL.COM</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use direcionais em minúsculas</em></th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">norte, sul, leste, oeste</td><td style="width: 50%;">Norte, Sul, Leste, Oeste</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Capitalize regiões específicas e use maiúsculas para regiões abreviadas</em></th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">o Noroeste</td><td style="width: 50%;">o noroeste</td></tr>
<tr><td style="width: 50%;">Sul de Connecticut</td><td style="width: 50%;">sul de Connecticut</td></tr>
<tr><td style="width: 50%;">Europa Oriental</td><td style="width: 50%;">europa oriental</td></tr>
<tr><td style="width: 50%;">APAC, EMEA</td><td style="width: 50%;">Apac, emea</td></tr>
</tbody>
</table>
{:/}

##### Marcas e produtos

Ao se referir a uma marca ou produto, use a capitalização que a marca usa. Na maioria dos casos, capitalize os nomes de marcas (Grindr, Walmart) e produtos (Benchmarks, Looker Blocks). É aceitável começar uma frase com minúscula se a primeira palavra for o nome estilizado de uma marca como eBay ou iTunes.

Para intercaps, sempre consulte o uso preferido pela marca em texto (OkCupid, YouTube). Não use intercaps que aparecem apenas em logotipos ou tratamentos de design gráfico (Amazon).

#### Ordem das cláusulas {#clause-order}

Se você quiser dizer ao leitor para fazer algo em uma circunstância específica, tente mencionar a circunstância antes de fornecer a instrução. Isso permite que o leitor pule a instrução se a circunstância não se aplicar.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Para passos de solução de problemas, consulte as FAQs de Campanhas.</td><td style="width: 50%;">Consulte as FAQs de Campanhas para passos de solução de problemas.</td></tr>
<tr><td style="width: 50%;">Para arquivar sua campanha, clique no ícone de engrenagem e selecione Arquivar.</td><td style="width: 50%;">Clique no ícone de engrenagem e selecione Arquivar para arquivar sua campanha.</td></tr>
</tbody>
</table>
{:/}

#### Formas combinadas {#combining-forms}

[Hifenize](#hyphens) formas combinadas quando a frase é usada como adjetivo antes do substantivo.

**Exemplo:** Um item único

#### Contrações {#contractions}

Uma contração é uma versão encurtada de uma palavra ou frase. Use contrações para manter um tom acessível e informal. No entanto, não use contrações de substantivo e verbo ou contrações duplas, ou uma combinação de duas contrações. Estas podem interromper o fluxo e a coerência da frase.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use contrações</em></th><th style="width: 50%;">Não faça: <em>Usar contrações de substantivo e verbo</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Se você é admin, pode gerenciar as informações de contato da sua empresa.</td><td style="width: 50%;">A Braze agora vai suportar integração com Shoptify.</td></tr>
<tr><td style="width: 50%;">Você não pode editar uma campanha arquivada.</td><td style="width: 50%;">Você talvez não tenha visto o tamanho restrito de upload.</td></tr>
</tbody>
</table>
{:/}

#### Modificadores soltos e mal posicionados {#dangling-and-misplaced-modifiers}

Modificadores são palavras ou frases que modificam outras palavras ou frases. Um modificador solto não modifica nenhum sujeito na frase. Um modificador mal posicionado está longe do sujeito que deveria modificar. Essencialmente, modificadores soltos e mal posicionados podem causar confusão ao se conectar à parte errada da frase.

Escrever com voz ativa ajuda a prevenir o uso de modificadores soltos e mal posicionados. Certifique-se de usar um modificador que modifique claramente.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Mantenha frases curtas e concisas. Use voz ativa.</em></th><th style="width: 50%;">Não faça: <em>Usar frases longas com modificadores que podem causar confusão</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Os clientes devem configurar suas definições de SAML.</td><td style="width: 50%;">Você pode ter mensagens de teste em suas campanhas que podem ser excluídas.</td></tr>
<tr><td style="width: 50%;">Certifique-se de salvar seus rascunhos de campanha.</td><td style="width: 50%;">No caminho para casa, Sarah encontrou um relógio de ouro de homem.</td></tr>
</tbody>
</table>
{:/}

#### Preposições {#prepositions}

Não há nada de errado em terminar uma frase com uma preposição quando isso melhora a legibilidade. Coloque uma preposição ou frase preposicional onde fizer mais sentido na frase. Se estiver com dificuldade, leia a frase em voz alta e veja se soa natural.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cada opção corresponde à prioridade em que a notificação aparece.</td><td style="width: 50%;">Cada opção corresponde à prioridade na qual a notificação aparece.</td></tr>
<tr><td style="width: 50%;">Para detalhes, consulte a documentação do SDK da plataforma com a qual você está trabalhando.</td><td style="width: 50%;">Para detalhes, consulte a documentação do SDK da plataforma com a qual você está trabalhando.</td></tr>
</tbody>
</table>
{:/}

#### Tempo presente {#present-tense}

Use o tempo presente em vez do tempo futuro. O tempo presente transmite imediatismo e demonstra confiança. Evite usar "vai" ou "iria" hipotético, especialmente ao se referir ao resultado de uma ação do usuário.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Grupos de inscrições arquivados não podem ser editados e não aparecem mais nos filtros de segmento.</td><td style="width: 50%;">Grupos de inscrições arquivados não podem ser editados e não vão mais aparecer nos filtros de segmento.</td></tr>
<tr><td style="width: 50%;">Usar um código curto é o tipo de número mais confiável para incluir links.</td><td style="width: 50%;">Usar um código curto seria o tipo de número mais confiável para incluir links.</td></tr>
</tbody>
</table>
{:/}

Só use o tempo futuro quando estiver realmente falando sobre o futuro. Evite prever [recursos futuros](#describing-limitations).

#### Palavrões {#profanity}

Mantenha o conteúdo adequado para todos os públicos. Isso tem menos a ver com moralidade do que com o fato de que palavrões podem ser divisivos e desagradáveis para um público tão amplo e internacional quanto o nosso. Também há um argumento de que às vezes palavrões são uma cobertura para escrita mal elaborada. Esse simplesmente não é o nosso estilo.

#### Plurais entre parênteses {#plurals-in-parentheses}

Não use plurais entre parênteses. Em vez disso, use a forma plural ou singular da palavra.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Personalize sua campanha com os seguintes filtros.</td><td style="width: 50%;">Personalize sua campanha com o(s) seguinte(s) filtro(s).</td></tr>
</tbody>
</table>
{:/}

#### Segunda pessoa e primeira pessoa {#second-person-and-first-person}

Use a segunda pessoa em suas instruções em vez da primeira pessoa — "você" em vez de "nós".

Refira-se ao leitor como quem está realizando a ação. Adote um tom conversacional — a maioria dos leitores recorre à documentação quando não tem acesso imediato a um agente de suporte. Faça parecer que o artigo está falando com eles.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Se você quiser adicionar uma variante...</td><td style="width: 50%;">Se quisermos adicionar uma variante...</td></tr>
</tbody>
</table>
{:/}

Se você está dizendo ao leitor para fazer algo, pode omitir o "você" e usar o imperativo.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Faça upload do arquivo CSV.</td><td style="width: 50%;">Você pode fazer upload do arquivo CSV.</td></tr>
<tr><td style="width: 50%;">Selecione Enviar.</td><td style="width: 50%;">Você precisará selecionar Enviar.</td></tr>
</tbody>
</table>
{:/}

Ao usar a segunda pessoa, certifique-se de saber quem é o público do documento e seja consistente sobre com quem está falando.

#### Gírias e expressões idiomáticas {#slang-and-idioms}

Somos um grupo direto. Evite usar gírias da moda ou expressões idiomáticas que falem muito especificamente para um único público. Isso também pode datar rapidamente os materiais e dificultar a localização do conteúdo.

#### Ortografia {#spelling}

Use a ortografia do inglês americano para palavras que diferem no inglês britânico. Se não tiver certeza de como escrever uma palavra, primeiro consulte o [Glossário](#glossary). Se a palavra não estiver listada lá, consulte o [Merriam-Webster's Collegiate Dictionary](https://www.merriam-webster.com/).

Para palavras acentuadas ou que contêm caracteres especiais, certifique-se de seguir corretamente a ortografia do dicionário. Em alguns casos, omitir involuntariamente esses acentos pode resultar em uma palavra diferente. Por exemplo, "resume" significa recomeçar após parar, enquanto "résumé" é um relato das qualificações de alguém.

### Pontuação {#punctuation}

#### E comercial {#ampersands}

Não use um e comercial (&) no lugar de "e" em texto ou títulos, a menos que esteja se referindo diretamente à interface do usuário.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">editor de arrastar e soltar</td><td style="width: 50%;">Drag & Drop Editor</td></tr>
<tr><td style="width: 50%;">SMS e MMS</td><td style="width: 50%;">SMS & MMS</td></tr>
</tbody>
</table>
{:/}

#### Apóstrofos {#apostrophes}

Usamos apóstrofos mais frequentemente para tornar um substantivo possessivo.

* Para substantivos singulares que terminam em S, é aceitável colocar outro S após o apóstrofo.
 * **Exemplo:** Chris's, business's, alias's
* Para substantivos plurais que terminam em S, adicione um apóstrofo, mas sem S adicional.
 * **Exemplo:** users'

#### Dois-pontos {#colons}

Use dois-pontos no final de uma frase introdutória que precede uma lista ou exemplo. Sua frase introdutória deve poder funcionar sozinha como uma frase completa. Isso é tanto para fins de acessibilidade quanto de localização, pois é difícil traduzir fragmentos de frases.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">A estrutura geral é a seguinte:</td><td style="width: 50%;">A estrutura geral é:</td></tr>
</tbody>
</table>
{:/}

Se o texto que precede os dois-pontos estiver em negrito, coloque os dois-pontos em negrito também.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Agendado:</strong> Entrada baseada em tempo.</td><td style="width: 50%;"><strong>Agendado</strong>: Entrada baseada em tempo.</td></tr>
</tbody>
</table>
{:/}

Se o texto que precede os dois-pontos for texto de código, não inclua os dois-pontos no texto de código, a menos que faça parte do elemento de código.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>user_alias_label</code>: Um rótulo comum para agrupar aliases de usuário.</td><td style="width: 50%;"><code>user_alias_label:</code> Um rótulo comum para agrupar aliases de usuário.</td></tr>
</tbody>
</table>
{:/}

Você também pode usar dois-pontos para unir duas frases relacionadas em uma sentença. No entanto, use dois-pontos para isso com moderação. Duas frases separadas geralmente são mais legíveis.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Na próxima semana: faremos um tour pelo West Village.</td></tr>
</tbody>
</table>
{:/}


#### Vírgulas {#commas}

A Braze usa a vírgula de Oxford (serial) ao escrever instruções ou conteúdo de aprendizado. Use uma vírgula antes da última conjunção para separar itens em uma série.

Use uma vírgula após uma frase introdutória.

Se uma conjunção coordenativa (palavras como "e", "mas", "ou", "ainda", "então") separa duas cláusulas independentes, coloque a vírgula após a primeira cláusula e antes da conjunção. No entanto, essa vírgula não é necessária se ambas as cláusulas forem curtas.

Por exemplo, aqui estão duas cláusulas independentes:

* "Todos os campos são opcionais."
* "Você deve especificar pelo menos um campo."

A frase ao usar a conjunção coordenativa "mas" é "Todos os campos são opcionais, mas você deve especificar pelo menos um campo."

Se uma cláusula independente e uma cláusula dependente são usadas na mesma frase, não use vírgula para separá-las. Só use vírgula nesse cenário se a frase puder ser mal interpretada sem a vírgula.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Os estados de inscrição por push são filtros e podem permitir que os usuários editem preferências de notificação.</td><td style="width: 50%;">Os estados de inscrição por push são filtros, e podem permitir que os usuários editem preferências de notificação.</td></tr>
</tbody>
</table>
{:/}

#### Travessões {#dashes}

##### Travessão longo

Use um travessão longo (—) ao usar um travessão em uma frase para indicar um pensamento separado ou interrupção. Não coloque espaços antes ou depois do travessão longo. Não use um travessão longo onde uma vírgula ou parênteses funcionaria igualmente bem.

Consulte seu sistema operacional para saber como digitar um travessão longo:

* **macOS:** Pressione Option + Shift + Hífen.
* **Windows:** Ative o num lock, depois segure a tecla Alt esquerda e digite 0151 no teclado numérico.

##### Travessão curto {#en-dash}

Use um travessão curto (–) para indicar um intervalo de números, como sinal de menos ou para indicar números negativos. Não coloque espaços antes ou depois do travessão curto, exceto quando usado como sinal de menos. Não use um hífen (-).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use um travessão curto para um intervalo de números</em></th><th style="width: 50%;">Não faça: <em>Usar um hífen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">2018–2021</td><td style="width: 50%;">2018-2021</td></tr>
</tbody>
</table>
{:/}

Não use um travessão curto para intervalos de tempo. Para mais detalhes, consulte a seção [Datas e horários](#dates-and-times).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use um travessão curto como sinal de menos e inclua espaços ao redor do travessão curto</em></th><th style="width: 50%;">Não faça: <em>Usar um hífen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">15 – 5 = 10</td><td style="width: 50%;">15-5=10</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use um travessão curto para números negativos</em></th><th style="width: 50%;">Não faça: <em>Usar um hífen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">–30</td><td style="width: 50%;">-30</td></tr>
</tbody>
</table>
{:/}

Consulte seu sistema operacional para saber como digitar um travessão curto:

* **macOS:** Pressione Option + Hífen.
* **Windows:** Ative o num lock, depois segure a tecla Alt esquerda e digite 0150 no teclado numérico.

#### Reticências {#ellipses}

Reticências são uma série de três pontos (...) que indicam a omissão de uma ou mais palavras. Em geral, evite usar reticências ao escrever instruções ou conteúdo de aprendizado.

#### Pontos de exclamação {#exclamation-points}

Um ponto de exclamação pode ser usado com moderação para um tom informal. No entanto, evite usar pontos de exclamação em excesso ao longo do texto. Em vez disso, considere usar [Alertas](#callouts-and-alerts).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use pontos de exclamação para um tom informal em lembretes e introduções</em></th><th style="width: 50%;">Não faça: <em>Usar pontos de exclamação para indicar aviso ou cautela aos leitores</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Certifique-se de salvar suas alterações antes de sair da página!</td><td style="width: 50%;">Os usuários devem receber uma ou mais mensagens de um passo para serem contados como destinatário único!</td></tr>
</tbody>
</table>
{:/}

#### Hífens {#hyphens}

Hífens podem ajudar o leitor a ganhar mais clareza em uma frase ao vincular palavras em uma expressão. Aqui estão algumas diretrizes para acertar.

Use hífens para modificadores compostos que ajudam o leitor a entender o sujeito mais claramente.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">fluxo de dados em tempo real</td></tr>
</tbody>
</table>
{:/}

Use hífens para vincular uma expressão, com um espaço entre o modificador e o sujeito.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Soluções tudo-em-um</td></tr>
</tbody>
</table>
{:/}

Use hífens para uma expressão que modifica um sujeito. Não é necessário usar hífen se a expressão é o sujeito.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Era um fato bem-conhecido.</td><td style="width: 50%;">Esse fato é bem-conhecido</td></tr>
</tbody>
</table>
{:/}

Não use hífens no lugar de um travessão longo para criar uma pausa em uma frase.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">...integrações de terceiros—como Slack—e automatize...</td><td style="width: 50%;">...integrações de terceiros-como Slack-e automatize...</td></tr>
</tbody>
</table>
{:/}

Não use hífen após um advérbio. Mantenha as palavras separadas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Feito às pressas</td><td style="width: 50%;">Feito-às-pressas</td></tr>
</tbody>
</table>
{:/}

#### Parênteses {#parentheses}

Use parênteses com moderação. Nunca coloque informações importantes entre parênteses, pois alguns leitores pulam conteúdo entre parênteses.

Para parênteses menos importantes, considere reformular a frase para remover os parênteses. Por exemplo, você pode separar a frase usando vírgulas, travessões, ponto e vírgula ou adicionando uma nova frase.

Se os parênteses fazem parte de uma frase maior, coloque o ponto final fora dos parênteses. Se os parênteses contêm uma frase completa, coloque o ponto final dentro.

**Seção relacionada:** [Plurais entre parênteses](#plurals-in-parentheses)

#### Pontos finais {#periods}

Use um ponto final para encerrar frases. Não use ponto final para encerrar manchetes, títulos, subtítulos ou elementos da interface.

Para diretrizes sobre quando usar pontos finais com itens de lista, consulte [Listas](#lists).

#### Ponto e vírgula {#semicolons}

Ponto e vírgula são ótimos para dividir uma frase mais longa e complicada. Use ponto e vírgula para separar duas cláusulas independentes que estão intimamente relacionadas em tópico.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça: <em>Use ponto e vírgula para dividir uma frase com duas cláusulas independentes relacionadas</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">O gato dormiu durante a tempestade; o cachorro se escondeu debaixo da cama.</td></tr>
</tbody>
</table>
{:/}

Ponto e vírgula podem ser usados para separar itens de lista se um (ou mais) dos itens contiver uma vírgula.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça: <em>Use ponto e vírgula para dividir uma frase mais longa</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Jane Lang, nossa moderadora; Simon Mayer, CEO e Cofundador da PantsLabyrinth; e Kara Seberg, CMO da Yachtr.</td></tr>
</tbody>
</table>
{:/}

#### Barras {#slashes}

Existem dois tipos de barras: invertida (\\) e normal (/). Não use barras para indicar palavras ou exemplos alternativos ("e/ou").

Use barras conforme necessário em caminhos de arquivo e URLs.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use barra para caminhos de arquivo</em></th><th style="width: 50%;">Não faça: <em>Usar barra para separar alternativas</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/campaigns/data_series</code></td><td style="width: 50%;">você/seus clientes</td></tr>
</tbody>
</table>
{:/}

#### Aspas {#quotation-marks}

Existem dois tipos de aspas: retas (" ") e curvas (" "). Pontos finais e vírgulas ficam dentro das aspas. Uma exceção é quando as aspas incluem informações exatas, como uma string. Use aspas ao direcionar usuários a inserir uma string específica de texto em um campo de texto.

{% alert note %}

Ao descrever a sintaxe de pesquisa, aspas são frequentemente usadas para indicar a busca por texto exato. Nesse caso, use colchetes ao redor da string de texto e aspas conforme exigido pela sintaxe de pesquisa. Por exemplo: <br><br>

*Coloque aspas ao redor de qualquer palavra ou frase, como ["segmento de teste"], e mostramos resultados que contêm apenas essas palavras ou frases exatas.*

{% endalert %}

Exemplos de código devem usar aspas retas. Para mais informações sobre formatação de código em texto, consulte [Código em texto](#code-in-text).

### Documentação técnica {#technical-documentation}

#### Endpoints de API {#api-endpoints}

Em geral, a documentação para endpoints de API deve seguir as diretrizes deste guia de estilo. No entanto, existem tópicos específicos que podem exigir diretrizes de conteúdo diferentes listadas neste documento. Para mais informações sobre como formatar e referenciar endpoints, consulte as [Diretrizes de documentação de endpoints de API]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

#### Evite garantias {#avoid-guarantees}

Nossa documentação deve evitar fazer compromissos que possam resultar em implicações legais. Evite usar termos definitivos como "garantir" ou "assegurar". Em vez disso, use declarações prospectivas como "Projetado para" ou "Destinado a" para transmitir com precisão as capacidades e intenções do produto.

#### Descrevendo interações com a interface {#describing-interactions-with-the-ui}

Ao se referir a elementos da interface, siga a capitalização como aparece na interface. No entanto, se um rótulo estiver todo em maiúsculas, use capitalização de frase (exceção: rótulos curtos, como operadores AND ou OR).

Ao instruir um leitor a interagir com a interface, coloque em negrito o elemento da interface com o qual estão interagindo. Para strings que um usuário inseriria em um campo, use aspas.

Para orientação sobre quais verbos usar ao descrever interações com a interface, consulte a tabela a seguir:

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 20%;">
<col style="width: 40%;">
<col style="width: 40%;">
</colgroup>
<thead>
<tr><th>Verbo</th><th>Uso</th><th>Exemplo</th></tr>
</thead>
<tbody>
<tr><td>Abrir</td><td><ul><li>Abrir apps</li><li>Abrir arquivos e pastas</li></ul></td><td><ul><li>Abra o Droidboy.</li><li>Abra o arquivo braze.xml.</li></ul></td></tr>
<tr><td>Fechar</td><td><ul><li>Fechar apps</li><li>Fechar arquivos e pastas</li></ul></td><td><ul><li>Feche o Droidboy.</li><li>Feche o arquivo braze.xml.</li></ul></td></tr>
<tr><td>Acesse</td><td><ul><li>Ir para uma página específica na interface (aba, página, seção)</li><li>Ir para uma página da web</li></ul></td><td><ul><li>Acesse a página <strong>Segmentos</strong> e clique em…</li><li>Acesse example.com para se cadastrar.</li></ul></td></tr>
<tr><td>&gt;</td><td>Seguir uma sequência de passos quando todos os passos são do mesmo tipo.</td><td>Acesse <strong>Segmentos</strong> &gt; <strong>Insights de segmento</strong>.</td></tr>
<tr><td>Escolha</td><td>Tomar uma decisão que é subjetiva, estratégica, aberta ou complexa.</td><td>Escolha uma estratégia de campanha.</td></tr>
<tr><td>Selecione</td><td><ul><li>Selecionar uma caixa de seleção</li><li>Selecionar itens de um dropdown</li><li>Selecionar uma aba</li><li>Tomar uma decisão simples</li></ul></td><td><ul><li>Selecione <strong>Mostrar senha</strong>.</li><li>Selecione um tipo de dados no dropdown.</li><li>Na página <strong>Gerenciar configurações</strong>, selecione a aba <strong>Eventos personalizados</strong>.</li><li>Selecione uma imagem.</li></ul></td></tr>
<tr><td>Desmarque</td><td>Desmarcar a seleção de uma caixa de seleção.</td><td>Desmarque a caixa de seleção <strong>Mostrar senha</strong>.</td></tr>
<tr><td>Selecione</td><td>Selecionar um elemento na interface.</td><td>Adicione um atributo personalizado e selecione <strong>Salvar</strong>.</td></tr>
<tr><td>Ative</td><td>Habilitar uma opção de alternância</td><td>Ative o <strong>Cabeçalho List-Unsubscribe</strong>.</td></tr>
<tr><td>Desative</td><td>Desabilitar uma opção de alternância</td><td>Desative <strong>CSS inline em novos e-mails por padrão</strong>.</td></tr>
<tr><td>Insira</td><td>Digitar um valor.</td><td><ul><li>No campo de texto, insira o nome do seu atributo personalizado.</li><li>Insira "Braze" como o nome da fonte.</li></ul></td></tr>
</tbody>
</table>
{:/}

#### Descrevendo limitações {#describing-limitations}

Escreva de forma franca sobre as limitações do produto, sem distorção ou manipulação. Os leitores reagem intensamente a serem manipulados ou enganados, e isso compromete a eficácia da documentação como fonte de verdade utilitária. Os clientes dependem da documentação para entender os limites do sistema no qual estão construindo para que possam usar a Braze com sucesso.

Ao mesmo tempo, apoie a intencionalidade do desenvolvimento do produto enquadrando as limitações com contexto positivo e apropriado.

* Se houver uma limitação flexível (por exemplo, um limite de taxa de API), enquadre a limitação falando sobre o **limite padrão** ou **alocação inicial.**
* Forneça um caminho significativo para navegar por limitações flexíveis. Forneça exemplos dessas soluções alternativas quando apropriado.
 * Por exemplo, a Braze usa exercícios de dimensionamento durante a integração para ajudar os clientes a entender como coisas como pontos de dados são usados por outras empresas de tamanho similar. Ao discutir pontos de dados, é apropriado falar sobre o exercício de dimensionamento ao mesmo tempo.
* É melhor descrever um caminho adiante de forma positiva do que como uma mitigação.
 * Por exemplo, em vez de dizer "A Braze não permite que os clientes façam isso por conta própria. A equipe de Suporte deve ativar esse recurso para você", diga "Para ativar esse recurso, entre em contato com a equipe de Suporte."
* Não dependa excessivamente das mesmas frases padrão para navegar por limitações flexíveis. Se um usuário lê "Fale com seu representante de atendimento ao cliente" repetidamente, o conselho se torna sem sentido.
* Se houver uma limitação rígida, tente descrever a lógica por trás desse limite.
 * Por exemplo: "Há um limite de 200 campanhas ativas de mensagens no app baseadas em ação por grupo de app para otimizar a velocidade de entrega de mensagens e prevenir timeouts. …O cliente médio da Braze tem um total de 26 campanhas ativas ao mesmo tempo — então é improvável que essa limitação afete você."
* Não descreva [funcionalidades planejadas ou recursos futuros](#future-features) como forma de explicar limitações atuais.
* Ao se referir a limites de dados personalizados, use o termo "capacidade" em vez de limites.
 * Por exemplo: Por padrão, você pode ter 20 propriedades de evento segmentáveis por espaço de trabalho. Entre em contato com seu gerente de conta da Braze para aumentar sua capacidade.

#### Recursos futuros {#future-features}

Evite referências a recursos futuros ou sugestões de que algo pode ser suportado no futuro.

Não use palavras e frases que ancorem sua escrita a um ponto no tempo, pois fazem o conteúdo ficar rapidamente desatualizado. Foque em como o produto funciona agora, não no que mudou (exceto para conteúdo focado em tempo, como notas de versão).

Especificamente, evite a seguinte lista de palavras e frases, retirada do [guia de estilo de documentação para desenvolvedores](https://developers.google.com/style/timeless-documentation) do Google:

* no momento desta escrita
* atualmente
* ainda não
* eventualmente
* futuro, no futuro
* mais recente
* novo, mais novo
* agora
* antigo, mais antigo
* presentemente, no presente
* em breve

#### Descontinuação de recursos {#features-deprecations}

Antes de incluir informações sobre descontinuação de recursos, certifique-se de ter um prazo geral de quando os leitores podem esperar que o recurso seja descontinuado (por exemplo, final de 2025).

Depois de ter um prazo geral, comunique a descontinuação do recurso com antecedência. Seja claro ao escrever sobre descontinuações para que os leitores possam entender claramente o que esperar.

Não use frases que possam incitar medo, incerteza ou dúvida nos leitores. Forneça um caminho claro adiante, como o que está substituindo o recurso descontinuado ou uma solução alternativa.

#### Geral versus específico {#general-vs-specific}

Como melhor prática, escreva artigos que discutam funcionalidades de forma geralmente aplicável. Se mais detalhes forem necessários para casos específicos ou exceções, crie uma seção separada (ou artigo separado se o conteúdo tiver o tamanho de um artigo web, ~500 palavras) que descreva esse caso atípico. Crie referências cruzadas do artigo geral para o específico para ajudar os usuários a conectar esses conceitos.

Evite criar conteúdo duplicado ou repetitivo para diferentes canais ou recursos. Se a repetição for necessária, use arquivos `includes` e outras [melhores práticas de conteúdo reutilizável]({{site.baseurl}}/contributing/content_management/reusing_content).

**Como exemplo:** Um caso de uso comum para clientes da Braze é redirecionar usuários que interagiram anteriormente com suas mensagens. O redirecionamento de usuários pode ser feito por meio de muitas ferramentas de engajamento, incluindo campanhas, Canvases, landing pages e segmentos. O redirecionamento de usuários pode ser feito por muitos canais: WhatsApp, SMS, Cartões de conteúdo, e-mail, notificações por push e mais. Frequentemente, os clientes tentam reengajar um usuário por meio de um canal diferente do usado anteriormente.
Em vez de criar um artigo para cada ferramenta de engajamento e cada canal, crie um único artigo que discuta estratégias para redirecionar usuários e descreva todas as opções disponíveis. Se houver considerações especiais para canais/ferramentas específicos, crie um artigo separado que descreva essas considerações e coloque-o dentro dessa seção de documentação. Crie referências cruzadas entre o artigo geral e o artigo específico.

#### Metadados e YAML {#metadata-and-yaml}

Artigos na documentação da Braze requerem certos metadados para fins de pesquisa e indexação. Para informações sobre quais metadados são necessários, consulte a página do GitHub sobre [YAML e Layouts de Metadados](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts).

#### Convenções de nomenclatura {#naming-conventions}

Ao nomear artigos e nomes de arquivo, certifique-se de descrever o tópico geral no título. Sempre inclua uma palavra-chave e uma breve descrição que os leitores entendam facilmente, especialmente com títulos de artigos.

Para nomes de arquivo, mantenha o nome breve e evite usar artigos (um, uma, o, a). Separe cada palavra com um sublinhado (_).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Direcionando usuários</td></tr>
<tr><td style="width: 100%;">Criando uma campanha de e-mail</td></tr>
<tr><td style="width: 100%;">Erros e respostas de API</td></tr>
<tr><td style="width: 100%;">sms_historical_performance.png</td></tr>
<tr><td style="width: 100%;">push_notification_test.png</td></tr>
</tbody>
</table>
{:/}

Em geral, para artigos e arquivos de imagem, use a mesma ortografia e capitalização do artigo e arquivos referenciados. Para diretrizes sobre estilo de título de artigo, consulte [Títulos e cabeçalhos](#headings-and-titles).

Ao se referir a um arquivo específico, use a mesma ortografia do nome do arquivo e fonte de código. Para detalhes de formatação, consulte a página do GitHub sobre [Formatação Especial](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting).

#### Procedimentos e instruções {#procedures-and-instructions}

Esta seção cobre algumas diretrizes a ter em mente ao escrever instruções para procedimentos no dashboard da Braze.

Diretrizes gerais:

* **Use o tom certo.** Para instruções, mantenha sua escrita curta, direta e orientada a tarefas. Sua escrita não precisa ser seca ou árida, mas deve ser direta. Ao introduzir tarefas ou subtarefas, você pode usar um tom mais informal para adicionar variedade. Evite usar "por favor" para manter o tom informal. Use contrações livremente para manter seu tom acessível.
* **Siga formato de cabeçalho paralelo.** Escolha um formato para seus cabeçalhos e mantenha-o. Mantenha seu conteúdo escaneável e previsível. Para cabeçalhos e títulos de página baseados em tarefas, prefira verbos imperativos (por exemplo, "Crie uma campanha de e-mail").

Antes das instruções:

* **Use introduções e pré-requisitos.** Não pule direto para os passos. Em vez disso, dê contexto sobre o que seu artigo ou seção cobre e forneça qualquer informação que o leitor precise saber antes de escanear as instruções. Certifique-se de que quaisquer pré-requisitos estejam listados no topo do artigo com o cabeçalho "Pré-requisitos". Os cabeçalhos de tabela nesta seção devem dizer "Requisitos". "Requisitos" é um termo aceitável para declarar um requisito da Braze, de um provedor terceirizado ou parceiro.
* **Comece no início do procedimento.** Não presuma que o leitor chegou a esta página após completar um passo anterior. Se as instruções para uma tarefa continuam de onde outra parou, dê uma visão geral de onde o leitor está no procedimento e o que deve completar antes deste passo. Inclua links para quaisquer passos anteriores.

Escrevendo instruções:

* **Use linguagem acionável.** Estruture a documentação em torno do que o usuário pode fazer, não do que o produto pode fazer. Evite linguagem como "Este recurso [faz xyz]". Em vez disso, pense em termos de "Use este recurso para [fazer xyz]".
* **Forneça passos de localização quando necessário.** Certifique-se de que o leitor está olhando no lugar certo com frases breves como "Na página **Configurações**, selecione **Editar**." Se isso não for claro o suficiente, forneça um passo introdutório. Por exemplo, "Acesse **Gerenciar configurações** e selecione a aba **Configurações**."
* **Antecipe declarações condicionais**. Coloque [cláusulas condicionais](#clause-order) primeiro. Para instruções condicionais, anteceda o passo com "se" para que o leitor saiba que pode pular o passo se a condição não se aplicar a ele. Por exemplo, "Se você precisar de X, faça A > B > C."
* **Reforce a ordem das tarefas.** Para progresso dentro de uma série de passos, use a frase "Quando você tiver" ou "Depois de ter". Para progresso entre tarefas, comece uma seção com "Agora que você" ou "Depois de ter". Evite a frase "Uma vez que você tenha", pois esse uso específico de "uma vez" não traduz bem.

#### Abas {#tabs}

Abas podem ser usadas na documentação técnica como forma de organizar informações agrupadas.

Uma aba se refere a um elemento que pode ser usado ao escrever instruções para demonstrar um resumo de fluxo de trabalho ou para organizar informações agrupadas. Isso é similar a uma tabela ou lista, mas as informações são agrupadas em painéis.

Considere usar abas quando as informações podem ser agrupadas para evitar duplicação ou para visualizar um fluxo de trabalho para os leitores. Certifique-se de que as abas incluam informações paralelas e não sejam usadas quando o leitor deve seguir passos sequenciais em um fluxo de trabalho.

Por exemplo, você pode usar abas para mostrar exemplos de código em diferentes linguagens de programação. Nesse caso, um leitor alternaria entre os exemplos com base nos rótulos das abas, em vez de rolar pelo artigo.

Para detalhes de formatação, consulte a página do GitHub sobre [Formatação Especial](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). Alternativamente, você também pode usar uma [lista](#lists) ou [tabela](#tables-1) para organizar informações.

### Formatação e organização {#formatting-and-organizing}

#### Endereços {#addresses}

Use o numeral seguido do nome da rua assim:

*330 W. 34th St.*

Para exibir um endereço completo, use o numeral, seguido do nome da rua, seguido da cidade, estado e CEP. Não é necessário vírgula entre o estado e o CEP.

*330 W. 34th St., New York, NY 10001*

#### Rótulos de botões {#buttons-labels}

Os rótulos de botões devem ser claros e previsíveis — o usuário deve saber qual ação ocorre ao selecionar o botão. Use capitalização de frase para rótulos de botões e comece com um verbo forte. Se não estiver claro a que o verbo se refere, use o formato [verbo] + [substantivo].

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cadastre-se</td><td style="width: 50%;">CADASTRE-SE</td></tr>
<tr><td style="width: 50%;">Entrar</td><td style="width: 50%;">ENTRAR</td></tr>
<tr><td style="width: 50%;">Inscrever-se</td><td style="width: 50%;">INSCREVER-SE</td></tr>
<tr><td style="width: 50%;">Saiba mais</td><td style="width: 50%;">Mais</td></tr>
</tbody>
</table>
{:/}

Omita palavras e artigos desnecessários, como "um", "uma" ou "o/a".

#### Alertas e destaques {#callouts-and-alerts}

Alertas, também conhecidos como destaques, são usados para chamar a atenção para informações úteis ao leitor. Existem quatro tipos de alertas usados em nossa documentação:

* Importante
* Nota
* Dica
* Aviso

Use alertas com moderação ao longo dos artigos. Para mais informações, consulte as [Melhores práticas de alertas]({{site.baseurl}}/contributing/style_guide/alerts/).

#### Código em texto {#code-in-text}

Existem alguns cenários em que você deve usar fonte de código para formatar texto dentro de uma frase. Aqui está uma lista incompleta de itens que devem estar em fonte de código:

* Nomes e valores de atributos
* Parâmetros de requisição de API
* Nomes de arquivo
* Caminhos de arquivo
* Nomes de métodos, variáveis ou parâmetros
* Nomes de elementos HTML e XML
* Códigos de status HTTP
* Texto inserido em um terminal

Para criar texto de código inline na documentação da Braze, envolva o texto em crases (`).

#### Exemplos de código {#code-samples}

Exemplos de código se referem a blocos de texto de código que exibem um trecho de código de amostra. Para fins de acessibilidade, introduza o exemplo de código com uma frase explicativa sempre que possível.

Para garantir que seus exemplos de código sejam legíveis, indente cada linha com dois espaços por nível de indentação. Se estiver com dificuldade para formatar seus exemplos de código, tente embelezar seu código usando um formatador de impressão bonita, como o [JSON Formatter](https://jsonformatter.org/json-pretty-print).

Para criar blocos de código na documentação da Braze, consulte [Teste de trecho de código](https://github.com/braze-inc/braze-docs/blob/develop/_docs/_home/styling_test_page.md#code-snippet-test). Lembre-se de que os blocos de código devem especificar o tipo de linguagem para garantir o destaque de sintaxe adequado.

#### Datas e horários {#dates-and-times}

Escreva o mês e os dias da semana por extenso. Evite abreviações quando possível. Para casos em que abreviar meses é necessário, abrevie apenas os seguintes:

* Jan.
* Fev.
* Ago.
* Set.
* Out.
* Nov.
* Dez.

Use uma [vírgula](#commas) para separar a data do ano. Se um dia da semana for usado com a data, adicione-o antes do mês.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça: <em>Use o formato de data preferido.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Setembro de 2021</td></tr>
<tr><td style="width: 100%;">15 de setembro de 2021</td></tr>
<tr><td style="width: 100%;">Quarta-feira, 15 de setembro de 2021</td></tr>
</tbody>
</table>
{:/}

Para intervalos de datas, use um [travessão curto](#en-dash).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">2010–2021</td></tr>
</tbody>
</table>
{:/}

Use um travessão curto para intervalos de datas.

Use numerais com am ou pm, seguidos de um espaço, seguido do período do dia (am ou pm). Remova os minutos de horários cheios.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use numerais com am ou pm.</em></th><th style="width: 50%;">Não faça: <em>Usar minutos para horários cheios (a menos que seja um intervalo).</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">12 pm</td><td style="width: 50%;">12:00 P.M.</td></tr>
</tbody>
</table>
{:/}

Para intervalos de horário, use um travessão curto para separar. Não adicione espaços antes ou depois do travessão curto.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça: <em>Use um travessão curto para intervalo de horário.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">12:45–2:30 pm</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça: <em>Use minutos para intervalos de horário.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">8:00 am–2:30 pm</td></tr>
</tbody>
</table>
{:/}

Para referência em casos onde participantes de outros fusos horários estão incluídos (como webinars, reuniões ou eventos), indique o fuso horário conforme abaixo:

* Eastern Standard Time: EST
* Central Standard Time: CST
* Mountain Standard Time: MST
* Pacific Standard Time: PST
* Greenwich Mean Time: GMT
* Coordinated Universal Time: UTC
* Central European Time: CET
* Eastern Europe Time: EET
* Western Europe Time: WET
* Singapore Time: SGT
* China Standard Time: CST

#### Emojis {#emojis}

Embora sejamos um grupo casual, evite usar emojis em conteúdo de aprendizado, pois podem ser interpretados de diferentes formas e frequentemente parecem pouco profissionais.

Exceções incluem os seguintes cenários:

* Ao usar ✅ e ❌ em tabelas para indicar conteúdo que é suportado versus não suportado, ou recomendado versus não recomendado
* Quando usados em texto de exemplo para uma campanha ou mensagem de Canvas

#### Nomes de exemplo {#example-names}

Nunca use nomes reais, endereços de e-mail ou qualquer outra informação pessoalmente identificável (PII). Em vez disso, use exemplos fictícios ou [texto de espaço reservado](#placeholder-text).

Quando precisar incluir nomes em sua escrita, consulte a lista da Wikipedia de [Nomes unissex](https://en.wikipedia.org/wiki/Unisex_name). Use os pronomes "eles/elas" quando possível e evite usar exemplos limitados a um gênero específico.

##### Endereços de e-mail de exemplo

Use o formato "nome@example.com" para endereços de e-mail genéricos. Substitua "nome" por um nome de exemplo. Por exemplo:

* alex@example.com
* lee@example.com
* yuri@example.com

#### Figuras e outras imagens {#figures-and-other-images}

Ao criar figuras e imagens, consulte o [Guia de estilo de cópia de imagem]({{site.baseurl}}/contributing/style_guide/image_style_guide/). Nunca inclua informações pessoalmente identificáveis (PII) em figuras ou imagens.

##### Texto alternativo {#alt-text}

Sempre inclua texto alternativo com imagens. Leitores de tela anunciam o texto alternativo para explicar imagens a pessoas com perda de visão. Portanto, seu texto alternativo deve transmitir todas as informações-chave representadas na imagem.
Use as seguintes diretrizes ao escrever texto alternativo:

* Use [linguagem simples](https://www.plainlanguage.gov/guidelines/).
* Escreva em frases completas e use capitalização de frase.
* Omita palavras desnecessárias.
* Não inclua "imagem de" ou "foto de". Já é entendido que você está se referindo a uma imagem.
* Não inclua caracteres especiais. Por exemplo, em vez de e comercial (&), use a palavra "e" por extenso.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Página de configurações de Eventos personalizados no dashboard da Braze com Adicionar relatório destacado.</td><td style="width: 50%;">Uma captura de tela da página Gerenciar configurações > Eventos personalizados no dashboard da Braze com a opção de adicionar um relatório destacada.</td></tr>
</tbody>
</table>
{:/}

Deixe tags alt explicitamente vazias (alt="") se a imagem estiver adicionando um componente visual redundante ao que é explicado no texto.

Adicionar texto alternativo a cada imagem não torna automaticamente o conteúdo da página fácil de navegar e consumir. Visuais redundantes são poderosos para usuários que enxergam porque informações visuais são fáceis de entender e lembrar. No entanto, texto alternativo descrevendo imagens redundantes pode ser desnecessário para usuários que não podem ver a imagem, porque cada elemento da página exige atenção igual dos usuários de leitores de tela para determinar se é útil para sua tarefa.

##### Nomes de empresas de exemplo

Se possível, tire capturas de tela do [dashboard-06](https://dashboard-06.braze.com/) para que você esteja usando um dos nomes de empresa FakeBrandz.

#### Tipos de arquivo e nomes de arquivo {#file-types-and-filenames}

Ao se referir a um tipo de arquivo, use o nome padrão do tipo. Se o tipo de arquivo for uma sigla, refira-se ao tipo de arquivo em maiúsculas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Use o nome padrão do tipo de arquivo</em></th><th style="width: 50%;">Não faça: <em>Usar a extensão do arquivo</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CSV</td><td style="width: 50%;">.csv</td></tr>
<tr><td style="width: 50%;">arquivo executável</td><td style="width: 50%;">.exe</td></tr>
<tr><td style="width: 50%;">GIF</td><td style="width: 50%;">.gif</td></tr>
<tr><td style="width: 50%;">JAR</td><td style="width: 50%;">.jar</td></tr>
<tr><td style="width: 50%;">JPEG</td><td style="width: 50%;">.jpg, .jpeg</td></tr>
<tr><td style="width: 50%;">JSON</td><td style="width: 50%;">.json</td></tr>
<tr><td style="width: 50%;">PDF</td><td style="width: 50%;">.pdf</td></tr>
<tr><td style="width: 50%;">PNG</td><td style="width: 50%;">.png</td></tr>
<tr><td style="width: 50%;">arquivo Python</td><td style="width: 50%;">.py</td></tr>
<tr><td style="width: 50%;">arquivo Bash</td><td style="width: 50%;">.sh</td></tr>
<tr><td style="width: 50%;">arquivo de texto</td><td style="width: 50%;">.txt</td></tr>
<tr><td style="width: 50%;">YAML</td><td style="width: 50%;">.yaml</td></tr>
<tr><td style="width: 50%;">ZIP</td><td style="width: 50%;">.zip</td></tr>
</tbody>
</table>
{:/}

Ao se referir ao nome de um arquivo, formate o nome do arquivo como texto de código. Para mais informações, consulte a seção [Código em texto](#code-in-text).

Ao nomear arquivos na documentação da Braze, como artigos ou arquivos de imagem, use todas as letras minúsculas e separe palavras com sublinhados, não hífens. Para mais informações, consulte [Criando arquivos e pastas](https://github.com/braze-inc/braze-docs/wiki/Creating-Files-&-Folders) no GitHub.

#### Notas de rodapé {#footnotes}

Notas de rodapé são anotações que fornecem informações adicionais e geralmente são colocadas no final de uma página. Devido à formatação do nosso texto, notas de rodapé não são ideais para a maioria dos casos de uso. O seguinte descreve quando usar notas de rodapé versus outros métodos de atribuição:

* Se você está apresentando uma lista de estatísticas ou outras informações densas que precisam ser atribuídas a fontes, use notas de rodapé.
* Se você está apresentando uma ou duas informações, use um link ou um alerta.
* Se precisar fornecer informações adicionais a itens em uma tabela, use um símbolo de asterisco (*) ao lado do item da tabela e apresente as informações após a tabela.

#### Formatação de texto em instruções {#formatting-text-in-instructions}

Use formatação de texto consistente para ajudar os leitores a encontrar e interpretar informações. Esta seção fornece diretrizes sobre qual formatação usar ao descrever ou se referir a diferentes elementos de texto em suas instruções.

Esta seção cobre os seguintes elementos:

* [Botões](#buttons)
* [Caixas de seleção](#checkboxes)
* [Comandos e opções de linha de comando](#command-line-commands-and-options)
* [Caixas de diálogo](#dialog-boxes-(modals))
* [Mensagens de erro](#error-messages)
* [Nomes de filtros e operadores](#filter-and-operator-names)
* [Nomes de pastas e arquivos](#folder-and-filenames)
* [Nomes e combinações de teclas](#key-names-and-combinations)
* [Métricas](#metrics)
* [Páginas](#pages)
* [Nomes de permissões](#permission-names)
* [Abas](#tabs-1)
* [Entrada de texto](#text-input)

##### Botões {#buttons}

Ao se referir a um botão, use texto em negrito para o rótulo do botão. Na maioria dos casos, siga a capitalização da interface. Para botões onde o rótulo está todo em maiúsculas (exceto botões OK), use capitalização de frase.

Para se referir a um botão, use apenas o rótulo do botão. Não se refira a um botão como "o botão [rótulo]".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecione <strong>Adicionar idiomas</strong>.</td><td style="width: 50%;">Selecione o botão <strong>Adicionar idiomas</strong>. <br><br> Selecione "Adicionar idiomas".</td></tr>
</tbody>
</table>
{:/}

Se o rótulo terminar com dois-pontos ou reticências, omita a pontuação final.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecione <strong>Salvar como</strong></td><td style="width: 50%;">Selecione <strong>Salvar como…</strong></td></tr>
</tbody>
</table>
{:/}

Se um botão for um ícone, inclua o nome do botão conforme mostrado na dica de ferramenta. Se um botão com ícone não incluir uma dica de ferramenta, envie uma solicitação para que uma dica de ferramenta seja adicionada.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecione ➕ <strong>Adicionar</strong>.</td><td style="width: 50%;">Selecione o ícone ➕.</td></tr>
</tbody>
</table>
{:/}

##### Caixas de seleção {#checkboxes}

Ao se referir a uma caixa de seleção, use texto em negrito para o rótulo da caixa de seleção. Não inclua a palavra "caixa de seleção" a menos que seja necessário para clareza. Prefira os termos "selecione/desmarque" em vez de "marque/desmarque".

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecione <strong>Enviar campanha para usuários no fuso horário local</strong>.</td><td style="width: 50%;">Marque <strong>Enviar campanha para usuários no fuso horário local</strong>.</td></tr>
<tr><td style="width: 50%;">Desmarque a caixa de seleção <strong>Sair</strong>.</td><td style="width: 50%;">Desmarque a caixa de seleção <strong>Sair</strong>.</td></tr>
</tbody>
</table>
{:/}

##### Comandos e opções de linha de comando {#command-line-commands-and-options}

Ao se referir a comandos ou opções de linha de comando, use formatação de código. Siga a capitalização conforme aparece ou conforme deve ser digitado.

##### Caixas de diálogo (modais) {#dialog-boxes-(modals)}

Evite se referir a caixas de diálogo pelo nome, a menos que seja necessário para clareza. Em vez disso, descreva o que o leitor precisa fazer. Se você se referir a uma caixa de diálogo, use texto em negrito para o nome da caixa de diálogo e siga a capitalização da interface.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecione <strong>Upload</strong> e depois selecione um arquivo para fazer upload.</td><td style="width: 50%;">Selecione <strong>Upload</strong> e use a caixa de diálogo <strong>Upload de arquivo</strong> para selecionar um arquivo para fazer upload.</td></tr>
</tbody>
</table>
{:/}

##### Mensagens de erro {#error-messages}

Ao se referir a mensagens de erro que um leitor pode encontrar, encapsule a mensagem de erro entre aspas. Para mensagens de erro mais longas, use uma citação em bloco.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">"Push Bounced: MismatchSenderId"</td><td style="width: 50%;"><em>Push Bounced: MismatchSenderID</em><br><br><code>Push Bounced: MismatchSenderID</code></td></tr>
</tbody>
</table>
{:/}

##### Nomes de filtros e operadores {#filter-and-operator-names}

Ao se referir aos nomes de filtros e operadores para segmentos ou outras áreas do dashboard, use texto de código. Siga a capitalização da interface, incluindo elementos que estão em maiúsculas como operadores `OR` e `AND`.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Selecione o filtro <code>First Used App</code> e…</td><td style="width: 50%;">Selecione o filtro <strong>First Used App</strong> e…</td></tr>
<tr><td style="width: 50%;">Combine filtros com o operador <code>OR</code>.</td><td style="width: 50%;">Combine filtros com o operador "OR".</td></tr>
</tbody>
</table>
{:/}

##### Nomes de pastas e arquivos {#folder-and-filenames}

Ao se referir a nomes de pastas e arquivos, use texto de código.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Abra o arquivo <code>braze.xml</code>.</td><td style="width: 50%;">Abra o arquivo <strong>braze.xml</strong>.</td></tr>
</tbody>
</table>
{:/}

##### Nomes e combinações de teclas {#key-names-and-combinations}

Ao se referir a nomes de teclas ou combinações de teclas, use a [tag HTML `<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd). Isso denota entrada textual do usuário a partir de um teclado, entrada de voz ou qualquer outro dispositivo de entrada de texto. Se estiver trabalhando em um editor que não suporta HTML personalizado, use [texto de código](#code-in-text).

Escreva os nomes das teclas como Command, Control, Option e Shift por extenso. Não use símbolos para essas teclas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Pressione <strong>Option</strong>.</td><td style="width: 50%;">Pressione ⌥.</td></tr>
</tbody>
</table>
{:/}

Para combinações de teclas, use um sinal de mais (+) entre as teclas, mas omita o sinal de mais de qualquer formatação especial.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Pressione <strong>Option + F12</strong>.</td><td style="width: 50%;">Pressione ⌥ + F12.</td></tr>
</tbody>
</table>
{:/}

Por exemplo, é assim que as tags de teclado aparecem na documentação da Braze:
Para parar o comando, pressione **Control + C**.

##### Métricas {#metrics}

Ao se referir a uma métrica em uma tabela ou entrada de glossário, use iniciais maiúsculas sem formatação especial. Ao se referir a uma métrica em uma frase, use iniciais maiúsculas com itálico (como *Machine Opens*).

##### Páginas

Use o termo página ao se referir a uma página da web em geral ou a uma página específica no dashboard da Braze. Ao se referir ao nome de uma página, use o formato "a página [rótulo]" e coloque o nome da página em negrito.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Acesse a página Segmentos.</td><td style="width: 50%;">Acesse a página "Segmentos".</td></tr>
</tbody>
</table>
{:/}

##### Nomes de permissões {#permission-names}

Ao se referir a nomes de permissões de usuário dentro do dashboard, coloque o nome da permissão entre aspas.

{% alert note %}

Atualmente estamos usando capitalização de título para corresponder à formatação do dashboard. Há um plano para atualizar os nomes de permissões dentro da interface para capitalização de frase para corresponder aos nossos padrões.

{% endalert %}

##### Abas {#tabs-1}

Ao se referir a uma aba, use o formato "a aba [rótulo]" e coloque o nome da aba em negrito.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Acesse a página <strong>Gerenciar configurações</strong> e selecione a aba <strong>Tags</strong>.</td><td style="width: 50%;">Acesse a página "Gerenciar configurações" e selecione a aba "Tags".</td></tr>
</tbody>
</table>
{:/}

##### Entrada de texto {#text-input}

Ao instruir um leitor a digitar uma string específica de texto, coloque o texto entre aspas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">No campo <strong>Nome</strong>, insira "Usuários inativos"</td><td style="width: 50%;">No campo <strong>Nome</strong>, insira <code>Usuários inativos</code>.</td></tr>
</tbody>
</table>
{:/}

#### Perguntas frequentes (FAQs) {#frequently-asked-questions-faqs}

Ordene as FAQs começando com as informações que as pessoas mais querem ou precisam saber, e depois organize as FAQs por categoria de problema se houver várias.

Para cada FAQ, comece respondendo diretamente à pergunta e depois entre em detalhes. Use perguntas reais que correspondam a consultas de pesquisa típicas e vocabulário do usuário, o que ajuda na encontrabilidade das FAQs. Inclua links para recursos que o usuário possa achar úteis, como artigos relacionados, instruções para contatar o suporte e materiais de ensino (guias práticos, tutoriais e outros) quando disponíveis.

#### Geografia {#geography}

##### Cidades

Escreva todos os nomes de cidades por extenso na primeira menção no texto. Depois disso, é aceitável abreviar nomes de cidades bem conhecidas como NYC ou LA.

**Primeira menção:** San Francisco
**Segunda menção:** SF

Para cidades bem conhecidas como Londres ou Tóquio, é aceitável apresentá-las sem vírgula seguida do estado, província ou país.

Para cidades ou vilas que possam ser desconhecidas para seu público, inclua o estado, província ou país.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Biloxi, Mississippi</td></tr>
<tr><td style="width: 100%;">New Bedford, MA</td></tr>
<tr><td style="width: 100%;">Antuérpia, Bélgica</td></tr>
</tbody>
</table>
{:/}

##### Países

Capitalize os nomes de todos os países. Para abreviar o nome de um país, escreva a primeira menção por extenso, seguida das iniciais nas menções seguintes.

**Primeira menção:** Estados Unidos
**Segunda menção:** EUA

Não coloque pontos entre nomes de países abreviados.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">UK</td><td style="width: 50%;">U.K.</td></tr>
<tr><td style="width: 50%;">Washington, DC</td><td style="width: 50%;">Washington, D.C.</td></tr>
</tbody>
</table>
{:/}

##### Regiões

Capitalize tanto a região quanto o direcional que a modifica.

**Exemplo:** Norte da Califórnia, Europa Oriental

Capitalize nomes próprios que descrevem uma região ou lugar específico.

**Exemplo:** West Midlands, América do Sul, South Chicago

##### Estados e províncias

Capitalize todos os estados e províncias.

**Exemplo:** New York, Quebec

#### Títulos e cabeçalhos {#headings-and-titles}

Para cabeçalhos e títulos de artigos, use capitalização de frase. Seja descritivo ao escrever cabeçalhos e títulos, e foque no propósito principal do conteúdo com base no tipo de artigo. Não use e comercial no lugar da palavra "e".

Para títulos de artigos, quando possível, evite gerúndios (verbos terminados em *-ndo*) em favor de verbos imperativos. Mantenha os títulos dos artigos concisos e certifique-se de que sejam apropriados para o conteúdo. Por exemplo, um artigo de referência sobre mensagens SMS poderia ser intitulado "Sobre SMS".

Para cabeçalhos de artigos, seja conciso e consistente entre os títulos dos cabeçalhos. Por exemplo, se o estilo de Cabeçalho 1 do artigo define cada passo (ex. **Passo 1: Crie uma nova campanha de push**), mantenha esse formato em todos os cabeçalhos do artigo para consistência.

Para ajuda de estilo no Braze Docs, consulte a página de Contribuição para [Exemplos de estilo]({{site.baseurl}}/contributing/styling_examples/?tab=markdown).

##### Subtarefas numéricas

Para cabeçalhos que descrevem passos ordenados, use numerais nos cabeçalhos de subtarefas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Passo 2: Crie uma campanha de SMS <br><br> Passo 2.1: Redija sua mensagem <br><br> Passo 2.2: Programe a entrega</td><td style="width: 50%;">Passo 2: Crie uma campanha de SMS <br><br> Passo 2a: Redija sua mensagem <br><br> Passo 2b: Programe a entrega</td></tr>
</tbody>
</table>
{:/}

#### Introduções {#introductions}

Introduções servem como uma verificação rápida para usuários perguntando:

* Estou no documento certo? Isso é relevante para mim?
* O que vou aprender se investir tempo lendo este documento?
* Sinto que estou seguindo uma jornada clara de integração ou configuração para SMS, e-mail, IAM ou outro (apesar de não especificar qual documento o usuário deve acessar em seguida)?

As seguintes são diretrizes gerais para introduções. Consulte diretrizes específicas de seção para casos de uso mais específicos.

* Introduções podem ter de 1 a 5 frases
* Introduções devem dar uma visão geral do conteúdo do documento ou ser uma abertura para o tópico
* Use citações em bloco
* Coloque introduções sob o cabeçalho H1 do artigo

##### Parceiros

Inclua uma visão geral do parceiro e uma breve descrição da empresa. Também inclua um link para o site do parceiro.

##### API

Inclua apenas a frase "Use este endpoint para..." na introdução. Queremos manter os endpoints de API o mais fáceis de navegar possível. Para mais informações sobre estrutura e formatação de endpoints de API, consulte as [Diretrizes de documentação de endpoints de API]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

##### Guia do usuário e guia do desenvolvedor

Parágrafos introdutórios devem ser escritos de uma das duas formas:

1. Com um parágrafo de abertura ou introdução ao tópico
2. Uma declaração do que o artigo contém. Isso geralmente se parece com "Este artigo de referência....".

Embora os passos no guia do usuário e no guia do desenvolvedor façam os usuários dependerem fortemente de pistas da navegação ao longo de sua jornada como cliente, embora às vezes redundante, é útil dizer explicitamente o valor do documento logo no início.

Por exemplo, se um usuário estivesse passando pelo guia do desenvolvedor integrando unity. Esta página com o título "Integração" não seria suficiente sem incluir a frase introdutória.

#### Listas {#lists}

Listas são melhor usadas para formatar informações relacionadas. Não use uma lista para mostrar apenas um item. Se quiser destacar um único item do texto ao redor, use outra formatação.

Existem três tipos de listas: com marcadores, com letras e numeradas. Inclua uma frase introdutória completa que pode terminar com dois-pontos ou ponto final.

* Listas com marcadores organizam informações que não precisam estar em uma ordem específica.
* Listas com letras são usadas para definir opções mutuamente exclusivas.
* Listas numeradas indicam uma sequência de passos ordenados.

Use a mesma sintaxe para todos os itens da lista, se possível.

Para capitalização de itens de lista, comece cada item com letra maiúscula. Para pontuação final de itens de lista, não use pontuação final nos seguintes cenários:

* Se o item da lista for uma única palavra ou frase incompleta
* Se o item da lista não incluir um verbo
* Se o item da lista estiver em fonte de código
* Se o item da lista for um link ou título de documento

#### Formatação de mídia {#media-formatting}

Esta seção inclui diretrizes gerais para formatação de imagens e GIFs em seu conteúdo. Para mais informações, incluindo capturas de tela de exemplo, consulte o [Guia de estilo de cópia de imagem]({{site.baseurl}}/contributing/style_guide/image_style_guide/).

| **Faça** | {::nomarkdown}<ul><li>Recorte bem próximo ao recurso ou componente mencionado.</li><li>Tire capturas de tela de alta qualidade, preferencialmente em um monitor retina (tela de MacBook).</li><li>Crie um GIF de uma interação ou fluxo de trabalho.</li><li>Tenha em mente que os usuários não podem pausar ou avançar em um GIF para ver detalhes.</li><li>Passe as imagens por um otimizador para reduzir o tamanho do arquivo (ImageOptim, TinyPNG ou Ezgif).</li><li>Busque alto contraste entre elementos para acessibilidade.</li><li>Redimensione imagens por porcentagens de altura em vez de valores de pixel distintos.</li></ul>{:/} |
| **Não faça** | {::nomarkdown}<ul><li>Não inclua o cabeçalho ou barra lateral do dashboard, pois podem ser explicados em uma frase simples.</li><li>Não inclua o dashboard inteiro.</li><li>Não inclua informações pessoalmente identificáveis (a menos que desfocadas ou de um usuário de demonstração).</li><li>Não inclua o quadro do navegador (campo de URL, favoritos, abas, etc.).</li><li>Não inclua dashboards de parceiros de tecnologia.</li><li>Não adicione borda ou sombra às imagens.</li></ul>{:/} |

#### Números {#numbers}

Nunca comece uma frase com um numeral. A exceção é ao se referir a um ano (exemplo: "2019 foi um ano memorável").

Escreva numerais por extenso até nove. Para unidades de medida ou números 10 ou maiores, use o numeral. Para números com mais de três dígitos, use ponto como separador de milhar. Escreva números maiores por extenso.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">1.000</td><td style="width: 50%;">1000</td></tr>
<tr><td style="width: 50%;">200.000</td><td style="width: 50%;">200000</td></tr>
<tr><td style="width: 50%;">1.000.000</td><td style="width: 50%;">1000000</td></tr>
<tr><td style="width: 50%;">9 bilhões</td><td style="width: 50%;">9000000000</td></tr>
<tr><td style="width: 50%;">5 MB</td><td style="width: 50%;">cinco MB</td></tr>
</tbody>
</table>
{:/}

##### Moeda

Sempre indique a qual moeda você está se referindo usando o símbolo da moeda antes do valor ou escreva por extenso (exemplo: pesos, euros, libras, etc.).

Use a vírgula decimal para valores onde o número de centavos é maior que zero. Para somas maiores que três dígitos, use ponto como separador de milhar. Não inclua ",00" em somas de dinheiro.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">US$ 20</td><td style="width: 50%;">$20</td></tr>
</tbody>
</table>
{:/}

##### Números de telefone

Quando um número de telefone é referenciado, coloque hífens entre os dígitos. Não coloque o código de área entre parênteses.

Ao formatar números de telefone com código de país, use um sinal de mais (+) antes do código do país e coloque o código de área entre parênteses.

Forneça um número com código de país assim: +1 (504) 327-7269

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">123-456-7890</td><td style="width: 50%;">(123)-456-7890</td></tr>
<tr><td style="width: 50%;">+1 (123) 456-7890</td><td style="width: 50%;">1 234-567-9012</td></tr>
</tbody>
</table>
{:/}

##### Frações

Escreva frações por extenso e use um hífen entre o numerador e o denominador. Não use numerais separados por uma barra.

Em alguns casos, quando expressar uma fração como decimal é necessário, adicione um zero antes do ponto decimal para frações menores que um.

Ao expressar sistemas de classificação usando frações, use numerais para escrever a classificação.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">0,5</td><td style="width: 50%;">1/2</td></tr>
<tr><td style="width: 50%;">um terço</td><td style="width: 50%;">um-terço</td></tr>
<tr><td style="width: 50%;">9 de 10</td><td style="width: 50%;">nove de dez</td></tr>
</tbody>
</table>
{:/}

##### Porcentagens

Use numerais e um sinal de porcentagem (%) sem espaço entre eles. No entanto, se a porcentagem iniciar a frase, escreva a porcentagem inteira por extenso (número e porcentagem).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">10%</td><td style="width: 50%;">10 %</td></tr>
<tr><td style="width: 50%;">Vinte por cento dos usuários da empresa são...</td><td style="width: 50%;">20% dos usuários da empresa são...</td></tr>
</tbody>
</table>
{:/}

##### Intervalos

Use um hífen para indicar um intervalo de números. Não use um travessão curto para separar números em um intervalo.

Para intervalos de números com unidades, repita a unidade de medida após o número. Isso não inclui repetir substantivos. Use a palavra "a" entre os números no intervalo para evitar confusão.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">5 a 100</td><td style="width: 50%;">5–100</td></tr>
<tr><td style="width: 50%;">-10°C a 50°C</td><td style="width: 50%;">-10°C-50°C</td></tr>
</tbody>
</table>
{:/}

#### Texto de espaço reservado {#placeholder-text}

Use texto de espaço reservado para indicar onde o leitor deve fornecer o valor relevante. O texto de espaço reservado deve indicar o conteúdo que está sendo representado. Por exemplo, *YOUR_API_KEY* indica a chave de API do leitor.

##### Escrevendo espaços reservados

Ao criar texto de espaço reservado, consulte as seguintes diretrizes:

| Diretriz | Exemplo |
| :---- | :---- |
| Use letras maiúsculas e separe palavras com sublinhados (_). | `PLACEHOLDER_VARIABLE` |
| Para texto de espaço reservado inline, use itálico. | *`PLACEHOLDER_VARIABLE`* |
| Para texto de espaço reservado em blocos de código de API (onde não é possível usar itálico), coloque os espaços reservados entre chaves ({}). | `<string name="com_appboy_api_key">{YOUR_APP_IDENTIFIER_API_KEY}</string>` |
| Para texto de espaço reservado em blocos de código Liquid (onde não é possível usar itálico), use letras maiúsculas. | `{% raw %}{%- connected_content YOUR-API-URL :save items -%}{% endraw %}` |
| Não sacrifique clareza por brevidade. Use quantas palavras forem necessárias para representar um espaço reservado. | **Faça:** `CAMPAIGN_NAME` <br> **Não faça**: _`NAME`_|

##### Usando espaços reservados

Ao introduzir ou explicar um espaço reservado, consulte as seguintes diretrizes:

| Diretriz | Exemplo |
| :---- | :---- |
| Destaque os espaços reservados imediatamente após o espaço reservado. | Substitua `<YOUR_APP_IDENTIFIER_API_KEY>` pela sua [chave de API do identificador do app]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key), que você pode encontrar na página **Configurações**. |
| Para destacar dois ou mais espaços reservados de uma vez, use uma lista com marcadores. Liste cada espaço reservado na ordem em que aparecem no código. | Substitua o seguinte: {::nomarkdown}<ul><li><code>PLACEHOLDER_VARIABLE</code>: uma descrição do que o espaço reservado representa</li><li><code>PLACEHOLDER_VARIABLE</code>: uma descrição do que o espaço reservado representa</li></ul>{:/} |
| Refira-se ao espaço reservado na mesma formatação em que é mostrado no texto ou código. | `target <YOUR_APP_TARGET> do pod 'Appboy-iOS-SDK' end` <br><br> Substitua `<YOUR_APP_TARGET>` pelo nome do seu app de destino. |

#### Produtos {#products}

Ao se referir à Braze e seus recursos, use nomes completos de produtos e recursos e capitalize-os de acordo com a interface. Não capitalize modelos ou recursos comuns. Para uma lista de nomes de produtos e sua ortografia, consulte o [Glossário](#glossary).

Não abrevie nomes de produtos ou recursos, exceto nos seguintes casos:

* Para corresponder à interface
* Para atender a restrições de espaço limitado

Nunca use nomes de produtos ou recursos como verbos.

Nunca use apóstrofo após Braze (exemplo: "Braze's"). Soa estranho. Em vez disso, forme possessivos usando uma preposição ("de", "da") seguida do nome da empresa.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">A atualização de produto mais recente da Braze</td><td style="width: 50%;">A atualização de produto mais recente de Braze's</td></tr>
<tr><td style="width: 50%;">Esse é um dos recursos definidores da Braze.</td><td style="width: 50%;">Esse é um dos recursos definidores de Braze's</td></tr>
</tbody>
</table>
{:/}

Refira-se à "Braze" como "nós/nosso/nossos". Nunca "ele/seu/eles/deles".

#### Tabelas {#tables}

Usar tabelas pode ser uma forma útil e organizada de exibir informações. Certifique-se de ter cabeçalhos claros e descritivos e dados relevantes dentro das respectivas colunas e linhas.

Sempre use uma frase introdutória para descrever o propósito da tabela. Evite usar tabelas no meio de procedimentos numerados. Em vez disso, considere usar uma lista.

#### Unidades de medida {#units-of-measurement}

Para HTML e Markdown, use um espaço não quebrável (&nbsp) entre o número e a unidade ao especificar uma unidade de medida. Isso inclui a maioria das unidades de medida como distância, pixels, pontos, peso e graus de temperatura (entre o grau e a unidade de medida).

Para moeda, porcentagem ou graus de um ângulo, não use espaço entre o número e a unidade.

Para intervalos de números com unidades, repita a unidade para cada número. Da mesma forma, para taxas, use "por" em vez de uma barra (/).

### Links {#linking}

#### Links de referência cruzada {#cross-reference-links}

Use referências cruzadas para guiar os usuários a recursos adicionais. Na documentação da Braze, use URLs relativos à raiz do site para vincular a outros documentos da Braze (substitua "www.braze.com/docs" por "{{site.baseurl}}").

Evite adicionar múltiplos links para o mesmo documento dentro de uma determinada página, pois isso pode causar fadiga de links. Links duplicados são aceitáveis com moderação se você estiver vinculando a uma seção específica em outra página, ou se a página de origem for longa.

#### Incorporando vídeos {#embedding-videos}

Similar a imagens, use vídeos para criar variedade em seus materiais de aprendizado. A maioria das pessoas aprende melhor com uma combinação de mídias, então certifique-se de que qualquer conteúdo incluído em um vídeo também seja coberto no artigo ou lição.

Para incorporar um vídeo na documentação da Braze, consulte [Teste de vídeo incorporado]({{site.baseurl}}/home/styling_test_page/#embedded-video-test).

#### Cabeçalhos como alvos de link {#headings-as-link-targets}

Na documentação da Braze, âncoras são criadas automaticamente para cabeçalhos. No entanto, você pode querer adicionar uma âncora personalizada a um cabeçalho se:

* Sua âncora gerada automaticamente for muito longa.
* Seu cabeçalho puder ser frequentemente vinculado. Adicionar uma âncora personalizada reduz a probabilidade de quebrar links se o texto do cabeçalho for alterado posteriormente.

Para adicionar uma âncora a um cabeçalho na documentação da Braze, consulte [Âncoras personalizadas]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor).

#### Texto de link {#link-text}

Texto de link eficaz ajuda a melhorar a encontrabilidade, descobribilidade e acessibilidade do seu conteúdo.

##### Estruturando links {#structuring-links}

Use um dos seguintes formatos ao escrever links:

* Faça o texto do link corresponder ao título ou cabeçalho do destino do link.
* Use uma descrição do destino do link como texto do link.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Faça o texto do link corresponder ao título ou cabeçalho do destino do link.</em></th><th style="width: 50%;">Faça: <em>Use uma descrição do destino do link como texto do link.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Comece com o <a href="{{site.baseurl}}/user_guide/getting_started/web_sdk/">Web SDK</a> da Braze.</td><td style="width: 50%;">Para descobrir seu cluster ou endpoint específico, <a href="{{site.baseurl}}/braze_support/">entre em contato com o Suporte</a>.</td></tr>
<tr><td style="width: 50%;">Para mais informações, consulte <a href="{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/">Abortando mensagens Liquid</a>.</td><td style="width: 50%;">Em caso de dúvida, você sempre pode <a href="{{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password">redefinir sua senha</a>.</td></tr>
</tbody>
</table>
{:/}

Você pode precisar reformular uma frase para criar um bom texto de link.

Se estiver vinculando a uma seção na mesma página, use uma frase padrão que indique essa ação. Por exemplo:

* Nesta página, consulte [cabeçalho].
* Neste documento, consulte [cabeçalho].
* Para mais informações, consulte a seção [cabeçalho].

##### Escrevendo links {#writing-links}

Aplique as seguintes diretrizes ao escrever texto de link:

* Coloque o link nas palavras-chave relevantes.
* Se estiver escrevendo uma frase completa que direciona o leitor a outro artigo, use a frase "Para mais informações, consulte" ou "Para mais informações sobre [tópico], consulte".
* Só adicione uma frase "Saiba mais…" se o texto de ajuda abordar mais de um conceito, cada um dos quais poderia ser vinculado ao seu próprio documento de ajuda. Nessa situação, escolha o link mais apropriado e contextualize com "Saiba mais…"
* Para manter um tom informal, não use "por favor" para introduzir texto de link. Por exemplo, evite as frases "Por favor, consulte", "Por favor, veja" e "Por favor, entre em contato".
* Escreva texto de link único e descritivo que faça sentido sem o texto ao redor. Pesquisas do [Nielsen Norman Group](https://www.nngroup.com/articles/link-promise/#links-should-stand-alone) (NN/g) mostram que os leitores escaneiam informações relevantes em uma página, então certifique-se de que os links possam funcionar sozinhos.
* Não use as seguintes palavras ou frases para texto de link. São ruins para acessibilidade e escaneabilidade.
 * Saiba mais (sozinho)
 * Clique aqui
 * aqui
 * este documento
 * este artigo

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Certifique-se de que o texto do link faça sentido sem o texto ao redor</em></th><th style="width: 50%;">Não faça: <em>Usar texto de link vago ou não descritivo</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Para mais informações sobre importação de dados de clientes, consulte <a href="{{site.baseurl}}">Importação de usuário</a>.</td><td style="width: 50%;">Para mais informações, <a href="{{site.baseurl}}">clique aqui</a>.</td></tr>
<tr><td style="width: 50%;">Este recurso se conecta ao endpoint <a href="{{site.baseurl}}">Rastrear usuários</a>.</td><td style="width: 50%;">Consulte <a href="{{site.baseurl}}">este artigo</a>.</td></tr>
<tr><td style="width: 50%;">Saiba mais sobre <a href="{{site.baseurl}}">as novidades no Android SDK 16.0.0</a>.</td><td style="width: 50%;">Siga as instruções <a href="{{site.baseurl}}">aqui</a>.</td></tr>
<tr><td style="width: 50%;">Saiba mais sobre a <a href="https://www.braze.com/product">plataforma Braze</a>.</td><td style="width: 50%;">Para os passos, consulte <a href="{{site.baseurl}}">este documento</a>. <a href="{{site.baseurl}}">Saiba mais</a>.</td></tr>
<tr><td style="width: 50%;">As chaves de API da Storefront são únicas por storefront Hydrogen, mas seus escopos de permissão são compartilhados por todas as storefronts Hydrogen. Saiba mais sobre <a href="{{site.baseurl}}">tokens de API da Storefront.</a></td><td style="width: 50%;"><a href="{{site.baseurl}}">Tokens de API da Storefront</a> são únicos por <a href="{{site.baseurl}}">storefront Hydrogen</a>, mas seus <a href="{{site.baseurl}}">escopos de permissão</a> são compartilhados entre todas as storefronts Hydrogen.</td></tr>
</tbody>
</table>
{:/}

#### Links para endpoints {#links-for-endpoints}

Ao referenciar artigos de endpoints, certifique-se de usar [texto de link significativo](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog) que faça sentido fora de contexto. Se estiver usando o caminho do endpoint como link, certifique-se de fornecer detalhes no texto ao redor, pois o caminho pode não comunicar claramente a função do endpoint.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Exclua perfis de usuário usando o <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">endpoint Excluir usuário</a> da Braze.</td><td style="width: 50%;">Exclua perfis de usuário usando o endpoint <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Excluir usuário</a> da Braze.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/">endpoint <code>/users/export/id</code></a></td><td style="width: 50%;">endpoint <a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a></td></tr>
</tbody>
</table>
{:/}

#### Links para download de arquivo {#links-for-file-download}

Se um link faz download de um arquivo, deixe isso claro no texto do link e mencione o tipo de arquivo.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça: <em>Certifique-se de que o texto do link comunique que selecioná-lo faz download de um arquivo</em></th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Para dicas, baixe o <a href="{{site.baseurl}}">PDF da folha de referência de Regex</a>.</td><td style="width: 50%;">Confira nossa <a href="{{site.baseurl}}">folha de referência de RegEx</a>.</td></tr>
<tr><td style="width: 50%;">Para mais informações, baixe o <a href="{{site.baseurl}}">PDF do Manual de Serviços de Sucesso e Suporte</a>.</td><td style="width: 50%;"><a href="{{site.baseurl}}">Manual de Serviços de Sucesso e Suporte</a></td></tr>
</tbody>
</table>
{:/}

#### Links para outros sites {#links-to-other-sites}

Como regra geral, não vincule a outro site se puder cobrir a informação com uma breve explicação. Não podemos acompanhar quando o conteúdo de outro site muda.

Se vincular a um site externo, certifique-se de que o site vinculado seja de alta qualidade, confiável e respeitável. Se possível, vincule ao cabeçalho mais relevante em uma página.

Use um ícone de link externo para indicar que o link vai para um domínio diferente. Para a documentação da Braze, isso é aplicado automaticamente a links externos.

#### URLs para imagens {#urls-for-images}

Na documentação da Braze, use URLs relativos à raiz do site para vincular a imagens. Para mais informações, consulte [Adicionando e editando imagens](https://github.com/braze-inc/braze-docs/wiki/Editing-Content#adding-and-editing-images).

### Glossário {#glossary}

⚠️ = Use com cautela, consulte as notas relevantes
⛔️ = Não use

#### Numerais

**24/7**
Hifenize (24-7) apenas quando usado como modificador antes de um substantivo.

**2D / bidimensional**

**3D / tridimensional**

#### A

**Testes A/B**

⚠️ **abort**
Evite usar a menos que se refira a um processo especificamente nomeado. Em vez disso, use palavras como "parar", "sair", "cancelar" ou "encerrar".

**botões de ação**

**entrega baseada em ação**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

⛔️ **ad hoc**
Não use. Use "pontual" ou similar.

**AI**
Preferido em vez de "inteligência artificial" após a primeira menção.

**recomendação de item por AI**

**Alloys / Braze Alloys**
Sempre capitalizado.

**alfanumérico**
Não hifenize.

**always-on**

**am**
Minúsculas quando usado para horário (por exemplo, "10 am"). Veja também [pm](#glossary).

**Amazon S3**

**Amazon Web Services (AWS)**
Sempre capitalizado. Escreva por extenso na primeira menção, depois é aceitável usar a sigla.

**AMP for Email / Braze AMP for Email**

**Android**

**API / Interface de programação de aplicativo**
Escreva por extenso na primeira menção, depois é aceitável usar a sigla.

**chave de API**

**APNs / serviço de Notificações por Push da Apple**

**⛔️ grupo de app**
Não use. Grupo de app foi renomeado para espaço de trabalho.

**plataforma Apple iOS**

**AppleWatch**

**.avro**

#### B

**comportamento, comportamentos**

**Benchmarks**

**beta**

**BI Insights**

**bingeing**

**Binge-watch**

**Bonfire / comunidade Bonfire / comunidade Braze Bonfire**
Use "comunidade Braze Bonfire" na primeira menção, depois é aceitável usar apenas "Bonfire" ou "comunidade Bonfire".

**booleano**

⛔️ **lista de proibições**
Não use. Em vez disso, use "lista de bloqueio" ou "lista de negação". Para a forma verbal dessas palavras, considere reformular a frase para remover o termo problemático. Por exemplo:

>✅ **Recomendado:** Para bloquear uma propriedade existente de ser usada em novas mensagens, selecione **Gerenciar propriedades**. <br>
>⛔️ **Não recomendado:** Para colocar na lista de bloqueio uma propriedade existente, selecione **Gerenciar propriedades**.

**webhook Braze-to-Braze**

**Business Intelligence (BI)**
Escreva por extenso na primeira menção, depois é aceitável usar a sigla.

#### C

**California Consumer Privacy Act (CCPA)**
Escreva por extenso na primeira menção, depois é aceitável usar a sigla. Veja também [conformidade com CCPA (substantivo) / compatível com CCPA (adjetivo)](#ccpa-compliance)

**pode**
Use "pode" para se referir a uma ação ou resultado opcional. Por exemplo:

> ✅ **Recomendado:** Você também pode fazer upload e atualizar perfis de usuário com arquivos CSV.
> ✅ **Recomendado:** O processo de importação pode levar alguns minutos.

Não use "pode" para direções. Em vez disso, prefira o verbo imperativo. Para exemplos, consulte [Segunda pessoa e primeira pessoa](#second-person-and-first-person).

**Canvas**
Sempre capitalizado. O plural é "Canvases".

**Canvas Flow**
Use ao diferenciar entre o editor Canvas original e o Canvas Flow. Caso contrário, use "Canvas".

**campanha**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**capacidade**
Use ao se referir a limites de dados personalizados em vez da palavra "limite".

**catálogo**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**conformidade com CCPA (substantivo) / compatível com CCPA (adjetivo)** {#ccpa-compliance}

**CEO, CFO, CMO, COO, CTO**

**churn**
Use para se referir à rotatividade ou perda de clientes.

**previsão de churn**
Minúsculas, exceto quando se refere à interface.

**caixa de seleção**

**Check-in (substantivo) / check in (verbo)**

**City x City**

**Cofundador**

**Cartões de conteúdo / Braze Content Cards**

**Content Blocks**

**grupo de controle**

**conversão**

**análise de grupo de conversão**
Minúsculas.

**Cordova**

**Currents / Braze Currents**
Sempre capitalizado.

**CRM / gestão de relacionamento com o cliente**
Escreva por extenso na primeira menção, depois é aceitável usar a sigla.

**envio de mensagens cross-channel / personalização cross-channel**

**C-suite**

**CSV / valores separados por vírgula**

**atributos personalizados**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**eventos personalizados**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**atributos de cliente**

**comportamento do cliente**

**plataforma de dados do cliente (CDP)**
Minúsculas.

**engajamento do cliente**

**eventos de cliente**

**jornada do cliente**

**permissões de cliente**

**retenção de cliente**

#### D

**Tema modo escuro / Prévia do modo escuro / conceito de modo escuro**

**dashboard / dashboard da Braze**
Use para se referir à Braze como plataforma. Use minúsculas (dashboard, não Dashboard).

**orientado por dados (adjetivo)**

**privacidade de dados**

**folha de dados**

**fluxo de dados**

**DAU / Usuários ativos diários**

**Decision Splits**

**deep linking**

**Delay Messages**

**Downtime**

**arrastar e soltar (verbo) / arrastar-e-soltar (adjetivo)** {#drag-and-drop}
Use ao se referir a arrastar arquivos para uma zona de upload.

**editor de arrastar e soltar**
Use capitalização de título ao se referir ao recurso na interface. Caso contrário, use minúsculas (editor de arrastar e soltar). Use o verbo ao referenciar como os clientes podem [arrastar e soltar](#drag-and-drop) elementos no editor.

**drill down (verbo) / drilldown (substantivo ou adjetivo)**
Use em conteúdo sobre dados e os relatórios gerados a partir deles.

**DTC / direto ao consumidor**

**conteúdo dinâmico**

#### E

**acesso antecipado**

⛔️ **e.g.**
Não use. Use as frases "por exemplo", "como" ou similar.

**eBook**

**e-commerce**
Não "ecommerce" ou "eCommerce".

**ecossistema**

**e-mail**
Não "Email" ou "e-mail".

**entregabilidade de e-mail**

**reputação de e-mail**

**EMEA (Europa, Oriente Médio e Ásia)**

**emoji**
Forma singular e plural.

**usuário final (substantivo) / de usuário final (adjetivo)**
Prefira "seus usuários" em vez de "usuários finais".

⚠️ **ensure**
Evite usar ao falar sobre o que um recurso faz. Consulte [Evite garantias](#avoid-guarantees) para mais informações.

**ESP / provedor de serviço de e-mail**

**previsão de evento**

**propriedades de evento / propriedades de evento personalizado**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**eventos de exceção**

**extrair**
Use "extrair" em vez de "descompactar" para se referir à extração de arquivos de uma pasta compactada.

**ID externo**
Não "External ID". Ao referenciar trechos de código, use external_id.

#### F

**Facebook**

**FCM / Firebase Cloud Messaging**

**Firebrand / Firebrands**

**Forge [ANO]**

**limite de frequência**

**Tela cheia**
Quando usado como adjetivo (por exemplo, "Mensagens no app em tela cheia"), renderize sem hífen.

#### G

**GDPR / Regulamento Geral de Proteção de Dados**
Escreva por extenso na primeira menção, depois é aceitável usar a sigla.

**conformidade com GDPR (substantivo) / compatível com GDPR (adjetivo)**

**geofence**

**GIF**

**GitHub**
Não "Github" ou "github".

**Google / pesquisável no Google**

#### H

**Alto desempenho**

**Ações de alto valor**

**HQ / sede**

**HTML Email Editor**

**HTTP**

#### I

⛔️ **i.e.**
Não use. Use a frase "ou seja" ou similar.

**mensagens no app**

**mensagem no navegador (IBM)**

**infográfico**

**atribuição da instalação**

**inteiro**

**Intelligence Suite**
Use capitalização de título.

**Intelligent Channel**
Use capitalização de título.

**Intelligent Selection**
Use capitalização de título.

**Intelligent Timing**
Use capitalização de título.

⛔️ **Internet das coisas**
Não use.

**iOS**

**aquecimento de IP**

**iPad**

**iPhone**

**TI**

#### J

**JavaScript**

**JPEG / JPG**

**JSON / JavaScript Object Notation**

#### K

**Keynote (programa) / keynote (substantivo)**

**kick off (verbo) / kickoff (substantivo)**

⚠️ **kill**
Evite usar a menos que se refira a um processo especificamente nomeado. Em vez disso, use palavras como "parar", "sair", "cancelar" ou "encerrar".

**KPI / indicador-chave de desempenho**

#### L

**landing page**

**ciclo de vida**

**Lift-rate**

**LinkedIn**

**Liquid**
Sempre capitalizado.

**Live Preview**

**longo prazo (substantivo) / de longo prazo (adjetivo)**

**LTV / Valor do tempo de vida**

#### M

**tecnologia de marketing**
Preferido em vez de "martech".

**MAU / Usuários ativos mensais**

**máximo**
Não "máx".

**biblioteca de mídia**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**Microsoft**

**Microsoft Azure**

**ML / machine learning**

**marketing para mobile**

**automação de marketing para mobile**

**momento de uso do dispositivo móvel**

**celular**

**campanha multicanal**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado. Sem hífen.

**suporte multi-idioma**

**testes multivariantes**

#### N

**N/A**
Não "NA". Use "N/A" conforme necessário em tabelas para indicar conteúdo de coluna ou linha que não se aplica a uma célula específica. Em texto inline, prefira "não disponível" ou "não aplicável" por extenso para clareza.

⚠️ **novo**
Evite usar em documentação de produto e material de aprendizado, pois isso pode datar rapidamente seu conteúdo. Para mais informações, consulte [Recursos futuros](#describing-limitations).

**NRT / quase em tempo real (adjetivo) / quase tempo real (substantivo)**

**NYC / New York City**

#### O

**sob demanda**

**integração**

**uma vez**
Use para se referir a realizar uma ação uma única vez. Não use "uma vez" no lugar de "depois" ou "quando".

**taxa de abertura (OR)**

**pedido de aceitação**

**orquestração**

**SO / Sistema Operacional**

**OTT / Serviços de mídia over-the-top**

⛔️ **out-of-the-box**
Não use. Em vez disso, use uma alternativa como "padrão".

#### P

**parceiro, parceiros, parceria**

**persona (singular) / personas (plural)**

**personalização**

**informações pessoalmente identificáveis (PII)**

**Personalized Path**
Use capitalização de título.

**Personalized Variant**
Use capitalização de título.

**PhD / PhDs**

**pm**
Minúsculas quando usado para horário (por exemplo, "10 pm"). Veja também [am](#glossary).

**precedente**

**previsão**
Minúsculas, a menos que precedido por "Braze", como "Uma Braze Prediction é…".

**análises preditivas**

**Predictive Churn**
Use capitalização de título. Predictive Churn é o nome do produto, enquanto os clientes criam uma [previsão de churn](#glossary).

**Predictive Events**
Use capitalização de título.

**Predictive Purchases**
Use capitalização de título. Predictive Purchases é o nome do produto, enquanto os clientes criam uma [previsão de compra](#glossary).

**Predictive Suite**
Use capitalização de título.

**Central de Preferências**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**preparação para localização**

**preparação para push**

**código de promoção**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado. Não use "código promo".

**previsão de compra**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**propriedades de compra**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**botões de ação por push**

**Push Max**
Use capitalização de título.

**notificação por push**

**Push Stories**
Use capitalização de título.

#### Q

**Q&A**

⛔️ **QA (garantia de qualidade)**
Não use a sigla como verbo. Em vez disso, reescreva como "realizar garantia de qualidade".

**horário de silêncio**
Use "Horário de silêncio" no início da frase e "horário de silêncio" no meio da frase. Não use capitalização de título "Horário de Silêncio" porque não é um recurso de marca.

⚠️ **rápido / rapidamente**
Evite usar. O que é rápido para você pode não ser rápido para outros. Para diretrizes relacionadas, consulte [Linguagem condescendente](#condescending-language).

#### R

**limite de taxa**

**tempo real (substantivo) / em tempo real (adjetivo)**

**reengajamento**

⚠️ **expressão regular / regex**
Prefira a versão por extenso em vez da abreviada "regex". Não use "RegEx".

**marketing de relacionamento**

**redirecionamento**

**retenção**

**rich push**

**clique com botão direito**

**deslize para a direita**

**ROI / retorno sobre o investimento**

#### S

**Sage AI by Braze™**

⛔️ **sanity check**
Não use. Em vez disso, use um termo como "verificação rápida" ou "verificação preliminar". Alternativamente, introduza instruções de verificação com uma frase como "Vamos verificar se tudo está funcionando".

**entrega agendada**
Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**captura de tela**

**captura de tela**

**SDK / Kit de desenvolvimento de software**

**segmento (público)**

**Extensões de segmento**
Use capitalização de título.

**Insights de segmento**
Use capitalização de título.

**Segmentação**

**seleção**
Como no recurso dentro de catálogos. Minúsculas, exceto quando se refere a um elemento da interface que está capitalizado.

**SF / San Francisco**

**Silicon Valley**

**silo, silos, isolado**

**pesquisa simples**

**apresentação de slides**

**Smartphone**

**Smartwatch**

**SMS**

**software como serviço (SaaS)**
Escreva por extenso na primeira menção, depois é aceitável usar a sigla.

**teste de spam**

**SQL / linguagem de consulta estruturada**

**SQL Segment Extensions**
Use capitalização de título.

**stickiness**

**streaming**

**string**
Para públicos não técnicos, defina uma string como texto que contém "caracteres alfanuméricos". Para públicos técnicos, não é necessário definir este termo.

**grupo de inscrições**

**sunsetting**

#### T

**resposta direcionada**

⚠️ **terminate**
Evite usar a menos que se refira a um processo especificamente nomeado. Em vez disso, use palavras como "parar", "sair", "cancelar" ou "encerrar".

**de terceiros**

**fuso horário**
Não "timezone".

**timestamp**

**tela sensível ao toque**

**mensagem disparada**

**Twitter**

#### U

**UK / Reino Unido**

⛔️ **unzip**
Não use. Em vez disso, use "extrair".

**URL**
Pronunciado como as letras individuais U-R-L, então escreva "uma URL" em vez de "um URL". Use maiúsculas. Para plurais, use URLs.

**US / USA**
Sem pontos.

**casos de uso**

**atributos de usuário / atributos de usuário padrão**
Use para se referir a dados de usuário capturados automaticamente pela Braze.

**perfil de usuário**

**nome de usuário**

⚠️ **utilizar**
Não use "utilizar" quando quer dizer "usar". Use "utilizar" para se referir a algo sendo usado além de seu propósito original pretendido.

#### V

**variante**

⛔️ **via**
Não use. Em vez disso, use termos como "por meio de" ou frases como "através de".

⛔️ **vice-versa**
Não use. Em vez disso, use termos como "inversamente" ou uma frase como "o contrário".

**somente visualização**

⚠️ **vs.**
Não use "vs." como abreviação de "versus". Em vez disso, escreva a palavra por extenso.

#### W

**mensagens pela internet**

**push para a web**

**webhook**

**webinar**

**marca branca**

⛔️ **lista de permissões**
Não use a menos que se refira à interface. Em vez disso, use "lista de permissões" ou "lista segura". Para a forma verbal dessas palavras, considere reformular a frase para remover o termo problemático. Para exemplos, consulte [lista de proibições](#glossary).

⚠️ **Wi-Fi**
Não use "WiFi", "wi-fi" ou "wifi".

**will**
Evite usar "will" ou "would". Consulte [Tempo presente](#present-tense).

**Winning Path**
Use capitalização de título.

**Winning Variant**
Use capitalização de título.

⛔️ **wizard**
Não use. Em vez disso, use "criador".

**WordPress**

**espaço de trabalho**

**www**

#### Y

**YAML**
Não use uma extensão de arquivo para se referir ao tipo de arquivo. Por exemplo, use "arquivo YAML" em vez de "arquivo .yaml".

**YouTube**

#### Z

**CEP**

**arquivo zip / arquivos compactados**

**ZIP**
Não use uma extensão de arquivo para se referir ao tipo de arquivo. Por exemplo, use "arquivo ZIP" em vez de "arquivo .zip".