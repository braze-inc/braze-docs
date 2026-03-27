---
nav_title: Registro de usuários de eventos
article_title: Registro de usuários de eventos
page_order: 7
page_type: reference
description: "Este artigo de referência aborda o registro de usuários de eventos, que pode ajudar você a fazer debug ou solucionar problemas na sua integração com a Braze."

---

# Registro de usuários de eventos

> O registro de usuários de eventos pode ajudar você a analisar, fazer debug ou solucionar problemas na sua integração com a Braze. Essa guia fornece um registro de erros que detalha o tipo de erro, a qual app ele está associado, quando ocorreu e, muitas vezes, uma oportunidade de visualizar os dados brutos associados a ele.

{% alert tip %}
Além deste artigo, também recomendamos conferir nosso curso do Braze Learning sobre [Ferramentas de garantia de qualidade e debug](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que aborda como usar o registro de usuários de eventos para conduzir sua própria solução de problemas e debug.
{% endalert %}

Para acessar o registro, acesse **Configurações** > **Registro de usuários de eventos**.

Para encontrar seus registros facilmente, você pode filtrar com base em:

* SDK ou API
* Nomes de apps
* Período
* Usuário

Cada registro é dividido em várias seções, que podem incluir:

* Atributos do dispositivo
* Atributos do usuário
* Eventos
* Eventos da campanha
* Dados de resposta

Selecione o ícone **Expandir dados** para mostrar os dados JSON brutos desse registro específico.

![O ícone "Expandir dados" ao lado de um registro específico.]({% image_buster /assets/img_archive/expand_data.png %})

Os registros de usuários de eventos permanecerão no dashboard por 30 dias após terem sido registrados.

![Registros brutos para eventos]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Solução de problemas

### Registros do SDK ausentes para usuários teste

Se você adicionou um usuário a um grupo interno, mas ele não está mostrando nenhum registro do SDK no registro de usuários de eventos, isso pode ser resultado de uma opção de configuração ausente. Para capturar os registros do SDK, certifique-se de selecionar **Record User Events for group members** nas **Internal Group Settings** desse [grupo interno]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/).

### Postergação nas atualizações dos registros

Isso é potencialmente uma lentidão normal por parte da nossa API.

Quando você chama os métodos do SDK, geralmente o SDK armazena esses eventos em cache localmente e os envia para o servidor a cada 10 segundos. Pode levar de um segundo a alguns minutos para que nossa fila de processamento ingira os eventos, dependendo da carga geral no momento.  

Se você quer que os eventos cheguem o mais rápido possível, tente chamar a função `requestImmediateDataFlush()`.

### Falhas de impressão de mensagens no app

Se uma mensagem no app não for exibida, você pode encontrar o motivo no registro de usuários de eventos expandindo os dados JSON brutos da solicitação do SDK relevante e procurando o campo `error_code` na resposta. O `error_code` identifica o motivo específico pelo qual a impressão falhou (por exemplo, um valor de cor inválido ou um problema de renderização). Compartilhe esse código de erro com o [suporte da Braze]({{site.baseurl}}/braze_support/) se for necessária uma investigação mais aprofundada.

### O fim e o início da sessão têm timestamps semelhantes (iOS)

O registro de usuários de eventos mostra o timestamp de quando a Braze foi notificada de que a sessão terminou, que será milissegundos antes do início da próxima sessão. A Braze não consegue saber que a sessão terminou antes de o app ser reaberto porque o iOS é agressivo ao interromper a execução de threads quando o app está em segundo plano — portanto, nenhum dado pode ser enviado à Braze até que o app seja reaberto.

Embora o horário de término da sessão seja especificado como segundos antes do início da sessão, quando o evento é enviado, a duração da sessão é enviada separadamente e está correta — refletindo o tempo em que o app estava aberto. Portanto, esse comportamento não afeta o filtro `Median Session Duration`.

Em relação às sessões de usuários, é possível usar a Braze para monitorar dados como:

- Quantas sessões um usuário teve
- Quando um usuário iniciou uma sessão pela última vez
- Se o usuário inicia uma sessão após receber uma campanha
- Qual é a duração média da sessão do usuário

Esses comportamentos não são afetados pelo fato de o evento de encerramento da sessão ser enviado na próxima sessão.