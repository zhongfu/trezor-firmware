## Sources

### Message type URLs

- https://github.com/cosmos/cosmos-sdk
- https://github.com/CosmWasm/wasmd
- https://github.com/cosmos/ibc-go
- https://github.com/scrtlabs/SecretNetwork
- https://github.com/tendermint/liquidity
- https://github.com/terra-money/core


## Parsing message lists

1. Clone the above repositories into some folder
2. From the same folder, run:

```bash
FILENAMES=$(find */proto -name "tx.proto" -o -name "msg.proto")
TYPE_URLS="$(grep -H -E "^message Msg" $FILENAMES | cut -d"/" -f 3- | cut -d" " -f 1-2 | sed -E -e "s| *\{?\}?$||" -e "s|/[a-z]+.proto:message |/|" | grep -v "Response$" | tr "/" "." | sort)"
for url in $TYPE_URLS; do echo -e "/$url\t$(sed -E -e 's/(^|\.)(.)/\u\2/g' <<< $url)"; done | jq --raw-input --slurp 'split("\n") | map(select(. != "") | split("\t") | { (.[0]): .[1] }) | add' > message-mapping.json
```
