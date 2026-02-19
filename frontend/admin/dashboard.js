document.addEventListener("DOMContentLoaded", async () => {
    // 1. Check Auth & Get User
    const session = await requireAuth();
    if (!session) return;

    const user = session.user;
    if (user && user.email) {
        const emailEl = document.getElementById("user-email");
        if (emailEl) emailEl.innerText = user.email;
    }

    // 2. Load Data
    await loadMetrics();
    await loadRecentLeads();

    // 3. Init Chart
    initChart();
});

async function loadMetrics() {
    try {
        const res = await apiFetch("/metrics");
        if (res && res.ok) {
            const data = await res.json();

            updateVal("val-clicks", data.clicks);
            updateVal("val-leads", data.leads);
            updateVal("val-hot", data.hot_leads);
            updateVal("val-conv", data.conversion + "%");
        }
    } catch (e) {
        console.error("Metrics load failed", e);
    }
}

function updateVal(id, val) {
    const el = document.getElementById(id);
    if (el) el.innerText = val;
}

async function loadRecentLeads() {
    const container = document.getElementById("leads-table-body");
    if (!container) return;

    try {
        // Fetch last 5 leads
        const res = await apiFetch("/leads?limit=5");

        if (res && res.ok) {
            const leads = await res.json();
            container.innerHTML = "";

            if (!leads || leads.length === 0) {
                container.innerHTML = '<div class="table-row" style="justify-content:center;color:var(--text-secondary)">Nenhum lead encontrado.</div>';
                return;
            }

            leads.forEach(lead => {
                const date = new Date(lead.created_at).toLocaleDateString("pt-BR", {
                    day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit'
                });

                let badgeClass = 'cold';
                let badgeText = 'Frio';

                if (lead.status === 'hot') { badgeClass = 'hot'; badgeText = 'Quente'; }
                else if (lead.status === 'warm') { badgeClass = 'warm'; badgeText = 'Morno'; }
                else if (lead.status === 'converted') { badgeClass = 'hot'; badgeText = 'Convertido'; }

                // HTML Template
                const row = document.createElement('div');
                row.className = 'table-row';
                row.innerHTML = `
                    <span style="font-weight:600;color:var(--text-primary)">${lead.name}</span>
                    <span style="font-family:'DM Mono',monospace;color:var(--accent)">${lead.internal_score}</span>
                    <span><div class="badge ${badgeClass}">${badgeText}</div></span>
                    <span style="color:var(--text-secondary);font-size:13px">${date}</span>
                    <span><button onclick="viewLead('${lead.id}')" style="background:none;border:none;color:var(--accent);cursor:pointer;font-weight:600;">Ver</button></span>
                `;
                container.appendChild(row);
            });
        }
    } catch (e) {
        console.error("Leads load failed", e);
        container.innerHTML = '<div class="table-row" style="color:var(--status-error)">Erro ao carregar leads.</div>';
    }
}

// Global scope for onclick
window.viewLead = function(id) {
    alert("Detalhes do lead " + id + " (Implementação futura)");
    // TODO: Implement Modal
}

function initChart() {
    const ctx = document.getElementById('leadsChart');
    if (!ctx) return;

    // Mock data for now
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
            datasets: [{
                label: 'Leads',
                data: [0, 0, 0, 0, 0, 0, 0], // Placeholder
                borderColor: '#2563EB',
                backgroundColor: 'rgba(37,99,235,0.1)',
                tension: 0.4,
                fill: true,
                pointBackgroundColor: '#2563EB'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: '#2A3242' },
                    ticks: { color: '#9CA3AF' }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: '#9CA3AF' }
                }
            }
        }
    });
}
