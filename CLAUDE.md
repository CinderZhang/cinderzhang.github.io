# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is Dr. Cinder Zhang's educational website hosted on GitHub Pages at https://cinderzhang.github.io/. It serves as the main hub for the DRIVER Framework - an AI-integrated approach to finance education. The site is a static HTML/CSS website without a build process or JavaScript framework.

## Architecture

### Core Structure
- **Static Website**: Pure HTML/CSS without JavaScript frameworks or build tools
- **GitHub Pages**: Automatically deployed from the master branch
- **Educational Hub**: Links to separate repositories for individual DRIVER textbooks
- **No Dependencies**: No package.json, npm scripts, or build process

### Key Files
- `index.html`: Main homepage showcasing DRIVER textbooks and framework
- `why-driver.html`: Detailed explanation of the DRIVER philosophy
- `student-portal.html`: Student-focused landing page
- `styles.css`: All website styling
- `404.html`: Custom error page with smart redirects

### Related Repositories
The main textbook content is hosted in separate repositories:
- DRIVER-FinancialManagement
- DRIVER-FinancialModeling  
- DRIVER-EssentialsofInvestment
- DRIVER-Investment-in-depth
- DRIVER-Presentations (separate repo for presentation materials)

## Development Workflow

### Making Changes
Since this is a static site without build tools:
1. Edit HTML/CSS files directly
2. Test changes by opening HTML files locally in a browser
3. Commit and push to master branch
4. Changes automatically deploy to GitHub Pages

### Git Commands
```bash
# View changes
git status
git diff

# Commit changes
git add .
git commit -m "Your commit message"
git push origin master
```

### Testing
- Open HTML files directly in browser for local testing
- No test suite or linting setup currently
- Validate HTML/CSS manually or with online validators

## SEO and Analytics

### Current Setup
- Meta tags and Open Graph data in HTML headers
- Structured data (Schema.org) for search engines
- Google Analytics placeholders (G-XXXXXXXXXX needs replacement)
- sitemap.xml and robots.txt configured

### Pending Tasks
- Replace Google Analytics placeholder IDs with actual measurement ID
- Submit sitemap to Google Search Console after GA setup

## Content Guidelines

### DRIVER Framework
The six-stage learning framework that should be referenced consistently:
- **D**iscover: Frame financial problems systematically (recently updated to "Define & Discover")
- **R**epresent: Visualize cash flows and logic before coding
- **I**mplement: Build solutions with Python and AI as thinking partners
- **V**alidate: Verify results using multiple approaches
- **E**volve: Recognize patterns across different contexts
- **R**eflect: Extract transferable principles for future problems

### Style Conventions
- Professional academic tone
- Emphasis on AI-integrated learning
- Focus on practical finance education
- Copyright notice: "All content is copyright Cinder Zhang"

## Important Notes

- **No Build Process**: This is intentionally a simple static site - don't add npm/webpack/etc.
- **GitHub Pages**: Deployment is automatic from master branch
- **External Content**: Textbook content lives in separate repositories, not here
- **Presentations**: Presentation materials moved to DRIVER-Presentations repository