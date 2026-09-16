from fastapi.responses import HTMLResponse


DEMO_LOGIN_PAGE = """<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tomate Cerise — Connexion</title>
  <style>
    :root { color-scheme: dark; --bg: #071b1b; --panel: #102b2a; --line: #28504c; --cream: #f4edda; --muted: #a9c0b9; --accent: #76b852; --danger: #f38b7d; --success: #83d6a5; }
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: radial-gradient(circle at 20% 0%, #17413c, var(--bg) 55%); color: var(--cream); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    main { width: min(430px, calc(100vw - 40px)); }
    .brand { display: flex; align-items: center; gap: 10px; margin-bottom: 22px; color: var(--accent); font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; }
    .brand-dot { width: 9px; height: 9px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 18px var(--accent); }
    .card { padding: 34px; border: 1px solid var(--line); border-radius: 18px; background: rgba(16, 43, 42, .94); box-shadow: 0 24px 70px rgba(0, 0, 0, .3); }
    h1 { margin: 0 0 9px; font-size: 30px; letter-spacing: -.03em; }
    .intro { margin: 0 0 28px; color: var(--muted); line-height: 1.5; }
    label { display: block; margin: 17px 0 7px; color: var(--muted); font-size: 13px; font-weight: 600; }
    input { width: 100%; padding: 13px 14px; border: 1px solid var(--line); border-radius: 9px; outline: none; background: #0a2221; color: var(--cream); font: inherit; transition: border .2s, box-shadow .2s; }
    input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(230, 184, 74, .14); }
    button { width: 100%; margin-top: 25px; padding: 13px; border: 0; border-radius: 9px; cursor: pointer; background: var(--accent); color: #182016; font: inherit; font-weight: 750; transition: transform .15s, opacity .15s; }
    button:hover { transform: translateY(-1px); } button:disabled { cursor: wait; opacity: .65; transform: none; }
    .feedback { display: none; gap: 12px; align-items: flex-start; margin-top: 22px; padding: 14px; border: 1px solid var(--line); border-radius: 11px; line-height: 1.4; }
    .feedback.visible { display: flex; }
    .feedback.success { border-color: rgba(131, 214, 165, .45); background: rgba(57, 122, 81, .16); }
    .feedback.error { border-color: rgba(243, 139, 125, .45); background: rgba(142, 56, 49, .16); }
    .feedback-icon { flex: 0 0 auto; width: 23px; height: 23px; display: grid; place-items: center; border-radius: 50%; font-weight: 800; }
    .success .feedback-icon { background: var(--success); color: #102b1c; } .error .feedback-icon { background: var(--danger); color: #3a1512; }
    .feedback-title { display: block; margin-bottom: 3px; font-weight: 750; } .feedback-text { color: var(--muted); font-size: 13px; }
    .technical { display: block; margin-top: 7px; color: inherit; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 11px; opacity: .72; }
    .retry { display: none; margin-top: 12px; padding: 0; border: 0; background: transparent; color: var(--accent); font-size: 12px; font-weight: 650; text-align: left; }
    .retry.visible { display: block; } .retry:hover { transform: none; text-decoration: underline; }
    .dashboard { display: none; }
    .dashboard.visible { display: block; }
    .dashboard-head { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px; }
    .eyebrow { margin: 0 0 7px; color: var(--accent); font-size: 11px; font-weight: 750; letter-spacing: .16em; text-transform: uppercase; }
    .dashboard h2 { margin: 0; font-size: 27px; letter-spacing: -.03em; }
    .logout { width: auto; margin: 0; padding: 8px 11px; background: transparent; color: var(--muted); font-size: 12px; }
    .basket { padding: 17px; border: 1px solid var(--line); border-radius: 12px; background: rgba(7, 27, 27, .5); }
    .basket + .basket { margin-top: 10px; }
    .basket-row { display: flex; justify-content: space-between; gap: 16px; align-items: center; }
    .basket strong { display: block; margin-bottom: 5px; font-size: 15px; }
    .basket small { color: var(--muted); }
    .price { color: var(--accent); font-weight: 750; white-space: nowrap; }
    .landing { width: min(900px, calc(100vw - 40px)); }
    .landing-nav { display: flex; justify-content: space-between; align-items: center; margin-bottom: 80px; }
    .landing-nav a { text-decoration: none; }
    .nav-link { padding: 10px 15px; border: 1px solid var(--line); border-radius: 8px; color: var(--cream); font-size: 13px; }
    .hero { max-width: none; min-height: 430px; display: flex; flex-direction: column; justify-content: center; padding: 34px 40px 34px 30px; border: 1px solid rgba(244, 237, 218, .18); border-radius: 20px; overflow: hidden; background-image: linear-gradient(90deg, rgba(7, 27, 27, .94) 0%, rgba(7, 27, 27, .72) 42%, rgba(7, 27, 27, .12) 100%), url('/static/hero-baskets.png'); background-position: center; background-size: cover; box-shadow: 0 24px 70px rgba(0, 0, 0, .28); }
    .hero h1 { margin: 0 0 18px; max-width: 560px; font-size: clamp(42px, 8vw, 76px); line-height: .98; letter-spacing: -.07em; } .hero h1 span { color: var(--accent); }
    .hero p { max-width: 520px; margin: 0; color: var(--cream); font-size: 18px; line-height: 1.55; text-shadow: 0 1px 16px rgba(0, 0, 0, .35); } .hero-cta { display: inline-block; align-self: flex-start; width: fit-content; margin-top: 30px; padding: 16px 24px 16px 30px; border-radius: 9px; background: #76b852; color: #102016; font-weight: 750; box-shadow: 0 8px 20px rgba(0, 0, 0, .18); }
    .landing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 18px; }
    .landing-tile { padding: 18px; border: 1px solid var(--line); border-radius: 12px; background: rgba(16, 43, 42, .65); }
    .landing-tile strong { display: block; margin-bottom: 7px; } .landing-tile span { color: var(--muted); font-size: 13px; line-height: 1.4; }
    @media (max-width: 650px) { .landing-nav { margin-bottom: 50px; } .landing-grid { grid-template-columns: 1fr; margin-top: 50px; } }
    footer { margin-top: 20px; color: var(--muted); font-size: 12px; text-align: center; } a { color: var(--accent); }
  </style>
</head>
<body>
  <main>
    <div class="brand"><span class="brand-dot"></span> Tomate Cerise</div>
    <section class="card">
      <h1>Bon retour</h1>
      <p class="intro">Connectez-vous pour retrouver vos paniers et vos points de retrait.</p>
      <form id="login-form">
        <label for="email">Adresse email</label>
        <input id="email" name="email" type="email" value="ade@softfluent.com" autocomplete="username" required>
        <label for="password">Mot de passe</label>
        <input id="password" name="password" type="password" value="demo-password" autocomplete="current-password" required>
        <button id="submit" type="submit">Se connecter</button>
      </form>
      <div id="dashboard" class="dashboard">
        <div class="dashboard-head"><div><p class="eyebrow">Mon espace</p><h2>Bonjour <span id="dashboard-user"></span></h2></div><button id="logout" class="logout" type="button">Se déconnecter</button></div>
        <div class="basket"><div class="basket-row"><div><strong>Panier de saison</strong><small>Retrait · Ferme des Lilas · vendredi</small></div><span class="price">24,90 €</span></div></div>
        <div class="basket"><div class="basket-row"><div><strong>Panier famille</strong><small>Retrait · Marché central · samedi</small></div><span class="price">38,50 €</span></div></div>
      </div>
      <div id="feedback" class="feedback" role="status" aria-live="polite">
        <span id="feedback-icon" class="feedback-icon"></span>
        <div><strong id="feedback-title" class="feedback-title"></strong><span id="feedback-text" class="feedback-text"></span><code id="technical" class="technical"></code></div>
      </div>
      <button id="retry" class="retry" type="button">← Réessayer avec une autre adresse</button>
    </section>
    <footer>Plateforme de réservation en circuit court · <a href="/docs">API</a></footer>
  </main>
  <script>
    const form = document.querySelector('#login-form');
    const button = document.querySelector('#submit');
    const feedback = document.querySelector('#feedback');
    const icon = document.querySelector('#feedback-icon');
    const title = document.querySelector('#feedback-title');
    const text = document.querySelector('#feedback-text');
    const technical = document.querySelector('#technical');
    const retry = document.querySelector('#retry');
    const dashboard = document.querySelector('#dashboard');
    const dashboardUser = document.querySelector('#dashboard-user');
    const logout = document.querySelector('#logout');
    function showDashboard(userEmail) {
      form.style.display = 'none';
      feedback.className = 'feedback';
      retry.className = 'retry';
      dashboardUser.textContent = userEmail.split('@')[0];
      dashboard.className = 'dashboard visible';
    }
    logout.addEventListener('click', () => { dashboard.className = 'dashboard'; form.style.display = ''; });
    function showFeedback(kind, heading, message, code, symbol) {
      feedback.className = 'feedback visible ' + kind;
      icon.textContent = symbol;
      title.textContent = heading;
      text.textContent = message;
      technical.textContent = code ? 'Code : ' + code : '';
      retry.className = kind === 'error' ? 'retry visible' : 'retry';
    }
    retry.addEventListener('click', () => { feedback.className = 'feedback'; retry.className = 'retry'; form.email.focus(); });
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      button.disabled = true;
      button.textContent = 'Connexion…';
      feedback.className = 'feedback'; retry.className = 'retry';
      try {
        const response = await fetch('/api/v1/auth/login', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({email: form.email.value, password: form.password.value}) });
        const body = await response.json();
        if (response.ok) showDashboard(body.user_email);
        else showFeedback('error', 'Adresse non reconnue', 'Vérifiez votre adresse email puis réessayez.', body.detail?.code || 'ACCOUNT_NOT_FOUND', '!');
      } catch (error) { showFeedback('error', 'Service indisponible', 'Impossible de joindre Tomate Cerise pour le moment.', 'NETWORK_ERROR', '!'); }
      finally { button.disabled = false; button.textContent = 'Se connecter'; }
    });
  </script>
</body>
</html>"""


def demo_login_page() -> HTMLResponse:
    return HTMLResponse(DEMO_LOGIN_PAGE)


LANDING_PAGE = """<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tomate Cerise — Des paniers qui ont du goût</title>
  <style>
    :root { color-scheme: dark; --bg: #071b1b; --panel: #102b2a; --line: #28504c; --cream: #f4edda; --muted: #a9c0b9; --accent: #76b852; }
    * { box-sizing: border-box; } body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: radial-gradient(circle at 80% 0%, #17413c, var(--bg) 60%); color: var(--cream); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .landing { width: min(900px, calc(100vw - 40px)); } .landing-nav { display: flex; justify-content: space-between; align-items: center; margin-bottom: 80px; }
    .brand { display: flex; align-items: center; gap: 10px; color: var(--accent); font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; } .brand-dot { width: 9px; height: 9px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 18px var(--accent); }
    .landing-nav a, .hero-cta { text-decoration: none; } .nav-link { padding: 10px 15px; border: 1px solid var(--line); border-radius: 8px; color: var(--cream); font-size: 13px; }
    .hero { min-height: 430px; display: flex; flex-direction: column; justify-content: center; padding: 34px 40px 34px 30px; border: 1px solid rgba(244, 237, 218, .18); border-radius: 20px; overflow: hidden; background-image: linear-gradient(90deg, rgba(7, 27, 27, .94) 0%, rgba(7, 27, 27, .72) 42%, rgba(7, 27, 27, .12) 100%), url('/static/hero-baskets.png'); background-position: center; background-size: cover; box-shadow: 0 24px 70px rgba(0, 0, 0, .28); }
    .hero h1 { margin: 0 0 18px; max-width: 560px; font-size: clamp(42px, 8vw, 76px); line-height: .98; letter-spacing: -.07em; } .hero h1 span { color: var(--accent); }
    .hero p { max-width: 520px; margin: 0; color: var(--cream); font-size: 18px; line-height: 1.55; text-shadow: 0 1px 16px rgba(0, 0, 0, .35); } .hero-cta { display: inline-block; align-self: flex-start; width: fit-content; margin-top: 30px; padding: 16px 24px 16px 30px; border-radius: 9px; background: #76b852; color: #102016; font-weight: 750; box-shadow: 0 8px 20px rgba(0, 0, 0, .18); }
    .landing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 18px; } .landing-tile { padding: 18px; border: 1px solid var(--line); border-radius: 12px; background: rgba(16, 43, 42, .65); }
    .landing-tile strong { display: block; margin-bottom: 7px; } .landing-tile span { color: var(--muted); font-size: 13px; line-height: 1.4; } footer { margin-top: 25px; color: var(--muted); font-size: 12px; }
    @media (max-width: 650px) { .landing-nav { margin-bottom: 50px; } .landing-grid { grid-template-columns: 1fr; margin-top: 50px; } }
  </style>
</head>
<body>
  <main class="landing">
    <nav class="landing-nav"><div class="brand"><span class="brand-dot"></span> Tomate Cerise</div><a class="nav-link" href="/demo">Se connecter</a></nav>
    <section class="hero"><h1>Des paniers frais.<br><span>Un circuit court.</span></h1><p>Tomate Cerise rapproche les producteurs locaux et les familles autour de paniers de saison, simples à réserver et agréables à retirer.</p><a class="hero-cta" href="/demo">Découvrir mon espace →</a></section>
    <section class="landing-grid"><div class="landing-tile"><strong>Local</strong><span>Des producteurs proches, des produits choisis au rythme des saisons.</span></div><div class="landing-tile"><strong>Simple</strong><span>Réservez votre panier en quelques secondes, sans détour.</span></div><div class="landing-tile"><strong>Humain</strong><span>Un point de retrait et une équipe qui restent proches de vous.</span></div></section>
    <footer>Tomate Cerise · Réservation de paniers en circuit court</footer>
  </main>
</body>
</html>"""


def landing_page() -> HTMLResponse:
    return HTMLResponse(LANDING_PAGE)
