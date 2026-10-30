# Probability Test — BETA

Probability Test is CourtsEdge's working experimental probability-modeling environment for NBA and NFL events.

It uses historical performance and current matchup context to generate forward-looking estimates for specific player markets and thresholds.

The central research question is whether those estimates correspond to observed outcomes over time. The evaluation workflow connects pregame prediction snapshots, postgame grading, calibration analysis, and model revisions.

The feature remains under development and evaluation. It is not considered fully calibrated, and no validated profitability or predictive-performance claim is made.

Production code and underlying datasets remain private.

## Why This Feature Exists

Historical frequency and future probability answer different questions.

A player exceeding a threshold in 18 of the last 20 games establishes a 90% historical hit rate. It does not automatically establish a 90% probability for the next game.

The next matchup may involve different usage, injuries, teammates, defensive conditions, or a different sportsbook threshold.

Probability Test explores how those conditions can inform an experimental estimate.

## Relationship to Other Features

[Parlay Lab](parlay-lab.md) uses historical qualification strategies and available sportsbook markets to construct combinations.

[Dive Deeper](dive-deeper.md) explains historical signals through recent games, streaks, opponent comparisons, and matchup context.

Probability Test adds an optional experimental modeling layer. It operates alongside the historical engine without replacing its qualification rules.

## Inputs and Thresholds

The beta combines current-season performance with relevant recent form, player usage, opponent information, positional defense, injuries, and role context.

The 2026-focused analysis keeps current-season observations distinct from the standard historical engine's last-20-game window, which can cross seasons.

NFL inputs concern opportunity and production, including attempts, carries, targets, receptions, yards, and touchdowns where available.

NBA inputs include minutes, attempts, scoring, rebounds, assists, starting status, and lineup context where available.

Feature availability varies by sport, market, and provider coverage. Feature selection and weighting continue to evolve during beta development.

Each estimate applies to a specific player, market, side, and threshold. Over 49.5 receiving yards is a different event from Over 59.5 receiving yards.

## Model and Market Outputs

The following values have separate meanings:

| Output | Meaning |
| --- | --- |
| Historical hit rate | Observed frequency in the selected historical sample |
| Model probability | Experimental estimate for the upcoming event |
| Sportsbook implied probability | Probability derived from the quoted market price |
| Fair odds | Theoretical price corresponding to the model estimate |
| Estimated edge | Model probability minus market-implied probability |
| Confidence | Indicator of estimate quality given data and model conditions |

Raw sportsbook implied probabilities include bookmaker margin. Margin removal remains a development area where suitable market data is available.

Estimated edge is expressed in percentage points. It is not equivalent to expected return or proof of a profitable opportunity.

Confidence is distinct from event probability. Sample size, missing inputs, role changes, and uncertain injury information affect how an estimate should be interpreted.

## Pregame Snapshot and Postgame Grading

The prediction-storage and grading architecture establishes the foundation for evaluating the beta.

A pregame snapshot preserves the prediction and the information associated with it before the event occurs.

Relevant fields include:

- Prediction timestamp and model version
- Sport, game, and player identifiers
- Market, side, and threshold
- Sportsbook and quoted odds
- Historical frequency and sample information
- Model probability and market-implied probability
- Estimated edge and confidence
- Available contextual inputs

The original prediction-time price remains associated with the prediction. A later market price must not replace it retrospectively.

After the game is finalized, the saved selection can be matched with the actual result and graded.

Grading records must distinguish resolved hits and misses from pushes, voids, cancellations, and unavailable results. Unresolved records should remain visible rather than silently disappearing from evaluation.

A pregame timestamp establishes when an estimate was recorded. Strong out-of-sample evaluation additionally requires that model tuning and feature construction exclude future information.

## Calibration and Evaluation

The evaluation objective is to determine whether assigned probabilities match observed frequencies over sufficiently large samples.

For example, events assigned probabilities near 70% should occur approximately 70% of the time across a suitable evaluation sample.

A single successful prediction does not demonstrate calibration. Counting wins alone does not establish the quality of probability estimates.

The evaluation plan includes:

- Probability buckets with prediction counts and observed frequencies
- Mean predicted probability within each bucket
- Brier Score for binary probability error
- Log loss to assess confident incorrect predictions
- Results separated by sport, market, and model version
- Sample sizes and unresolved-result counts

Brier Score averages the squared difference between predicted probability and the binary outcome. Log loss places a stronger penalty on confidently incorrect estimates.

Automated calibration dashboards, Brier Score tracking, and log-loss tracking remain roadmap work. This guide does not present completed measurements for them.

Evaluation should retain losing predictions as well as winners. A promotional Winners view cannot substitute for the complete evaluation dataset.

## Model Versions and Experiment Tracking

The experimental loop is:

1. Generate and save a pregame prediction.
2. Observe and grade the finalized result.
3. Compare predicted probabilities with outcomes.
4. Identify weaknesses by market, sample, or context.
5. Revise the model or its features.
6. Assign a new version and evaluate subsequent predictions.

Model-version comparisons and experiment tracking are being developed so that changes can be assessed without mixing incompatible configurations.

An experiment record should identify the hypothesis, model version, feature changes, evaluation period, results, and decision.

A revision should earn its place through evaluation rather than appearing better solely because it was tuned to previously observed results.

## Chronological Validation

Walk-forward validation is a planned evaluation method.

Under this approach, information available through one period is used to predict the next period. The process then advances chronologically.

This helps prevent later games, postgame injury updates, or season averages containing the predicted game from entering earlier predictions.

Historical data used to develop or tune the model must remain distinguishable from data used to assess its performance.

## SGP and Multi-Game Experiments

Probability Test supports experimentation with same-game and multi-game combinations.

SGP candidates remain tied to the selected matchup. Pregame selection workflows exclude games that have already started.

Individual leg probabilities do not automatically establish a combined parlay probability. Same-game selections can share workload, pace, scoring, and other influences.

Correlation handling remains experimental. Multiplying individual probabilities requires an independence assumption that may be inappropriate for the selected legs.

## Data Architecture

The beta reuses normalized server-side sports and market data within the broader CourtsEdge refresh architecture.

Player, team, event, market, and threshold identifiers connect historical observations, current context, sportsbook quotes, and prediction records.

Shared data retrieval reduces repeated external requests and supports provider quota management.

Missing information must remain distinguishable from a measured zero. Data availability and limited samples are important considerations throughout beta development.

## Current Status and Roadmap

### Working Beta

- Experimental NBA and NFL probability outputs
- Current-season analysis and sportsbook threshold comparisons
- Implied probability, fair odds, and estimated edge
- SGP and multi-game experimentation
- Pregame prediction-storage and postgame evaluation architecture

### In Progress

- Calibration improvements
- Correlation handling
- Confidence criteria and sample protections
- Injury and workload integration
- Model-version comparisons

### Planned Evaluation Extensions

- Automated calibration dashboard
- Brier Score and log-loss tracking
- Walk-forward validation
- Market-specific model comparisons
- Closing-line comparisons
- Distribution-based and correlated simulation research

These are development directions, not completed performance results.

## Known Limitations

Early-season samples, missing usage metrics, uncertain injuries, role changes, provider availability, and sportsbook line movement can affect estimates.

Opponent-specific samples may be small. Historical relationships may change. Correlation modeling and calibration remain unfinished research areas.

No measured accuracy, validated betting edge, or financial return is claimed in this showcase.

## What This Demonstrates

This feature demonstrates probability reasoning, feature requirements, market-price comparisons, data integration, prediction-record design, and the development of an evaluation framework.

I defined the analytical requirements and experimental workflow, using AI-assisted development to implement and refine the beta.

The goal is to build a system whose estimates can be recorded, tested, challenged, and improved.
