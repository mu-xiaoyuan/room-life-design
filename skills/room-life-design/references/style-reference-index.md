# Visual style-reference index

Read this reference only when an image-generation/editing tool can accept multiple image inputs. The files are local assets selected from the user's high-engagement reference library.

## Selection rule

Use the customer room as the **only edit target**. Select one closest style reference, plus an optional second reference only when it supplies a missing density or lighting pattern. Never send every reference at once.

For an ordinary customer run, shortlist from the text table first and visually inspect only the selected one or two images. If a candidate fails inspection, explain the mismatch briefly and inspect up to two additional indexed candidates; still send at most two style images to the renderer. Do not build a whole-library contact sheet or inspect every asset. If no suitable reference exists, use the maintained text grammar and the target image rather than forcing a template or requiring the customer to supply more examples. Full-library analysis belongs only to an explicit learning/audit request. Paths beginning with `assets/` are relative to the skill root, not this reference directory.

Tell the image tool that style references control mood, relational density, textile looseness, lighting topology, object layering, and vlog-ready framing—not architecture, room size, exact furniture, or personal possessions. The edit target's camera may change, but its geometry and chosen layout may not.

For an explicit request for more lived-in irregularity, match distributed active surfaces, object states and overlap as well as capacity. A sparse sleep/lounge reference does not become sufficient just because its function labels match. The room-4/9 `compact-bookish-bed-work-overview.jpg` can guide density even for a sleep/lounge plan; explicitly exclude its office layout and exact possessions. Retain the bright-warm lighting target independently.

| Asset | Best use | Learn from it | Do not copy blindly |
|---|---|---|---|
| `assets/style-references/compact-navy-collector.jpg` | Small, bed-dominant room; dark/blue preference | Dense bed-edge world, playful identity, mixed rugs, irregular wall layer, reachable objects | Exact toys, bed size, or every wall object |
| `assets/style-references/paper-lantern-eclectic.jpg` | Small-medium sleep/work room; broad warm-fill lighting reference (latest set, image 4) | Large diffuse shade plus local lamps connect warm wall/bed/floor coverage without erasing light hierarchy | Oversized lantern, every small object, or assuming a pendant is mandatory |
| `assets/style-references/bookish-layered-full-life.jpg` | Medium-large sleep/work/reading room | Accumulated bookish identity, mixed wood, plaid softened by flowers/toys, overlapping life scenes | Density in a room too small to support it |
| `assets/style-references/earthy-layered-multiscene.jpg` | Medium-large room with seating capacity | Interconnected scenes, mixed furniture, brown/wood continuity, rugs and plant layers | Extra sofa or lounge chair without space |
| `assets/style-references/earthy-botanical-lounge.jpg` | Large rectangular room; darker optional mood (latest set, image 2) | Warm wall/cabinet pools and tactile depth even at lower brightness | Its dim exposure as the default, large beanbag without capacity, or open-flame styling |
| `assets/style-references/light-natural-micro-retreat.jpg` | Small bright room needing one micro-corner | Pale room with dense, usable pause corner; rounded shapes and low light | Beanbag when the room cannot support its minimum posture/access envelope |
| `assets/style-references/light-natural-sleep-lounge.jpg` | Medium room with room for a compact second scene | Low shelf as permeable boundary, two related rugs, lounge cluster, retained original floor | Exact layout or sofa if access is uncertain |
| `assets/style-references/graphic-urban-nest.jpg` | Modern room; black/deep-blue preference | Warmth without beige, graphic art, sculptural stacks, strong corner cluster | Unstable stacks or excessive black in a dark room |
| `assets/style-references/compact-bookish-bed-work-overview.jpg` | Compact pale-wood bedroom needing sleep + work and a rich life image | Two-wall bed/daybed, full work wall, distributed low/open storage, dense vertical identity, mixed wood, checks, plants, warm local lamps, connected bed–desk composition | Creator-specific art/toys, exact objects, or assumed room expansion |
| `assets/style-references/compact-bookish-daybed-detail.jpg` | Compact sleep + leisure/daybed brief; secondary detail reference | Bed as a genuine reclining lounge through layered cushions, plush objects, reachable reading material, local light, wall collage, and foreground rug | Exact plaid set, plush collection, or wall art |
| `assets/style-references/compact-blue-hour-three-scene-overview.png` | Compact/medium room that must hold sleep + independent office + independent lounge | Slide the bed toward the entrance/front to release a window-side work wall and a separate residual lounge corner; use a shallow desk with push-under wood chair, low open cubbies, warm local lamps against cool blue window light, plant layers, and triangular foreground-to-background composition | Exact guitar, posters, plush toys, green bedding, or creator-specific collections |
| `assets/style-references/compact-blue-hour-lounge-detail.png` | Secondary reference when the missing quality is emotional lounge closure, warm/cool mood, or silhouette variety | A slouching lounge chair + footstool + soft rug + side storage + local lamp + plants + hobby/play cues form a complete independent retreat; soft/round/vertical silhouettes break the rectangular shell | Exact beanbag model, guitar, toys, wall art, or copying the room's architecture |
| `assets/style-references/warm-daylight-diffuse-bedroom.jpg` | Primary lighting reference for a bright warm bedroom (latest set, image 1) | Neutral daylight plus broad diffuse warm ambient coverage, ceiling/wall bounce, local table lamps and readable materials | Exact bed, toys, scenic window view, or assuming visible fixtures prove measured output |
| `assets/style-references/warm-daylight-work-nest.jpg` | Primary lighting reference for bright layered sleep/work scenes (latest set, image 3) | Filtered daylight, distinct warm lamps, readable bed/desk/floor midtones, soft shadows and preserved object colors | Its exact layout, personal items or measured lamp temperatures |

## Matching order

1. Match room capacity and existing functions.
2. Match the desired emotional density: compact nest, layered work/sleep, or multi-scene room.
3. Match palette/material preference.
4. Prefer a reference whose furniture scale and scene logic the customer room can plausibly support. For multiple selected functions, the independent-scene blue-hour reference may guide layout when compact anchors make separate office/lounge scenes possible, but do not inherit its dimness or saturated blue grading. Copy a bed/daybed functional layout only when independent candidates fail or the brief is deliberately bed-centered; its object-density grammar may still be used separately without changing the selected functions.
5. If the user gave no style preference, prioritize emotional specificity, capacity, and scene relationships over a safe neutral palette or preserving movable possessions.
6. For lighting, default to bright warm mixed light: favor the latest set's images 1 and 3 for brightness/neutral-window balance, and image 4 for broad diffuse plus local light layering. Use [lighting-model.md](lighting-model.md). A spatial reference and a lighting reference may supply different qualities; blue-hour/dim grading is optional, not inherited automatically.

## Image-tool input roles

Label inputs explicitly:

- **Image 1 — edit target:** preserve its architecture, proportions, fixed elements, chosen furniture layout, and resident requirements; allow a more flattering faithful viewpoint.
- **Image 2 — primary style reference:** borrow comfort density, layering, lighting, textile looseness, and relationship patterns only.
- **Image 3 — optional secondary reference:** borrow one named quality only, such as light topology or youthful bookish irregularity.

Require no text or watermark in the output. Do not reproduce creator-specific art, exact collections, logos, or watermarks from a reference.
