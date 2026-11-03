# Excalidraw file format

Reference for writing `.excalidraw` files by hand. Excalidraw fills in missing optional fields on load, so the fields below are enough.

## File

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [],
  "appState": { "viewBackgroundColor": "#ffffff", "gridSize": null },
  "files": {}
}
```

## Common element fields

Every element carries:

```json
{
  "id": "svc-api",
  "type": "rectangle",
  "x": 0, "y": 0, "width": 200, "height": 80,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "#a5d8ff",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "groupIds": [],
  "frameId": null,
  "roundness": { "type": 3 },
  "seed": 1,
  "version": 1,
  "versionNonce": 1,
  "isDeleted": false,
  "boundElements": [],
  "updated": 1,
  "link": null,
  "locked": false
}
```

- `id`: readable and unique (`svc-api`, `call-create-order`, `note-outcome`). Readable ids make updates traceable.
- `seed`, `versionNonce`: any integers; give each element different ones.
- `link`: a URL opened on click. Use it wherever a node or arrow has a page of its own: a ticket, a PR, a doc, a dashboard, a block-explorer entry for a transaction or account.
- Shapes: `rectangle`, `ellipse`, `diamond`. Use `"roundness": null` for sharp corners.

## Text

Standalone text, or a label inside a shape:

```json
{
  "id": "svc-api-label",
  "type": "text",
  "x": 10, "y": 28, "width": 180, "height": 25,
  "text": "Orders API\nsvc-7f3a9c21…",
  "originalText": "Orders API\nsvc-7f3a9c21…",
  "fontSize": 20,
  "fontFamily": 5,
  "textAlign": "center",
  "verticalAlign": "middle",
  "lineHeight": 1.25,
  "containerId": "svc-api",
  "autoResize": true
}
```

plus the common fields (`backgroundColor: "transparent"`).

- **Binding a label**: set the text's `containerId` to the shape id, and add `{ "type": "text", "id": "<text id>" }` to the shape's `boundElements`. Both sides are required.
- Standalone text: `containerId: null`, `textAlign: "left"`, `verticalAlign: "top"`.
- `height` ≈ `fontSize × 1.25 × line count`; `width` ≈ `fontSize × 0.6 × longest line`.
- Shorten long IDs and hashes to the first 8 characters plus `…`; put the full value in `link`.

## Arrows

```json
{
  "id": "call-create-order",
  "type": "arrow",
  "x": 200, "y": 40, "width": 160, "height": 0,
  "points": [[0, 0], [160, 0]],
  "startBinding": { "elementId": "svc-api", "focus": 0, "gap": 4 },
  "endBinding": { "elementId": "db-orders", "focus": 0, "gap": 4 },
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "roundness": { "type": 2 }
}
```

plus the common fields.

- `x`, `y` is the first point; `points` are relative to it; `width`/`height` are the points' bounding box.
- **Binding an arrow**: each bound shape lists `{ "type": "arrow", "id": "<arrow id>" }` in its `boundElements`.
- **Labelling an arrow**: a text element with `containerId` = the arrow id, and the arrow lists it in `boundElements` as `type: "text"`. Label with the action and its key detail, e.g. `POST /orders\n201 Created` or `Payment 100 XRP\nA1B2C3D4…`.
- Use `type: "line"` with the same `points` model for unbound lines (timeline axis, lifelines). Use `"strokeStyle": "dashed"` for lifelines.

## Layout grid

- Title: standalone text, `fontSize: 36`, at `(0, -120)`. Date beneath it at `fontSize: 16`.
- Nodes: 200 × 80. Spacing: 120 horizontally, 100 vertically. Snap positions to multiples of 20.
- Flow and timeline read left → right; sequence messages top → bottom, 60 apart.
- The Outcome / Next steps note sits below the main diagram, 120 under its lowest element.

## Colours

One meaning per colour, consistent across the diagram (`backgroundColor`, with `strokeColor: "#1e1e1e"`):

| Meaning | Colour |
| --- | --- |
| Actor / account / component | `#a5d8ff` (blue) |
| Token / issuance / data | `#b2f2bb` (green) |
| External party / client / network | `#ffec99` (yellow) |
| Decision / success | `#d0bfff` (violet) |
| Open question / risk / failure | `#ffc9c9` (red) |
| Notes | `#f1f3f5` (grey) |

## Updating an existing file

- Read the whole file first. Leave every existing element's `id`, `x`, `y`, size, and style untouched.
- New elements: place the new region to the right of the current bounding box (max `x + width` + 200) or below it (max `y + height` + 200), whichever keeps the reading direction. Use a new id prefix per update (`u2-…`, `u3-…`).
- Add a section title for the new region with the update date.
- To change a fact on an existing element, edit its `text`/`originalText`, increment its `version`, and set a new `versionNonce` and `updated`.
- To connect new elements to existing ones, add the arrow id to the existing shape's `boundElements`; this is the only change made to an unchanged element.
- To retire an element, set `"isDeleted": true` rather than removing it.
