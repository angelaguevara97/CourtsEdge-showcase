# Saved Parlays, Results Tracking, and Winners

CourtsEdge connects generated parlays with saved pregame records, automated postgame grading, and the user-facing Winners section.

The lifecycle preserves what was selected before the outcome was known:

Generate → Finalize → Snapshot → Grade → Store → Evaluate

Winning finalized tickets feed the Winners display. Losing records remain relevant to strategy evaluation and model development.

Production code and underlying datasets remain private.

## Finalizing a Tracked Ticket

Parlay Lab distinguishes the editable draft from the finalized ticket being tracked.

Users can replace individual legs before finalization. The saved final ticket reflects those changes rather than an abandoned selection.

Final slips save when the user leaves Parlay Lab or requests another parlay. Edits remain in the current draft until that save boundary.

The tracked record preserves the selected sportsbook, strategy, parlay type, individual selections, and relevant pregame context.

Only selections recorded before their associated games begin belong in pregame performance evaluation.

## Pregame Snapshots

A saved ticket preserves the information associated with its generation and finalization.

Relevant ticket-level information includes:

- Ticket identifier and timestamps
- Sport and sportsbook
- SGP or multi-game format
- Selected strategy and leg count
- Combined quoted odds where available
- Generation or model version where applicable
- Grading status and finalization time

Individual leg records connect the player, team, opponent, and game with the selected market, side, threshold, and quoted price.

The original threshold and analytical context remain associated with that prediction. Later sportsbook prices or updated historical averages must not silently replace them.

A saved generated ticket is an analytical record. It does not establish that a user placed a wager or received the quoted price.

## X-Factor Snapshots

The snapshot design preserves more than the final selection and its eventual result.

Generation-time analytical factors provide the evidence needed to investigate why a selection qualified and whether that reasoning remains useful.

Relevant factors include:

| Factor group | Generation-time context |
| --- | --- |
| Historical performance | Hits, sample size, threshold, and historical rate |
| Current season | 2026 hits, available games, and season-only rate |
| Recent form | Recent results, averages, and usage |
| Player signals | Hot, Cold, and Hot-vs-Team status |
| Streaks | Length, continuation frequency, and comparison sample |
| Opponent history | Previous meetings and threshold results |
| Defense | Positional matchup, rank, and available sample |
| Role and availability | Workload, injuries, and starter or bench context |
| Market | Sportsbook, price, threshold, and alternate-line status |
| Probability Test | Model version, probability, implied probability, edge, and confidence where applicable |

Field coverage depends on the selected strategy and available data. Missing context should remain distinguishable from a measured zero or a negative signal.

These factors describe what was available at prediction time. For example, a defensive rank saved before a game should not be replaced by that team's later-season rank.

## Why Preserve the Factors?

With sufficient tracked results, the dataset can support questions such as:

- Do Hot-vs-Team selections perform differently from general Hot selections?
- Does streak continuation add information beyond historical hit rate?
- Does positional defensive context improve estimates?
- How do current-season and last-20-game strategies compare?
- How do alternate-line selections behave at their actual prices?
- Does Probability Test edge correspond with better subsequent outcomes?

These are research questions, not established findings.

Simple group comparisons can reveal associations, but they do not establish that a factor independently improves predictions. Strategies may select different players, thresholds, prices, and markets.

Stronger evaluation requires comparable samples, chronological testing, and model comparisons with and without the factor.

## Automated Postgame Grading

The scheduled grading process checks saved tickets against finalized game results.

For each leg, the grader identifies the associated event and compares the reported result with the original stored market and threshold.

Leg outcomes distinguish:

- Hit
- Miss
- Push
- Void
- Pending or unresolved

A missing result is not automatically a loss. Push and void treatment depends on the applicable market rules.

Complete ticket results are determined from the leg outcomes. A ticket with four successful legs and one failed required leg is a losing parlay, even though its leg hit rate is 80%.

Finalized Winners publication waits for the required results to resolve.

## Winners Display

The Winners section presents qualifying finalized winning tickets, with strategy categories and counters.

Generation time and the date of the last relevant game serve different purposes: one records when the ticket was created, while the other places the completed outcome in time.

Individual selections and their results make each displayed winner inspectable.

Win counters describe the displayed successful records. They do not establish an overall success rate without the corresponding prediction totals and losing outcomes.

## Complete Results and Evaluation

Winners presentation and performance evaluation serve different purposes.

Evaluation requires the full defined tracked dataset, including wins, losses, pushes, voids, and unresolved records.

Useful breakdowns include:

- Strategy
- Sport and market
- Sportsbook
- SGP versus multi-game tickets
- Leg count
- Historical qualification tier
- Model version
- Available X-factors

Leg hit rate and complete-parlay win rate must remain separate.

Repeated appearances of the same player selection across tickets also create dependent observations. They should not be treated as independent evidence when assessing uncertainty.

User-edited finalized tickets describe the performance of that workflow. They should not automatically be presented as the performance of every unedited generator output.

## Record Integrity

Stable ticket identifiers and grading state support repeatable processing without duplicate Winners publication.

Duplicate generation events and repeated identical combinations require an explicit counting policy so they do not inflate performance totals.

When official statistics are corrected, any resulting grade revision should remain traceable while preserving the original prediction context.

The evaluation dataset should document its inclusion rules, save boundaries, duplicate handling, and grading rules.

## Connection to Probability Test

[Probability Test — BETA](probability-test.md) adds experimental model estimates to applicable saved selections.

Preserving the pregame probability, market price, contextual inputs, and model version provides the foundation for later calibration and version comparisons.

Calibration dashboards, automated probability-quality metrics, and controlled X-factor comparisons remain part of the ongoing evaluation work.

A collection of winning tickets alone cannot validate probability estimates.

## Connection to Other Features

[Parlay Lab](parlay-lab.md) constructs and edits qualifying selections.

[Dive Deeper](dive-deeper.md) explains historical and matchup signals.

Results tracking preserves the selected ticket and available context, reconciles it with subsequent outcomes, and provides evidence for future improvements.

## What This Demonstrates

This system demonstrates workflow requirements, prediction persistence, scheduled processing, result reconciliation, analytical record design, and outcome reporting.

I defined the save behavior, grading requirements, strategy context, and evaluation goals, using AI-assisted development to implement and refine the application.

The central principle is to preserve what was selected, when it was selected, what supported it, and what actually happened.
