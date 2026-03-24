---
nav_title: Solução de problemas
article_title: Solução de Problemas de Segmentos
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Este artigo de referência aborda as etapas de solução de problemas e as considerações que devem ser levadas em conta ao usar segmentos."
---

# Solução de problemas de segmentos

## Erros

### O público-alvo é muito complexo para ser lançado

Este erro raro ocorre se seu público-alvo contiver muitos valores regex, valores regex excessivamente longos, filtros excessivamente detalhados (como "é qualquer um dos 30.000 códigos postais") ou muitos filtros. Isso inclui todos os filtros em uma campanha ou público do Canvas, independentemente de os filtros estarem localizados dentro dos segmentos referenciados ou adicionados como filtros na etapa **Público-Alvo**.

![Erro para um público-alvo que atinge o limite de complexidade.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Quando você adiciona filtros de segmento a uma campanha ou Canvas, esses filtros são traduzidos em consultas no Braze (a contagem de caracteres dessas consultas não é 1:1 com o número de caracteres que um usuário do dashboard vê). Quando o Braze envia uma campanha ou Canvas, executamos uma consulta que combina todos os filtros no público-alvo. Aplicamos um limite que restringe o número de caracteres na consulta resultante para um público-alvo. Para uma determinada campanha ou Canvas, somamos a contagem de caracteres em todos os segmentos referenciados, incluindo todos os filtros adicionais. Para um determinado segmento, somamos a contagem de caracteres em todos os filtros e valores de filtro.

Seu dashboard exibirá um erro quando uma campanha, Canvas ou segmento exceder o limite e não puder ser lançado. Se você receber este erro, simplifique seu público-alvo antes de lançar novamente, incluindo:

- Se seu público referenciar vários segmentos, certifique-se de que os segmentos não tenham redundâncias, como os mesmos filtros aparecendo em vários segmentos.
- Certifique-se de que você não está referenciando dados desatualizados nos filtros de segmento. Por exemplo, um filtro desatualizado pode procurar usuários que não receberam uma determinada etapa do Canvas na última semana, mesmo que o Canvas tenha sido interrompido há meses.
- Segmentos que são apenas listas de IDs de usuários ou e-mails (que frequentemente usam um filtro regex) podem ser convertidos em um [importação CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) e simplificados em um único filtro CSV.
- Se você tiver CDI, pode ser capaz de criar um segmento CDI que puxe o grupo diretamente do seu data warehouse.

Você também pode [contatar o Suporte]({{site.baseurl}}/braze_support/) para mais assistência com a otimização de filtros.

{% alert note %}
Começamos a limitar a contagem de caracteres em abril de 2025. Campanhas e Canvases que foram lançados antes de abril de 2025 foram isentos, o que significa que podem continuar excedendo o limite, enquanto campanhas e Canvases recém-criados não podem exceder o limite. Se você editar ou clonar uma campanha ou Canvas que já foi criada, você **não** poderá lançá-la até que o público seja atualizado para ficar abaixo do limite.
{% endalert %}

### X campanhas ou Canvases ativas ou paradas excedem o limite de complexidade do público

Este banner é exibido no topo de uma lista de campanhas ou Canvases sempre que campanhas ou Canvases ativas ou paradas têm públicos que excedem o limite de complexidade do público. Selecione o banner para filtrar a lista apenas para as campanhas ou Canvases que excedem o limite, e siga os passos de solução de problemas em [O público-alvo é muito complexo para lançar](#target-audience-is-too-complex-to-launch).

![Banner de erro que diz que 4 Canvases ativas ou paradas excedem o limite de complexidade do público.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### O filtro excede 10.000 bytes ou é longo demais para salvar

A Braze limita os filtros de segmentos individuais a um máximo de 10.000 bytes, o que equivale a 10.000 caracteres em inglês ou 3.333 caracteres em japonês. Um aviso aparece sempre que um filtro individual excede 10.000 bytes, seja o filtro dentro de um segmento ou adicionado diretamente à campanha ou Canvas. 

![Banner de erro para um filtro que tem um valor que excede 10.000 caracteres.]({% image_buster /assets/img/segment/filter_error.png %})

![Erro para um filtro de atributo personalizado, `menu_item`, que tem um valor de atributo que excede 10.000 caracteres.]({% image_buster /assets/img/segment/segment_filter_error.png %})


Esse erro ocorre muito raramente, mas quando ocorre, geralmente é com filtros regex que visam uma lista de IDs de usuários ou endereços de e-mail. Nesse caso, você pode seguir estas etapas para converter os filtros em um CSV:

1. Exporte os usuários do segmento afetado ou do filtro regex específico. 
2. Limpe o CSV conforme necessário. Você precisa do Braze ID ou Appboy ID, mas pode remover todas as outras colunas se não forem necessárias. Também recomendamos revisar seus dados para confirmar que estão recentes (por exemplo, remover usuários que você não está mais tentando segmentar).
3. [Importar]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) o arquivo CSV novamente, o que agrupa automaticamente os usuários em um único filtro baseado em CSV altamente eficiente.

## Comportamento do usuário

### O usuário não está mais em um segmento

Se um usuário não estiver disponível durante a criação de um segmento, os dados de usuários que determinam a elegibilidade do segmento poderão ter sido alterados como resultado de sua própria atividade ou de outras campanhas e Canvases com os quais ele interagiu anteriormente. Se a reelegibilidade estiver ativada, o perfil do usuário mostrará os dados mais recentes da campanha recebida.

### As informações são exibidas para usuários de outros aplicativos quando eu filtro para um aplicativo específico

Os usuários podem ter vários aplicativos, portanto, a seleção de um aplicativo específico na seção **Aplicativos usados** da página de segmentação produzirá resultados para os usuários que têm pelo menos esse aplicativo. O filtro não produz resultados para os usuários que têm exclusivamente esse app.

## Filtragem

### Opções de filtro alteradas

Suas opções de filtro estão relacionadas ao formato (tipo de dados) que você está passando para o Braze para seu atributo personalizado. Para revisar o tipo de dados que a Braze está reconhecendo para seus atributos personalizados, navegue até **Configurações de dados** > **Atributos personalizados**.

Se as opções de filtro tiverem mudado, isso é uma indicação de que os dados estão sendo passados para o Braze em um formato (tipo de dados) diferente do anterior. Para obter descrições detalhadas de diferentes tipos de dados e suas opções de filtragem, consulte [tipos de dados de atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#custom-attribute-data-types).

Lembre-se de que a alteração do tipo de dados de um atributo personalizado no dashboard rejeitará os dados que forem enviados ao Braze em um formato diferente.

## Análise de dados e relatórios

### *A mensagem enviada* ou *os destinatários únicos* na análise de dados da campanha não correspondem à contagem do segmento 

Se a contagem da análise de *dados* da sua campanha de *Mensagens enviadas* ou *Destinatários únicos* não corresponder ao número de usuários no filtro de segmento `Has received message from campaign X`, pode haver dois motivos possíveis para isso:

1. **Os usuários podem ter sido arquivados, tornados órfãos ou excluídos desde o lançamento da campanha**<br><br>Por exemplo, digamos que 1.000 usuários recebam uma campanha e você faça uma exportação CSV no mesmo dia. Você verá 1.000 usuários relatados. No mês seguinte, 50 desses 1.000 usuários são excluídos (por exemplo, pelo endpoint `users/delete`). Quando fizer outra exportação CSV, verá 950 usuários relatados, enquanto a contagem de *Unique Recipient (destinatário único* ) no **Campaign Analytics** ainda é de 1.000.<br><br>Em outras palavras, a métrica *Unique Recipients* é uma contagem incrementada, enquanto o segmentador e a exportação CSV fornecem uma contagem de usuários existentes no momento.<br><br>

2. **A campanha tem a reelegibilidade definida, de modo que os usuários podem entrar novamente na campanha várias vezes**<br><br>Por exemplo, digamos que uma campanha de e-mail tenha a reelegibilidade definida como zero minutos (os usuários podem entrar novamente na campanha desde que atendam aos requisitos do segmento de público) e a campanha esteja em execução há mais de um mês. O número de *mensagens enviadas* no **Campaign Analytics** não corresponderia ao número no segmento porque esse campo incluiria mensagens enviadas a usuários duplicados.<br><br>Isso ocorre porque o Braze conta os usuários únicos como *Unique Daily Recipients*, ou o número de usuários que receberam uma determinada mensagem em um dia. Isso significa que os usuários reelegíveis serão contados mais de uma vez como um destinatário único, porque a janela "única" dura apenas um dia. Isso pode fazer com que o número de *destinatários diários exclusivos* seja maior do que o número de perfis de usuário na exportação CSV. Os perfis de usuário no arquivo CSV serão realmente exclusivos.

### O usuário está atribuído a dois apps, apesar de ter registrado uma sessão em apenas um app

Ao criar um segmento, você pode segmentar usuários que [usaram apps específicos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform). Um usuário precisa ter tido uma sessão em um aplicativo específico para ser atribuído a esse aplicativo; no entanto, existem dois cenários em que um usuário ainda pode ser atribuído a um aplicativo específico sem ter feito sessões no aplicativo. 

O primeiro cenário é se o campo `app_id` estiver preenchido ao usar o endpoint `/users/track`—especificamente ao usar um [evento]({{site.baseurl}}/api/objects_filters/event_object/) ou [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/), como neste exemplo:

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

O segundo cenário é se o campo `app_id` estiver preenchido ao usar o endpoint `/users/track` para migrar tickets de push, como neste exemplo: 

```json
{
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
}
```
