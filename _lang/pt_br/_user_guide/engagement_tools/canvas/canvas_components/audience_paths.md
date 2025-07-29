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

## Como funciona?



Os caminhos do público são semelhantes a funis de classificação com critérios de classificação. Os usuários são avaliados para cada critério em ordem de prioridade e enviados pela jornada dos critérios de maior classificação para os quais se qualificam. Isso reduz a ambiguidade de onde os usuários irão e quais mensagens eles receberão. Nota que os rankings não são [editáveis após o lançamento]({{site.baseurl}}/post-launch_edits/).

Com as jornadas do público, você pode:

- Envie os usuários por diferentes caminhos de canva com base em critérios do público.
- Atribuir prioridade a diferentes grupos de público, para que suas mensagens cheguem aos usuários corretos. 
  - Anteriormente, se os usuários atendessem aos critérios de dois possíveis passos completos, eles seriam atribuídos aleatoriamente. 
- Direcione usuários de forma precisa em grande escala.
  - Crie até oito grupos de público (dois padrões e seis grupos adicionais) por componente, mas você pode querer conectar várias Etapas de Caminhos de Público para classificar ainda mais seus usuários. 

### Permitir tempo para avaliações de usuários



Os usuários são avaliados assim que chegam à etapa da jornada do público. Depois de serem avaliados, eles passarão imediatamente para a próxima etapa. Isso torna importante permitir que uma janela de tempo apropriada passe se a Jornada do público for determinada por uma ação do usuário.

Por exemplo, se os usuários receberem a Mensagem A e a próxima etapa for uma jornada do público que avalia se eles interagiram com essa mensagem, todos os usuários avançarão para a etapa daqueles que não interagiram com essa mensagem. Isso ocorre porque os usuários avançaram imediatamente para a etapa da jornada do público sem tempo para interagir com a mensagem. Em outras palavras, os usuários são avaliados quanto a uma interação com a mensagem quase imediatamente após o envio da mensagem.

Para dar aos usuários tempo para interagir com uma mensagem enviada, é necessário haver uma postergação entre a etapa Mensagem e a Jornada do público. Por exemplo, uma postergação de 24 horas daria aos usuários 24 horas após o envio da mensagem para interagir com a Mensagem A antes de ser avaliada.

 

## Criando uma jornada do público

Para adicionar uma etapa de Jornadas do público, faça o seguinte: 

1. Adicione uma etapa ao seu canva. 
2. Arraste e solte o componente da barra lateral ou selecione <i class="fas fa-plus-circle"></i> **Add** na parte inferior de uma etapa e selecione **Jornadas do público**.

O componente de Caminhos de Público padrão contém dois grupos de público padrão, **Grupo 1** e **Todos os Outros**. O grupo **Todos os Outros** inclui qualquer usuário que não se enquadre em um grupo de público definido. Este grupo sempre será o último na classificação.

### Definindo grupos de público

A captura de tela a seguir mostra o layout de uma etapa de Caminhos do público expandida. Aqui, você pode definir até oito grupos de público (um predefinido e sete personalizáveis). Para definir um grupo de público, selecione o nome do grupo no editor de Caminhos do Público. Você pode renomear seu grupo de público, escolher os filtros e segmentos que se aplicam ao seu grupo e adicionar ou excluir grupos.





Depois que a etapa Jornada do público estiver concluída, cada grupo de público terá um ramo separado. Você pode continuar usando os Caminhos do Público para filtrar ainda mais seu público, ou continuar sua jornada no Canva com as etapas padrão do Canva. 



### Testando grupos de público

Depois de adicionar segmentos e filtros ao seu público, você pode testar se seus grupos de público estão configurados conforme o esperado [procurando um usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar se eles correspondem aos critérios do público.



## Uso de jornadas do público

O verdadeiro poder dos Caminhos do público reside na capacidade de atribuir prioridade. Embora esse recurso não precise ser usado estrategicamente, alguns <b><i><u>}profissionais de marketing<{biu} podem se ver empurrando certos produtos para os usuários, como <b><i><u>}ofertas especiais<{biu} ou lançamentos de edição limitada. 

Ao atribuir alta prioridade a esses grupos, você pode direcionar usuários que se enquadram em filtros e segmentos específicos, enquanto ainda direciona usuários que podem não se encaixar nesses critérios específicos—tudo em uma única etapa do canva.



Por exemplo, digamos que você queria enviar a um grupo de usuários anúncios de novos produtos. Você começaria classificando os filtros que se enquadram nesses produtos no topo da jornada do público.  

    

Você também pode ver a performance desta etapa usando [canva análise de dados]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization).

### Segmentando caminhos do público com números de bucket aleatórios

Se o seu canva usar um [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) (como limitar o total de usuários que receberão o canva), a Braze recomenda que você não use números de bucket aleatórios para segmentar seus caminhos de público. 

Um [número de balde aleatório]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) é um atributo de usuário que pode ser usado para criar segmentos uniformemente distribuídos de usuários aleatórios. Braze usa o número do bucket aleatório para agrupar usuários durante a fase de segmentação da entrada do canva, e cada grupo é processado separadamente. Dependendo de quais grupos terminam o processamento primeiro, alguns usuários podem ser limitados na entrada devido ao limite de frequência, o que pode causar uma distribuição desigual de usuários quando eles alcançam a etapa de Caminhos do Público.

Neste cenário, tente usar [Caminhos de Experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) em vez disso.

### Uso do filtro de canal inteligente com jornadas do público

Usando uma combinação de etapas de jornadas do público e filtros de canais inteligentes, é possível personalizar a experiência de envio de mensagens de acordo com as preferências e os comportamentos de cada usuário. Dessa forma, seus usuários receberão as mensagens mais relevantes por meio dos canais apropriados.

Por exemplo, em uma etapa de jornadas do público, você pode criar três públicos: E-mail, push móvel e todos os outros. Para o público de e-mail, adicione o filtro `Intelligent Channel is Email`. Para o público do Mobile Push, adicione o filtro `Intelligent Channel is Mobile Push`. Em seguida, você pode adicionar uma etapa de Mensagem para cada uma das jornadas do público para fornecer mensagens personalizadas e relevantes.

{% alert tip %}
Confira nossos [modelos do Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para ver exemplos de como você pode personalizar esses modelos pré-criados a seu favor.
{% endalert %}
