# xrpl plugin

Gives Claude Code the XRPL tools (accounts, wallets, faucet funding, transactions, queries) and the `iou-issuance`, `mpt-issuance`, `confidential-mpt` and `lending-setup` workflows. Everything runs on your machine through [`@florent-uzio/xrpl-mcp`](https://www.npmjs.com/package/@florent-uzio/xrpl-mcp), with no model key involved. The plugin only holds the MCP server config.

## Install

Requires Node 22.13 or later.

```
/plugin marketplace add florent-uzio/skills
/plugin install xrpl@florent-uzio-plugins
```

Restart Claude Code, then run `/mcp` to check that `xrpl` is connected.

The plugin runs the latest published version of the server each time it starts. Claude Code reads the tool list only when the server starts, so after a new release, reconnect `xrpl` in `/mcp` or restart Claude Code to get the new tools.

Since 2.0.0, tools are named in camelCase without a `Tool` suffix (`submitPayment`, `getAccountInfo`). If your Claude Code permission rules name the old tools, update them: `mcp__plugin_xrpl_xrpl__submitPaymentTool` becomes `mcp__plugin_xrpl_xrpl__submitPayment`.

## Usage

Ask in plain language, for example: "Create and fund a testnet wallet, send 10 XRP to a second wallet, and save both wallets as a flow record."

Flow records (wallets, MPT IDs, keys, hashes) are saved in `~/.xrpl-mcp/records`, so you can reload them in a later session.

## Seeds on test networks only

Queries work on any network, mainnet included. Wallet seeds are refused on any network that is not a test network. Testnet, devnet and Xahau testnet (and their Clio, honeycluster and xrpl-labs alternatives) are allowed. On mainnet, sign the transaction yourself and have Claude submit the signed blob with `submitSignedBlob`.

To use a seed on another test network, add its URL to `XRPL_EXTRA_TEST_NETWORKS` (comma-separated). The plugin's config can't carry this, so run the server with `claude mcp add` instead of installing the plugin:

```bash
claude mcp add xrpl --env XRPL_EXTRA_TEST_NETWORKS=wss://my-testnet.example.com/,ws://localhost:6006 -- npx -y @florent-uzio/xrpl-mcp@latest
```

If the plugin is also installed, disable it so the two servers don't clash.
