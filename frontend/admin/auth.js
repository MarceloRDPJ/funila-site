// frontend/admin/auth.js

// ⚠️ SUBSTITUA PELAS SUAS CHAVES DO SUPABASE ⚠️
const SUPABASE_URL = "https://YOUR_PROJECT.supabase.co";
const SUPABASE_KEY = "YOUR_ANON_KEY"; // Chave pública (anon)

let supabaseClient;

// Verifica se a biblioteca foi carregada
if (typeof supabase !== 'undefined') {
    supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
} else {
    console.error("Supabase JS not loaded. Include the CDN script.");
}

/**
 * Verifica autenticação. Redireciona para login se não logado.
 * Retorna a sessão se válido.
 */
async function requireAuth() {
    if (!supabaseClient) return null;

    const { data: { session } } = await supabaseClient.auth.getSession();

    const isLoginPage = window.location.pathname.includes("login.html");

    if (!session) {
        if (!isLoginPage) {
            window.location.href = "login.html";
        }
        return null;
    } else {
        if (isLoginPage) {
            window.location.href = "index.html";
        }
        return session;
    }
}

/**
 * Realiza o login
 */
async function login(email, password) {
    if (!supabaseClient) throw new Error("Supabase not initialized");

    const { data, error } = await supabaseClient.auth.signInWithPassword({
        email,
        password
    });

    if (error) throw error;
    return data;
}

/**
 * Logout
 */
async function logout() {
    if (!supabaseClient) return;
    await supabaseClient.auth.signOut();
    window.location.href = "login.html";
}

/**
 * Helper para fazer fetch na API Backend com o token
 */
async function apiFetch(endpoint, options = {}) {
    const session = await requireAuth();
    if (!session) return;

    const token = session.access_token;

    const headers = {
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json",
        ...options.headers
    };

    // Use a URL da API definida no manual (Render)
    const API_BASE = "https://funila-api.onrender.com";

    const response = await fetch(`${API_BASE}${endpoint}`, {
        ...options,
        headers
    });

    if (response.status === 401) {
        // Token inválido ou expirado
        logout();
        return;
    }

    return response;
}
