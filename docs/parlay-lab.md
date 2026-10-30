# Parlay Lab

Parlay Lab is the configurable selection and analysis workflow in the private CourtsEdge NBA/NFL application. It combines historical player performance with available sportsbook markets, user-selected strategies, editable combinations, and an external sportsbook ticket handoff.

This document describes the private application's functionality. The public showcase contains documentation and a separate synthetic analysis example; it does not include the production generator or live sportsbook integrations.

## User Workflow

1. Select a supported sportsbook or CourtEdge analysis-only mode.
2. Choose Same Game Parlay (SGP) or a multi-game parlay.
3. Select NBA or NFL.
4. For SGP, choose one upcoming game from a list ordered by date and time.
5. Select the number of legs and an analysis approach.
6. Generate and review the selections.
7. Replace individual legs, edit the combination, or regenerate it.
8. Where supported, open a sportsbook ticket for final review.

Standard multi-game generation supports 2–6 legs. SGP selections remain within the chosen matchup.

## Historical Analysis

Standard historical analysis uses the player's last 20 relevant games, which may cross seasons. The separate 2026 mode uses the available current-season sample without adding previous-season games to reach 20 observations.

Historical frequency is calculated against the specific condition being evaluated. For example, exceeding 49.5 receiving yards in 18 of 20 games produces a 90% historical hit rate for that threshold.

Available approaches include historical consistency tiers, season-only analysis, history versus price, longer odds, and touchdown-focused selections. “Feeling lucky?” provides a more aggressive combination mode using historical qualification rules for individual legs.

Historical hit rates describe past observations. They are not predicted win probabilities for individual selections or complete parlays. Strategy thresholds and sample sizes must be interpreted together.

## Strategy Rules and Game Windows

Standard generation supports two through six legs. Feeling Lucky builds a 10–14-leg combination.

NBA generation uses today's upcoming games. NFL SGP and multi-game generation use the next seven days. Feeling Lucky can combine NBA games scheduled today with NFL games through Sunday of the current Monday–Sunday week.

Games that have already started are excluded.

| Approach | Qualification |
| --- | --- |
| 90%+ historical hits | At least 15 relevant appearances, at least 90% hits across the selected sample and last 10, and negative individual odds |
| 80% Historical Hit Rate | At least 15 relevant appearances, at least 80% hits across the selected sample and last 10, and negative individual odds |
| 66.7% historical odds 2026 | At least five recorded 2026 regular-season games and 66.7–100% hits at the exact offered threshold |
| Longer odds | 50–75% historical hits, with individual odds capped at +300 |
| Feeling Lucky | Non-touchdown legs use 50–75% historical hits and a +300 individual price cap; scorer-touchdown legs use 50–100% historical hits |
| History versus price | Weighs historical results against the available price |

Historical strategies use up to the last 20 relevant games. Minimum sample and recent-consistency requirements depend on the approach.

Unqualified slots remain empty. In the 90% approach, users can explicitly request optional favorite fills requiring at least 70% historical hits across both comparison samples and negative odds. These selections are labeled below the 90% standard.

### NFL Touchdown Approaches

Anytime TD scorers uses rushing or receiving touchdowns, with at least five recorded appearances and a touchdown in the last five appearances or a previous opponent meeting.

Any Time Touchdowns Longer Odds evaluates offered 1+, 2+, or 3+ scorer-touchdown thresholds, requiring 50–75% historical hits at the exact threshold across at least five recorded appearances.

Quarterback rushing touchdowns count as scorer touchdowns. Passing touchdowns do not.

### Ticket Editing and Display

Users can add legs, remove individual selections, replace a selection through its dropdown, or request a qualifying similar leg near the original odds at the same sportsbook.

Each leg displays its threshold, price, quote age, historical qualifying count, sample size, and comparison average.

Combined odds and the $10 return/profit example are illustrative calculations from individual leg prices. Actual sportsbook combination pricing can differ.

The combined historical estimate multiplies individual historical frequencies under an independence assumption. It is not a calibrated probability that the ticket will win, particularly when selections share a player or game.

## Alternate Lines and Market Matching

The selected sportsbook determines the available market pool when its props have been published.

Matching considers the event, player or team, market, side, and line. Alternate thresholds are separate propositions: performance above 49.5 yards cannot be treated as performance above 72.5 yards.

The ticket integration searches for available matches, including nearby lines when an exact match is unavailable. Users must review the resulting sportsbook selections because a changed line can change the meaning of the original analysis.

The sportsbook options currently exposed in the application are DraftKings, FanDuel, BetMGM, and Caesars. Market coverage and ticket-link availability depend on the provider and sportsbook.

An exact threshold match and a nearest available threshold are distinct outcomes. If the sportsbook ticket uses a different threshold, the original historical rate or model estimate does not automatically apply to that replacement. The matched threshold must be shown explicitly, and analytical values must be recalculated for it or identified as belonging to the original selection.

## Editing and Eligibility

Individual-leg replacement preserves the rest of the ticket while searching for a compatible alternative. Full regeneration rebuilds the combination.

Replacement candidates follow the relevant sport, sportsbook, strategy, historical qualification, and event constraints. SGP replacements remain within the selected game.

Games that have started are excluded from new pregame generation and replacement searches. If qualifying markets are unavailable, the requested combination may not be generated.

## API Refresh and Shared Data

Both automated background refreshes and browser-based refresh loops are active. Background refreshes run independently of an open browser, while browser loops run while the page remains open. Successful updates refresh shared server data for visitors.

Sportsbook props are not always published far in advance. A matchup can exist in the schedule before its player markets become available.

CourtsEdge combines several refresh paths:

- A targeted process runs every minute, updating up to 12 props per run and prioritizing games approaching their start time.
- Broader refreshes cover the eligible slate at midnight and noon Eastern.
- Additional Sunday refreshes run at 11 a.m., 1 p.m., 3 p.m., and 7 p.m. Eastern.
- A shared “Refresh All Props” fallback can be triggered by any user, subject to a global limit of twice daily.

Refreshed data is shared across users. This balances slate coverage and near-start updates against API quotas.

Polling frequency does not guarantee that every prop is current. Quotes carry an age, and sportsbook prices or availability may change before a ticket is opened.

## Sportsbook Handoff

An external API supports sportsbook ticket creation and linking. Users open the resulting ticket in the sportsbook to review selections, current lines, prices, and stake.

CourtsEdge does not submit wagers. Final availability and acceptance are determined by the sportsbook. Region preferences filter sportsbook brands; they do not verify individual markets for a particular state.

## Saved Results

The application supports saved slips, postgame grading, and a Winners display. These features distinguish generated selections from later outcomes.

A Winners display is not a complete performance evaluation. Measuring strategy results requires accounting for all eligible saved tickets, including losses, voids, and unresolved outcomes.

## What This Demonstrates

The project demonstrates requirements definition, historical analysis, API orchestration, market matching, shared caching, request prioritization, exception handling, state management, and user-controlled workflows.

I defined the product behavior and analytical rules, used AI-assisted development to help implement the application, and reviewed outputs and application behavior.
