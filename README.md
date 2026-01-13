# RANKIN - SEO-Optimized Multi-Niche Ranking Website

## Site Overview
Rankin is a content-driven, Google-optimized website that ranks local services across multiple niches using transparent, data-driven methodology. Built with clean URL architecture, E-E-A-T signals, and modern SEO best practices.

## Site Architecture

```
/
├── index.html (Homepage - hub linking to all niches)
├── robots.txt
├── sitemap.xml (sitemap index)
├── sitemap-main.xml
├── sitemap-design-studios.xml
├── sitemap-dentists.xml
├── sitemap-gyms.xml
│
├── assets/
│   ├── css/
│   │   └── main.css (modern, minimal design system)
│   └── js/
│       └── main.js (search, table sorting, interactions)
│
├── design-studios/ (Niche hub)
│   ├── index.html
│   ├── how-we-rank/index.html (niche-specific methodology)
│   ├── new-york/index.html (city ranking page)
│   ├── los-angeles/index.html
│   ├── chicago/index.html
│   ├── austin/index.html
│   ├── miami/index.html
│   ├── type/
│   │   ├── branding/index.html (service type pages)
│   │   ├── ux-design/index.html
│   │   └── digital-design/index.html
│   └── listings/
│       └── pentagram-new-york/index.html (individual listing)
│
├── dentists/ (Niche hub)
│   ├── index.html
│   ├── how-we-rank/index.html
│   ├── new-york/index.html
│   ├── los-angeles/index.html
│   ├── chicago/index.html
│   ├── austin/index.html
│   ├── miami/index.html
│   ├── type/
│   │   ├── cosmetic-dentistry/index.html
│   │   ├── dental-implants/index.html
│   │   ├── orthodontics/index.html
│   │   └── pediatric-dentistry/index.html
│   └── listings/
│       └── [practice-slug]/index.html
│
├── gyms/ (Niche hub)
│   ├── index.html
│   ├── how-we-rank/index.html
│   ├── austin/index.html (example city)
│   ├── [other-cities]/index.html
│   ├── type/
│   │   ├── strength-training/index.html
│   │   ├── crossfit/index.html
│   │   ├── boutique-fitness/index.html
│   │   └── boxing-mma/index.html
│   └── listings/
│       └── [gym-slug]/index.html
│
├── how-we-rank/ (Global methodology)
│   └── index.html
│
├── about/
│   └── index.html
│
├── editorial-policy/
│   └── index.html
│
├── contact/
│   └── index.html
│
└── corrections/
    └── index.html
```

## URL Patterns

### Core Patterns
- **Niche hub:** `/[niche]/`
- **City ranking:** `/[niche]/[city]/`
- **Service type (niche-wide):** `/[niche]/type/[service-type]/`
- **Listing page:** `/[niche]/listings/[provider-slug]/`
- **Niche methodology:** `/[niche]/how-we-rank/`

### Slug Rules
- All lowercase
- Hyphens for multi-word (not underscores)
- No special characters
- Descriptive and readable
- Trailing slashes on all directory URLs

## SEO Strategy

### On-Page Optimization
- **Title tags:** Keyword-optimized, 50-60 chars, includes year and brand
- **Meta descriptions:** 150-160 chars, includes CTA and value prop
- **H1-H6 hierarchy:** Semantic structure, one H1 per page
- **Schema markup:** ItemList for rankings, LocalBusiness for listings, BreadcrumbList
- **Canonical tags:** Self-referencing on all pages
- **Last updated dates:** Visible on all ranking pages

### Content Depth
- **Niche hubs:** 1,500-2,500 words
- **City ranking pages:** 2,000-3,500 words
- **Listing pages:** 1,200-2,000 words
- **Methodology pages:** 2,500-4,000 words

### Internal Linking
- Breadcrumbs on every page
- Contextual links within content
- "Related rankings" modules
- Footer sitewide navigation
- Hub → city → listing flow

### Trust Signals (E-E-A-T)
- Transparent methodology pages
- Editorial policy published
- Corrections process documented
- Last updated dates
- No paid placements disclosure
- Contact information
- About team/process

## Technical SEO

### Core Web Vitals
- Minimal CSS/JS (no bloated frameworks)
- Optimized images (when added)
- Clean HTML structure
- Fast server response target

### Indexation Strategy
- **Index:** All niche hubs, city pages, methodology, listings, about/contact
- **Noindex:** Search results (when built), parameter-based filters
- **Sitemaps:** Split by niche + main for management
- **Robots.txt:** Allows all, blocks search params

### Schema Types Used
- **WebSite** (homepage with SearchAction)
- **CollectionPage** (niche hubs)
- **ItemList** (city rankings)
- **LocalBusiness** / **Dentist** / **ExerciseGym** (listings)
- **BreadcrumbList** (navigation)

## Google Penalty Avoidance

### NOT Doorway Pages Because:
- Each city page has unique, substantial content (2,000+ words)
- Different rankings, local context, pricing, recommendations per city
- Genuine user value, not template spam
- No keyword stuffing
- Natural language throughout

### NOT Thin Content Because:
- Minimum word counts enforced
- Original analysis and insights
- Multiple content blocks per page
- FAQs with detailed answers
- Comparison tables with real data

### Editorial Integrity
- No paid placements
- Transparent criteria
- Corrections process
- Fact-checking documented
- Sources cited

## Content Model

### Core Objects
1. **Niche** (design-studios, dentists, gyms)
2. **Location** (new-york, los-angeles, etc.)
3. **Service Type** (branding, cosmetic-dentistry, crossfit)
4. **Listing** (individual providers)
5. **Methodology** (how rankings are determined)

### Relationships
- Niche → Cities (one-to-many)
- Niche → Service Types (one-to-many)
- City + Niche → Listings (many-to-many)
- Each entity has unique URL and content

## Page Templates

### 1. Homepage
- Hero with value prop
- Category grid with city links
- Trust signals
- Schema: WebSite

### 2. Niche Hub
- Niche overview
- City links (cards with CTAs)
- Service type browse
- Criteria overview
- FAQs
- Schema: CollectionPage

### 3. City Ranking Page
- Hero with last updated
- Methodology disclosure box
- Top 10 table with scores
- Use-case recommendations
- Pricing context
- Local considerations
- FAQs
- Related links
- Schema: ItemList

### 4. Listing Page
- Quick facts sidebar
- Overall score + breakdown
- Pros/cons
- Services
- Pricing guidance
- Scoring detail
- Alternatives module
- Schema: LocalBusiness (or specialized type)

### 5. Methodology Page
- Criteria + weights
- Process explanation
- Data sources
- Update cadence
- Limitations acknowledged
- Transparency commitment

### 6. Utility Pages
- About (mission, team, monetization)
- Editorial policy (standards, ethics)
- How we rank (global principles)
- Contact (form + email)
- Corrections (accuracy policy)

## Scalability

### Adding New Niches
1. Create `/[new-niche]/` folder
2. Build hub page following template
3. Create methodology page
4. Add city pages (5 minimum to launch)
5. Create type pages as needed
6. Update homepage
7. Add to sitemap

### Adding New Cities
1. Research local market (30-50 providers)
2. Evaluate using criteria
3. Create `/[niche]/[city]/index.html`
4. Update niche hub
5. Add to sitemap
6. Build 3-5 listing pages for top providers

### Adding New Listings
1. Verify eligibility (2 years, 5 projects)
2. Evaluate using scoring rubric
3. Create `/[niche]/listings/[slug]/index.html`
4. Link from city ranking page
5. Add to sitemap

## Quality Gates

### Before Publishing Any Page
- [ ] Minimum word count met
- [ ] Title tag optimized (<60 chars)
- [ ] Meta description written
- [ ] H1-H6 hierarchy correct
- [ ] Schema markup added
- [ ] Canonical tag present
- [ ] Breadcrumbs implemented
- [ ] Internal links added (min 3)
- [ ] Last updated date included
- [ ] No keyword stuffing
- [ ] Fact-checked
- [ ] Added to sitemap

## Future Enhancements

### Phase 2 (Q1 2026)
- HTML sitemap page
- Changelog/update log page
- Privacy policy + Terms
- Search functionality
- Filter/sort on ranking tables
- More cities (15 total)
- 2 more niches

### Phase 3 (Q2 2026)
- Author bylines + bios
- "Why trust us" expanded
- Data visualizations (charts)
- User feedback mechanism
- Related content algorithm
- Performance optimization

### Phase 4 (Q3 2026)
- International expansion
- Multi-language support
- Advanced filters
- Comparison tools
- Email newsletter
- API for data access

## Maintenance Schedule

- **Daily:** Monitor for broken links, check form submissions
- **Weekly:** Review analytics, check Core Web Vitals
- **Monthly:** Update pricing estimates, check for closed businesses
- **Quarterly:** Full ranking reviews, methodology refinement
- **Annually:** Complete site audit, strategy review

## Tech Stack

- **Frontend:** Pure HTML5, CSS3, vanilla JavaScript
- **No frameworks:** Fast, simple, easy to maintain
- **No build process:** Direct deployment
- **Future backend:** Node.js/Python for forms, dynamic content

## Deployment

1. Host on fast server (Netlify, Vercel, or traditional host)
2. Enable HTTPS (required for SEO)
3. Set up redirects (if needed)
4. Submit sitemaps to Google Search Console
5. Monitor indexation
6. Track rankings and traffic

---

## Contact & Credits

Built following Google's E-E-A-T guidelines and modern SEO best practices. No black-hat techniques, no doorway pages, no spam. Pure helpful content.

