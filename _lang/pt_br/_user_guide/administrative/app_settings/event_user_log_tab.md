---
nav_title: Registro de usuário de eventos
article_title: Registro de usuário de eventos
page_order: 7
page_type: reference
description: "Este artigo de referência aborda o Log do usuário de eventos, que pode ajudá-lo a depurar ou solucionar problemas em sua integração do Braze."

---

# Registro de usuário de eventos

> O registro de usuário de eventos pode ajudá-lo a analisar, depurar ou solucionar problemas em sua integração Braze. Essa guia fornece um registro de erros que detalha o tipo de erro, a qual aplicativo ele está associado, quando ocorreu e, muitas vezes, uma oportunidade de visualizar os dados brutos associados a ele.

{% alert tip %}
Além deste artigo, também recomendamos que você confira nosso curso [Ferramentas de garantia de qualidade e depuração](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) do Braze Learning, que aborda como usar o log de usuário de eventos para conduzir sua própria solução de problemas e depuração.
{% endalert %}

Para acessar o registro, vá para **Settings** > **Event User Log**.

Para encontrar seus registros facilmente, você pode filtrar com base em:

* SDK ou API
* Nomes de aplicativos
* Prazo
* Usuário

Cada registro é dividido em várias seções, que podem incluir:

* Atributos do dispositivo
* Atributos do usuário
* Eventos
* Eventos da campanha
* Dados de resposta

Selecione o ícone **Expandir dados** para mostrar os dados JSON brutos desse registro específico.

\![O ícone "Expandir dados" ao lado de um registro específico.]({% image_buster /assets/img_archive/expand_data.png %})

Os registros de usuário de eventos permanecerão no painel por 30 dias após terem sido registrados.

\![Registros brutos de eventos]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Solução de problemas

### Registros de SDK ausentes para usuários de teste

Se você adicionou um usuário a um grupo interno, mas ele não está mostrando nenhum registro do SDK no Event User Log, isso pode ser resultado de uma opção de configuração ausente. Para capturar os logs do SDK, certifique-se de selecionar **Record User Events (Registrar eventos do usuário) para os membros do grupo** nas **Internal Group Settings (Configurações do grupo interno)** para esse [grupo interno]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/).

### Atraso nas atualizações de registros

Isso é potencialmente uma lentidão normal por parte da nossa API.

Quando você chama os métodos do SDK, geralmente o SDK armazena em cache esses eventos localmente e os envia para o servidor a cada 10 segundos. Pode levar de um segundo a alguns minutos para que nossa fila de processamento de trabalho ingira eventos, dependendo da carga geral no momento.  

Se estiver procurando que os eventos cheguem o mais rápido possível, tente chamar a função `requestImmediateDataFlush()`.

### O fim e o início da sessão têm registros de data e hora semelhantes (iOS)

O registro de eventos do usuário mostra o registro de data e hora em que o Braze foi notificado do término da sessão, que será milissegundos antes do início da próxima sessão. O Braze não consegue saber que a sessão terminou antes de o aplicativo ser reaberto porque o iOS é agressivo ao interromper a execução de threads quando o aplicativo está em segundo plano - portanto, nenhum dado pode ser enviado ao Braze até que o aplicativo seja reaberto.

Embora o horário de término da sessão seja especificado como segundos antes do início da sessão, quando o evento é liberado, a duração da sessão é liberada separadamente e está correta, refletindo o horário em que o aplicativo estava aberto. Portanto, esse comportamento não afeta o filtro `Median Session Duration`.

Em relação às sessões de usuário, você pode usar o Braze para monitorar dados como:

- Quantas sessões um usuário teve
- Quando um usuário iniciou uma sessão pela última vez
- Se o usuário iniciar uma sessão após receber uma campanha
- Qual é a duração média da sessão do usuário

Esses comportamentos não são afetados pelo fato de o evento de fim de sessão ser liberado na próxima sessão.

