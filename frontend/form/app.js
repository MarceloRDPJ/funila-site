const API_URL = "https://funila-api.onrender.com"; // Configure as needed

const state = {
    step: 1,
    data: {
        name: "",
        phone: "",
        has_clt: false,
        clt_years: "",
        income: "",
        tried_financing: false,
        cpf: "",
        consent: false,
        utm_source: "",
        utm_medium: "",
        utm_campaign: "",
        link_slug: ""
    }
};

// Utils
function getUTMParams() {
    const params = new URLSearchParams(window.location.search);

    // Attempt to get slug from query param (e.g. ?slug=abc)
    let slug = params.get("slug");

    // Fallback: Attempt to get from path
    if (!slug) {
        const pathParts = window.location.pathname.split('/').filter(p => p && !p.includes(".html"));
        if (pathParts.length > 0) {
            slug = pathParts[pathParts.length - 1];
        }
    }

    return {
        utm_source: params.get("utm_source") || "",
        utm_medium: params.get("utm_medium") || "",
        utm_campaign: params.get("utm_campaign") || "",
        utm_content: params.get("utm_content") || "",
        utm_term: params.get("utm_term") || "",
        link_slug: slug || "unknown"
    };
}

// Init
document.addEventListener("DOMContentLoaded", () => {
    const utms = getUTMParams();
    state.data = { ...state.data, ...utms };

    setupListeners();
    updateUI();
});

function setupListeners() {
    // Step 1
    const nameInput = document.getElementById("name");
    const phoneInput = document.getElementById("phone");
    const btnStep1 = document.getElementById("btn-step-1");

    function validateStep1() {
        if (nameInput.value.length > 2 && phoneInput.value.length > 10) {
            btnStep1.disabled = false;
        } else {
            btnStep1.disabled = true;
        }
    }

    nameInput.addEventListener("input", (e) => {
        state.data.name = e.target.value;
        validateStep1();
    });

    phoneInput.addEventListener("input", (e) => {
        // Simple mask (99) 99999-9999
        let v = e.target.value.replace(/\D/g, "");
        if (v.length > 11) v = v.slice(0, 11);
        e.target.value = v; // Display raw or implement mask logic
        state.data.phone = v;
        validateStep1();
    });

    btnStep1.addEventListener("click", () => {
        goToStep(2);
        // Optional: Send Step 1 event
    });

    // Step 3
    document.getElementById("cpf").addEventListener("input", (e) => {
        state.data.cpf = e.target.value;
    });

    const consentBox = document.getElementById("consent");
    const btnSubmit = document.getElementById("btn-submit");

    consentBox.addEventListener("change", (e) => {
        state.data.consent = e.target.checked;
        checkStep3Completion();
    });

    btnSubmit.addEventListener("click", submitForm);
}

function selectClt(hasClt) {
    state.data.has_clt = hasClt;
    // Highlight button
    // ...
    if (hasClt) {
        document.getElementById("clt-years-container").classList.remove("hidden");
    } else {
        document.getElementById("clt-years-container").classList.add("hidden");
        state.data.clt_years = null;
        goToStep(3);
    }
}

function selectCltTime(years) {
    state.data.clt_years = years;
    goToStep(3);
}

function selectIncome(range) {
    state.data.income = range;
    // Highlight
}

function selectFinancing(tried) {
    state.data.tried_financing = tried;
    checkStep3Completion();
}

function checkStep3Completion() {
    const btn = document.getElementById("btn-submit");
    if (state.data.income && state.data.consent && state.data.tried_financing !== undefined) {
        btn.disabled = false;
    } else {
        btn.disabled = true;
    }
}

function goToStep(step) {
    state.step = step;

    document.querySelectorAll(".step").forEach((el, index) => {
        if (index + 1 === step) el.classList.add("active");
        else el.classList.remove("active");
    });

    // Update progress dots
    document.querySelectorAll(".progress-dot").forEach((dot, index) => {
        if (index + 1 <= step) dot.classList.add("active");
        else dot.classList.remove("active");
    });
}

async function submitForm() {
    const btn = document.getElementById("btn-submit");
    btn.disabled = true;
    btn.innerText = "Enviando...";

    try {
        const payload = {
            name: state.data.name,
            phone: state.data.phone,
            has_clt: state.data.has_clt,
            clt_years: state.data.clt_years,
            income: state.data.income,
            tried_financing: state.data.tried_financing,
            cpf: state.data.cpf,
            consent_given: state.data.consent,
            // UTMs
            utm_source: state.data.utm_source,
            utm_campaign: state.data.utm_campaign,
            utm_medium: state.data.utm_medium,
            link_slug: state.data.link_slug
        };

        const res = await fetch(`${API_URL}/leads`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (res.ok) {
            const result = await res.json();
            // Show result
            document.getElementById("result-badge").innerText = `Score: ${result.score} - ${result.status}`;
            const waLink = document.getElementById("whatsapp-link");
            waLink.href = result.whatsapp_url;
            goToStep(4);
        } else {
            alert("Erro ao enviar. Tente novamente.");
            btn.disabled = false;
            btn.innerText = "Enviar";
        }
    } catch (e) {
        console.error(e);
        alert("Erro de conexão.");
        btn.disabled = false;
        btn.innerText = "Enviar";
    }
}
