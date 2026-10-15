(() => {
  const d = document, root = d.documentElement, body = d.body;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header: tło po scrollu, chowanie przy scrollu w dół, pasek postępu */
  const header = d.querySelector('.site-header');
  const bar = d.querySelector('.progress');
  let lastY = scrollY, ticking = false;
  const onScroll = () => {
    const y = scrollY;
    header.classList.toggle('scrolled', y > 40);
    if (!body.classList.contains('menu-open')) header.classList.toggle('hide', y > 500 && y > lastY + 4);
    if (y < lastY - 4) header.classList.remove('hide');
    lastY = y;
    const h = root.scrollHeight - innerHeight;
    if (bar) bar.style.transform = `scaleX(${h > 0 ? y / h : 0})`;
    parallax(); modelBar();
    ticking = false;
  };
  addEventListener('scroll', () => { if (!ticking) { requestAnimationFrame(onScroll); ticking = true; } }, { passive: true });

  /* menu mobilne */
  const burger = d.querySelector('.burger');
  burger?.addEventListener('click', () => {
    const open = body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', open);
    header.classList.remove('hide');
  });
  d.querySelectorAll('.menu a').forEach(a => a.addEventListener('click', () => body.classList.remove('menu-open')));
  addEventListener('keydown', e => { if (e.key === 'Escape') { body.classList.remove('menu-open'); closeLb(); } });

  /* podział nagłówków na słowa */
  d.querySelectorAll('.split-words').forEach(el => {
    let i = 0;
    const walk = node => {
      [...node.childNodes].forEach(n => {
        if (n.nodeType === 3) {
          const frag = d.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.append(' '); return; }
            const w = d.createElement('span'); w.className = 'w';
            const s = d.createElement('span'); s.textContent = part; s.style.setProperty('--i', i++);
            w.append(s); frag.append(w);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') walk(n);
      });
    };
    walk(el);
  });

  /* reveal */
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { rootMargin: '0px 0px -8% 0px', threshold: .08 });
  d.querySelectorAll('.rv, .rv-img, .rv-line, .split-words').forEach(el => io.observe(el));
  d.querySelectorAll('[data-stagger]').forEach(g => [...g.children].forEach((c, i) => { c.classList.add('rv'); c.style.setProperty('--d', `${i * 0.09}s`); io.observe(c); }));

  /* parallax zdjęć */
  const px = [...d.querySelectorAll('.parallax')];
  function parallax() {
    if (reduce) return;
    px.forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > innerHeight) return;
      const p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
      el.style.setProperty('--py', `${(-p * 40).toFixed(1)}px`);
    });
  }

  /* oś modelu inwestycyjnego wypełnia się przy scrollu */
  const model = d.querySelector('.model');
  const steps = model ? [...model.querySelectorAll('.step')] : [];
  function modelBar() {
    if (!model) return;
    const r = model.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, (innerHeight * .75 - r.top) / (r.width * .6)));
    model.style.setProperty('--p', p.toFixed(3));
    steps.forEach((s, i) => s.classList.toggle('lit', p >= i / steps.length));
  }

  /* poświata kart za kursorem */
  d.querySelectorAll('.card').forEach(c => c.addEventListener('pointermove', e => {
    const r = c.getBoundingClientRect();
    c.style.setProperty('--mx', `${e.clientX - r.left}px`);
    c.style.setProperty('--my', `${e.clientY - r.top}px`);
  }));

  /* liczniki */
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target, to = +el.dataset.count, dur = 1600, t0 = performance.now();
    const step = t => { const k = Math.min(1, (t - t0) / dur); el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); };
    reduce ? (el.textContent = to) : requestAnimationFrame(step);
    cio.unobserve(el);
  }), { threshold: .6 });
  d.querySelectorAll('[data-count]').forEach(el => cio.observe(el));

  /* przeciąganie poziomej galerii */
  d.querySelectorAll('.hscroll').forEach(s => {
    let down = false, x0 = 0, l0 = 0;
    s.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; x0 = e.clientX; l0 = s.scrollLeft; s.style.scrollSnapType = 'none'; });
    addEventListener('pointerup', () => { if (down) { down = false; s.style.scrollSnapType = ''; } });
    s.addEventListener('pointermove', e => { if (down) { e.preventDefault(); s.scrollLeft = l0 - (e.clientX - x0); } });
  });

  /* lightbox */
  const lb = d.querySelector('.lb');
  let group = [], idx = 0;
  const show = () => { const img = lb.querySelector('img'); img.src = group[idx].dataset.full || group[idx].src; img.alt = group[idx].alt; };
  function closeLb() { lb?.classList.remove('on'); }
  d.querySelectorAll('[data-lb] img').forEach(img => img.closest('figure').addEventListener('click', () => {
    group = [...img.closest('[data-lb]').querySelectorAll('img')]; idx = group.indexOf(img); show(); lb.classList.add('on');
  }));
  lb?.querySelector('.x').addEventListener('click', closeLb);
  lb?.addEventListener('click', e => { if (e.target === lb) closeLb(); });
  lb?.querySelector('.pv').addEventListener('click', () => { idx = (idx - 1 + group.length) % group.length; show(); });
  lb?.querySelector('.nx').addEventListener('click', () => { idx = (idx + 1) % group.length; show(); });

  /* formularz — w demie bez wysyłki */
  d.querySelectorAll('form.form').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    if (!f.reportValidity()) return;
    f.classList.add('sent');
    f.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
  }));

  /* link z ?temat= albo data-topic ustawia temat formularza */
  d.querySelectorAll('[data-topic]').forEach(a => a.addEventListener('click', () => {
    const r = d.querySelector(`.chips input[value="${a.dataset.topic}"]`);
    if (r) r.checked = true;
  }));

  onScroll();
})();
