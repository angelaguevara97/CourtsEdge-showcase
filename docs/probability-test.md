# Probability Test — BETA

Probability Test is CourtsEdge's working experimental NBA/NFL probability environment.

The current implementation, Probability Model v2 · 2026 baseline, estimates threshold outcomes from eligible 2026 game results, compares those estimates with sportsbook prices, saves predictions before games, and grades available results.

The beta includes individual-prop testing, experimental parlay construction, saved prediction records, an evaluation dashboard, and optional Arian AI commentary grounded in existing supporting context.

Model estimates remain experimental. The application does not place wagers, and no validated predictive advantage or profitability is claimed.

## Current Model Methodology

The current estimate is:

Probability = (threshold hits + 1) / (eligible games + 2)

This smoothing prevents a perfect historical sample from becoming a 100% estimate.

For example, five hits in five eligible games produces:

6 / 7 = 85.7%

This is a model estimate derived from historical counts, not a calibrated guarantee for the next game.

The displayed 2026 average comes from the same eligible observations. It provides context and is not counted again as an independent probability signal.

The current model does not apply separate recent-game weighting, opponent, injury, usage, home/away, or environmental adjustments.

## Arian AI and the Quantitative Model

Arian AI is separate from Probability Model v2.

The stored probability estimate, fair odds, market-implied probability, estimated edge, EV calculation, and postgame grade are produced by CourtsEdge's documented quantitative workflow. Gemini does not generate or replace those values.

For an existing selection, Arian can receive relevant supporting context already available to CourtsEdge and explain factors that strengthen, weaken, or limit the case in natural language. This creates an interpretation layer without making the LLM the underlying probability model.

The distinction matters for reproducibility: the quantitative calculation can be inspected independently of how an LLM phrases its explanation.

[Read the Arian AI design guide](arian-ai.md)

## Eligible Historical Data

NFL analysis uses the 2026 season, excluding prior-season playoff games played in January 2026.

NBA analysis uses official games dated in calendar year 2026. This is a calendar-year definition rather than an NBA season definition.

Preseason and future games are excluded. The model does not backfill older periods to meet its minimum sample.

At least five eligible games are required for individual props and both parlay types.

## Confidence and Evidence

Samples below 15 games remain Low confidence.

Older quote and history timestamps can lower confidence without changing the underlying probability estimate.

The evidence panel exposes the calculation, eligible sample, historical period, limitations, and odds timestamp.

An evidence score describes the system's evidence assessment. It is distinct from event probability and is not a statistical confidence interval.

## User Workflow

Users select NBA or NFL, choose SGP or multi-game Parlay, and select Conservative, Balanced, or Longshot.

In SGP mode, users select the game.

Available standard and alternate lines are considered together. No fixed mixture is required, and unavailable thresholds or prices are not invented.

Build & save creates a two- or three-leg experimental combination at one sportsbook when sufficient candidates qualify.

Test available props saves individual predictions without requiring a parlay. Reload saved results retrieves the stored evaluation records.

## Threshold and Market Identity

Each prediction identifies the player, game, market, side, threshold, sportsbook, and quoted price.

Over an integer threshold means strictly greater than that value. An N+ selection means at least N.

Alternate thresholds are evaluated separately.

The tested-prop explorer supports filtering by player, game, sportsbook, or prop. A test retains up to 200 predictions ranked by estimated edge.

## Outputs and Market Comparison

The interface distinguishes:

| Output | Meaning |
| --- | --- |
| Historical hits | Qualifying outcomes divided by eligible observations |
| Estimated probability | Smoothed threshold estimate from the current model |
| Fair odds | Theoretical odds corresponding to the estimated win probability |
| Market implied probability | Probability derived from the recorded sportsbook price |
| Edge | Model probability minus market implied probability, in percentage points |
| EV per $1 | Model-based expected net return using the quoted price |
| Confidence | Assessment of sample and data conditions |

Raw market implied probabilities include bookmaker margin.

The Top probability edges view requires at least five eligible games, estimated probability of at least 60%, edge of at least three percentage points, and positive estimated EV.

These are selection criteria, not evidence that the model has a validated advantage.

For integer-line markets, the displayed fair odds correspond to win probability and are not push-adjusted break-even odds.

## Combination Estimates

Same-game selections are not treated as automatically independent.

Within each game, the model uses a Fréchet lower bound as a conservative joint-outcome scenario:

Maximum of zero and:
sum of individual probabilities − (number of legs − 1)

This is a mathematical bound given the marginal estimates, not an empirically fitted correlation model. Its usefulness still depends on the quality of those estimates.

Across games, independence remains an assumption.

## Pregame Prediction Records

Generated tests save prediction records before the associated games begin.

Stored records expose the save timestamp, model version, selection, probability, recorded odds, sportsbook, result, and parlay association.

Prediction values remain unchanged during grading. Saved predictions from earlier model versions retain their original estimates and version identity.

A stored timestamp helps establish prediction timing. It does not by itself prove that historical features were free from leakage or that the evaluation sample is independent.

## Grading and Results Dashboard

Grading reuses finalized box scores and settled outcomes already cached by CourtsEdge. It does not require new result requests for this grading workflow.

Unavailable statistics remain pending. Pushes are reported separately.

The dashboard displays:

- Predictions saved and tested
- Wins, losses, and pushes
- Resolved hit rate
- Average estimated probability across saved records
- Simulated single-selection ROI
- Complete parlays won versus resolved
- Separate SGP and multi-game results
- Breakdowns by model version, sport, and prop type
- Probability-range calibration summaries
- Individual saved prediction records

The displayed dashboard covers the latest 2,000 records.

Repeated tests count separately and are not independent trials. Multiple sportsbook quotes or thresholds can also refer to the same underlying player outcome.

## Calibration Interpretation

Probability buckets compare average estimates with observed win frequency and sample counts.

The current calibration table treats pushes as non-wins, as stated in its heading. That convention must remain explicit when interpreting the figures.

Average probability across all saved predictions includes unresolved records. It should not be compared directly with resolved hit rate as though both describe the same sample.

Calibration summaries support investigation. Small, repeated, or concentrated samples do not establish general calibration.

## Simulated Returns

Single-selection ROI uses a flat hypothetical $1 stake and the recorded individual odds.

This is a paper calculation, not verified betting-account performance.

Parlay ROI requires an actual recorded combined price. It remains unavailable when that price was not saved rather than substituting a multiplied approximation.

## Evaluation and Development

Existing dashboard summaries provide an initial evaluation framework.

Further work includes:

- Brier Score and log-loss tracking
- Chronological and walk-forward validation
- Duplicate-aware evaluation and uncertainty estimates
- Comparisons against simple historical and market baselines
- Controlled model-version comparisons
- Research into additional contextual features
- Empirically evaluated dependence modeling

Opponent, injury, workload, and environmental adjustments are potential extensions rather than inputs to the current v2 baseline.

## Relationship to Other Features

[Dive Deeper](dive-deeper.md) provides broader historical and matchup exploration. Its available contextual information should not be confused with inputs used by this probability model.

[Parlay Lab](parlay-lab.md) retains its separate historical qualification strategies.

[Arian AI](arian-ai.md) explains supporting context without replacing this quantitative methodology.

[Results Tracking](results-tracking.md) explains the broader saved-ticket and grading lifecycle.

## Limitations

Small samples, repeated outcomes, stale prices, provider coverage, and changing player roles limit interpretation.

Smoothing avoids certainty from a perfect sample but does not establish predictive validity.

The current baseline does not adjust for several factors that can influence upcoming performance. Its same-game bound is not a learned correlation model, and cross-game independence remains an assumption.

LLM commentary does not establish predictive validity either. A fluent explanation can still reflect limited or stale supporting evidence.

Dashboard results are preliminary operational observations rather than validated accuracy or profitability claims.

## My Contribution

I defined the workflows, analytical requirements, evidence displays, prediction-record behavior, evaluation goals, and the boundaries between deterministic model outputs and Arian's LLM commentary, using AI-assisted development to implement and refine the beta.
