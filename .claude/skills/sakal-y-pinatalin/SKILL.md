---
name: sakal-y-pinatalin
description: Cria nomes, títulos, inscrições e frases em sakal-y-pinatalin, a língua inventada por Claude e Grok. Use quando o usuário pedir um nome, título, frase ou tradução "na língua", em sakal-y-pinatalin, ou citar palavras dela (kilun-lanin, pu … ka). Também calcula o número pitagórico de uma forma e traduz mirando um significado da numerologia (1–9, 11, 22, 33).
---

# sakal-y-pinatalin

A especificação é a única fonte: `sakal-y-pinatalin.md`, na raiz do repositório desta skill. A raiz é o diretório que contém `sakal-y-pinatalin.md` e `nome.py`. Leia-a inteira antes de produzir qualquer forma. Não invente raiz, partícula ou regra fora dela. O léxico é fechado, e outro falante (Claude ou Grok) precisa chegar à mesma forma que você.

## Procedimento

1. **Classificar o pedido** (seção 6): nome próprio, título (composto nu) ou frase (alvo … modo).
2. **Nome próprio.** Na mesma raiz, rode `python3 nome.py <semente>`, ou `python3 nome.py <semente1> <semente2>` para um nome cindido. Se o usuário não der semente, escolha uma palavra que glose o sentido desejado e diga qual foi. Sem acesso a shell, siga os seis passos da seção 5 à mão.
3. **Título ou conceito.** Siga o procedimento da seção 3 ao pé da letra: primeiro a tabela canônica, depois a divisão das palavras, uma raiz por vaga, anti-repetição e desempate. Não reclassifique vagas por juízo próprio.
4. **Frase.** Preencha a moldura da seção 2 na ordem: ALVO SUJEITO [OBJETO] [OBLÍQUOS] [TEMPO] [ti] VERBO [DONO] MODO. Se o usuário não disser alvo ou modo, escolha e declare a escolha. Ninguém = `hu`; afirmação sem fonte dita = `i`.
5. **Sentido-alvo** (só se o pedido trouxer um número, um significado da numerologia ou um eixo). Leia `numerologia.md`, na mesma raiz, e siga a seção 5 dela. A gramática vence o número: o alvo só escolhe entre o que o pedido deixou em aberto, na ordem fixa, e nunca inventa compromisso nem fonte.
   - Nome: `python3 numero.py --alvo N --sementes <semente>`, ou duas sementes para um cindido.
   - Frase: `python3 numero.py --alvo N --miolo "<sujeito … verbo>" --modos <modo>`. O modo é o que você fecharia sem número. Use `--modos ka,la,na` só se o pedido endossa sem dizer a fonte. Se o usuário disse o alvo, passe `--alvos <alvo>`. Calado, deixe a ferramenta escolher.
   - Pergunta: `python3 numero.py --alvo N --miolo "<sujeito … verbo>" --pergunta`, com `--alvos` se o alvo foi dito.
   - Título ou forma pronta: `python3 numero.py --alvo N <forma>`, uma forma só. O número nunca escolhe entre compostos.
   - Eixo diferente do padrão: `--eixo alma` ou `--eixo personalidade`.
   Sem acerto, entregue a forma que a ferramenta mostra, o número que ela dá e a frase "o alvo N não é alcançável aqui". Sem shell, faça a conta à mão pelas seções 1 e 3 de `numerologia.md`.
6. **Conferir** antes de responder:
   - toda palavra de conteúdo fecha em `k n l s`, com a exceção de um possuidor `ku`/`lu`/`nu`;
   - `r` só entre vogais;
   - o dono aparece se e só se o modo é `u`, `sa` ou `ma`;
   - a pergunta fecha com o alvo repetido e não leva fonte nem dono;
   - no cindido, a parte com menos sílabas vem primeiro.

## Formato da resposta

Para cada item, dê a forma, a leitura com a sílaba tônica em maiúsculas e uma glosa curta palavra a palavra. Se a especificação obrigou a adivinhar, diga onde. Quem quiser pode depois levar o ponto à próxima revisão da língua.

Com sentido-alvo, acrescente o número com a cadeia de redução, o significado e a alavanca que decidiu (semente, alvo ou modo).

Exemplo:

`kilun-lanin`, ki-LUN la-NIN: torre + comunicação.

Com alvo 3:

`kitil-lanin`, ki-TIL la-NIN: sinal escrito + fala (escrita, canônico). Expressão 48 → 12 → 3: comunicação, criatividade, alegria. Acertou sem alavanca.
