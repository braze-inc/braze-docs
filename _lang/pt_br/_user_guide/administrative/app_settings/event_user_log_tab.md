---
nav_title: Registro de usuários de eventos
article_title: Registro de usuários de eventos
page_order: 7
page_type: reference
description: "Este artigo de referência aborda o registro de usuários de eventos, que pode ajudá-lo a depurar ou solucionar problemas em sua integração Braze."

---

# Registro de usuários de eventos

> O registro de usuários de eventos pode ajudar a analisar, depurar ou solucionar problemas em sua integração da Braze. Essa guia fornece um registro de erros que detalha o tipo de erro, a qual app ele está associado, quando ocorreu e, muitas vezes, uma oportunidade de visualizar os dados brutos associados a ele.

{% alert tip %}
Além deste artigo, também recomendamos conferir nosso curso do Braze Learning sobre [Ferramentas de garantia de qualidade e depuração](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que aborda como usar o registro de usuários de eventos para conduzir sua própria solução de problemas e depuração.
{% endalert %}

Para acessar o registro, acesse **Configurações** > **Registro de usuários de eventos**.

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
* Dados de respostas

Selecione o ícone **Expandir dados** para mostrar os dados JSON brutos desse registro específico.

![O ícone "Expandir dados" ao lado de um registro específico.]({% image_buster /assets/img_archive/expand_data.png %})

Os registros de usuários de eventos permanecerão no dashboard por 30 dias após terem sido registrados.

![Registros brutos de eventos]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Solução de problemas

### Registros do SDK ausentes para usuários teste

Se você adicionou um usuário a um grupo interno, mas ele não está mostrando nenhum registro do SDK no Registro de usuários de eventos, isso pode ser resultado de uma opção de configuração ausente. Para capturar os registros **do** SDK, certifique-se de selecionar **Record User Events (Registrar eventos do usuário) para os membros do grupo** nas **Internal Group Settings (Configurações do grupo interno)** para esse [grupo interno]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/).

### Postergação nas atualizações dos registros

Isso é potencialmente uma lentidão normal por parte de nossa API.

Quando você chama os métodos do SDK, geralmente o SDK armazena esses eventos em cache localmente e os envia para o servidor a cada 10 segundos. Pode levar de um segundo a alguns minutos para que nossa fila de processamento de trabalhos ingira eventos, dependendo da carga geral no momento.  

Se estiver procurando que os eventos cheguem o mais rápido possível, tente chamar a função `requestImmediateDataFlush()`.

### O fim e o início da sessão têm registros de data e hora semelhantes (iOS)

O registro de usuários de eventos mostra o carimbo de data/hora de quando o Braze foi notificado de que a sessão terminou, que será milissegundos antes do início da próxima sessão. O Braze não consegue saber que a sessão terminou antes de o aplicativo ser reaberto porque o iOS é agressivo ao interromper a execução de threads quando o aplicativo está em segundo plano - portanto, nenhum dado pode ser enviado ao Braze até que o aplicativo seja reaberto.

Embora o horário de término da sessão seja especificado como segundos antes do início da sessão, quando o evento é liberado, a duração da sessão é liberada separadamente e está correta, refletindo o horário em que o app estava aberto. Portanto, esse comportamento não afeta o filtro `Median Session Duration`.

Em relação às sessões de usuários, é possível usar a Braze para monitorar dados como:

- Quantas sessões um usuário teve
- Quando um usuário iniciou uma sessão pela última vez
- Se o usuário iniciar uma sessão após receber uma campanha
- Qual é a duração média da sessão do usuário

Esses comportamentos não são afetados pelo fato de o evento de ponta a ponta da sessão ser liberado na próxima sessão.

