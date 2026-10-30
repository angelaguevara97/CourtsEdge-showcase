# Dive Deeper

Dive Deeper is the private CourtsEdge application's interactive NBA and NFL analysis environment. It connects signals in the game feed with the historical games, matchup comparisons, and calculations behind them.

The application retrieves analytical data from the server and displays the results in the interface. Production code and underlying datasets remain outside this public showcase repository.

## From Signal to Evidence

The game feed uses visual indicators to summarize player and team performance. These indicators also provide direct entry points into deeper analysis.

Selecting a signal preserves the relevant game, player, team, opponent, and statistical context. Users arrive at the corresponding analysis without reconstructing the search.

Entry points include:

- General player Hot and Cold indicators
- Strong performance against the selected opponent
- Team winning and losing streaks
- Head-to-head matchup streaks
- Recent-average indicators

Dive Deeper remains focused on the selected matchup and its players.

## Hot and Cold Analysis

Expandable Hot and Cold sections explain the statistical conditions behind each classification.

Users can inspect the relevant statistic, threshold, streak length, recent results, and comparison averages.

The analysis goes beyond identifying a current streak. It examines comparable historical conditions and the player's performance in the following game.

This supports questions such as:

- What caused the current signal?
- How long has the pattern lasted?
- Has the player experienced comparable streaks before?
- What happened immediately afterward?
- Did the condition continue or end?

Following-game results provide evidence behind the aggregate continuation frequency.

### Illustrative Example

Suppose a player has scored at least 25 points in five consecutive games.

If six comparable historical instances have an available following game, and the player reached 25 points in four of those games, the historical continuation frequency is:

4 / 6 = 66.7%

This example illustrates the calculation. It is not a measured CourtsEdge performance result or a prediction for the next game.

## Opponent-Specific Analysis

General recent form and performance against a particular opponent are analyzed separately.

Selecting an opponent-specific signal opens the player's history against the team in the selected matchup.

Users can inspect:

- Individual previous meetings
- Statistical averages against that opponent
- Threshold hit counts and sample sizes
- Current opponent-specific streaks
- Following-meeting outcomes after comparable opponent-specific patterns

Team-level head-to-head history adds wins, losses, streaks, and scoring context where available.

First-meeting and limited-history indicators communicate when the relevant matchup sample is absent or small. A first meeting after a team change is distinct from having no career history against an opponent.

## Recent Averages and Game Samples

Selectable recent-game windows, from one through eight games, let users compare immediate performance with a broader recent sample.

Game-by-game results make the observations behind averages and streaks inspectable.

The interface uses expandable sections to reveal detail progressively. Users can investigate a signal without having every statistic displayed at once.

## NBA Analysis

NBA analysis combines player statistics, recent form, opponent history, team matchup information, injuries, and simulations.

Statistical categories include points, three-pointers, field-goal attempts, rebounds, assists, steals, and fouls.

Starting players and bench players remain distinguishable, with expandable bench information supporting deeper roster review.

## NFL Analysis

NFL analysis uses statistics relevant to each player's position, including passing, rushing, receiving, receptions, attempts, and touchdowns.

Opponent defensive comparisons provide position-specific context for quarterbacks, running backs, wide receivers, and tight ends. Rankings are accompanied by the available game sample.

Common-opponent analysis compares results against teams both sides have faced. These comparisons provide historical context and remain separate from simulation probabilities.

Position-specific team defense does not establish which individual defender will cover a particular player.

## Simulations and Workload

Player and game simulations add model-generated estimates alongside observed historical results.

Player analysis incorporates relevant performance and matchup inputs, including recent form, workload, defensive context, and injury information where available.

NFL workload controls allow users to explore assumptions such as carries, targets, and passing attempts.

Game simulations provide matchup estimates such as projected scores, totals, and win probabilities.

Simulation outputs remain distinct from historical averages, observed hit frequencies, and sportsbook implied probabilities.

## Sportsbook Threshold Context

Available sportsbook props connect the analysis to a specific statistical threshold.

Users can compare a proposed line with recent game results, opponent history, streaks, and relevant matchup information.

The threshold matters: performance against one line does not establish the same historical frequency against a different line.

## Relationship to Parlay Lab

Dive Deeper explains the evidence behind a player, statistic, or matchup.

[Parlay Lab](parlay-lab.md) finds and combines qualifying selections from available sportsbook markets.

The features complement each other while serving different analytical purposes.

## Interpretation and Limitations

Historical hit rates describe observed outcomes. Continuation frequencies describe what followed comparable historical conditions. Neither establishes the probability that a future selection or complete parlay will win.

Sample sizes matter, especially for opponent-specific meetings and uncommon streaks. Injuries, roster changes, workload, and data freshness can affect how useful a historical comparison is.

The public Python sample in this repository demonstrates a separate synthetic historical calculation. It does not reproduce the private Dive Deeper system.

## What This Demonstrates

This feature demonstrates product requirements, contextual navigation, historical sequence analysis, opponent comparisons, configurable averages, simulation integration, server-based data retrieval, and explainable presentation of analytical results.

I defined the workflows, analytical requirements, and interface behavior, using AI-assisted development to implement and refine the application.
