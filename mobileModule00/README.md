# Piscine Mobile — Module 00

React Native (Expo) implementation of the Module 00 exercises — an introduction to mobile development with four progressive projects building a fully functional calculator app.

## Repository Structure

```
mobileModule00/
├── ex00/              # Basic display — centered text + button
├── ex01/              # Toggle text between "Initial Text" and "Hello World!"
├── ex02/              # Calculator UI — button grid layout (no logic)
├── calculator_app/    # Full calculator with evaluation engine
├── .gitignore
└── README.md
```

---

## Prerequisites

- **Node.js** >= 18
- **npm** or **yarn**
- **Expo Go** app on your phone (SDK 54) — or an Android/iOS emulator
- **Web browser** (optional, for `--web` mode)

---

## How to Run

Each exercise is a standalone Expo project. Navigate into any one and run:

```bash
cd mobileModule00/<exercise>
npm install
npx expo start
```

Then:
- Press **`a`** — open on Android emulator
- Press **`i`** — open on iOS simulator
- Press **`w`** — open in web browser
- **Scan the QR code** — open in Expo Go on your phone

---

## Exercise 00 — A Basic Display

**Directory:** `ex00/`

A minimal single-screen app demonstrating the fundamental building blocks of a React Native screen.

### Features
- `Text` element displaying "Initial Text"
- `TouchableOpacity` button labeled "Press me" below the text
- Both elements centered horizontally and vertically using `flex: 1` + `justifyContent: 'center'` + `alignItems: 'center'`
- On button press: logs `"Button pressed"` to the debug console

### Key Files
| File | Purpose |
|---|---|
| `App.js` | Main component with text, button, and centered layout |
| `package.json` | Expo SDK 54 dependencies |
| `app.json` | Expo project configuration (portrait, tablet support) |

### Console Output
```
Button pressed
```

---

## Exercise 01 — Say Hello to the World

**Directory:** `ex01/`

Extends ex00 with stateful toggle behavior.

### Features
- Displays "Initial Text" by default
- Button press toggles between "Initial Text" and "Hello World!"
- Uses `useState` hook to manage display state
- Logs `"Button pressed"` on every press
- Fully centered, responsive layout (identical to ex00)

### Key Files
| File | Purpose |
|---|---|
| `App.js` | Toggle logic via `useState`, `useCallback` for stable handler |

### State Flow
```
Initial Text  --[button press]-->  Hello World!
Hello World!  --[button press]-->  Initial Text
```

### Console Output
```
Button pressed
Button pressed
...
```

---

## Exercise 02 — More Buttons (UI Only)

**Directory:** `ex02/`

A calculator user interface with all buttons laid out but no computation logic — the UI prototype for the final calculator.

### Features
- **Header:** Custom AppBar-style `View` with title "Calculator"
- **Display area:** Two `TextInput` fields (non-editable):
  - _Expression_ (top) — shows `"0"` initially
  - _Result_ (bottom) — shows `"0"` initially
- **Button grid** (4-column layout, responsive via `flex`):
  - **Row 1:** `AC`, `C`, `/`, `*`
  - **Row 2:** `7`, `8`, `9`, `-`
  - **Row 3:** `4`, `5`, `6`, `+`
  - **Row 4:** `1`, `2`, `3`, `=`
  - **Row 5:** `0`, `.`
- **Styling:** iOS-calculator-inspired dark theme:
  - Number buttons: dark gray (`#2C2C2E`)
  - Operator buttons: orange (`#FF9F0A`)
  - Clear buttons: darker gray with red text (`#FF453A`)
- **Debug logging:** every button press outputs its label to the console

### Key Files
| File | Purpose |
|---|---|
| `App.js` | Calculator UI: header, TextInputs, button grid, console logging |

### Console Output (sample)
```
AC
7
+
8
=
```

---

## Exercise 03 / calculator_app — It's Alive!

**Directory:** `calculator_app/`

The fully functional calculator extending the ex02 UI with a complete expression evaluation engine powered by `mathjs`.

### Features
- **Expression input:** dynamically updated as user types (shows `"0"` when empty)
- **Result output:** displays evaluation result after pressing `=`
- **Operations:** `+`, `-`, `*`, `/` with standard math operator precedence
- **Negative numbers:** press `-` at the start or after any operator (e.g., `5 + -3`)
- **Decimal numbers:** smart decimal handling — prevents multiple dots per number, auto-prepends `0` when needed (`.5` → `0.5`)
- **C button:** deletes the last character; resets result to `"0"` when expression becomes empty
- **AC button:** clears entire expression and resets result to `"0"`
- **Error safety** — the app **never crashes**:
  - Division by zero → displays `"Error"`
  - Invalid/malformed expressions → `try/catch` → `"Error"`
  - Oversized numbers → `toFixed(10)` clamping for clean display
- **Previous-result chaining:** after `=`, pressing an operator uses the result as the left operand (e.g., `5+3` → `=` → `8` → `+` → `8+` → `2` → `=` → `10`)
- **Fresh start after evaluation:** pressing a digit after `=` begins a new expression

### Evaluation Engine

Uses `mathjs` (`evaluate()`), a well-established math library that handles:
- Operator precedence (PEMDAS/BODMAS)
- Proper floating-point arithmetic
- Error throwing for invalid expressions

```js
import { evaluate } from 'mathjs';
const result = evaluate('1 + 2 * 3 - 5 / 2'); // → 2.5
```

### Key Files
| File | Purpose |
|---|---|
| `App.js` | Full calculator: state management, button handling, evaluation, error recovery |
| `package.json` | Includes `mathjs: "^13.0.0"` |

### State Variables
| Variable | Type | Purpose |
|---|---|---|
| `expression` | `string` | Raw expression string (e.g., `"5+3*2"`) |
| `result` | `string` | Displayed result or `"Error"` / `"0"` |
| `justEvaluated` | `boolean` | Flag to trigger fresh start on next digit |

### Console Output (sample)
```
5
+
3
=
10
```

### Error Handling Summary

| Scenario | Behavior |
|---|---|
| `5 / 0` | `Infinity` → `!isFinite()` → displays `"Error"` |
| `0 / 0` | `NaN` → `!isFinite()` → displays `"Error"` |
| `5 + * 3` | `mathjs` throws → `catch` → displays `"Error"` |
| Empty expression + `=` | Evaluates `"0"` → displays `"0"` |
| `9999999999999 * 9999999999999` | Displays result (may use scientific notation) |
| After `"Error"` — press `AC` | Full reset to `"0"` |

---

## Responsive Design

All four projects use the same responsive foundation:

| Technique | Purpose |
|---|---|
| `flex: 1` | Full-screen layout that adapts to any screen size |
| `SafeAreaView` | Avoids notches, status bars, and rounded corners |
| `justifyContent` + `alignItems` | True centering regardless of device dimensions |
| `supportsTablet: true` | Explicit iPad/tablet support in `app.json` |
| `flex: 1` per button | Buttons and grid cells scale proportionally |
| Dark theme | Consistent across ex02 and calculator_app |

---

## Common Issues & Troubleshooting

### `expo-asset` not found
Removed old `node_modules` and run:
```bash
rm -rf node_modules package-lock.json
npm install
```

### Expo Go SDK mismatch
Ensure your Expo Go app supports **SDK 54**. Update via the app store if needed.

### Port already in use
```bash
npx expo start --port 19002
```

### mathjs import error
Make sure `npm install` was run in the `calculator_app/` directory — `mathjs` is NOT a global dependency.

---

## Dependencies

### ex00, ex01, ex02
| Package | Version |
|---|---|
| `expo` | `~54.0.0` |
| `react` | `19.1.0` |
| `react-native` | `0.81.5` |
| `expo-asset` | `~12.0.13` |
| `expo-constants` | `~18.0.13` |
| `expo-font` | `~14.0.11` |
| `expo-status-bar` | `~3.0.9` |
| `react-native-web` | `^0.21.0` |

### calculator_app (additional)
| Package | Version | Purpose |
|---|---|---|
| `mathjs` | `^13.0.0` | Safe expression evaluation |

---

## Submission Notes

- Turn-in directory: **mobileModule00/**
- Each exercise is an independent Expo project
- The peer evaluator will run each project by navigating into each directory and running `npm install && npx expo start`
- No global setup or additional tooling required

---

*Piscine Mobile — Module 00 | React Native (Expo SDK 54)*
