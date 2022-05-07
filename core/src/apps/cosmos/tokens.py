# generated from tokens.py.mako
# do not edit manually!
# fmt: off

class TokenInfo:
    def __init__(self, symbol: str, decimals: int) -> None:
        self.symbol = symbol
        self.decimals = decimals


UNKNOWN_TOKEN = TokenInfo("uUNKN", 0)


def token_by_chain_type_tokenid(chain_id: str, token_type: str, token_id: str) -> TokenInfo:
    if chain_id == "Oraichain":
        if token_type == "native" and token_id == "orai":
            return TokenInfo("ORAI", 6)  # oraichain / Oraichain
    if chain_id == "agoric-3":
        if token_type == "native" and token_id == "ubld":
            return TokenInfo("BLD", 6)  # agoric / Agoric Staking Token
        if token_type == "native" and token_id == "urun":
            return TokenInfo("RUN", 6)  # agoric / Agoric Stable Token
    if chain_id == "akashnet-2":
        if token_type == "native" and token_id == "uakt":
            return TokenInfo("AKT", 6)  # akash / Akash Network
    if chain_id == "arkh":
        if token_type == "native" and token_id == "uarkh":
            return TokenInfo("ARKH", 6)  # arkh / Arkh
    if chain_id == "axelar-dojo-1":
        if token_type == "native" and token_id == "uaxl":
            return TokenInfo("AXL", 6)  # axelar / Axelar
        if token_type == "native" and token_id == "dai-wei":
            return TokenInfo("DAI", 18)  # axelar / Dai Stablecoin
        if token_type == "native" and token_id == "frax-wei":
            return TokenInfo("FRAX", 18)  # axelar / Frax
        if token_type == "native" and token_id == "uusdc":
            return TokenInfo("USDC", 6)  # axelar / USD Coin
        if token_type == "native" and token_id == "uusdt":
            return TokenInfo("USDT", 6)  # axelar / Tether USD
    if chain_id == "bitcanna-1":
        if token_type == "native" and token_id == "ubcna":
            return TokenInfo("BCNA", 6)  # bitcanna / BitCanna
    if chain_id == "bitsong-2b":
        if token_type == "native" and token_id == "ubtsg":
            return TokenInfo("BTSG", 6)  # bitsong / BitSong
    if chain_id == "bostrom":
        if token_type == "native" and token_id == "boot":
            return TokenInfo("BOOT", 0)  # bostrom / Bostrom
    if chain_id == "carbon-1":
        if token_type == "native" and token_id == "swth":
            return TokenInfo("SWTH", 0)  # carbon / Carbon
    if chain_id == "cerberus-chain-1":
        if token_type == "native" and token_id == "ucrbrus":
            return TokenInfo("CRBRUS", 6)  # cerberus / Cerberus
    if chain_id == "cheqd-mainnet-1":
        if token_type == "native" and token_id == "ncheq":
            return TokenInfo("CHEQ", 9)  # cheqd / cheqd
    if chain_id == "chihuahua-1":
        if token_type == "native" and token_id == "uhuahua":
            return TokenInfo("HUAHUA", 6)  # chihuahua / Chihuahua
    if chain_id == "colosseum-1":
        if token_type == "native" and token_id == "ufct":
            return TokenInfo("FCT", 6)  # firmachain / FirmaChain
    if chain_id == "columbus-5":
        if token_type == "native" and token_id == "ukrw":
            return TokenInfo("KRT", 6)  # terra / TerraKRW
        if token_type == "native" and token_id == "uluna":
            return TokenInfo("LUNA", 6)  # terra / Luna
        if token_type == "native" and token_id == "uusd":
            return TokenInfo("UST", 6)  # terra / TerraUSD
        if token_type == "cw20" and token_id == "terra183cvzy6knvva6mpvzcq86uyfxw0nd4925m0d0m":
            return TokenInfo("WHALE", 6)  # terra / White Whale
    if chain_id == "comdex-1":
        if token_type == "native" and token_id == "ucmdx":
            return TokenInfo("CMDX", 6)  # comdex / Comdex
    if chain_id == "core-1":
        if token_type == "native" and token_id == "uxprt":
            return TokenInfo("XPRT", 6)  # persistence / Persistence
    if chain_id == "cosmoshub-4":
        if token_type == "native" and token_id == "uatom":
            return TokenInfo("ATOM", 6)  # cosmoshub / Cosmos
    if chain_id == "crescent-1":
        if token_type == "native" and token_id == "ubcre":
            return TokenInfo("bCRE", 6)  # crescent / Bonded Crescent
        if token_type == "native" and token_id == "ucre":
            return TokenInfo("CRE", 6)  # crescent / Crescent
    if chain_id == "cronosmainnet_25-1":
        if token_type == "native" and token_id == "basecro":
            return TokenInfo("CRO", 18)  # cronos / Cronos
    if chain_id == "crypto-org-chain-mainnet-1":
        if token_type == "native" and token_id == "basecro":
            return TokenInfo("CRO", 8)  # cryptoorgchain / Cronos
    if chain_id == "darchub":
        if token_type == "native" and token_id == "udarc":
            return TokenInfo("DARC", 6)  # konstellation / DARC
    if chain_id == "desmos-mainnet":
        if token_type == "native" and token_id == "udsm":
            return TokenInfo("DSM", 6)  # desmos / Desmos
    if chain_id == "dig-1":
        if token_type == "native" and token_id == "udig":
            return TokenInfo("DIG", 6)  # dig / Dig Chain
    if chain_id == "echelon_3000-3":
        if token_type == "native" and token_id == "aechelon":
            return TokenInfo("ECH", 18)  # echelon / Echelon
    if chain_id == "emoney-3":
        if token_type == "native" and token_id == "eeur":
            return TokenInfo("EEUR", 0)  # emoney / e-Money EUR
        if token_type == "native" and token_id == "ungm":
            return TokenInfo("NGM", 6)  # emoney / e-Money
    if chain_id == "evmos_9001-2":
        if token_type == "native" and token_id == "aevmos":
            return TokenInfo("EVMOS", 18)  # evmos / Evmos
    if chain_id == "fetchhub-4":
        if token_type == "native" and token_id == "afet":
            return TokenInfo("FET", 18)  # fetchhub / fetch-ai
        if token_type == "native" and token_id == "nanomobx":
            return TokenInfo("MOBX", 9)  # fetchhub / MOBIX
    if chain_id == "galaxy-1":
        if token_type == "native" and token_id == "uglx":
            return TokenInfo("GLX", 6)  # galaxy / Galaxy
    if chain_id == "gravity-bridge-3":
        if token_type == "native" and token_id == "ugraviton":
            return TokenInfo("GRAV", 6)  # gravitybridge / Graviton
    if chain_id == "impacthub-3":
        if token_type == "native" and token_id == "uixo":
            return TokenInfo("IXO", 6)  # impacthub / IXO
    if chain_id == "injective-1":
        if token_type == "native" and token_id == "uinj":
            return TokenInfo("INJ", 6)  # injective / Injective
    if chain_id == "iov-mainnet-ibc":
        if token_type == "native" and token_id == "uiov":
            return TokenInfo("IOV", 6)  # starname / Starname
    if chain_id == "irishub-1":
        if token_type == "native" and token_id == "uiris":
            return TokenInfo("IRIS", 6)  # irisnet / IRISnet
    if chain_id == "juno-1":
        if token_type == "cw20" and token_id == "juno1y9rf7ql6ffwkv02hsgd4yruz23pn4w97p75e2slsnkm0mnamhzysvqnxaq":
            return TokenInfo("BLOCK", 6)  # juno / Block
        if token_type == "cw20" and token_id == "juno1tdjwrqmnztn2j3sj2ln9xnyps5hs48q3ddwjrz7jpv6mskappjys5czd49":
            return TokenInfo("DHK", 0)  # juno / DHK
        if token_type == "cw20" and token_id == "juno1re3x67ppxap48ygndmrc7har2cnc7tcxtm9nplcas4v0gc3wnmvs3s807z":
            return TokenInfo("HOPE", 6)  # juno / Hope Galaxy
        if token_type == "native" and token_id == "ujuno":
            return TokenInfo("JUNO", 6)  # juno / Juno
        if token_type == "cw20" and token_id == "juno1g2g7ucurum66d42g8k5twk34yegdq8c82858gz0tq2fc75zy7khssgnhjl":
            return TokenInfo("MARBLE", 3)  # juno / Marble
        if token_type == "cw20" and token_id == "juno168ctmpyppk90d34p3jjy658zf5a5l3w8wk35wht6ccqj4mr0yv8s4j5awr":
            return TokenInfo("NETA", 6)  # juno / Neta
        if token_type == "cw20" and token_id == "juno1r4pzw8f9z0sypct5l9j906d47z998ulwvhvqe5xdwgy8wf84583sxwh0pa":
            return TokenInfo("RAC", 6)  # juno / Racoon
    if chain_id == "kava-9":
        if token_type == "native" and token_id == "ukava":
            return TokenInfo("KAVA", 6)  # kava / Kava
    if chain_id == "kichain-2":
        if token_type == "native" and token_id == "uxki":
            return TokenInfo("XKI", 6)  # kichain / Ki
    if chain_id == "laozi-mainnet":
        if token_type == "native" and token_id == "uband":
            return TokenInfo("BAND", 6)  # bandchain / Band Protocol
    if chain_id == "likecoin-mainnet-2":
        if token_type == "native" and token_id == "nanolike":
            return TokenInfo("LIKE", 9)  # likecoin / LikeCoin
    if chain_id == "lum-network-1":
        if token_type == "native" and token_id == "ulum":
            return TokenInfo("LUM", 6)  # lumnetwork / Lum
    if chain_id == "mainnet-3":
        if token_type == "native" and token_id == "udec":
            return TokenInfo("DEC", 6)  # decentr / Decentr
    if chain_id == "mantle-1":
        if token_type == "native" and token_id == "umntl":
            return TokenInfo("MNTL", 6)  # assetmantle / AssetMantle
    if chain_id == "meme-1":
        if token_type == "native" and token_id == "umeme":
            return TokenInfo("MEME", 6)  # meme / MEME
    if chain_id == "microtick-1":
        if token_type == "native" and token_id == "utick":
            return TokenInfo("TICK", 6)  # microtick / Microtick
    if chain_id == "osmosis-1":
        if token_type == "native" and token_id == "uion":
            return TokenInfo("ION", 6)  # osmosis / Ion
        if token_type == "native" and token_id == "uosmo":
            return TokenInfo("OSMO", 6)  # osmosis / Osmosis
    if chain_id == "panacea-3":
        if token_type == "native" and token_id == "umed":
            return TokenInfo("MED", 6)  # panacea / MediBloc
    if chain_id == "pio-mainnet-1":
        if token_type == "native" and token_id == "nhash":
            return TokenInfo("HASH", 9)  # provenance / Hash
    if chain_id == "regen-1":
        if token_type == "native" and token_id == "uregen":
            return TokenInfo("REGEN", 6)  # regen / Regen Network
    if chain_id == "secret-4":
        if token_type == "native" and token_id == "uscrt":
            return TokenInfo("SCRT", 6)  # secretnetwork / Secret Network
    if chain_id == "sentinelhub-2":
        if token_type == "native" and token_id == "udvpn":
            return TokenInfo("DVPN", 6)  # sentinel / Sentinel
    if chain_id == "shentu-2.2":
        if token_type == "native" and token_id == "uctk":
            return TokenInfo("CTK", 6)  # shentu / Shentu
    if chain_id == "sifchain-1":
        if token_type == "native" and token_id == "rowan":
            return TokenInfo("ROWAN", 18)  # sifchain / Sifchain Rowan
    if chain_id == "sommelier-3":
        if token_type == "native" and token_id == "usomm":
            return TokenInfo("SOMM", 6)  # sommelier / Somm
    if chain_id == "stargaze-1":
        if token_type == "native" and token_id == "ustars":
            return TokenInfo("STARS", 6)  # stargaze / Stargaze
    if chain_id == "titan-1":
        if token_type == "native" and token_id == "uatolo":
            return TokenInfo("ATOLO", 6)  # rizon / Rizon Chain
    if chain_id == "umee-1":
        if token_type == "native" and token_id == "uumee":
            return TokenInfo("UMEE", 6)  # umee / Umee
    if chain_id == "vidulum-1":
        if token_type == "native" and token_id == "uvdl":
            return TokenInfo("VDL", 6)  # vidulum / Vidulum
    return UNKNOWN_TOKEN
