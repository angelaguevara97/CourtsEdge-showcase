# CourtsEdge — Sports Analytics Product Showcase

A case study of an independent personal application built through AI-assisted development, demonstrating business analysis, product requirements, API workflows, and data validation.

**Status:** Public showcase under construction. The original application and its production source code remain private.

## The Problem

Sports analysis often requires switching between multiple sources to review recent performance, matchups, player availability, and odds. Differences in identifiers, update times, and available history can make comparisons difficult.

I created CourtsEdge to bring these analytical workflows into one application, with attention to the context and limitations behind the numbers.

## My Role

I defined the product requirements, analytical rules, user workflows, interface behavior, and edge cases. I used ChatGPT, Codex, and Gemini to assist with implementation and troubleshooting.

My contributions included:

- Translating analytical questions into feature requirements
- Defining recent-game and player-versus-team comparisons
- Specifying historical hit-rate calculations and sample-size displays
- Designing data-refresh behavior around freshness and API limits
- Reviewing outputs and identifying unexpected behavior
- Iterating on the interface and analytical workflows

This is a personal project, separate from my professional employment. AI-assisted implementation is part of the development process; this project does not represent professional machine-learning engineering experience.

## Application Scope

The private application includes workflows for:

- Basketball and football performance analysis
- Recent-game and historical matchup comparisons
- Player statistics, odds, and alternate-line analysis
- Injury and player-availability information
- Sportsbook selection and multi-selection analysis
- Recurring data retrieval and refresh controls
- Reviewing historical results

These features provide the context for this case study. Public examples will use fictional players, teams, and synthetic records.

## Public Showcase Scope

This repository is being built to demonstrate:

1. **Problem:** Define the analytical need and user requirements.
2. **Architecture:** Explain how retrieval, normalization, validation, and presentation connect.
3. **Data:** Use synthetic records with documented fields and assumptions.
4. **Workflow:** Show how a user moves from a question to an analytical result.
5. **Analysis:** Demonstrate representative calculations with clear denominators.
6. **Validation:** Check duplicates, missing values, sample sizes, and freshness.
7. **Result:** Present reproducible sample findings and explain their limitations.

## Analytical Principles

- Historical hit rates describe the selected sample; they are not calibrated forecasts.
- Missing statistics must not automatically become zero.
- Duplicate records must not inflate sample sizes.
- Comparisons must use consistent players, markets, units, and time windows.
- Small samples and stale data should be visible to the user.
- Data available after an event begins must not be presented as pre-event evidence.

## Publication Boundaries

The public showcase will contain independently created documentation and synthetic examples.

It excludes production source code, credentials, API keys, private databases, provider data exports, scraped historical datasets, and third-party logos or graphics.

Public examples are illustrative and should not be interpreted as an exact reproduction of the private implementation.

## About

Created by **Angel Guevara** as an independent personal project.

CourtsEdge is not affiliated with or endorsed by any sports league, team, sportsbook, or data provider.
