# Lighting model: bright warm interior, not a dark blue-hour default

Use for lighting plans, image prompts, reference matching, and lighting-only render critique. This is the user's current product preference, superseding the blue-hour default introduced in version 1.9. Keep blue hour as an optional requested mood, not a universal recipe.

## Outcome

Create a room that feels bright enough to live in and warmly enveloping: warm lamps visibly shape the interior, while soft daylight can keep it open and readable. Brightness, warmth, softness, and contrast are separate decisions. More yellow does not mean brighter; more lamps do not necessarily mean better ambient coverage. Do not ban natural light or neutral object colors.

## Four layers

| Layer | Role | Prompt / visual evidence |
|---|---|---|
| 1. Soft exterior / base light | Establish daytime or late-afternoon context and support visibility without overwhelming the warm interior | Neutral or gently cool window light softened by sheers or blinds; recognizable exterior where available; no compulsory deep blue or cyan window. With little/no daylight, use plausible warm-neutral indirect fill rather than inventing a window. |
| 2. Broad warm ambient light | Connect the room between local lamps, lifting the walls, ceiling and room-middle surfaces | A diffuse paper/fabric shade, a suitable uplight, bounced floor lamp, or overlapping diffuse lamps. Choose the mechanism that fits the room; a paper lantern is an example, not mandatory furniture. Show believable warm bounce on adjacent walls and textiles. |
| 3. Local task / accent pools | Give the desk, lounge and bedside distinct inviting focal areas | Visible table, floor, wall or shelf lamps at varied heights, brighter locally than the base but not isolated dots in a dark shell. Use enough sources for the actual scenes, not a fixed lamp quota; tiny decorative lights cannot substitute for ambient fill. |
| 4. Open, readable shadows | Retain depth while keeping furniture, materials and routes legible | Soft contact shadows and gradual falloff; readable bedding folds, chair, wall art, plants and floor in the darker areas. Do not crush foreground/ceiling/room-middle detail or flatten everything into uniform brightness. |

Layer 4 is a light/exposure relationship, not a required fourth lamp. Daylight and artificial light may both contribute physically; the intended perceptual emphasis is warm artificial illumination and personal intimacy, not a claim that daylight contributes nothing.

## Color and exposure guidance

- Favor warm-white/cream light over saturated orange. Approximate 2700–3200 K local lights are prompt starting points, not temperatures measured from reference photographs. Ambient fill may be warm or warm-neutral as needed; no numeric temperature is a pass/fail rule.
- Separate window tone, lamp tone, diffuse bounce, exposure, and shadow lift. Preserve green leaves, wood variations, pale fabrics and intentional dark anchors.
- Make lamps/glowing shades visibly brighter than surrounding surfaces, but retain shade detail; do not make the brightest object an overexposed white hole.
- Raise room midtones and broad warm coverage before adding more tiny lamps, increasing orange saturation, replacing dark materials, or turning up window brightness.
- A room can have plenty of light and still have local glow. Do not dim the whole room merely to make lamps visible.

## Reference selection

Use the brightness and warm-neutral balance of `warm-daylight-diffuse-bedroom.jpg` and `warm-daylight-work-nest.jpg` as default lighting anchors. Use `paper-lantern-eclectic.jpg` for broad diffuse plus local layering. `earthy-botanical-lounge.jpg` demonstrates a darker valid mood, not the default brightness target. Find these assets through [style-reference-index.md](style-reference-index.md).

When a spatial reference is dark or strongly blue, borrow only its layout/density and state that this lighting model overrides its exposure and color grading. Do not inherit every attribute of one reference.

## Ready-to-use prompt block

> Bright, enveloping warm interior in soft daytime or late-afternoon light. Preserve the source room and chosen furniture layout. Keep window light neutral or gently cool, never saturated deep blue. Use broad diffuse warm ambient illumination and believable wall/ceiling bounce to lift room midtones, plus distinct warmer table/floor/wall lamp pools around the actual activities. Keep the bed, desk, lounge, plants, wall details and floor clearly readable. Preserve soft contact shadows and material colors; maintain visible lamp glow without clipping shades, flattening contrast, or applying a global yellow/orange filter. Cozy and lived-in, not dim, nocturnal, or ceiling-only flat lighting.

## Render acceptance and correction

Review both the whole frame and interior areas excluding the window and luminous shades:

1. Does the room itself look sufficiently bright, rather than just the window and lamps?
2. Does warmth extend across meaningful wall/textile/furniture surfaces, not only around lamp bulbs?
3. Are all chosen life scenes inviting and readable, including foreground and room-middle details?
4. Are local warm pools distinct but connected by softer ambient light?
5. Are shadows soft and legible without becoming flat gray? Are object colors preserved?

If dark: improve diffuse warm coverage, bounce and room exposure first. If flat: restore local emphasis and soft contact shadows, not global darkness. If orange: reduce saturation/global color cast while retaining localized warmth. If blue-dominated: reduce exterior blue saturation/contrast rather than removing all exterior light. For a lighting-only revision, hold layout and furniture constant unless the new luminaire needs a small supported placement change.

Optional encoded-image brightness statistics can support same-room/similar-crop comparisons, but they are not illuminance, lamp-output or exposure-stop measurements. Window area, dark furniture, cropping, white balance and tone mapping affect them. Do not impose universal dark-pixel percentages, Kelvin estimates, or EV differences from image averages. This four-layer model is a prompt and visual-review rubric, not an engineering lighting calculation.
