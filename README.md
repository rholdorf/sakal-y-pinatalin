# sakal-y-pinatalin

Língua inventada em conversa por Claude e Grok. Este repositório traz a especificação fechada, o gerador de nomes próprios e a skill que faz o Grok produzir nomes, títulos e frases sem inventar raiz.

A skill mora em `.claude/skills/sakal-y-pinatalin/`. O Claude Code a encontra nesse caminho. O Grok também, porque lê skills de projeto em `.claude/skills/`. A especificação, em `sakal-y-pinatalin.md`, é a única fonte das formas. `conversa.md` registra como a língua foi fechada e não substitui a especificação.

## Requisitos

- [Grok](https://x.ai/grok), no terminal
- Python 3, só para `nome.py` (biblioteca padrão; nada para instalar)

## Instalar

A skill precisa continuar dentro deste repositório. Ela lê `sakal-y-pinatalin.md` e chama `nome.py` na raiz, a pasta que contém esses dois arquivos. Copiar só a pasta da skill para outro lugar quebra esses caminhos.

### Neste repositório

Clone e abra o Grok na raiz:

```bash
git clone https://github.com/rholdorf/sakal-y-pinatalin.git
cd sakal-y-pinatalin
grok
```

Na primeira abertura de uma pasta ainda não confiada, o Grok pede confiança antes de carregar skills do projeto. Aceite o pedido, ou rode `grok --trust` na raiz. Confira com:

```bash
grok inspect
```

A skill aparece com o nome `sakal-y-pinatalin` e a origem no projeto.

### Em outros projetos

Deixe o clone num caminho estável e acrescente a pasta de skills em `~/.grok/config.toml`:

```toml
[skills]
paths = ["<caminho-do-clone>/.claude/skills"]
```

Abra um Grok novo. `grok inspect` lista a skill com origem `config`.

## Usar

### Pela skill

No Grok, chame pelo nome:

```text
/sakal-y-pinatalin
um nome a partir da semente farol
```

O Grok também aciona a skill sozinho quando o pedido fala em sakal-y-pinatalin, "na língua", ou pede um nome, título, inscrição ou frase dela.

Cada resposta traz a forma, a leitura com a sílaba tônica em maiúsculas e uma glosa curta. Exemplo de forma pronta da especificação: `kilun-lanin`, ki-LUN la-NIN, torre + comunicação.

Pedidos que a skill cobre:

- Nome próprio. Dê uma semente, ou duas para um nome cindido. Sem semente, a skill escolhe uma palavra que glose o sentido e declara qual foi.
- Título. Um composto nu, como "porta da cidade" ou "torre de comunicação".
- Frase. A moldura inteira, com alvo e modo. Se você não disser os dois, a skill escolhe e declara a escolha.

### Pelo script

`nome.py` segue a seção 5 da especificação e não precisa do Grok. Rode na raiz do repositório:

```bash
python3 nome.py farol
python3 nome.py lua sol
```

A primeira imprime `parul`. A segunda imprime `sul-y-lutan`: dois nomes soldados com `y`, o de menos sílabas primeiro.

## O que a língua marca

Toda frase diz a quem se fala e quanto quem fala assina o que diz. Não marca tempo, gênero nem plural. Há 81 raízes. Conceito novo é composto dessas raízes, pelo procedimento da seção 3. Nome próprio é a única invenção livre, e sai da semente pelo algoritmo da seção 5.

Três produtos, na seção 6:

| pedido | o que sai |
| --- | --- |
| nome | a forma nua, sem alvo e sem modo |
| título | um composto nu |
| frase | alvo, o resto da moldura e modo |

O léxico, os compostos já decididos e os exemplos de frase estão em `sakal-y-pinatalin.md`.
