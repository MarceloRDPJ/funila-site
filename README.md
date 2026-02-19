# FUNILA — Sistema de Inteligência Comercial (V3.0)

> **DESENVOLVIDO POR:** [RDP Studio](https://rdpstudio.com.br/)
> **COPYRIGHT © 2026** — TODOS OS DIREITOS RESERVADOS.

![Status](https://img.shields.io/badge/STATUS-ONLINE-success?style=for-the-badge) ![Security](https://img.shields.io/badge/SECURITY-ENCRYPTED-blue?style=for-the-badge) ![Version](https://img.shields.io/badge/VERSION-3.0-orange?style=for-the-badge)

---

## ⚠️ AVISO DE PROPRIEDADE INTELECTUAL

**ATENÇÃO:** Este código é propriedade exclusiva da **RDP Studio**.
A reprodução, distribuição, engenharia reversa, ou uso não autorizado deste software (total ou parcial) é estritamente proibida.

O código fonte contém marcadores de rastreamento digital ("watermarks") e metadados de autoria que comprovam a propriedade original em caso de litígio.

---

## 📂 Estrutura do Projeto (Esqueleto)

Abaixo está a documentação linha-por-linha da arquitetura de arquivos para facilitar a manutenção futura.

```
/
├── assets/                  # [DIRETÓRIO] Arquivos de mídia e imagens
│   ├── apple-touch-icon.png # Ícone para dispositivos Apple (180x180)
│   ├── favicon-32x32.png    # Favicon padrão (32x32)
│   └── favicon-16x16.png    # Favicon reduzido (16x16)
│
├── index.html               # [CORE] Arquivo Principal do Frontend
│   ├── <head>               # Metadados, SEO, Fontes e CSS Global
│   ├── <body>               # Estrutura visual
│   │   ├── .intro-overlay   # Animação de entrada (Raio Laser + Logo)
│   │   ├── nav              # Barra de navegação fixa
│   │   ├── .hero            # Seção principal com CTA e Hook Psicológico
│   │   ├── #problema        # Seção de Conscientização
│   │   ├── #solucao         # Seção de Explicação da Tecnologia
│   │   ├── footer           # Rodapé com links legais
│   │   └── #demoModal       # Modal de Simulação do Sistema
│   └── <script>             # Lógica de interação e animação do modal
│
└── README.md                # Este arquivo de documentação
```

---

## 🛠️ Manual de Manutenção e Customização

Siga este guia para realizar alterações seguras no sistema sem quebrar a integridade visual ou funcional.

### 1. Alterar o Favicon (Ícone da Aba)
Para trocar o ícone que aparece na aba do navegador:
1.  Gere seu novo ícone em formatos `.png`.
2.  Renomeie os arquivos exatamente para: `favicon-32x32.png`, `favicon-16x16.png` e `apple-touch-icon.png`.
3.  Substitua os arquivos existentes na pasta `/assets/`.
4.  **Não é necessário alterar o código** se os nomes dos arquivos forem mantidos.

### 2. Alterar a Copy do "Hero Pill" (Gancho Psicológico)
O elemento flutuante no topo do site ("Novo Lead Qualificado...") é controlado diretamente no HTML.

*   **Localização:** `index.html` (Linha ~360)
*   **Código Alvo:**
    ```html
    <div class="pill">
      <div class="pill-dot"></div>
      <span>Novo Lead Qualificado Detectado: Score 850+</span> <!-- EDITAR AQUI -->
    </div>
    ```
*   **Dica:** Use gatilhos de urgência ou prova social. Evite textos estáticos como "Versão 3.0".

### 3. Alterar o Link da "Área do Cliente"
*   **Localização:** `index.html` (Dentro da tag `<nav>`)
*   **Código Alvo:**
    ```html
    <a href="https://app.funila.com.br/" class="btn-member"> <!-- EDITAR O HREF -->
    ```

### 4. Ajustar Cores da Marca (CSS Variables)
O sistema utiliza variáveis CSS globais para facilitar a troca de tema.
*   **Localização:** `index.html` (Dentro de `<style> :root { ... }`)
*   **Variáveis Principais:**
    *   `--blue`: Cor primária (Botões, Detalhes).
    *   `--blue-neon`: Cor de brilho e efeitos de luz.
    *   `--bg-main`: Cor de fundo principal.

---

## 🔒 Segurança e Compliance (LGPD)

Este sistema foi projetado seguindo princípios de **Security by Design** e **Privacy by Default**.

### 1. Link Tracker & Criptografia
Embora o frontend seja a interface de apresentação, a arquitetura do Funila (Backend) utiliza criptografia ponta-a-ponta para o rastreamento de leads.
*   **No Código:** As referências a "DADOS CRIPTOGRAFADOS" no rodapé do Hero servem para aumentar a confiança do usuário (Trust Signal).

### 2. Conformidade LGPD
O site inclui links placeholders para "Privacidade", "Termos de Uso" e "LGPD" no rodapé.
*   **Ação Necessária:** Ao implantar em produção, certifique-se de vincular esses `href="#"` às páginas reais de política de privacidade da sua empresa para garantir conformidade legal total.

### 3. Proteção contra Cópia (Anti-Plágio)
Implementamos técnicas de **Impregnação de Marca** no código-fonte:
*   **Headers ASCII:** Cabeçalhos visuais ocultos no HTML.
*   **Meta Tags de Autoria:** Tags `<meta name="author">` e `<meta name="copyright">` indeléveis.
*   **Comentários de Propriedade:** Blocos de aviso legal espalhados pelo CSS e JS.

---

## 📞 Suporte e Contato

Para modificações avançadas, suporte técnico ou dúvidas sobre licenciamento:

**RDP Studio**
🌐 [www.rdpstudio.com.br](https://rdpstudio.com.br/)
📍 Goiânia, Brasil.

> *"O design não é apenas o que se vê e o que se sente. O design é como funciona."*
