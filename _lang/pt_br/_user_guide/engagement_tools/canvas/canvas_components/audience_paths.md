---
nav_title: Jornadas do público 
article_title: Jornadas do público 
alias: /audience_paths/
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como usar os Caminhos do Público no seu Canva para filtrar e segmentar usuários de forma intuitiva em grande escala com agrupamentos de usuários baseados em prioridades estratégicas."
tool: Canvas

---

# Jornadas do público 

> Caminhos de {canva} {público} permitem que você filtre e segmente usuários de forma intuitiva em grande escala com agrupamentos de usuários estratégicos baseados em prioridades. 

Este componente de canva substitui a necessidade de criar etapas completas baseadas em público excessivo, permitindo que você combine o que poderia ter sido oito componentes completos em um. Isso ajuda você a simplificar o direcionamento do usuário enquanto limpa seus canvas de desordem e complexidade desnecessárias. 

![][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

Os caminhos do público são semelhantes a funis de classificação com critérios de classificação. Os usuários são avaliados para cada critério em ordem de prioridade e enviados pela jornada dos critérios de maior classificação para os quais se qualificam. Isso reduz a ambiguidade de onde os usuários irão e quais mensagens eles receberão. Nota que os rankings não são [editáveis após o lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/).

Com as jornadas do público, você pode:

- Envie os usuários por diferentes caminhos de canva com base em critérios do público.
- Atribuir prioridade a diferentes grupos de público, para que suas mensagens cheguem aos usuários corretos. 
  - Anteriormente, se os usuários atendessem aos critérios de dois possíveis passos completos, eles seriam atribuídos aleatoriamente. 
- Direcione usuários de forma precisa em grande escala.
  - Crie até oito grupos de público (dois padrões e seis grupos adicionais) por componente, mas você pode querer conectar várias Etapas de Caminhos de Público para classificar ainda mais seus usuários. 

## Criando uma jornada do público

![][1]{: style="float:right;max-width:20%;margin-left:15px;"}

Para adicionar uma etapa de Jornadas do público, faça o seguinte: 

1. Adicione uma etapa ao seu canva. 
2. Arraste e solte o componente da barra lateral ou clique em <i class="fas fa-plus-circle"></i> **Adicionar** na parte inferior de uma etapa e selecione **Caminhos do Público**.

O componente de Caminhos de Público padrão contém dois grupos de público padrão, **Grupo 1** e **Todos os Outros**. O grupo **Todos os Outros** inclui qualquer usuário que não se enquadre em um grupo de público definido. Este grupo sempre será o último na classificação.

### Definindo grupos de público

A captura de tela a seguir mostra o layout de uma etapa de Caminhos do público expandida. Aqui, você pode definir até oito grupos de público (um predefinido e sete personalizáveis). Para definir um grupo de público, selecione o nome do grupo no editor de Caminhos do Público. Você pode renomear seu grupo de público, escolher os filtros e segmentos que se aplicam ao seu grupo e adicionar ou excluir grupos.

Por exemplo, se você quiser enviar recomendações úteis de alimentos para um grupo de usuários, pode selecionar filtros de atributo personalizado que você já criou, como "Ama a Culinária Asiática", "Ama a Culinária Latina" e "Ama a Culinária Europeia". 

![][3]{: style="max-width:90%;margin-left:15px;"}

Depois que a etapa Jornada do público estiver concluída, cada grupo de público terá um ramo separado. Você pode continuar usando os Caminhos do Público para filtrar ainda mais seu público, ou continuar sua jornada no Canva com as etapas padrão do Canva. 

![][4]{: style="max-width:90%;margin-left:15px;"}

### Testando grupos de público

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Depois de adicionar segmentos e filtros ao seu público, você pode testar se seus grupos de público estão configurados conforme o esperado [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) para confirmar se eles correspondem aos critérios do público. 

## Uso de jornadas do público

O verdadeiro poder dos Caminhos do público reside na capacidade de atribuir prioridade. Embora esse recurso não precise ser usado estrategicamente, alguns <b><i><u>}profissionais de marketing<{biu} podem se ver empurrando certos produtos para os usuários, como <b><i><u>}ofertas especiais<{biu} ou lançamentos de edição limitada. 

Ao atribuir alta prioridade a esses grupos, você pode direcionar usuários que se enquadram em filtros e segmentos específicos, enquanto ainda direciona usuários que podem não se encaixar nesses critérios específicos—tudo em uma única etapa do canva.

![][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Por exemplo, digamos que você queria enviar a um grupo de usuários anúncios de novos produtos. Você começaria classificando os filtros que se enquadram nesses produtos no topo da jornada do público. Se você estivesse criando uma campanha de marketing para a empresa "Big Brand" e uma nova marca de sapatos tivesse acabado de ser lançada, você poderia selecionar filtros como "Gosta de Sapatos Big Brand" ou "Gosta de Big Brand", e enviar diferentes mensagens de e-mail com base no grupo filtrado em que eles se enquadram. 

Quando os usuários entrarem neste componente de Caminhos do Público, eles serão avaliados primeiro se estiverem no grupo de público mais bem classificado: Público Grupo A "Gosta de Sapatos de Grandes Marcas". Se for o caso, eles continuarão para o próximo componente definido na sua canva. Se eles não "Gostam de Grandes Marcas de Sapatos", eles serão então avaliados para o próximo grupo de público, Grupo de Público B "Gosta de Grandes Marcas", e continuarão para o próximo componente do canva se os critérios forem atendidos. Por fim, os usuários que não se enquadram nos grupos anteriores se enquadrariam no grupo **Todos os Outros** e continuariam para o próximo componente da canva que você definir para essa jornada.

Você também pode ver a performance desta etapa usando [canva análise de dados]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization).

### Segmentando caminhos do público com números de bucket aleatórios

Se o seu canva usar um [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) (como limitar o total de usuários que receberão o canva), a Braze recomenda que você não use números de bucket aleatórios para segmentar seus caminhos de público. 

Um [número de balde aleatório]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/) é um atributo de usuário que pode ser usado para criar segmentos uniformemente distribuídos de usuários aleatórios. Braze usa o número do bucket aleatório para agrupar usuários durante a fase de segmentação da entrada do canva, e cada grupo é processado separadamente. Dependendo de quais grupos terminam o processamento primeiro, alguns usuários podem ser limitados na entrada devido ao limite de frequência, o que pode causar uma distribuição desigual de usuários quando eles alcançam a etapa de Caminhos do Público.

Neste cenário, tente usar [Caminhos de Experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) em vez disso.

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
