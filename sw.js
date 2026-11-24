/* Loose! service worker. The game itself (index.html) is served from a pinned copy, so a new release
   only takes effect when the player chooses "Update now". Everything else is network-first. */
const APP = 'loose-app', ASSETS = 'loose-assets-1';
self.addEventListener('install', e => { self.skipWaiting(); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== APP && k !== ASSETS).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
const isShell = u => u.origin === location.origin && !u.search && (u.pathname.endsWith('/') || u.pathname.endsWith('/index.html'));
async function fresh(){ const r = await fetch('./index.html', {cache:'reload'}); if (!r.ok) throw new Error('fetch failed'); const c = await caches.open(APP); await c.put('./index.html', r.clone()); await c.put('./', r.clone()); return r; }
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (u.origin !== location.origin || e.request.method !== 'GET' || u.search) return;
  if (e.request.mode === 'navigate' || isShell(u)) {
    e.respondWith(caches.open(APP).then(c => c.match('./index.html')).then(hit => hit || fresh()).catch(() => fetch(e.request)));
    return;
  }
  e.respondWith(fetch(e.request, {cache:'no-cache'}).then(r => { const cp = r.clone(); caches.open(ASSETS).then(c => c.put(e.request, cp)); return r; }).catch(() => caches.match(e.request)));
});
self.addEventListener('message', e => { if (e.data === 'apply-update') e.waitUntil(fresh().then(() => e.source && e.source.postMessage('update-applied')).catch(() => e.source && e.source.postMessage('update-failed'))); });
self.addEventListener('notificationclick', e => { e.notification.close(); e.waitUntil(clients.matchAll({type:'window'}).then(cs => cs.length ? cs[0].focus() : clients.openWindow('./'))); });
