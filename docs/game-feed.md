# Game Feed and Visual Signals

The Game Feed is CourtsEdge's entry point for exploring NBA and NFL matchups.

It brings game information, player statistics, recent performance, matchup history, injuries, and available sportsbook context into one interface.

Visual indicators summarize analytical conditions. Relevant interactive signals connect users directly to the evidence in Dive Deeper.

## Game and Player Context

Users select a sport and game to explore the corresponding teams and players.

NBA views distinguish the starting five from expandable bench information. Statistical categories include points, three-pointers, field-goal attempts, rebounds, assists, steals, and fouls.

NFL views use position-relevant statistics, including passing, rushing, receiving, receptions, attempts, and touchdowns.

Selectable recent-game windows from one through eight games support comparisons across different recent samples.

## Date and Game Selection

Users can browse the next seven days, select Today or Tomorrow, or choose a specific date.

Matchup cards show the teams, scheduled start time, game status, and NFL week. Selecting a card opens the corresponding matchup analysis.

Shared-data controls let users reload available server data. The interface also displays refresh timing and provides the globally limited Refresh All Props fallback.

## Position and Opponent Filters

NFL player tables are organized by position, including quarterback, running back, wide receiver, tight end, and kicker.

Position filters narrow the displayed players. An opponent-sample selector controls the historical comparison sample.

Player statistics show the available opponent-game count alongside the comparison average. Season averages remain visible for context, and expandable bench sections provide additional roster detail.

## Shared-Opponent Comparisons

Users can select a shared opponent to compare how both teams performed against that team.

The selected comparison updates the relevant historical scores and player averages. Sportsbook odds and defensive simulations remain tied to the scheduled matchup rather than switching to the historical comparison opponent.

A separate Common Opponents section supports season-range and statistical-category selection. It displays shared-opponent counts, opponent-season comparisons, team game counts, production differences, and expandable scores and dates.

Comparison estimates summarize historical evidence. They are not calibrated win probabilities.

## Market Availability

The feed displays moneyline, spread, total, and available player props with sportsbook names, thresholds, and prices.

Player markets appear alongside the relevant statistical categories. When a line has not been supplied, the interface can display “Awaiting published lines.”

Anytime touchdown statistics count rushing or receiving touchdowns. Passing touchdowns remain a separate category.

## Visual Signal Reference

Users can hover over or tap an emoji to see its explanation. Meaning depends on whether the indicator accompanies a team, player, or matchup.

| Indicator | Meaning |
| --- | --- |
| 🔥 Team winning streak | Consecutive team wins |
| Blue fire — opponent streak | Consecutive wins against that opponent |
| ❄️ Team losing streak | Consecutive team losses |
| 🔥 / 🧊 Player Hot or Cold | Performance above or below the player's comparison average |
| 🔥 NFL touchdowns | Player touchdown streak |
| Blue fire — NFL touchdowns | Touchdown history against the opponent |
| 🔔 New-team matchup | First recorded meeting with the opponent since changing teams |
| ❗ Limited history | Fewer games available for the displayed average |
| 🏆 Key player | Top performer from a past win |
| 🌡️ Temperature | Historical averages in similar temperatures, NFL only |
| 🌧️ / 🌨️ Rain or snow | Historical averages in matching weather, NFL only |
| Mixed precipitation / ice | Sleet or freezing-rain forecast flag |
| 🏟️ Indoor or covered | Outdoor weather comparisons do not apply, or roof status is unknown |

These indicators summarize historical observations or contextual conditions. They do not independently establish future probabilities.

## From Signal to Dive Deeper

Selecting an interactive analytical signal preserves the relevant player, game, opponent, and statistical context.

For example, selecting a player's Hot indicator opens the corresponding analysis of recent performance, the current streak, comparable historical conditions, and following-game outcomes.

An opponent-specific signal opens the relevant player-versus-opponent history.

Team streaks and head-to-head analysis provide team-level context alongside individual player information.

[Explore Dive Deeper](dive-deeper.md)

## Matchup Context

The feed connects recent performance with opponent history, injuries, team streaks, and available market information.

NFL weather indicators add context for outdoor games. Historical weather comparisons describe the available observations; they do not establish that weather caused a particular result.

First-meeting and limited-history indicators communicate different limitations. A first recorded meeting after a team change does not necessarily mean the player has never faced that opponent.

## Progressive Disclosure

Expandable sections keep detailed information available without displaying every statistic at once.

Users can begin with the matchup overview, investigate a signal, and then inspect the underlying games and comparisons.

The goal is to make analytical summaries readable while preserving access to their supporting evidence.

## Shared Data and Freshness

The feed retrieves information through the application's server-based data workflow.

Update timestamps and available samples help users interpret the information shown. Provider coverage and refresh timing can affect individual statistics, injury information, and sportsbook markets.

[Explore architecture and shared data](architecture.md)

## What This Demonstrates

The Game Feed demonstrates information hierarchy, contextual navigation, interactive analytical state, sport-specific presentation, and accessible explanations of statistical signals.

I defined the indicators, analytical workflows, and interface requirements, using AI-assisted development to implement and refine the application.
