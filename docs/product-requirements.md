# Product Requirements: Recent-Game Performance Summary

## Purpose and Scope

This is a representative requirements example created for the public CourtsEdge showcase. It documents a recent-game analysis workflow using synthetic data.

It separates behavior demonstrated by the Python sample from proposed interface behavior.

## User Need

As a user reviewing player performance, I want to select a statistic, threshold, and recent-game window so I can see how often the player exceeded that threshold and understand the sample behind the result.

## Example

For fictional player P001:

- Statistic: points
- Threshold: above 20.5
- Window: six most recent completed games with confirmed participation
- Analysis cutoff: October 28, 2026, exclusive

Expected summary:

> Above 20.5 points in 4 of 6 eligible games (66.7%).

The interface should also explain that this is a historical frequency, not a forecast.

## Functional Requirements

| ID | Requirement | Public showcase status |
|---|---|---|
| FR-01 | Identify a player and supported statistic | Implemented through script settings |
| FR-02 | Apply an explicit analysis cutoff | Implemented using game dates |
| FR-03 | Include completed games with confirmed participation | Implemented |
| FR-04 | Remove identical duplicate observations | Implemented and checked |
| FR-05 | Stop calculation when duplicate records conflict | Implemented and checked |
| FR-06 | Select the most recent eligible games before validating statistic values | Implemented |
| FR-07 | Stop calculation when a selected statistic is missing or invalid | Implemented; missing-value scenario checked |
| FR-08 | Display qualifying count, actual sample size, and percentage | Implemented as terminal output |
| FR-09 | Let users change player, threshold, and window through interface controls | Proposed interface behavior |
| FR-10 | Display freshness and incomplete-coverage notices | Proposed interface behavior |

“Implemented” refers to the public sample script, not a claim about the private application's implementation.

## Business Rules

- An observation represents one player, one game, and one statistic.
- “Above” means strictly greater than the threshold.
- Confirmed participation with zero points is a valid observation.
- Nonparticipation does not count as a played game.
- Missing statistics must not become zero.
- Missing selected statistics must not trigger silent replacement with older games.
- If fewer than six eligible games exist, report the actual sample size.
- If no eligible games exist, show insufficient data without a percentage.
- Use the same threshold across the selected historical games.

This example compares historical performance against one selected threshold. It does not evaluate each game's original betting line or historical betting returns.

## Acceptance Examples

### Identical duplicate

Given two identical observations for P001, G004, and points,
when the script prepares the sample,
then G004 counts once.

### Conflicting duplicate

Given point totals of 27 and 30 for the same player/game/statistic,
when the script checks duplicates,
then calculation stops with a review-required error.

### Missing statistic

Given a selected game with a blank points value,
when the script validates the selected window,
then calculation stops without producing a percentage.

### Valid sample

Given the six unique point totals 24, 18, 27, 21, 16, and 23,
when the threshold is above 20.5,
then the result is 4 of 6 games, or 66.7%.

## Design Decision: Stop on Incomplete Data

The public script stops when a selected value is missing. This keeps the example small and prevents an incomplete sample from looking complete.

A future interface could show a partial result with explicit coverage, such as “4 of 5 available observations; coverage 5 of 6 selected games.” That behavior would require separate implementation and validation.

## Known Limits

- Player and analysis settings are edited in code.
- The sample supports one counting statistic and date-based cutoffs.
- It does not reconstruct which records were available at a historical moment.
- It does not connect to live APIs or check data freshness.
- It does not estimate future probabilities.
- Verification currently covers the baseline, conflicting duplicates, and a missing selected value.

## Definition of Done for This Sample

- Synthetic data is available in the repository.
- The script runs without external packages.
- The baseline output matches a manual calculation.
- Conflicting duplicates and missing selected values stop calculation.
- Run instructions and observed checks are documented.
- Proposed behavior is distinguished from implemented behavior.
