from flask import Flask, render_template_string, make_response
from datetime import date
import os

app = Flask(__name__)

# After deployment, set SITE_URL to your real website address.
SITE_URL = os.environ.get("SITE_URL", "https://your-domain.com").rstrip("/")

PERSON = {
    "name": "Blacksane Thala",
    "birth_date": "2005-12-18",
    "location": "Malawi",
    "description": (
        "Blacksane Thala is a Malawian creative professional "
        "working in photography, web development, videography "
        "and graphic design."
    ),
    "professions": [
        "Photographer",
        "Web Developer",
        "Videographer",
        "Graphic Designer",
    ],
}

PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="google-site-verification" content="fOLM2RCx1aZznT1pAdm8HhjOBzxHkyTM-MbEzy3eSx4" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Blacksane Thala | Photographer, Web Developer & Creative in Malawi</title>
  <meta name="description" content="Official website of Blacksane Thala, a Malawi-based photographer, web developer, videographer and graphic designer. Explore services and creative work.">
  <meta name="keywords" content="Blacksane Thala, Blacksane Thala Malawi, Malawi photographer, Malawi web developer, Malawi videographer, Malawi graphic designer">
  <meta name="author" content="Blacksane Thala">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{{ site_url }}/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Blacksane Thala | Official Website">
  <meta property="og:description" content="{{ person.description }}">
  <meta property="og:url" content="{{ site_url }}/">
  <meta name="theme-color" content="#090909">

  <script type="application/ld+json">
  {{ schema | tojson }}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body { background: #090909; color: #f7f7f7; font-family: "DM Sans", sans-serif; line-height: 1.7; }
    a { color: inherit; text-decoration: none; }
    header { position: sticky; top: 0; z-index: 10; display: flex; justify-content: space-between; align-items: center; gap: 20px; padding: 20px 8%; background: rgba(9,9,9,.96); border-bottom: 1px solid #242424; }
    .logo { font: 800 24px "Space Grotesk", sans-serif; letter-spacing: -1px; }
    .logo span, h1 span, .section-title span { color: #d5ad45; }
    nav { display: flex; flex-wrap: wrap; gap: 24px; }
    nav a { color: #c4c4c4; font-size: 14px; }
    nav a:hover { color: #d5ad45; }
    .hero { min-height: 620px; display: flex; flex-direction: column; justify-content: center; padding: 110px 10%; background: radial-gradient(ellipse at 80% 30%, #302711 0%, transparent 55%), #090909; }
    .eyebrow { color: #d5ad45; font-size: 12px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 22px; }
    h1 { max-width: 950px; font: 700 clamp(48px, 8vw, 100px)/1.04 "Space Grotesk", sans-serif; letter-spacing: -4px; }
    .hero p { max-width: 650px; color: #b8b8b8; font-size: 18px; margin: 26px 0 30px; }
    .button { display: inline-block; width: fit-content; padding: 13px 25px; border-radius: 3px; background: #d5ad45; color: #101010; font-weight: 800; }
    .button:hover { background: #fff; }
    section { padding: 90px 10%; }
    .section-title { margin-bottom: 22px; font: 700 clamp(30px, 5vw, 44px) "Space Grotesk", sans-serif; }
    .about-copy, .intro { max-width: 850px; color: #b5b5b5; }
    .details { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; max-width: 760px; margin-top: 30px; }
    .detail, .service { padding: 24px; background: #141414; border: 1px solid #292929; }
    .detail small { display: block; color: #d5ad45; letter-spacing: 1.5px; text-transform: uppercase; }
    .services, .contact { background: #101010; }
    .service-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; margin-top: 32px; }
    .service { transition: border-color .2s, transform .2s; }
    .service:hover { border-color: #d5ad45; transform: translateY(-3px); }
    .service h3 { color: #d5ad45; font: 600 22px "Space Grotesk", sans-serif; margin-bottom: 8px; }
    .service p, .portfolio p, .contact p { color: #b5b5b5; }
    .portfolio { text-align: center; }
    .portfolio .intro { margin: 0 auto; }
    .portfolio-note { max-width: 760px; margin: 30px auto 0; padding: 30px; border: 1px dashed #555; color: #aaa; }
    .contact { text-align: center; }
    .contact p { max-width: 620px; margin: 15px auto 25px; }
    .contact .button { margin: 5px; }
    footer { padding: 28px 8%; text-align: center; border-top: 1px solid #292929; color: #888; font-size: 13px; }
    @media (max-width: 700px) {
      header { padding: 17px 6%; flex-direction: column; align-items: flex-start; }
      nav { gap: 14px; }
      nav a { font-size: 12px; }
      .hero { min-height: 540px; padding: 85px 7%; }
      h1 { letter-spacing: -2px; }
      section { padding: 70px 7%; }
      .details, .service-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
<header>
  <a class="logo" href="/">BLACK<span>SANE.</span></a>
  <nav aria-label="Main navigation">
    <a href="#about">About</a><a href="#services">Services</a>
    <a href="#portfolio">Portfolio</a><a href="#contact">Contact</a>
  </nav>
</header>

<main>
  <section class="hero">
    <div class="eyebrow">Creative Professional · Malawi</div>
    <h1>BLACKSANE<br><span>THALA.</span></h1>
    <p>Photography. Videography. Web Development. Graphic Design.
       Creative ideas brought to life through visual storytelling and technology.</p>
    <a class="button" href="#about">DISCOVER MY STORY</a>
  </section>

  <section id="about">
    <div class="eyebrow">Get to know me</div>
    <h2 class="section-title">About <span>Blacksane Thala</span></h2>
    <div class="about-copy">
      <p><strong>Blacksane Thala</strong> is a Malawi-based creative professional with interests and skills in photography, videography, web development and graphic design.</p>
      <br>
      <p>His work brings together visual creativity and digital technology, with a focus on telling stories, developing online experiences and communicating ideas through design.</p>
    </div>
    <div class="details">
      <div class="detail"><small>Full name</small><strong>Blacksane Thala</strong></div>
      <div class="detail"><small>Based in</small><strong>Malawi</strong></div>
      <div class="detail"><small>Date of birth</small><strong>18 December 2005</strong></div>
      <div class="detail"><small>Fields</small><strong>Creative & Digital Media</strong></div>
    </div>
  </section>

  <section class="services" id="services">
    <div class="eyebrow">What I do</div>
    <h2 class="section-title">My <span>Expertise</span></h2>
    <div class="service-grid">
      <article class="service"><h3>01. Photography</h3><p>Capturing people, events and stories through thoughtful composition and visual storytelling.</p></article>
      <article class="service"><h3>02. Web Development</h3><p>Creating responsive, accessible and user-friendly websites for individuals, organisations and businesses.</p></article>
      <article class="service"><h3>03. Videography</h3><p>Producing engaging visual stories through filming, creative direction and video content.</p></article>
      <article class="service"><h3>04. Graphic Design</h3><p>Designing visual identities, branding materials and digital graphics that communicate clearly.</p></article>
    </div>
  </section>

  <section class="portfolio" id="portfolio">
    <div class="eyebrow">Selected creative work</div>
    <h2 class="section-title">My <span>Portfolio</span></h2>
    <p class="intro">Explore photography, video productions, websites and graphic design projects by Blacksane Thala.</p>
    <div class="portfolio-note">Portfolio gallery coming soon. Add your own project images, descriptions and video links here before launch.</div>
  </section>

  <section class="contact" id="contact">
    <div class="eyebrow">Let's connect</div>
    <h2 class="section-title">Let's Create <span>Something.</span></h2>
    <p>For photography, web development, videography or graphic design enquiries, contact Blacksane Thala.</p>
    <!-- Replace the email address below with a real contact email. -->
    <a class="button" href="mailto:YOUR_EMAIL@example.com">CONTACT ME</a>
  </section>
</main>

<footer>© {{ year }} Blacksane Thala. All rights reserved. · Malawi</footer>
</body>
</html>
"""


def person_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": PERSON["name"],
        "birthDate": PERSON["birth_date"],
        "description": PERSON["description"],
        "nationality": {"@type": "Country", "name": "Malawi"},
        "address": {"@type": "PostalAddress", "addressCountry": "MW"},
        "jobTitle": PERSON["professions"],
        "url": SITE_URL,
    }


@app.route("/")
def home():
    return render_template_string(
        PAGE,
        person=PERSON,
        schema=person_schema(),
        site_url=SITE_URL,
        year=date.today().year,
    )


@app.route("/robots.txt")
def robots():
    response = make_response(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
    )
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    return response


@app.route("/sitemap.xml")
def sitemap():
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{SITE_URL}/</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>"""
    response = make_response(xml)
    response.headers["Content-Type"] = "application/xml; charset=utf-8"
    return response


if __name__ == "__main__":
    # debug=False is safer as a default. Use a production WSGI server when deployed.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
