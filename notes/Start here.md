# Locus demo

One note, one flowchart and a few files, to show what Locus does. Click any green link to jump to the exact place it cites; hover one for a preview. Press **Tour** to step through every link in order.

## PDF

A page: [the scope (page 6)](/docs/standard.pdf#page=6&at=79fe4364be). A highlighted passage: [Table 1](/docs/standard.pdf#page=18&viewrect=83,120,460,108&at=79fe4364be "Table 1—Minimum Design and Test Factors for Metallic Structures Verification Approach Ultimate Design Factor Yield Design Factor Qualification Test Factor Proof Test Factor Prototype 1.4 1.0* 1.4 N/A "). The same passage in the older edition: [Table 1 in the 2014 edition](/docs/standard.pdf#page=17&viewrect=83,340,460,108&rev=674909f969 "Table 1—Minimum Design and Test Factors for Metallic Structures Verification Approach Ultimate Design Factor Yield Design Factor Qualification Test Factor Proof Test Factor Prototype 1.4 1.0* 1.4 N/A ") (a pinned link, with a date badge). Open the PDF and press **Compare** on its history strip to see both editions side by side.

## Code

[check()](/src/margins.py#L12&at=79fe4364be "def check(cases, parts):") is a live link: lines were added above it after this note was written, and Locus follows them. [margin()](/src/margins.py#L7-L9&at=79fe4364be "def margin(allowable, load, factor=FACTORS[\"ultimate\"]): \"\"\"Margin of safety: allowable / (load x factor) - 1.\"\"\" return allowable / (load * factor) - 1") shows **changed** because its lines were edited since. [the first draft of check()](/src/margins.py#L11&rev=674909f969 "def check(cases, parts):") is pinned to the first version; hover it and press **Compare with latest** for a diff.

## Spreadsheet

A named range: [the mass table](/data/loads.xlsx#MassTable&at=79fe4364be). A cell range: [bracket mass](</data/loads.xlsx#'Mass properties'!A5:C5&at=79fe4364be>), and the same cells in the first draft: [bracket mass at the first draft](</data/loads.xlsx#'Mass properties'!A5:C5&rev=674909f969>).

## Slides, image and audio

Slides: [the margins slide](/docs/review.pptx#slide=5&at=79fe4364be) and [open items](/docs/review.pptx#slide=6&at=79fe4364be). The recording: [the start](/media/review.wav#t=0:00&at=79fe4364be), [the decision](/media/review.wav#t=0:06&at=79fe4364be), [the action](/media/review.wav#t=0:12&at=79fe4364be).

![The bracket](/images/bracket.png)

That's [the drawing](/images/bracket.png#at=79fe4364be) shown inside the note.

## Table

| Claim | Evidence |
| --- | --- |
| Ultimate factor is 1.4 | [Table 1](/docs/standard.pdf#page=18&viewrect=83,120,460,108&at=79fe4364be "Table 1—Minimum Design and Test Factors for Metallic Structures Verification Approach Ultimate Design Factor Yield Design Factor Qualification Test Factor Proof Test Factor Prototype 1.4 1.0* 1.4 N/A ") |
| Bolts take a fitting factor | [the action](/media/review.wav#t=0:12&at=79fe4364be) |
| The bracket got heavier | [bracket mass at the first draft](</data/loads.xlsx#'Mass properties'!A5:C5&rev=674909f969>) → [bracket mass](</data/loads.xlsx#'Mass properties'!A5:C5&at=79fe4364be>) |

## Flowchart

[The margin check](/notes/flow.canvas#at=93b612da4a) is a flowchart of `check()`: a loop inside a loop, a decision, and code citations in its boxes.

## Try it

- [ ] Open a document on the right, select something, and press **Cite** to link it here.
- [ ] Hover a link, then **Pin** or **Make live**.
- [ ] Rename `src/margins.py` from Open (Ctrl+P): the live links here follow it.
- [ ] Open **Version history** from Open, and look at what each version changed.
- [ ] This link is deliberately broken: [old analysis](/docs/old-analysis.pdf#page=2). Back to the [top](/notes/Start%20here.md#locus-demo).
