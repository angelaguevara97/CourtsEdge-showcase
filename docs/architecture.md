# CourtsEdge Architecture and Shared Data

CourtsEdge connects NBA and NFL data retrieval, historical analysis, interactive exploration, sportsbook market matching, grounded LLM explanations, and saved-result grading.

This guide describes the application at a functional level. Production source code, credentials, prompts, and underlying datasets remain private. The public repository contains documentation and a separate runnable synthetic analysis example.

## Server and Interface

The private application retrieves data and analytical results from the server for presentation in the beta interface.

Moving data retrieval and application logic to the server reduces the amount of implementation and underlying data delivered to testers' browsers.

Information displayed in a browser can still be inspected or copied. Server-side processing protects private implementation details; it does not make displayed information inaccessible.

The Gemini credential used by Arian AI is handled server-side rather than being intentionally exposed to the browser or public repository.

## Design for Additional Sports

CourtsEdge currently supports NBA and NFL workflows. Its underlying application structure is designed to accommodate additional sports, including NHL, MLB, and MLS.

Shared concepts include game selection, player and team identity, historical comparisons, contextual navigation, market matching, prediction snapshots, LLM explanation context, and result grading.

Each additional sport requires its own data integration, statistical categories, analytical rules, market definitions, and grading behavior. The shared structure provides a foundation for expansion; it does not imply that NBA or NFL modeling assumptions transfer directly to other sports.

NHL, MLB, and MLS are expansion targets rather than currently supported application features.

## Shared Data Across Features

Sports statistics, game information, sportsbook markets, and relevant contextual data support multiple application features.

The same player and matchup context connects the Game Feed, Dive Deeper, Parlay Lab, simulations, Probability Test, and Arian AI explanations.

Saved selections then connect pregame analysis with postgame results.

The following diagram shows functional relationships rather than a database schema or deployment topology.

```mermaid
flowchart TD
    A["Sports and market providers"] --> B["Server retrieval and shared data"]
    B --> C["Historical and matchup analysis"]
    C --> D["Game Feed and Dive Deeper"]
    B --> E["Parlay Lab"]
    C --> E
    B --> F["Probability Test BETA"]
    C --> F
    E --> K["Selected leg + supporting context"]
    F --> K
    K --> L["Server-side Arian context builder"]
    L --> M["Gemini LLM"]
    M --> N["Grounded explanation"]
    E --> G["Saved pregame records"]
    F --> G
    B --> H["Postgame grading"]
    G --> H
    H --> I["Winners display"]
    H --> J["Results and evaluation"]
```

Users can open features directly. The diagram does not imply that every user must follow one fixed sequence.

## Deterministic Analysis and LLM Interpretation

Arian AI is intentionally downstream of CourtsEdge's analytical workflows.

Parlay Lab continues to qualify selections through its documented historical rules. Probability Test continues to produce its experimental quantitative outputs through its documented model methodology. Arian receives selected supporting context after those calculations exist and uses Gemini to explain the evidence in natural language.

This separation supports a useful rule for the architecture:

> **CourtsEdge calculates; Arian interprets.**

The LLM is not the source of historical hit rates, Probability Test estimates, fair odds, market-implied probabilities, edge calculations, or postgame grades.

[Read the Arian AI design guide](arian-ai.md)

## Shared Refresh Architecture

CourtsEdge combines automated background refreshes with browser-based refresh loops that run while the page remains open. Both update shared server data used by visitors.

Broad refreshes, targeted updates near game time, and a globally limited manual fallback work together to maintain available sportsbook data within provider quotas.

The documented schedule is:

| Process | Schedule or limit | Purpose |
| --- | --- | --- |
| Broad props refresh | Midnight and noon Eastern | Refresh markets across games |
| Additional Sunday refreshes | 11 a.m., 1 p.m., 3 p.m., and 7 p.m. Eastern | Refresh around Sunday game windows |
| Targeted update process | Every minute, up to 12 props per run | Prioritize games approaching their start |
| Refresh All Props | Shared limit of twice daily | Manual fallback available to users |

The targeted batch size is not a claim that every market refreshes every minute.

A manual refresh updates shared data for users. Its allowance is global rather than a separate allowance for each person.

## Availability and Freshness

Sportsbook markets become available at different times. A later-week game may have limited props early in the week and more markets closer to its start.

Refreshing can retrieve published markets; it cannot create a market that a provider has not supplied.

Quote age and update timestamps help users distinguish saved data from current sportsbook availability. Scheduled retrieval does not guarantee that every stored price matches a sportsbook at every moment.

LLM commentary inherits the limitations of the supporting context it receives. A fluent explanation does not make stale, missing, or limited data more reliable.

## Matching Context Across Sources

Analytical workflows connect players, teams, games, statistical categories, and sportsbook markets.

Market identity includes the sportsbook, event, player, category, side, and threshold. Different thresholds represent different events even when the player and statistical category match.

The exact provider mappings, internal storage schema, and production LLM context schema are implementation details outside this public guide.

## Game Eligibility and Results

Game status affects how information is used.

Before a game starts, eligible markets can support generation and replacement selections.

Once the game starts, it is excluded from new pregame generation. Previously saved selections remain available for subsequent grading.

After results are finalized, the grading process compares actual performance with the stored selection and threshold.

## Preserving Prediction Context

Saved records connect selections with their original sportsbook, strategy, thresholds, and available analytical context.

Later games, changing prices, or updated averages must not silently replace the original prediction context.

The results guide explains finalized-ticket save boundaries, X-factor snapshots, grading, and the distinction between Winners presentation and complete performance evaluation.

## Experimental Evaluation

Probability Test remains an active beta.

Its experimental estimates share relevant application data while remaining distinct from observed historical frequencies and from Arian's generated commentary.

Calibration improvements, automated evaluation metrics, and model comparisons remain ongoing work. The presence of a data pipeline, LLM integration, or saved predictions does not itself establish predictive validity.

## Related Guides

- [Parlay Lab](parlay-lab.md)
- [Dive Deeper](dive-deeper.md)
- [Probability Test BETA](probability-test.md)
- [Arian AI](arian-ai.md)
- [Results Tracking and Winners](results-tracking.md)
