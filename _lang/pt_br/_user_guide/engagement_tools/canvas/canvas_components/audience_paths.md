---
nav_title: Caminhos do público
article_title: Caminhos do público 
alias: /audience_paths/
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como usar o Audience Paths no Canvas para filtrar e segmentar intuitivamente os usuários em grande escala com agrupamentos estratégicos de usuários baseados em prioridades."
tool: Canvas

---

# Caminhos do público 

> Os Canvas Audience Paths permitem filtrar e segmentar intuitivamente os usuários em grande escala com agrupamentos estratégicos de usuários baseados em prioridades. 

Esse componente do Canvas substitui a necessidade de criar etapas completas excessivas com base no público, permitindo que você combine o que poderiam ser oito componentes completos em um só. Isso ajuda a simplificar a segmentação de usuários e, ao mesmo tempo, a eliminar a desordem e a complexidade desnecessárias dos Canvases. 

## Como funciona

\![Um Audience Path com dois grupos: usuários engajados e todos os outros.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Os caminhos do público-alvo são semelhantes aos funis de classificação com critérios de classificação. Os usuários são avaliados para cada critério em ordem de prioridade e enviados para o caminho dos critérios de classificação mais alta que se qualificam. Isso reduz a ambiguidade de onde os usuários irão e quais mensagens eles receberão. Observe que as classificações não são [editáveis após o lançamento]({{site.baseurl}}/post-launch_edits/).

Com o Audience Paths, você pode:

- Envie os usuários para diferentes caminhos do Canvas com base nos critérios do público.
- Atribua prioridade a diferentes grupos de público, para que suas mensagens cheguem aos usuários corretos. 
  - Anteriormente, se os usuários atendessem aos critérios de duas etapas completas em potencial, eles seriam atribuídos aleatoriamente. 
- Direcione com precisão os usuários em grande escala.
  - Crie até oito grupos de público-alvo (dois grupos padrão e seis grupos adicionais) por componente, mas talvez você queira conectar várias etapas de caminhos de público-alvo para classificar ainda mais seus usuários. 

### Permitir tempo para avaliações de usuários

Canvas mostrando um atraso de 24 horas após uma etapa de Mensagem, seguido por um Caminho do Público.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Os usuários são avaliados assim que chegam à etapa Audience Path. Depois de serem avaliados, eles passarão imediatamente para a próxima etapa. Isso torna importante permitir que uma janela de tempo apropriada passe se o Caminho do público-alvo for determinado por uma ação do usuário.

Por exemplo, se os usuários receberem a Mensagem A e a próxima etapa for um Caminho do público-alvo que avalia se eles interagiram com essa mensagem, todos os usuários avançarão para a etapa daqueles que não interagiram com essa mensagem. Isso ocorre porque os usuários avançaram imediatamente para a etapa do Caminho do público-alvo sem tempo para interagir com a mensagem. Em outras palavras, os usuários são avaliados quanto a uma interação com a mensagem quase imediatamente após o envio da mensagem.

Para que os usuários tenham tempo de interagir com uma mensagem enviada, é necessário haver um atraso entre a etapa da mensagem e o caminho do público-alvo. Por exemplo, um atraso de 24 horas daria aos usuários 24 horas após o envio da mensagem para interagir com a Mensagem A antes de ser avaliada.

Observe que os usuários avançam para a próxima etapa com base na primeira ação que realizaram após entrar na etapa Audience Path na janela de avaliação. Isso significa que, se um usuário realizar um segundo evento personalizado, ele não trocará de grupo de público.

## Criação de um caminho de público-alvo

Para adicionar uma etapa do Audience Paths, faça o seguinte: 

1. Adicione uma etapa ao seu Canvas. 
2. Arraste e solte o componente da barra lateral ou selecione <i class="fas fa-plus-circle"></i> **Add** na parte inferior de uma etapa e selecione **Audience Paths**.

O componente Audience Paths padrão contém dois grupos de público-alvo padrão, **Group 1** e **Everybody Else**. O grupo **Everybody Else** inclui qualquer usuário que não se enquadre em um grupo de público-alvo definido. Esse grupo sempre será classificado em último lugar.

### Definição de grupos de público-alvo

A captura de tela a seguir mostra o layout de uma etapa expandida de Audience Paths. Aqui, você pode definir até oito grupos de público (um predefinido e sete personalizáveis). Para definir um grupo de público-alvo, selecione o nome do grupo no editor de Caminhos de público-alvo. Você pode renomear seu grupo de público-alvo, escolher os filtros e segmentos que se aplicam ao seu grupo e adicionar ou excluir grupos.

Por exemplo, se você quiser direcionar mensagens de integração para um grupo de usuários, poderá selecionar filtros de redirecionamento, como "Clicou no e-mail" e "Clicou na mensagem no aplicativo".

\![Um caminho de público expandido com grupos para "Loves Asian Cuisine", "Loves Latin Cuisine", "Loves European Cuisine" e "Everyone Else".]({% image_buster /assets/img/audience_path/audience_path3.png %})

Após a conclusão da etapa Caminhos do público-alvo, cada grupo de público-alvo terá uma ramificação separada. Você pode continuar usando os Caminhos do público-alvo para filtrar ainda mais seu público-alvo ou continuar sua jornada no Canvas com as etapas padrão do Canvas. 

\![Dois caminhos de público com grupos diferentes com base no engajamento.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

### Teste de grupos de público-alvo

Depois de adicionar segmentos e filtros ao seu público, você pode testar se os grupos de público estão configurados conforme o esperado, [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

\![A seção "User Lookup" (Pesquisa de usuário).]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Uso de caminhos de público-alvo

O verdadeiro poder do Audience Paths está na capacidade de atribuir prioridade. Embora esse recurso não precise ser usado estrategicamente, alguns profissionais de marketing podem acabar empurrando determinados produtos para os usuários, como promoções ou lançamentos de edição limitada. 

Ao atribuir uma alta prioridade a esses grupos, você pode direcionar usuários que se enquadram em filtros e segmentos específicos e, ao mesmo tempo, direcionar usuários que talvez não se encaixem nesses critérios específicos - tudo em uma única etapa do Canvas.

\![Um caminho de público-alvo com grupos para "Gosta de calçados de marca grande", "Gosta de marca grande" e "Todos os outros".]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Por exemplo, digamos que você queira enviar a um grupo de usuários anúncios de novos produtos. Você começaria classificando os filtros que se enquadram nesses produtos no topo do caminho do público-alvo. Se você estivesse criando uma campanha de marketing para a empresa "Big Brand" e uma nova marca de varejo tivesse acabado de ser lançada, você poderia selecionar filtros como "Gosta de sapatos Big Brand" ou "Gosta de bolsas Big Brand" e enviar mensagens de e-mail diferentes com base no grupo filtrado em que eles se enquadram. 

Quando os usuários entrarem nesse componente Audience Paths, eles serão avaliados primeiro se se enquadram no grupo de público-alvo mais bem classificado: O Grupo de Público 1 "Gosta de calçados de grandes marcas". Em caso afirmativo, eles continuarão para o próximo componente definido em seu Canvas. Se não "Gostar de calçados de grandes marcas", eles serão avaliados para o próximo grupo de público-alvo, o Grupo de público-alvo 2 "Gostar de bolsas de grandes marcas", e continuarão na próxima etapa se os critérios forem atendidos. Por fim, os usuários que não se enquadram nos grupos anteriores se enquadrariam no grupo "Todos os outros" e também continuariam na próxima etapa do Canvas que você definiu para esse caminho.

Você também pode ver o desempenho dessa etapa usando [o Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization).

### Segmentação de caminhos de público-alvo com números aleatórios

Se o seu Canvas usar um [limite de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) (como limitar o número total de usuários que receberão o Canvas), a Braze recomenda que você não use números aleatórios para segmentar seus Caminhos do público. 

Um [número de bucket aleatório]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) é um atributo de usuário que pode ser usado para criar segmentos uniformemente distribuídos de usuários aleatórios. O Braze usa o número de bucket aleatório para agrupar usuários durante a fase de segmentação da entrada do Canvas, e cada grupo é processado separadamente. Dependendo de quais grupos terminam o processamento primeiro, alguns usuários podem ser limitados na entrada devido ao limite de taxa, o que pode causar uma distribuição desigual de usuários quando eles alcançam a etapa de Caminhos do público.

Nesse cenário, tente usar [os caminhos de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).

### Uso do filtro de canal inteligente com caminhos de público-alvo

Usando uma combinação de etapas do Audience Paths e filtros do Intelligent Channel, você pode personalizar a experiência de mensagens de acordo com as preferências e os comportamentos de cada usuário. Dessa forma, seus usuários receberão as mensagens mais relevantes por meio dos canais apropriados.

Por exemplo, em uma etapa de Caminhos do público, você pode criar três públicos: E-mail, Mobile Push e todos os outros. Para o público-alvo Email, adicione o filtro `Intelligent Channel is Email`. Para o público do Mobile Push, adicione o filtro `Intelligent Channel is Mobile Push`. Em seguida, você pode adicionar uma etapa de Mensagem para cada um dos caminhos de público-alvo para fornecer mensagens personalizadas e relevantes.

{% alert tip %}
Confira nossos [modelos do Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para ver exemplos de como você pode personalizar esses modelos pré-criados para seu benefício.
{% endalert %}
