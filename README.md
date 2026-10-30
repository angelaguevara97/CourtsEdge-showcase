# CourtsEdge — Sports Analytics Product Showcase

A public case study of an independent NBA/NFL analytics application built through AI-assisted development. CourtsEdge connects historical performance, matchup exploration, sportsbook markets, configurable parlay generation, and automated results tracking, with an experimental probability-modeling beta.

**Status:** The private application is working, with Probability Test under active beta development. This public showcase includes feature guides, architecture documentation, and a runnable synthetic Python example. Production source code and underlying datasets remain private.

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

## Explore the Application

| Guide | Coverage |
| --- | --- |
| [Game Feed](docs/game-feed.md) | Matchups, player statistics, visual signals, and contextual navigation |
| [Dive Deeper](docs/dive-deeper.md) | Streaks, following-game outcomes, opponent history, and simulations |
| [Parlay Lab](docs/parlay-lab.md) | Historical strategies, sportsbook markets, alternate lines, and leg replacement |
| [Probability Test — BETA](docs/probability-test.md) | Experimental probabilities, market comparisons, and evaluation methodology |
| [Results Tracking and Winners](docs/results-tracking.md) | Saved tickets, X-factor snapshots, grading, and outcome records |
| [Architecture](docs/architecture.md) | Shared server data, refresh schedules, and provider quota management |

The guides describe the private application. The runnable public example uses fictional records and demonstrates a separate historical calculation.

## Analytical Principles

- Historical hit rates describe the selected sample; they are not calibrated forecasts.
- Missing statistics must not automatically become zero.
- Duplicate records must not inflate sample sizes.
- Comparisons must use consistent players, markets, units, and time windows.
- Small samples and stale data should be visible to the user.
- Data available after an event begins must not be presented as pre-event evidence.

## Publication Boundaries

The public showcase contains independently created documentation and synthetic examples.

It excludes production source code, credentials, API keys, private databases, provider data exports, scraped historical datasets, and third-party logos or graphics.

Public examples are illustrative and should not be interpreted as an exact reproduction of the private implementation.

## Game Feed and Visual Signals

The Game Feed brings NBA/NFL matchups, player statistics, recent averages, injuries, and historical signals into one interface.

Interactive Hot, Cold, and opponent-specific indicators connect users to the relevant Dive Deeper analysis. Explanatory labels clarify team streaks, touchdown history, limited samples, and NFL weather context.

[Explore the Game Feed and visual signals](docs/game-feed.md)

## Dive Deeper

Dive Deeper connects interactive game-feed indicators with the analysis behind them. Selecting a player’s Hot, Cold, or opponent-specific signal opens the relevant matchup context and historical evidence.

Users can inspect recent games, comparable streaks, following-game outcomes, opponent history, and sample sizes. NBA and NFL analysis also includes injuries, matchup context, player and game simulations, and NFL positional defense and workload adjustments.

The private application retrieves data from the server. Historical observations and simulated estimates remain clearly distinguished.

[Explore Dive Deeper analysis and game feed integration](docs/dive-deeper.md)

## Parlay Lab

The private application includes an NBA/NFL Parlay Lab that combines historical player performance with available sportsbook markets.

Users can select a sportsbook, choose a single-game or multi-game combination, apply a historical analysis strategy, replace individual legs, and open a matched sportsbook ticket for review.

The workflow uses shared API data, scheduled refreshes, targeted updates near game time, and a globally limited manual refresh fallback. Historical hit rates describe past observations, not the probability that a generated parlay will win.

[Explore the Parlay Lab workflow and design](docs/parlay-lab.md)

## Probability Test — BETA

Probability Test is a working experimental NBA/NFL modeling feature that combines current-season performance, recent form, usage, matchup context, and sportsbook thresholds to estimate event probabilities.

It distinguishes historical hit rates, model estimates, market-implied probabilities, fair odds, and estimated edge.

Its evaluation framework centers on pregame prediction snapshots, postgame grading, calibration, and model-version comparisons. Calibration improvements and automated evaluation metrics remain ongoing development work. No validated accuracy or profitability is claimed.

[Explore Probability Test and its evaluation workflow](docs/probability-test.md)

## Results Tracking and Winners

Finalized parlays are saved with their selections, sportsbook, strategy, original thresholds, and available generation-time analytical context.

Automated postgame grading evaluates individual legs and complete tickets. Qualifying finalized wins appear in Winners, while the broader results records support evaluation.

X-factor snapshots preserve signals such as Hot status, opponent history, streak continuation, defensive context, historical samples, and applicable Probability Test outputs. These records provide a foundation for investigating which factors contribute predictive value.

[Explore saved parlays, grading, and X-factor tracking](docs/results-tracking.md)

## Architecture and Shared Data

CourtsEdge uses shared server data to connect historical analysis, matchup exploration, sportsbook markets, and postgame grading.

Broad scheduled refreshes, targeted updates near game time, and a globally limited manual fallback coordinate retrieval within provider quotas.

[Explore the architecture and shared data workflows](docs/architecture.md)

## Run the Sample Analysis

Parlay Lab belongs to the private application. The public Python sample below demonstrates a separate synthetic historical calculation.

Requires Python 3. No external packages or API credentials are needed.

Download and extract this repository, open a terminal in the extracted folder, and run:

```bash
python3 analysis/hit_rate.py
```

Expected output:

```text
Source rows: 7
Identical duplicates removed: 1
Selected games: 6 of 6 requested
Games above 20.5: 4 of 6
Historical hit rate: 66.7%
Synthetic historical sample; not a prediction.
```

The sample contains seven fictional records, including one intentional duplicate. The script removes the identical duplicate before selecting the six-game window.

Without duplicate removal, counting all seven rows would incorrectly produce 5 of 7 (71.4%). The correct six-game result is 4 of 6 (66.7%).

Conflicting duplicate records and invalid selected values stop the calculation for review.

### Explore the Evidence

- [Workflow, design decisions, and acceptance criteria](docs/workflow.md)
- [Synthetic sample dataset](data/synthetic_player_games.csv)
- [Python analysis script](analysis/hit_rate.py)
- [Product requirements and acceptance examples](docs/product-requirements.md)

### Verification and Limitations

The following checks were run successfully on macOS:

| Check | Observed result |
|---|---|
| Baseline dataset with one identical duplicate | Removed the duplicate; returned 4 of 6 games (66.7%) |
| Conflicting point totals for the same player/game/statistic | Stopped with a review-required error |
| Missing statistic in a selected game | Stopped with a review-required error; produced no percentage |

The two error checks used temporary CSV copies. The original sample dataset was unchanged. These checks cover the listed scenarios, not every acceptance criterion in the workflow document.

This script demonstrates a historical calculation and basic validation. It does not retrieve live data, enforce API limits, check freshness, or predict future performance.

## About

Created by **Angel Guevara** as an independent personal project.

CourtsEdge is not affiliated with or endorsed by any sports league, team, sportsbook, or data provider.
