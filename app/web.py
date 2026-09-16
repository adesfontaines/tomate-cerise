from fastapi.responses import HTMLResponse


DEMO_LOGIN_PAGE = """<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tomate Cerise — Connexion</title>
  <style>
    :root { color-scheme: dark; --bg: #071b1b; --panel: #102b2a; --line: #28504c; --cream: #f4edda; --muted: #a9c0b9; --accent: #e6b84a; --danger: #f38b7d; --success: #83d6a5; }
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: radial-gradient(circle at 20% 0%, #17413c, var(--bg) 55%); color: var(--cream); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    main { width: min(420px, calc(100vw - 40px)); }
    .brand { display: flex; align-items: center; gap: 10px; margin-bottom: 22px; color: var(--accent); font-size: 13px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; }
    .brand-dot { width: 9px; height: 9px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 18px var(--accent); }
    .card { padding: 34px; border: 1px solid var(--line); border-radius: 18px; background: rgba(16, 43, 42, .92); box-shadow: 0 24px 70px rgba(0, 0, 0, .3); }
    h1 { margin: 0 0 9px; font-size: 30px; letter-spacing: -.03em; }
    .intro { margin: 0 0 28px; color: var(--muted); line-height: 1.5; }
    label { display: block; margin: 17px 0 7px; color: var(--muted); font-size: 13px; font-weight: 600; }
    input { width: 100%; padding: 13px 14px; border: 1px solid var(--line); border-radius: 9px; outline: none; background: #0a2221; color: var(--cream); font: inherit; }
    input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(230, 184, 74, .14); }
    button { width: 100%; margin-top: 25px; padding: 13px; border: 0; border-radius: 9px; cursor: pointer; background: var(--accent); color: #182016; font: inherit; font-weight: 750; }
    button:disabled { cursor: wait; opacity: .65; }
    #result { min-height: 22px; margin: 18px 0 0; font-size: 14px; line-height: 1.45; }
    .success { color: var(--success); } .error { color: var(--danger); }
    footer { margin-top: 20px; color: var(--muted); font-size: 12px; text-align: center; }
    a { color: var(--accent); }
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
      <p id="result" role="status"></p>
    </section>
    <footer>Plateforme de réservation en circuit court · <a href="/docs">API</a></footer>
  </main>
  <script>
    const form = document.querySelector('#login-form');
    const button = document.querySelector('#submit');
    const result = document.querySelector('#result');
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      button.disabled = true;
      result.className = '';
      result.textContent = 'Vérification en cours…';
      try {
        const response = await fetch('/api/v1/auth/login', {
          method: 'POST', headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({email: form.email.value, password: form.password.value})
        });
        const body = await response.json();
        if (response.ok) {
          result.className = 'success';
          result.textContent = 'Connexion réussie — session ouverte pour ' + body.user_email;
        } else {
          result.className = 'error';
          result.textContent = 'Connexion refusée — ' + (body.detail || 'identifiants invalides');
        }
      } catch (error) {
        result.className = 'error';
        result.textContent = 'Le service est momentanément indisponible.';
      } finally {
        button.disabled = false;
      }
    });
  </script>
</body>
</html>"""


def demo_login_page() -> HTMLResponse:
    return HTMLResponse(DEMO_LOGIN_PAGE)
