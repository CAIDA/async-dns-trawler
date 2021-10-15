# DNS Trawler (DNS TRust crAWLER)

```
______ _   _  _____   _____                  _
|  _  \ \ | |/  ___| |_   _|                | |
| | | |  \| |\ `--.    | |_ __ __ ___      _| | ___ _ __
| | | | . ` | `--. \   | | '__/ _` \ \ /\ / / |/ _ \ '__|
| |/ /| |\  |/\__/ /   | | | | (_| |\ V  V /| |  __/ |
|___/ \_| \_/\____/    \_/_|  \__,_| \_/\_/ |_|\___|_|
```

The DNS Trawler is a research tool to map implicit and explicit trust
base for domains and nameservers.

## Installation

To get the most out of DNSTrawler a _DGraph_ backend is needed.

Note DNSTrawler needs python3.8 to work correctly. Use of _virtualenv_ is recommeneded.

```
git clone git@github.com:vinapill/async-dns-trawler.git
cd dns-trawler
pip3 install .
```

### Development

If you plan to modify code use the -e option when installing

```
pip3 install -e .
```

## Usage

Find sample usage below. A _DGraph_ backend is needed for analysis.

dns_trawler module can be used in python shell without DGraph.

### Sample Usage (DGraph Mode)

```
./scripts/dns_trawler --domain-list domains.txt --db-connection  "<dgraph_ip>:<dgraph_port>" --log-level debug --workers 10
```

### Options

```
usage: dns_trawler [-h] --domain-list DOMAIN_LIST --db-connection DB_CONNECTION [--log-path LOG_PATH] [--proxy-list PROXY_LIST] [--custom-config CUSTOM_CONFIG]
                   [--workers WORKERS] [--log-level {debug,info,warning,error,critical}] [--quiet]

DNSTrawler

optional arguments:
  -h, --help            show this help message and exit
  --domain-list DOMAIN_LIST
                        file with list of domains to map
  --db-connection DB_CONNECTION
                        db connection str IP:Port
  --log-path LOG_PATH   file path to save log output
  --proxy-list PROXY_LIST
                        file with list of proxies to use
  --custom-config CUSTOM_CONFIG
                        file with json formatted config
  --workers WORKERS     number of workers
  --log-level {debug,info,warning,error,critical}
  --quiet               Quiesce output
```

## Architecture

![DNSTrawler Architecture](docs/DNSTrawlerArchitecture.png)

## Authors

Gautam Akiwate

Vinay Pillai
