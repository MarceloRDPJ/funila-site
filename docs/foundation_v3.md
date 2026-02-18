# Funila — Documentação Fundacional v3.0

**Marcelo Rodrigues | RDP Studio | 2026**
**funila.com.br | rdpstudio.com.br**

---

## 1. O Problema que Resolvo
O Funila afunila o caos do tráfego pago em leads qualificados. Este documento é meu mapa de construção e apresentação do produto.

### 1.1 O Ciclo do Desperdício
Toda empresa que investe em tráfego pago vive a mesma frustração. O dinheiro sai, os leads entram, mas ninguém sabe o que acontece no meio. O processo padrão hoje é assim:

1.  A empresa investe em Meta Ads ou Google Ads.
2.  O cliente clica e é mandado direto para o WhatsApp ou site.
3.  O vendedor recebe: nome + telefone. Sem contexto nenhum.
4.  Começa a investigação manual do zero a cada lead.
5.  Tempo desperdiçado. Lead frio tratado igual ao quente.

**O resultado prático:**
*   Não sei qual campanha gerou o cliente que fechou — só vejo o que gastei
*   Não sei onde o lead desistiu — se foi no anúncio, na página ou na conversa
*   Base desorganizada, remarketing genérico, ROI invisível
*   O vendedor faz o trabalho de SDR manualmente toda vez

### 1.2 O Gargalo Real — O WhatsApp como Buraco Negro
A maioria dos corretores e empresas usam o WhatsApp como destino dos anúncios. O problema é que quando o lead chega no WhatsApp, os dados se perdem. Não há como saber:
*   De qual campanha ou anúncio esse contato veio
*   Quantas pessoas clicaram mas não mandaram mensagem
*   Qual o perfil financeiro do lead antes de ele abrir a boca
*   Se esse lead tem potencial real de fechamento

O Funila resolve esse buraco negro colocando uma camada de inteligência ANTES do lead chegar no WhatsApp — e entregando ao vendedor um contato já qualificado, com contexto completo.

### 1.3 Os Três Mercados com Essa Dor

| Mercado | Dor específica | O que o Funila entrega |
| :--- | :--- | :--- |
| **Corretor de Imóveis** | Investe em tráfego mas não sabe qual campanha gera lead que financia. Perde tempo com lead frio no WhatsApp. | Lead chega no WhatsApp já com nome, CLT, renda e Score Serasa. Vendedor só fecha. |
| **Empresa Comercial / Agência** | Clientes da agência não conseguem provar ROI. Leads entram sem inteligência. | Dashboard de ROI + funil com abandono + CPL real por campanha. |
| **Igreja / Pastoral** | Dados de membros ficam perdidos. Ninguém sabe quem some. | Centralização pastoral + alerta de desistentes + histórico individual. |

---

## 2. A Solução Completa — As 4 Camadas do Funila
O Funila não é um formulário. É um funil de inteligência com quatro camadas que trabalham juntas para rastrear, qualificar e afunilar cada lead antes de chegar no vendedor.

### 2.1 Visão do Funil Completo

```
[ ANÚNCIO META / GOOGLE ADS ]
         ↓  cliente coloca link do Funila no anúncio
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CAMADA 1 — LINK TRACKER
  funila.com.br/t/abc123
  → registra: clique, dispositivo, horário, localização, UTM
         ↓  redirect instantâneo (< 300ms)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CAMADA 2 — SQUEEZE PAGE (Landing Page de Qualificação)
  Etapa 1: Nome + Telefone
  Etapa 2: Tem CLT? Há quanto tempo?
  Etapa 3: Renda + já tentou financiar?
  (CPF opcional — libera consulta Serasa no plano Pro)
         ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CAMADA 3 — QUALIFICAÇÃO AUTOMÁTICA
  → Score interno calculado (CLT + renda + histórico)
  → Consulta Serasa Score via API (plano Pro)
  → Status: 🔥 Quente | 🟡 Morno | ❄️ Frio
         ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CAMADA 4 — ENTREGA INTELIGENTE NO WHATSAPP
  Botão abre wa.me com mensagem pré-preenchida:
  'Olá João! Sou Ana, CLT há 4 anos, renda R$4.200,
   Serasa 720. Vi seu anúncio do apto no Setor Oeste.'
         ↓
[ VENDEDOR RECEBE LEAD QUALIFICADO — SÓ FECHA ]
```

### 2.2 Camada 1 — Link Tracker (Rastreamento de Clique)
O corretor usa hoje um link qualquer no anúncio — site, WhatsApp, Linktree, o que for. O Funila não muda esse destino. Só adiciona uma camada antes.

**Como funciona na prática:**
1.  No painel do Funila, o cliente cria um link de rastreamento e informa o destino (a Squeeze Page do Funila ou qualquer URL).
2.  O sistema gera: `funila.com.br/t/xk7p2`
3.  O cliente troca o link do anúncio por esse. Só isso.
4.  Cada clique registra: timestamp, dispositivo (mobile/desktop), sistema operacional, cidade estimada via IP, UTM da campanha.

O cliente não precisa saber o que é UTM nem pixel. Ele só troca o link. O Funila rastreia tudo silenciosamente.

**O que o painel mostra com os dados do tracker:**
*   Total de cliques por campanha e por período
*   Taxa de clique → formulário (quantos clicaram e quantos foram além)
*   Distribuição por dispositivo — mobile vs desktop
*   Horários de pico de clique — quando o público está ativo

### 2.3 Camada 2 — Squeeze Page (A Landing Page de Qualificação)
A Squeeze Page é a landing page intermediária entre o clique e o WhatsApp. É aqui que o Funila faz o trabalho de SDR de forma automatizada.

**Por que isso funciona:**
Quando o lead precisa preencher 3 etapas simples antes de falar com o corretor, dois efeitos acontecem: (1) leads sem interesse real desistem — filtragem natural; (2) os que continuam chegam no WhatsApp já motivados e com contexto. A taxa de conversão no WhatsApp sobe porque o vendedor não perde tempo qualificando.

**Técnica usada: Progressive Profiling (Coleta Progressiva)**
Cada etapa pede só o necessário. Nunca mostro todos os campos de uma vez — isso derruba a conversão. A lógica é: quanto mais o lead investe tempo, mais ele se compromete psicologicamente.

| Etapa | Campos | Barreira | Objetivo |
| :--- | :--- | :--- | :--- |
| **1 — Entrada** | Nome + Telefone | Mínima — todo mundo preenche | Capturar contato. Já salvo no banco mesmo se abandonar aqui. |
| **2 — Qualificação Profissional** | CLT? Há quanto tempo? | Baixa — 2 cliques | Dado mais valioso para corretor. Define 45pts do score. |
| **3 — Qualificação Financeira** | Renda estimada + já tentou financiar? | Média — 2 seleções | Completa o perfil de crédito. Libera Score Serasa se CPF fornecido. |

### 2.4 Camada 3 — Qualificação Automática e Score Serasa

**Score Interno (gratuito — todos os planos)**
| Critério | Pontos | Lógica |
| :--- | :--- | :--- |
| CLT há 3+ anos | +30 | Maior chance de aprovação FGTS/CAIXA |
| Renda acima de R$ 3.000 | +25 | Compatível com Minha Casa Minha Vida |
| Nunca tentou financiar | +20 | Perfil limpo, sem restrição prévia |
| Emprego 2+ anos | +15 | Estabilidade comprovada |
| Telefone informado | +10 | Canal ativo |

**Score Serasa via API (plano Profissional e Agência)**
O Serasa Score é a pontuação oficial de crédito do Brasil — vai de 0 a 1.000. Com o CPF do lead, o Funila consulta a API da Serasa (via SOAWebServices ou Serasa Developer) e adiciona esse dado ao perfil.

| Score Serasa | Interpretação | Ação sugerida |
| :--- | :--- | :--- |
| **700 – 1.000** | Excelente — aprovação quase certa | Contato imediato. Alta prioridade. |
| **500 – 699** | Bom — aprovação provável | Contato em até 2 horas. |
| **300 – 499** | Regular — risco moderado | Qualificar mais antes de avançar. |
| **0 – 299** | Baixo — alto risco de reprovação | Base de remarketing. Não priorizar. |

**Custo da consulta Serasa:**
*   Via SOAWebServices (intermediário): ~R$ 0,40 a R$ 0,80 por consulta
*   Via Serasa Developer Portal (direto): preço por volume, exige contrato
*   Estratégia: cobrar CPF apenas na etapa 3, consultar só para leads que completaram o formulário. Reduz custo e aumenta relevância.

### 2.5 Camada 4 — Entrega Inteligente no WhatsApp
Depois de calcular o score, a tela de confirmação do formulário mostra um botão de WhatsApp. Mas não é um botão genérico — a mensagem já vem pré-preenchida com os dados do lead.

**Exemplo de mensagem gerada automaticamente:**
> Olá! Me chamo João Silva. Vi seu anúncio sobre o apartamento no Setor Oeste. Tenho CLT há 5 anos, renda de aproximadamente R$ 4.500 e nunca fiz financiamento. Gostaria de mais informações.

O corretor recebe isso no WhatsApp. Ele já sabe o nome, o perfil financeiro e o interesse. Começa a conversa no ponto certo, sem perguntar o que já está respondido.

Isso é exatamente o que um SDR faz manualmente. O Funila faz o mesmo — sem salário, sem domingo de folga, sem reclamação.

---

## 3. Arquitetura do Sistema
### 3.1 Visão Geral — Stack Técnica

| Camada | Tecnologia | Onde roda | Função |
| :--- | :--- | :--- | :--- |
| **Link Tracker** | Python FastAPI — rota GET /t/{slug} | Render Starter | Registra clique e redireciona < 300ms |
| **Squeeze Page** | HTML + JS puro (PWA) | GitHub Pages | Formulário progressivo, lê UTM, envia para API |
| **Painel Admin** | HTML + JS + Chart.js | GitHub Pages | Dashboard do cliente: leads, métricas, exportação |
| **API Backend** | Python + FastAPI | Render Starter (~R$42/mês) | Score, Serasa, CRUD de dados, métricas |
| **Banco de Dados** | PostgreSQL | Supabase (grátis até 500MB) | Leads, cliques, campanhas, eventos |
| **Autenticação** | JWT via Supabase Auth | Supabase | Login do cliente, isolamento por tenant |
| **Serasa Score** | SOAWebServices API | Externo (pago por consulta) | Score de crédito via CPF — plano Pro |

### 3.2 Novas Tabelas do Banco — Versão Completa

**links — Tabela de rastreamento de cliques**
*   `id` UUID PK
*   `client_id` UUID FK
*   `slug` TEXT UNIQUE
*   `name` TEXT
*   `destination` TEXT
*   `utm_source` TEXT
*   `utm_campaign` TEXT
*   `created_at` TIMESTAMP

**clicks — Registro de cada clique**
*   `id` UUID PK
*   `link_id` UUID FK
*   `ip_hash` TEXT (LGPD)
*   `device_type` TEXT
*   `os` TEXT
*   `referrer` TEXT
*   `created_at` TIMESTAMP

**leads — Enriquecida com Serasa**
*   `id` UUID PK
*   `link_id` UUID FK
*   `name` TEXT
*   `phone` TEXT
*   `cpf` TEXT ENCRYPTED (LGPD)
*   `has_clt` BOOLEAN
*   `clt_years` INTEGER
*   `income` DECIMAL
*   `tried_financing` BOOLEAN
*   `internal_score` INTEGER
*   `serasa_score` INTEGER
*   `status` TEXT (hot / warm / cold / converted)
*   `created_at` TIMESTAMP

### 3.3 Rota do Link Tracker — Código

```python
@app.get('/t/{slug}')
async def track_and_redirect(slug: str, request: Request):
    link = await db.get_link(slug)
    if not link:
        raise HTTPException(404)
    # Registra o clique anonimizado
    await db.save_click({
        'link_id': link['id'],
        'ip_hash': hashlib.sha256(request.client.host.encode()).hexdigest(),
        'device_type': parse_device(request.headers.get('user-agent')),
        'referrer': request.headers.get('referer', ''),
    })
    # Redirect instantâneo para destino
    return RedirectResponse(url=link['destination'], status_code=302)
```

---

## 4. Funis Completos por Vertical
### 4.1 Funil Corretor de Imóveis — Fluxo Completo

```
[ ANÚNCIO INSTAGRAM / GOOGLE ]
  ↓  link: funila.com.br/t/joao-setor-oeste
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CLIQUE REGISTRADO
  dispositivo | horário | UTM
  ↓  redirect para Squeeze Page
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ETAPA 1: Nome + Telefone
  ↓
  ETAPA 2: CLT? Há quanto tempo?
  ↓
  ETAPA 3: Renda + tentou financiar? + CPF (opcional)
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SCORE CALCULADO
  Interno (0-100) + Serasa (0-1000) se CPF fornecido
  → 🔥 Quente: alerta no WhatsApp do corretor
  → 🟡 Morno: entra em fila de nutrição
  → ❄️ Frio: base de remarketing
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  BOTÃO WHATSAPP COM MENSAGEM PRÉ-PREENCHIDA
  Lead clica → abre zap com contexto completo
  ↓
[ CORRETOR RECEBE LEAD QUALIFICADO — SÓ FECHA ]
```

### 4.2 Funil Igreja / Pastoral
*   **Entrada:** QR Code no culto ou link no slide.
*   **Etapas:** Nome/Contato -> Membro/Ministério -> Interesse/Pedido de Oração.
*   **Painel:** Quem entrou este mês, quem sumiu (30+ dias), alertas de desistência.

### 4.3 Funil Agência / Empresa Comercial
*   **Entrada:** Tráfego pago do cliente da agência (Funila Link Tracker).
*   **Painel:** Multi-cliente, performance por cliente, CPL real, relatórios exportáveis com logo do cliente.

---

## 5. Infraestrutura e Custos Reais
*   **Render Starter:** US$7/mês (~R$42) para backend Python/FastAPI (sem sleep).
*   **Supabase:** Grátis até 500MB (PostgreSQL + Auth).
*   **GitHub Pages:** Grátis (Frontend Squeeze Page + Admin).
*   **Serasa API:** ~R$0,50/consulta (pago por uso).
*   **BrasilAPI:** Grátis (validação CPF/CEP).
*   **Resend:** Grátis até 3k emails/mês.

**Custo fixo infra:** ~R$ 46/mês.
**Margem:** Com 1 cliente no plano Starter (R$147/mês), a infraestrutura já está paga.

---

## 6. Precificação e Visão de Mercado
### 6.1 Concorrência
*   **Agendor:** R$65/usuário (sem tracker, sem score).
*   **Ploomes:** R$225/mês (sem tracker, sem Serasa).
*   **Pipedrive:** US$14/usuário (em dólar, sem adaptação BR).
*   **Facilita CRM:** R$149 + setup (focado em imobiliárias grandes).
*   **RD Station CRM:** R$50-3000 (complexo, sem Serasa).

**Gap do Funila:** Rastreamento desde o anúncio + Squeeze Page + Score Serasa + Entrega no WhatsApp. Acessível para corretor solo.

### 6.2 Planos do Funila

| Plano | Público | Setup | Mensal | Serasa |
| :--- | :--- | :--- | :--- | :--- |
| **Solo** | Corretor individual | R$ 500 | R$ 147 | Não incluso |
| **Profissional** | Pequena empresa | R$ 800 | R$ 247 | 100 consultas/mês |
| **Agência** | Multi-cliente | R$ 1.500 | R$ 497 | 500 consultas/mês |

---

## 7. Mapa do Sistema — Telas e Funcionalidades
### 7.1 Interfaces
*   **Link Tracker:** `funila.com.br/t/[slug]` (Invisível, redirect).
*   **Squeeze Page:** `app.funila.com.br/form/[slug]` (Lead preenche).
*   **Painel Admin:** `app.funila.com.br/admin` (Cliente gerencia).

### 7.2 Squeeze Page — Tela a Tela
1.  **Entrada:** Nome + Telefone (Obrigatório).
2.  **Qualificação Profissional:** CLT? Tempo de casa?
3.  **Qualificação Financeira:** Renda? Tentou financiar? CPF (Opcional).
4.  **Confirmação:** Botão WhatsApp com mensagem pré-preenchida.

### 7.3 Painel Admin — Tela a Tela
*   **Dashboard:** Métricas (cliques, leads, quentes), gráficos.
*   **Leads:** Tabela com status, score, origem. Exportar CSV.
*   **Links:** Gerenciador de links de rastreamento (criar, copiar).
*   **Detalhe do Lead:** Linha do tempo, dados completos.

### 7.4 Fluxo de Teste (Validação)
1.  Criar link no admin.
2.  Clicar no link (celular).
3.  Preencher formulário (dados teste).
4.  Clicar no WhatsApp (verificar mensagem).
5.  Painel Admin: verificar lead, score, origem.

---

## 8. LGPD — Conformidade Obrigatória
### 8.1 O que fazer
*   CPF criptografado no banco (AES-256).
*   Consentimento explícito (checkbox).
*   Política de Privacidade clara.
*   Botão de exclusão de lead.
*   IP armazenado como hash (SHA-256).

### 8.2 O que NÃO fazer
*   Vender/compartilhar dados.
*   Consultar Serasa sem CPF fornecido.
*   Armazenar Score Serasa desnecessariamente.

---

## 9. Roteiro de Desenvolvimento
**Dia 1 — Setup:** GitHub, Supabase, Render, estrutura de pastas.
**Dia 2 — Backend:** Link Tracker + API Base (FastAPI).
**Dia 3 — Squeeze Page:** Frontend HTML/JS, formulário progressivo.
**Dia 4 — Painel Admin:** Dashboard, tabela de leads, auth.
**Dia 5 — Deploy:** Render, GitHub Pages, testes finais.

---

## 10. Ecossistema RDP Studio
**Produtos:**
1.  **Funila (SaaS):** R$147-497/mês.
2.  **Landing Page (Projeto):** R$800-2.500 (pontual).
3.  **Site Institucional (Projeto):** R$1.500-5.000 (pontual).

**Estratégia:** Agência parceira vende consultoria -> detecta falta de CRM/Site -> repassa para RDP Studio.

---

## 11. LGPD — Conformidade Obrigatória (Detalhes)
*   **Controlador:** Cliente (corretor/empresa).
*   **Operador:** RDP Studio (Funila).
*   **Checklist:** Consentimento, Criptografia, Política de Privacidade, Exclusão.

---

## 12. Identidade Visual — Funila Design System
**Cores:**
*   **Azul Primário:** `#2563EB` (Primary 500).
*   **Dark Theme:** `#0F1115` (Bg Primary), `#161A22` (Bg Secondary).
*   **Status:** 🔥 `#22C55E`, 🟡 `#F59E0B`, ❄️ `#38BDF8`.

**Tipografia:**
*   **Display:** Syne.
*   **Body:** DM Sans.
*   **Mono:** DM Mono.

**Regras:**
*   Azul é a única cor dominante.
*   Status são funcionais (nunca decorativos).
*   Dark mode é o padrão.

---

## 13. Estrutura Oficial do Sistema — Layout Base
**Layout:** Sidebar fixa (esquerda), Header fixo (topo), Conteúdo central.
**Sidebar:** Logo, Cliente, Menu (Dashboard, Leads, Links, etc.), Footer (Plano, Sair).
**Header:** Breadcrumb, Busca, Filtro Período, Toggle Theme, Avatar.
