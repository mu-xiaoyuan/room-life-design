# Delivery templates

Use only the section matching the request.

## Target-room diagnosis and plan

Lead with a one-sentence diagnosis of the root issue. Then provide:

1. **Known constraints and assumptions** — structure, fixed furniture, likely scale, resident needs, missing measurements.
2. **Existing-object classification** — active-use evidence, identity/collection, generic decoration, and functional noise/hazard; state what will be retained, reconnected, contained, or removed.
3. **Recovered-capacity audit** — compare the photographed occupied state with the plausible state after temporary functional noise is removed or contained; reserve an existing bed or a 1.8 m × 2.0 m bed when empty; compare the photographed position, both 90-degree axes, 180-degree head/foot reversal, wall-axis slides and every viable corner; test compact furniture envelopes before reducing scene count; distinguish capacity from wide-angle illusion without asking for measurements.
4. **Zoning and life-scene plan** — state the analyzed auxiliary-scene count and functions, honoring customer choices or choosing automatically when absent. For each, state posture/seat, anchor, resources, reachable support, light/power, and use envelope.
5. **Spatial moves in priority order** — name the chosen bed candidate and why competing orientations failed; default the bed to a two-wall corner in ordinary rooms, then state what to reroute, move, turn, overlap, cluster, bridge, or leave calm; show that independent auxiliary micro-scenes were attempted before any bed/daybed compound shortcut; explain the relationship each move creates and account for major floor areas as scene, transition, route, access, or intentional relief.
6. **Aesthetic target** — select one compatible family from the high-acceptance grammar; define the dominant scene, secondary visual stops, connected density transitions, palette echoes rather than matching sets, depth layers, and desired comfort density.
7. **Atmosphere system** — intentional capture time, warm/cool light topology, material and silhouette contrast, color/value structure, active surfaces, personal evidence, activation of major visible walls, and at least three plausible plant placements unless the user opts out. When unspecified, use the four-layer bright-warm model in [lighting-model.md](lighting-model.md): soft exterior base, broad warm ambient fill, local activity pools and open shadows.
8. **Minimum logic check** — fixed openings, plausible scale, at least one bed entry, and a real entry/posture/use/exit sequence for every selected activity. Treat circulation width, storage volume, cleaning, upkeep, and two-sided bed access as optional notes only when the user asks.
9. **Phased action list** — rearrange/no-buy; low-cost; furniture/lighting; optional structural work.
10. **Confidence** — distinguish image-visible facts, assumptions, and choices requiring dimensions or user preference.

Do not begin with a shopping list or style name.

## Case-study report

Report the dataset audit first. Then provide a compact per-independent-room table with evidence state, main mechanism, tradeoff, and confidence. Follow it with:

- repeated high-confidence mechanisms
- conditional mechanisms and counterexamples
- claims the evidence does not support
- changes to the previous design model
- target-aesthetic patterns learned from curated/high-engagement finished rooms
- evidence-base version update

Keep transformation conclusions and target-aesthetic conclusions in separate subsections, then explain how they combine in a customer-room generation workflow.

## Customer-upload image workflow

1. Inspect the uploaded image and explicitly lock architecture, proportions, fixed openings/equipment, and access constraints. Treat the original camera as evidence, not a required final viewpoint.
2. Preserve an existing mattress's apparent size/type; otherwise reserve a 1.8 m × 2.0 m bed. Preserve architecture, windows and air conditioner. Allow the frame, bed position, large wardrobe and all other movable items to change for the visual result unless explicitly retained. Compare occupied and recovered capacity; enumerate the photographed position, both 90-degree axes, 180-degree head/foot reversal, wall-axis slides and every viable corner; test compact anchor furniture; and choose an emotionally specific style compatible with the fixed surfaces.
3. Apply [customer-intake.md](customer-intake.md): honor supplied functions or choose fitting functions automatically for a photo-only makeover. Ask one short function question only when guided choice was requested; show only capacity-approved options. Do not ask dimensions, sleeper count, bed placement, style, ordinary-item retention or plant count.
4. Briefly state inferred bed/style and chosen functions, then continue. Wait only for explicitly requested guided choice or genuinely critical missing input.
5. Compare the viable bed-and-scene candidates before producing the transformation specification. Reject only layouts that break fixed geometry or make a selected activity impossible. Confirm approach, posture, use, reachable resources/support/light and exit; allow compact sequential overlap and one-sided bed access. For multiple selected functions, first use slim/shallow anchors to form independent scenes; use a bed as lounge/daybed only after those candidates fail or for an explicitly bed-centered brief. Among passing candidates, prioritize emotional composition over conventional ergonomics or generous clearance.
6. Produce a separate aesthetic specification using one compatible high-acceptance family, with a three-second invitation target, dominant scene, secondary stops, connected density transitions, intentional capture time, warm/cool light nodes, tactile layers, material and silhouette variation, activated visible walls, at least three plausible plant placements unless opted out, depth layers, active surfaces, and a light identity scaffold.
7. When multiple image inputs are supported, shortlist from [style-reference-index.md](style-reference-index.md) before opening one matched reference, optionally a second for one named quality. Do not scan the entire image library. Keep the uploaded room as the only edit target.
8. Merge the specifications into the image-edit prompt. Do not let style references overwrite source-room geometry or resident requirements. Permit a better camera angle that faithfully shows the same furniture layout.
9. Inspect the generated image first with the three-second invitation test, then against geometry fidelity, minimum scene plausibility, independent-versus-compound zoning, floor-area purpose, broad warm coverage and readable interior midtones, aesthetic gates, and the over-completion rejection test. Visually trace a person entering, using and leaving every selected scene. Do not reward conventional office furniture or flat natural daylight, and do not reject compactness or upkeep; reject only a desk or lounge scene with no plausible human posture or access at all.

## AI-render prompt

Write prompts in this order:

1. Inputs and roles: label Image 1 as the edit target; label any additional images as style references that control comfort density, lighting, layering, and emotional tone only.
2. Preserve: walls, doors, windows, proportions, fixed equipment, the existing mattress footprint/type, and user-specified keeps. The camera may move to a stronger vlog-ready viewpoint while depicting the same geometry and furniture layout.
3. Recovered capacity and candidate search: state which temporary obstructions and visually unhelpful movable storage are removed, replaced or redistributed; retain an existing mattress's size/type or reserve a 1.8 m × 2.0 m bed when empty; compare the photographed position, both 90-degree axes, 180-degree head/foot reversal, wall-axis slides and every viable two-wall corner; infer capacity without widening the room; identify which candidate releases the most valuable complete residual corner.
4. Zoning and life scenes: state mandatory sleep plus capacity-approved functions chosen by the customer or selected automatically when unspecified. For each named scene, specify approach, posture/seat, anchor, reachable resources, support surface/storage, light/power and exit. First attempt independent scenes with compact anchors. Allow sequentially shared movement space. For an office, show believable knee space, a seated chair position and a plausible way in/out; prefer a shallow desk and armless push-under chair when they protect an independent lounge, unless long-hour ergonomic work was explicitly requested.
5. Spatial relationships: declare the chosen bed orientation and corner after candidate comparison; then specify anchor orientation, overlapping adjacency clusters, shared edges, storage-to-activity reach, soft boundaries, and minimum usable access. Do not prioritize a window-side desk if a side-wall desk with a different bed orientation creates a stronger complete scene.
6. Composition: name the dominant scene, secondary visual stops, dense lived-in anchors, connected transitions, a legible route, silhouette contrasts, and foreground/middle/background. When geometry permits, build a triangular depth sequence with one foreground anchor and two distinct background life scenes. Assign every major floor area a purpose; do not let a large rug or empty patch impersonate a missing scene.
7. Aesthetic family: use fixed floor/wall color and daylight as compatibility anchors, then choose the strongest emotionally specific high-acceptance family; state palette roles, material echoes, deliberate mismatch, and visual richness. Pale wood may support youthful bookish retro. Do not ask the customer, mix all references, or specify a matching furniture set.
8. Lighting and capture time: default to a bright warm interior with soft daytime/late-afternoon context. Specify soft neutral/gently cool exterior base light, a plausible broad diffuse warm ambient source with wall/ceiling bounce, visible local task/accent pools around activities, and open readable shadows. Bed, desk, lounge and floor must remain legible beyond the lamps. Follow [lighting-model.md](lighting-model.md); no compulsory blue hour, saturated blue window, crushed blacks, clipped shades, or global yellow/orange filter.
9. Materials and color: tactile contrast, sufficient value depth, mixed origins, and natural wear/softness; avoid reducing “warm” to all-beige.
10. Identity, wall activation, and active surfaces: retain or add activity-linked possessions around a coherent reversible resident story. Hobby, display, playful and active-use cues are roles, not one-item limits. Apply the activity-state map in [comfort-density.md](comfort-density.md): name several relevant surfaces, their stored/in-use/temporarily placed objects, and their neighboring relationships. Connect wall layers to the life below rather than isolating a generic collage. Avoid both cleared surfaces and unrelated filler.
11. Greenery: require at least three visible, varied and plausible plant placements unless the user opts out; connect them to daylight, scene edges, and different height layers without blocking use.
12. Comfort irregularity: specify actual uneven stacks, selective offsets, leaning/resting objects, partial visual overlaps and textile edges connecting activity clusters. Preserve some ordinary alignment and quieter intervals. A wrinkled duvet and one open book cannot substitute for distributed life; use the prompt block in [comfort-density.md](comfort-density.md), adapted to this room instead of copying an object list.
13. Negative constraints: no changed architecture, impossible scale, blocked fixed doors/windows, artificial room widening, activity with no human posture or entry/exit, premature bed-as-lounge shortcut, bulky conventional office chair used only by habit, matching furniture package, formal art grid, showroom-tight bedding, large emotionally empty rug stage, unexplained blank wall field, token single plant, generic prop dumping, flat daylight-only illumination, dark light-islands, saturated blue-window dominance, crushed interior shadows, uniform amber wash, uniform ceiling-only lighting, style soup, random clutter, or over-completion. Do not forbid one-sided bed access, tight passages, open storage, plush toys, relaxed bedding, sequential overlap, or a changed but faithful camera angle.

If dimensions are unknown, ask the renderer to keep furniture scale physically plausible and avoid adding a full auxiliary zone merely to fill space.

## Render critique

Compare the render to both the source room and the plan:

- geometry fidelity
- credible and functionally closed life scenes
- recovered-capacity use and agreement between promised versus visible scene count
- compliance with the minimum zoning tier and whether leisure is genuinely closed, either as a separate seat/floor scene or an explicitly equipped bed/daybed mode
- whether independent auxiliary scenes were attempted with slimmer anchors and alternate bed slides before a compound bed/daybed shortcut
- wall/corner versus centered bed logic and the usefulness of residual floor areas
- whether multiple plausible bed orientations were considered instead of preserving the photographed layout by habit
- resource reach, support surfaces, light/power, and minimum use sequences; storage may be redistributed
- visible approach, occupied position and plausible exit for every seated scene—especially the office
- purpose of every major rug and open floor area
- activation of major visible walls and at least three plausible plant placements unless opted out
- relationship/cluster completeness
- dominant-scene clarity and secondary visual stops
- density gradient and quieter transitions
- macro order, meso overlap, and micro irregularity
- agreement with the activity-state map and chosen density reference: multiple surfaces in use, stored/current/temporary states, selective overlap and connected scene edges beyond a token open book or duvet wrinkles
- boundary and circulation logic
- light topology
- four-layer lighting: gentle exterior base, broad warm ambient coverage, local pools and readable shadows; evaluate interior brightness separately from windows and glowing shades
- tactile and color depth
- vertical field and foreground/middle/background
- coherence of the chosen aesthetic family
- personal specificity
- meaningful active-use evidence versus generic props
- signs of matching-set design, universal alignment, formal nostalgia, or emotional distance
- emotional comfort and vlog-frame strength
- three-second desire to enter and stay
- camera/layout consistency when the viewpoint changes

Name the two highest-leverage revisions. Avoid responding with a long list of decorative additions.
