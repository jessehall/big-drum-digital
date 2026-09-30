# Big Drum Digital

A buildless website for GitHub Pages. Open with `python3 -m http.server 4173` and visit http://localhost:4173.

## Production version

Homepage, ten complete free tutorials, searchable learning index, pricing from Jesse’s planning notes, portfolio, privacy page, and an inquiry form that opens an email draft. No submissions are claimed to be stored or delivered by the website.

## Deployment

Choose the destination repository, authenticate GitHub CLI, add the remote, and push main. In repository Settings → Pages, select GitHub Actions. The included workflow publishes only public website files. No custom domain file is included because the existing bigdrumdigital.com website must not be replaced until the destination is confirmed. Add CNAME and configure DNS when ready.

The `codex/staging` branch contains B. It is deployed independently in the big-drum-digital-staging repository. Production A retains the original homepage and ten free tutorials. Both versions use clean directory URLs and a 160ms native crossfade where the browser supports it. Existing .html tutorial and privacy links redirect to their clean addresses.

## Launch decisions

Confirm the inquiry email, plan pricing and scope. The monthly plan inclusions and 30-day love-the-work-or-do-not-pay promise now follow Jesse’s planning document. Scope is agreed before starting. The 100-business revenue goal is explicitly a mission rather than a achieved result or promise to individual customers. The voice editor remains a future service pending a working editor. No made-up customer result is used.

Connect an email provider and inquiry endpoint if direct web submissions are desired. V2 email access needs server-side verification and protected content storage outside the public GitHub Pages repository. Browser storage is not an access gate. The homepage includes Jesse’s 80-second YouTube introduction. Its local thumbnail opens a privacy-enhanced player only when clicked. Podcast content still needs Jesse’s actual media assets.

## Design references and assets

Palette sampled from JesseHall.com Elementor global CSS: yellow #F8C805, peach #FFBC7D, charcoal, white. Awwwards MCP references: CoMinVi for confident typography and Jesper Landberg for project presentation. Mobbin MCP references: Oevra for restrained founder media, OFF+BRAND for project presentation, and basement.studio for clear typography hierarchy. Logo supplied by Jesse. Jesse portrait and portfolio screenshots copied from JesseHall.com with authorization. Mary Pratt quote excerpt and attribution from JesseHall.com. Google Fonts: Space Grotesk and DM Sans. Two Unsplash photos illustrate small business life. They are not labeled as actual customers. Real customer portraits from JesseHall.com accompany testimonials, including Theo Chilicas. The strongest excerpts lead a consistent grid with larger portraits. Two Google review excerpts and the current 5.0 / 3-review rating were verified on the exact Big Drum listing on September 30, 2026. Full provenance is in content/source-credits.json. No Envato stock assets used.

## Copy structure

Customer goal, time and clarity problem, an experienced guide, three-step plan, direct goal inquiry, useful DIY alternative, and a picture of steady progress. Pricing is a conversation CTA rather than checkout.
