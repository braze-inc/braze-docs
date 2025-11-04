---
nav_title: Espaços de Trabalho
article_title: "Introdução: Espaços de Trabalho"
page_order: 3
page_type: reference
description: "Tudo o que você faz na plataforma Braze acontece dentro de um espaço de trabalho. Este artigo descreve como eles funcionam e quais considerações importantes ter em mente ao planejar seus espaços de trabalho no Braze."
---

# Introdução: Espaços de Trabalho

Tudo o que você faz na plataforma Braze acontece dentro de um espaço de trabalho. Os espaços de trabalho atuam como silos de dados separados e permitem que você mantenha diferentes marcas ou atividades separadas. Múltiplas versões do seu site ou aplicativo móvel podem enviar dados para o mesmo espaço de trabalho. Nos referimos aos diferentes sites e aplicativos que são coletados dentro de um espaço de trabalho como "instâncias de aplicativo."

## Entendendo os espaços de trabalho

Os espaços de trabalho servem a dois propósitos principais:

- **Unificando dados do usuário:** Quando várias instâncias de aplicativo estão em um espaço de trabalho, você pode reunir e segmentar dados do usuário de forma contínua entre diferentes versões do seu aplicativo, como iOS, Android e web. Isso garante que você sempre tenha informações atualizadas sobre cada usuário, independentemente da plataforma que estão usando.
- **Separando atividades distintas:** Os espaços de trabalho também fornecem um meio de manter marcas ou atividades distintas separadas. Por exemplo, se você tiver várias sub-marcas com diferentes bases de usuários, é benéfico criar espaços de trabalho separados para cada uma.

{% alert tip %}
Essa abordagem é particularmente útil para empresas como firmas de jogos móveis que podem gerenciar espaços de trabalho individuais para cada um de seus jogos ou sites de eCommerce que desejam espaços de trabalho separados para cada região em que operam.
{% endalert %}

## Planejando espaços de trabalho

Você deve criar instâncias de aplicativo separadas para cada versão do seu aplicativo em cada plataforma. Ao decidir quais instâncias de aplicativo incluir em um espaço de trabalho, pense nos usuários que você deseja atingir e agrupe-os de acordo.

A atração de ter várias instâncias de aplicativo sob um único espaço de trabalho pode ser tentadora, pois permite limitar a taxa de mensagens em todo o seu portfólio de aplicativos. No entanto, como uma boa prática, sugerimos colocar apenas diferentes versões dos mesmos aplicativos (ou muito semelhantes) juntas em um único espaço de trabalho.

### Espaços de trabalho compartilhados

Exemplos comuns de quando você gostaria de ter várias instâncias de aplicativo no mesmo espaço de trabalho:

- Quando você tem vários aplicativos quase idênticos em diferentes plataformas
- Quando você tem diferentes revisões principais do aplicativo, mas deseja continuar engajando os mesmos usuários quando eles atualizam
- Quando você tem diferentes versões do aplicativo que o mesmo usuário pode alternar (como de gratuito para premium)

#### Impacto nos filtros de segmentação

Quaisquer aplicativos que você escolher ter em um espaço de trabalho terão seus dados agregados. Isso terá um impacto notável nos seguintes filtros de segmentação no Braze (esta não é uma lista exaustiva):

- Último Aplicativo Usado
- Primeiro Aplicativo Usado
- Contagem de Sessões
- Dinheiro Gasto Dentro do Aplicativo
- Assinatura de Push (Isso se torna uma situação de tudo ou nada—se seus usuários cancelarem a assinatura de um aplicativo, eles serão cancelados de todos os aplicativos no espaço de trabalho.)
- Assinatura de Email (Isso se torna uma situação de tudo ou nada e pode deixá-lo vulnerável a problemas de conformidade.)

{% alert note %}
A agregação de dados entre instâncias de aplicativo nesses filtros é a razão pela qual não recomendamos abrigar aplicativos substancialmente diferentes dentro do mesmo espaço de trabalho. Isso pode tornar a segmentação complicada!
{% endalert %}

### Espaços de trabalho separados

Outras vezes, você pode desejar ter múltiplos espaços de trabalho separados. Exemplos comuns disso incluem:

- Espaços de trabalho separados para ambientes de desenvolvimento e produção do mesmo aplicativo
- Diferentes sub-marcas, por exemplo, uma empresa de jogos móveis que oferece vários jogos
- Diferentes localizações do mesmo aplicativo ou site que operam em diferentes países ou visam diferentes idiomas

### Considerações importantes

Lembre-se, os espaços de trabalho atuam como silos de dados separados. Todos os dados, sejam dados de usuários ou ativos de marketing, são armazenados dentro de um espaço de trabalho. Esses dados não podem ser facilmente compartilhados fora desse espaço de trabalho. 

Os seguintes são todos elementos-chave que são configurados dentro de um espaço de trabalho:

- [Instâncias de aplicativo](#app-instances)
- [Equipes](#teams)
- [Permissões de usuário do Braze](#braze-user-permissions) (mas não usuários do Braze)
- [Conectores Currents](#currents-connectors)
- [Perfis de usuário](#user-profiles) e os dados de usuário associados
- [Segmentos, campanhas e Canvases](#segments-campaigns-and-canvases)

#### Instâncias de aplicativo

Você deve criar instâncias de aplicativo separadas para cada versão do seu aplicativo em cada plataforma. Por exemplo, se você tiver versões Free e Pro do seu aplicativo tanto no iOS quanto no Android, crie quatro instâncias de aplicativo dentro do seu espaço de trabalho (aplicativo iOS gratuito, aplicativo Android gratuito, aplicativo iOS pro e aplicativo Android pro). Isso lhe dará quatro chaves de API para usar, uma para cada instância de aplicativo.

#### Equipes

[Equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) podem ser configuradas com base na localização da base de clientes, idioma e atributos personalizados, para que membros da equipe e não membros tenham diferentes acessos a recursos de mensagens e dados dos clientes.

#### Permissões de usuário do Braze

Os espaços de trabalho têm acesso independente e definições de permissões de usuário. [Permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) permitem que você crie controles granulares sobre o que um usuário de painel individual ou equipe tem acesso dentro de um único espaço de trabalho.

#### Conectores Currents

A ferramenta [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) é um fluxo de dados em tempo real dos seus eventos de engajamento que é a exportação mais robusta e ainda granular da plataforma Braze. Os conectores Currents estão incluídos em certos pacotes do Braze, e você pode ter recebido um inicialmente, assumindo um único espaço de trabalho.

Ao decidir entre criar espaços de trabalho separados ou combinados, é importante pensar sobre o número de conectores Currents que você possui, pois os conectores Currents não são compartilhados entre espaços de trabalho. 

Por exemplo, se você tiver espaços de trabalho separados para os ambientes de desenvolvimento e produção do mesmo aplicativo, ative seu conector Currents no espaço de trabalho de produção. Para habilitar Currents em ambos os espaços de trabalho, você precisará comprar um conector Currents adicional.

#### Perfis de usuário

Todos os dados persistentes associados a um usuário são armazenados em seu [perfil de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). No entanto, os perfis de usuário também são um ótimo recurso para solução de problemas e testes, pois você pode acessar facilmente informações sobre o histórico de engajamento de um usuário, associação a segmentos, dispositivo e sistema operacional.

#### Segmentos, campanhas e Canvases

Um segmento, campanha ou Canvas não pode referenciar ou acessar dados armazenados em outro espaço de trabalho. Por outro lado, quando vários aplicativos estão no mesmo espaço de trabalho, todos os aplicativos terão seus dados agregados. Isso terá um [impacto nos filtros no Braze](#impact-on-segmentation-filters).

### Visão geral de cada abordagem

A tabela a seguir descreve os benefícios e desvantagens dessas duas abordagens para o planejamento de espaços de trabalho:

- **Espaços de trabalho separados e perfis de usuário:** Um espaço de trabalho tem uma instância de aplicativo e uma pessoa tem um perfil de usuário para essa instância de aplicativo.
- **Espaços de trabalho compartilhados e perfis de usuário:** Um espaço de trabalho tem várias instâncias de aplicativo e uma pessoa tem um perfil de usuário para todas essas instâncias de aplicativo.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
</style>

<table>
    <tr>
        <th></th>
        <th colspan="2">Espaços de trabalho separados</th>
        <th colspan="2">Espaços de trabalho compartilhados</th>
    </tr>
    <tr>
        <th></th>
        <th>Benefícios</th>
        <th>Desvantagens</th>
        <th>Benefícios</th>
        <th>Desvantagens</th>
    </tr>
    <tr>
        <td>Segmentação</td>
        <td>A maneira mais segura de manter as comunicações separadas. As campanhas são garantidas para direcionar apenas perfis de usuário específicos.</td>
        <td>Incapaz de enviar mensagens de promoção cruzada, mesmo que você saiba que um usuário tem outro perfil de usuário em um espaço de trabalho diferente.</td>
        <td>Pode enviar mensagens de promoção cruzada se souber que um usuário tem vários aplicativos em seu espaço de trabalho.<br><br>Pode referenciar dados de usuário de diferentes aplicativos. Por exemplo, John tem o atributo X relevante para o App 1 e o atributo Y relevante para o App 2, que podem ser referenciados em uma campanha.</td>
        <td>Mais espaço para erro humano—você pode acidentalmente direcionar usuários em várias instâncias de aplicativo.<br><br>Para enviar mensagens no aplicativo, você deve ter eventos personalizados específicos do aplicativo para que uma campanha não apareça em outro aplicativo por acidente. Por exemplo, <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <td>Eventos e atributos personalizados</td>
        <td>Atributos e eventos personalizados são garantidos para serem específicos de uma instância de aplicativo.</td>
        <td>Não é possível rastrear o comportamento do usuário entre espaços de trabalho.<br><br><b>Dica:</b> Você pode aproveitar vários conectores Currents para realizar isso.</td>
        <td>Pode rastrear o comportamento do usuário em todas as instâncias do aplicativo no espaço de trabalho.</td>
        <td>Atributos e eventos personalizados se aplicariam a todas as instâncias do aplicativo, o que poderia dificultar a identificação de quais dados em um perfil de usuário são relevantes para qual instância do aplicativo. Por exemplo, "date_of_parking" é relevante para o App 1 ou App 2? Para combater isso, certifique-se de usar convenções de nomenclatura bem estruturadas.</td>
    </tr>
    <tr>
        <td>Limitação de frequência</td>
        <td>A limitação de frequência pode ser definida separadamente para cada instância do aplicativo (com base no espaço de trabalho).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>A limitação de frequência se aplica a todas as campanhas, não em uma base por aplicativo, o que torna mais difícil evitar o excesso de mensagens para os clientes.</td>
    </tr>
    <tr>
        <td>Status de assinatura para perfis de usuário</td>
        <td>O status de assinatura de cada perfil de usuário é exclusivo para cada instância do aplicativo.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Os status de assinatura de um perfil de usuário são combinados entre as instâncias do aplicativo.<br><br><b>Dica:</b> Você poderia usar <a href='/docs/user_guide/data/custom_data/custom_attributes'>atributos personalizados</a> para gerenciar as assinaturas de seus usuários.</td>
    </tr>
    <tr>
        <td>Permissões de usuário do Braze</td>
        <td>N/A</td>
        <td>Atualizar <a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>permissões do usuário</a> para um usuário do painel deve ser feito separadamente para cada espaço de trabalho ao qual o usuário precisa de acesso.</td>
        <td><a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>Permissões do usuário</a> podem ser definidas uma vez para um usuário do painel, e ele terá as mesmas permissões para todas as instâncias do aplicativo no espaço de trabalho.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Duplicando conteúdo</td>
        <td>N/A</td>
        <td>Não é possível duplicar segmentos, campanhas de push ou Content Card, ou Canvases entre espaços de trabalho.</td>
        <td>Pode [duplicar campanhas entre workspaces]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/copying_across_workspaces/) para os seguintes canais suportados: SMS, mensagens no aplicativo, e-mail, modelos de e-mail e Blocos de Conteúdo. <br><br>Pode duplicar segmentos, campanhas e Canvases para reutilizar conteúdo de uma instância do aplicativo para outra.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Análise</td>
        <td>As estatísticas globais serão precisas na página inicial.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>As estatísticas globais serão agregadas para todas as instâncias do aplicativo no espaço de trabalho na página inicial.</td>
    </tr>
</table>

## Melhores práticas

### Configure um espaço de trabalho de teste

Como uma melhor prática, sempre que você planejar configurar um espaço de trabalho de produção (um espaço de trabalho que enviará mensagens para usuários reais), você também deve configurar um espaço de trabalho de teste. Um espaço de trabalho de teste é uma duplicata do seu espaço de trabalho de produção sem nenhum dado de usuário real. 

Isso é considerado uma melhor prática por várias razões:

- **Isolamento de mudanças:** Permite que você teste novos recursos, configurações ou atualizações em um ambiente isolado sem afetar seu ambiente de produção ao vivo. Dessa forma, se algo der errado durante os testes, seu ambiente de produção permanece inalterado.
- **Teste preciso:** Permite testes mais precisos, uma vez que os dados no ambiente de teste podem ser controlados e manipulados sem se preocupar com dados do mundo real.
- **Depuração:** É mais fácil depurar problemas em um ambiente de teste, pois você pode manipular livremente o ambiente sem se preocupar em impactar o ambiente de produção.
- **Treinamento:** Novos membros da equipe podem se familiarizar com o espaço de trabalho em um ambiente seguro onde erros não terão consequências no mundo real.

{% alert tip %}
A ordem em que você configura um espaço de trabalho de teste e um espaço de trabalho de produção pode depender de suas necessidades e circunstâncias específicas. No entanto, geralmente é uma boa ideia configurar um espaço de trabalho de teste primeiro. Isso permite que você teste recursos, configurações e atualizações antes de serem implementados no espaço de trabalho de produção. Depois que você estiver satisfeito com os testes e resultados, poderá então estabelecer seu espaço de trabalho de produção.
{% endalert %}

### Adicionar administradores

Você deve ter mais de um usuário Braze com permissões de administrador para um único espaço de trabalho. Isso garante que haja pessoas suficientes em sua organização para gerenciar as permissões de outros usuários.

## Próximos passos

Depois de determinar seu plano de espaço de trabalho, é hora de criar seu espaço de trabalho e adicionar instâncias de aplicativo. Para etapas, confira [Criando e gerenciando espaços de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/).

