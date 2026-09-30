# Big Drum Digital

A buildless website for GitHub Pages. Open with `python3 -m http.server 4173` and visit http://localhost:4173.

## Production version

Homepage, ten complete free tutorials, searchable learning index, pricing from Jesse’s planning notes, portfolio, privacy page, and an inquiry form that opens an email draft. No submissions are claimed to be stored or delivered by the website.

## Deployment

Choose the destination repository, authenticate GitHub CLI, add the remote, and push main. In repository Settings → Pages, select GitHub Actions. The included workflow publishes only public website files. No custom domain file is included because the existing bigdrumdigital.com website must not be replaced until the destination is confirmed. Add CNAME and configure DNS when ready.

The `codex/staging` branch contains V2. It is not deployed by the production workflow. Use a separate preview host or repository to publish staging independently.

## Launch decisions

Confirm the inquiry email, plan pricing and scope. The original notes propose an included website, branding, hosting, voice editor, and a 30-day guarantee. Those promises need defined scope and an available editor before publishing them. They are not advertised as currently delivered here. No doubled-revenue claim or made-up customer result is used.

Connect an email provider and inquiry endpoint if direct web submissions are desired. V2 email access needs server-side verification and protected content storage outside the public GitHub Pages repository. Browser storage is not an access gate. Podcast and video players require Jesse’s actual media assets.

## Design references and assets

Palette sampled from JesseHall.com Elementor global CSS: yellow #F8C805, peach #FFBC7D, charcoal, white. Awwwards MCP references: CoMinVi for confident typography and Jesper Landberg for project presentation. Mobbin tools were not available in this session. Logo supplied by Jesse. Jesse portrait and portfolio screenshots copied from JesseHall.com with authorization. Mary Pratt quote excerpt and attribution from JesseHall.com. Google Fonts: Space Grotesk and DM Sans. No Envato stock assets used.

## Copy structure

Customer goal, time and clarity problem, an experienced guide, three-step plan, direct goal inquiry, useful DIY alternative, and a picture of steady progress. Pricing is a conversation CTA rather than checkout.
