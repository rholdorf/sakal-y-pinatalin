# sakal-y-pinatalin

Língua inventada em conversa por Claude e Grok. Este repositório traz a especificação fechada, o gerador de nomes próprios e a skill que produz nomes, títulos e frases sem inventar raiz.

A skill mora em `.claude/skills/sakal-y-pinatalin/`. É uma [Agent Skill](https://agentskills.io): um diretório com `SKILL.md`, o nome e a descrição no frontmatter, e o procedimento em Markdown. O Claude Code lê `.claude/skills/` no projeto. O Grok também. Serve outro CLI de outra LLM se ele fizer o mesmo com este arquivo: reconhecer a skill pela descrição, seguir as instruções e deixar o modelo ler `sakal-y-pinatalin.md` e rodar `python3`. A pasta que cada um vasculha pode ser outra (`.agents/skills/`, `.cursor/skills/` e semelhantes). O arquivo da skill é o mesmo.

A especificação, em `sakal-y-pinatalin.md`, é a única fonte das formas. `conversa.md` registra como a língua foi fechada e não substitui a especificação.

## Requisitos

- Claude Code, Grok, ou outro CLI que carregue uma Agent Skill
- Python 3, para `nome.py` (biblioteca padrão; nada para instalar). Sem shell, a skill manda seguir os seis passos da seção 5 à mão

## Instalar

A skill precisa continuar dentro deste repositório. Ela lê `sakal-y-pinatalin.md` e chama `nome.py` na raiz, a pasta que contém esses dois arquivos. Copiar só a pasta da skill para outro lugar quebra esses caminhos.

```bash
git clone https://github.com/rholdorf/sakal-y-pinatalin.git
cd sakal-y-pinatalin
```

### Claude Code

Abra o Claude Code na raiz. A skill entra como `/sakal-y-pinatalin`.

### Grok

```bash
grok
```

Na primeira abertura de uma pasta ainda não confiada, o Grok pede confiança antes de carregar skills do projeto. Aceite o pedido, ou rode `grok --trust` na raiz. Confira com `grok inspect`: a skill aparece com o nome `sakal-y-pinatalin` e a origem no projeto.

### Outro CLI

Se ele procura skills em `.claude/skills/` do projeto, abrir a raiz basta. Se procura em outro diretório, aponte a busca para `.claude/skills/sakal-y-pinatalin` dentro deste clone. Um symlink para essa pasta preserva a spec e o `nome.py` ao lado da skill, desde que o CLI siga o caminho real. Separar o `SKILL.md` dos dois arquivos da raiz faz o modelo perder a fonte.

### Em outros projetos, com o Grok

Deixe o clone num caminho estável e acrescente a pasta de skills em `~/.grok/config.toml`:

```toml
[skills]
paths = ["<caminho-do-clone>/.claude/skills"]
```

Abra um Grok novo. `grok inspect` lista a skill com origem `config`.

## Usar

### Pela skill

No Claude Code ou no Grok, chame pelo nome:

```text
/sakal-y-pinatalin
um nome a partir da semente farol
```

O CLI também aciona a skill sozinho quando o pedido fala em sakal-y-pinatalin, "na língua", ou pede um nome, título, inscrição ou frase dela. Outro CLI faz o mesmo se decidir a skill pela descrição.

Cada resposta traz a forma, a leitura com a sílaba tônica em maiúsculas e uma glosa curta. Exemplo de forma pronta da especificação: `kilun-lanin`, ki-LUN la-NIN, torre + comunicação.

Pedidos que a skill cobre:

- Nome próprio. Dê uma semente, ou duas para um nome cindido. Sem semente, a skill escolhe uma palavra que glose o sentido e declara qual foi.
- Título. Um composto nu, como "porta da cidade" ou "torre de comunicação".
- Frase. A moldura inteira, com alvo e modo. Se você não disser os dois, a skill escolhe e declara a escolha.

### Pelo script

`nome.py` segue a seção 5 da especificação e não precisa de um agente. Rode na raiz do repositório:

```bash
python3 nome.py farol
python3 nome.py lua sol
```

A primeira imprime `parul`. A segunda imprime `sul-y-lutan`: dois nomes soldados com `y`, o de menos sílabas primeiro.

### Numerologia

`numerologia.md` acrescenta uma camada opcional: cada forma tem um número pela numerologia pitagórica, com redução a 1–9 e os mestres 11, 22 e 33 preservados. O pedido pode mirar um desses significados. A gramática vence o número: o alvo só escolhe entre o que o pedido deixou em aberto (a semente do nome, o alvo calado da frase, a fonte de um endosso sem fonte), numa ordem fixa, e nunca inventa compromisso. Quando não há acerto possível, a resposta avisa.

```bash
python3 numero.py sakal-y-pinatalin
python3 numero.py --alvo 7 --sementes farol
python3 numero.py --alvo 9 --miolo "ku nil ti mil" --modos ka,la,na --alvos pu
```

A primeira detalha cada domínio e dá os três eixos: expressão 57 → 12 → 3, alma 11, personalidade 1. A segunda afina a semente até `farol3`, que dá `parulas`. A terceira fixa o alvo `pu`, endossa sem fonte e deixa o número escolher a fonte: `pu ku nil ti mil la`. Esta camada foi revisada com o Grok; o registro está no fim de `conversa.md`.

Na skill, basta pedir: "um nome a partir de farol, com número 7".

## O que a língua marca

Toda frase diz a quem se fala e quanto quem fala assina o que diz. Não marca tempo, gênero nem plural. Há 81 raízes. Conceito novo é composto dessas raízes, pelo procedimento da seção 3. Nome próprio é a única invenção livre, e sai da semente pelo algoritmo da seção 5.

Três produtos, na seção 6:

| pedido | o que sai |
| --- | --- |
| nome | a forma nua, sem alvo e sem modo |
| título | um composto nu |
| frase | alvo, o resto da moldura e modo |

O léxico, os compostos já decididos e os exemplos de frase estão em `sakal-y-pinatalin.md`.
