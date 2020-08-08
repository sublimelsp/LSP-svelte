import os
import sublime
from lsp_utils import NpmClientHandler


def plugin_loaded():
    LspSveltePlugin.setup()


def plugin_unloaded():
    LspSveltePlugin.cleanup()


class LspSveltePlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'server'
    server_binary_path = os.path.join(server_directory, 'node_modules', 'svelte-language-server', 'bin', 'server.js')
