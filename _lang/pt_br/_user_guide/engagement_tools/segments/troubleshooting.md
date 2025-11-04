---
nav_title: Solução de problemas
article_title: Segmentos de solução de problemas
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Este artigo de referência aborda as etapas de solução de problemas e as considerações que devem ser levadas em conta ao usar segmentos."
---

# Segmentos de solução de problemas

## Erros

### O público-alvo é muito complexo para ser lançado

Esse erro raro ocorre se o público-alvo contiver muitos valores de regex, valores de regex excessivamente longos, filtros excessivamente detalhados (como "é qualquer um dos 30.000 códigos postais") ou muitos filtros. Isso inclui todos os filtros em uma campanha ou público-alvo do Canvas, quer os filtros estejam localizados nos segmentos referenciados ou adicionados como filtros na etapa **Público-alvo**.

Quando você adiciona filtros de segmento a uma campanha ou Canvas, esses filtros são traduzidos em consultas no Braze (a contagem de caracteres dessas consultas não é 1:1 para o número de caracteres que um usuário do painel vê). Quando a Braze envia uma campanha ou Canvas, executamos uma consulta que combina todos os filtros do público-alvo. Aplicamos um limiar que limita o número de caracteres na consulta resultante para um público-alvo. Para uma determinada campanha ou Canvas, somamos a contagem de caracteres em todos os segmentos referenciados, incluindo todos os filtros adicionais. Para um determinado segmento, somamos a contagem de caracteres em todos os filtros e valores de filtro.

Seu painel exibirá um erro quando uma campanha, Canvas ou segmento exceder o limite e não puder ser lançado. Se você receber esse erro, simplifique seu público-alvo antes de iniciar novamente, inclusive:

- Se o seu público-alvo fizer referência a vários segmentos, certifique-se de que os segmentos não tenham redundâncias, como os mesmos filtros que aparecem em vários segmentos.
- Certifique-se de que não esteja fazendo referência a dados desatualizados nos filtros de segmento. Por exemplo, um filtro desatualizado pode procurar usuários que não tenham recebido uma determinada etapa do Canvas na semana passada, mesmo que o Canvas tenha sido interrompido há meses.
- Os segmentos que são apenas listas de IDs de usuários ou e-mails (que geralmente usam um filtro regex) podem ser convertidos em uma [importação de CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) e simplificados em um único filtro CSV.
- Se você tiver CDI, poderá criar um segmento de CDI que extraia o grupo diretamente do seu data warehouse.

Você também pode [entrar em contato com o Suporte]({{site.baseurl}}/braze_support/) para obter mais assistência com a otimização do filtro.

{% alert note %}
Começamos a limitar a contagem de caracteres em abril de 2025. As campanhas e os Canvases lançados antes de abril de 2025 foram protegidos, o que significa que eles podem continuar excedendo o limite, enquanto as campanhas e os Canvases recém-criados não podem exceder o limite. Se você editar ou clonar uma campanha ou um Canvas antigo, **não poderá** lançá-lo até que o público-alvo seja atualizado para ficar abaixo do limite.
{% endalert %}

### X campanhas ou Canvases ativos ou parados excedem o limite de complexidade do público-alvo

Esse banner é exibido na parte superior de uma lista de campanhas ou telas sempre que campanhas ou telas ativas ou interrompidas têm públicos que excedem o limite de complexidade do público. Selecione o banner para filtrar a lista apenas para as campanhas ou Canvases que excedem o limite e, em seguida, siga as etapas de solução de problemas em [O público-alvo é muito complexo para ser lançado](#target-audience-is-too-complex-to-launch).

### O filtro excede 10.000 caracteres ou é muito longo para ser salvo

A Braze limita os filtros de segmentos individuais a um máximo de 10.000 caracteres. Um aviso é exibido sempre que um filtro individual excede 10.000 caracteres, quer o filtro esteja em um segmento ou seja adicionado diretamente à campanha ou ao Canvas. 

Esse erro ocorre muito raramente, mas, quando ocorre, é normalmente com filtros regex que têm como alvo uma lista de IDs de usuário ou endereços de e-mail. Nesse caso, você pode seguir estas etapas para converter os filtros em um CSV:

1. Exporte os usuários do segmento afetado ou do filtro regex específico. 
2. Limpe o CSV conforme necessário. Você precisa do Braze ID ou do Appboy ID, mas pode remover todas as outras colunas se elas não forem necessárias. Também recomendamos revisar seus dados para confirmar se são recentes (por exemplo, remover usuários que não estão mais tentando segmentar).
3. [Importe]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) o arquivo CSV novamente, o que agrupa automaticamente os usuários em um único filtro baseado em CSV altamente eficiente.

## Comportamento do usuário

### O usuário não está mais em um segmento

Se um usuário não estiver disponível durante a criação de um segmento, seus dados de usuário que determinam a elegibilidade do segmento poderão ter sido alterados como resultado de sua própria atividade ou de outras campanhas e Canvases com os quais ele interagiu anteriormente. Se a reelegibilidade estiver ativada, seu perfil de usuário mostrará os dados mais recentes da campanha recebida.

### As informações são exibidas para usuários de outros aplicativos quando eu filtro para um aplicativo específico

Os usuários podem ter vários aplicativos, portanto, a seleção de um aplicativo específico na seção **Aplicativos usados** da página de segmentação produzirá resultados para os usuários que tenham pelo menos esse aplicativo. O filtro não produz resultados para os usuários que têm exclusivamente esse aplicativo.

## Filtragem

### Opções de filtro alteradas

Suas opções de filtro estão relacionadas ao formato (tipo de dados) que você está passando para o Braze para seu atributo personalizado. Para revisar o tipo de dados que o Braze está reconhecendo para seus atributos personalizados, navegue até **Configurações de dados** > **Atributos personalizados**.

Se as opções de filtro tiverem mudado, isso é uma indicação de que os dados estão sendo passados para o Braze em um formato (tipo de dados) diferente do anterior. Para obter descrições detalhadas de diferentes tipos de dados e suas opções de filtragem, consulte [tipos de dados de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#custom-attribute-data-types).

Lembre-se de que alterar o tipo de dados de um atributo personalizado no painel rejeitará os dados enviados ao Braze em um formato diferente.

## Análises e relatórios

### *A mensagem enviada* ou *os destinatários únicos* no Campaign Analytics não correspondem à contagem de segmentos 

Se a contagem da análise de sua campanha para *Message Sent* ou *Unique Recipients* não corresponder ao número de usuários no filtro de segmento `Has received message from campaign X`, pode haver dois motivos possíveis:

1. **Os usuários podem ter sido arquivados, abandonados ou excluídos desde o lançamento da campanha**<br><br>Por exemplo, digamos que 1.000 usuários recebam uma campanha e você faça uma exportação CSV no mesmo dia. Você verá 1.000 usuários relatados. No mês seguinte, 50 desses 1.000 usuários são excluídos (por exemplo, pelo endpoint `users/delete` ). Ao fazer outra exportação CSV, você verá 950 usuários relatados, enquanto a contagem de *Unique Recipient* no **Campaign Analytics** ainda é de 1.000.<br><br>Em outras palavras, a métrica *Unique Recipients* é uma contagem incrementada, enquanto o segmentador e a exportação de CSV fornecem uma contagem de usuários existentes no momento.<br><br>

2. **A campanha tem a reelegibilidade definida, de modo que os usuários podem entrar novamente na campanha várias vezes**<br><br>Por exemplo, digamos que uma campanha de e-mail tenha a reelegibilidade definida como zero minutos (os usuários podem entrar novamente na campanha desde que atendam aos requisitos do segmento de público-alvo) e a campanha esteja em execução há mais de um mês. O número de *mensagens enviadas* no **Campaign Analytics** não corresponderia ao número no segmento porque esse campo incluiria mensagens enviadas a usuários duplicados.<br><br>Isso ocorre porque o Braze conta os usuários únicos como *Unique Daily Recipients*, ou o número de usuários que receberam uma determinada mensagem em um dia. Isso significa que os usuários reelegíveis serão contados mais de uma vez como um destinatário único, pois a janela "única" dura apenas um dia. Isso pode fazer com que o número de *destinatários diários únicos* seja maior do que o número de perfis de usuário na exportação CSV. Os perfis de usuário no arquivo CSV serão realmente exclusivos.

### O usuário é atribuído a dois aplicativos, apesar de registrar uma sessão em apenas um aplicativo

Ao criar um segmento, você pode segmentar usuários que [usaram aplicativos específicos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform). Um usuário precisa ter tido uma sessão em um aplicativo específico para ser atribuído a esse aplicativo; no entanto, há dois cenários em que um usuário ainda pode ser atribuído a um aplicativo específico sem ter registrado sessões no aplicativo. 

O primeiro cenário é se o campo `app_id` for preenchido ao usar o ponto de extremidade `/users/track` \- especificamente ao usar um [evento]({{site.baseurl}}/api/objects_filters/event_object/) ou [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/), como neste exemplo:

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

O segundo cenário é se o campo `app_id` for preenchido ao usar o ponto de extremidade `/users/track` para migrar tickets por push, como neste exemplo: 

```json
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
```
