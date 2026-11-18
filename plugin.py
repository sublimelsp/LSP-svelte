from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import OnPreStartContext
from lsp_utils import NodeManager
from pathlib import Path
from sublime_lib import ResourcePath
from typing import cast
from typing_extensions import override
import sublime

TYPESCRIPT_PLUGIN_NAME = "typescript-svelte-plugin"


def log(message: str) -> None:
    print(f"[{__package__}] {message}")


def find_node_modules_with(path: Path, package_name: str) -> Path | None:
    """Return the `node_modules` directory that Node.js would load `package_name` from, for a module at `path`."""
    path = path.resolve()
    for directory in path.parents:
        node_modules = directory / "node_modules"
        if (node_modules / package_name / "package.json").is_file():
            return node_modules
    return None


def plugin_loaded():
    LspSveltePlugin.register()


def plugin_unloaded():
    LspSveltePlugin.unregister()


class LspSveltePlugin(LspPlugin):

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        NodeManager.on_pre_start_async(
            context,
            cls.plugin_storage_path,
            ResourcePath("Packages", package_name, "server"),
            Path("node_modules", "svelte-language-server", "bin", "server.js"),
            node_version_requirement=">=14",
        )
        if context.configuration.root_settings.get("typescript_plugin"):
            cls._register_typescript_plugin(context)

    @classmethod
    def _register_typescript_plugin(cls, context: OnPreStartContext) -> None:
        # Load the plugin installed with the server, which can be a custom one set with `server_path`.
        if not (window := context.view.window()):
            return
        server_path = cast("str", sublime.expand_variables(context.variables["server_path"], context.variables))
        if not (location := find_node_modules_with(Path(server_path), TYPESCRIPT_PLUGIN_NAME)):
            log(f'No "{TYPESCRIPT_PLUGIN_NAME}" for the server at "{server_path}". Svelte support in JS/TS is off.')
            return
        # No `selector` or `languages`: the plugin works in JS/TS files, while Svelte files are handled by this server.
        window.run_command("lsp_typescript_register_plugin", {
            "name": TYPESCRIPT_PLUGIN_NAME,
            "location": str(location),
        })
