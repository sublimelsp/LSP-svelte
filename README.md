# LSP-svelte

This is a helper package that automatically installs and updates the [Svelte Language Server](https://github.com/sveltejs/language-tools) for you.


## Installation

1. Install [LSP](https://packagecontrol.io/packages/LSP), [Svelte](https://packagecontrol.io/packages/Svelte) and `LSP-svelte` from Package Control.
2. (Optional but recommended) Install the [LSP-file-watcher-rust](https://packagecontrol.io/packages/LSP-file-watcher-rust) via Package Control to enable functionality to notify the server about new files.
3. Restart Sublime.


## Configuration

Open configuration file using command palette with `Preferences: LSP-svelte Settings` command or opening it from the Sublime menu (`Preferences > Package Settings > LSP > Servers > LSP-svelte`).


## Svelte support in JS/TS files

The [typescript-svelte-plugin](https://www.npmjs.com/package/typescript-svelte-plugin) provides additional Svelte-related functionality in JS/TS files, like go to definition, find references and rename across Svelte files, Svelte component types and SvelteKit route types. It requires [LSP-typescript](https://packagecontrol.io/packages/LSP-typescript).

`LSP-svelte` includes the plugin. To enable it, set `"typescript_plugin": true` in the `LSP-svelte` settings. `LSP-typescript` loads the plugin once `LSP-svelte` has started in the window, restarting if it's already running. Changes to Svelte files are only seen by the plugin after they are saved.
