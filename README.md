
# FinanceScraper

## Overview

FinanceScraper is a comprehensive tool designed to collect, process, and analyze financial data from various sources. The repository contains scripts to fetch data from APIs, process and transform this data, and perform technical analysis. The data sources include Alpha Vantage, Marketstack, World Bank, and Coinbase.

This repository is meant to create files to build a database using another repository. The `src` directory is responsible for collecting data which ends up in `raw_collected_data`, which is then preprocessed for storing in a database using `preprocessing_db/data_sources`.

## Directory Structure

```
financeScraper/
├── raw_collected_data/
│   ├── find_csv.sh
│   └── group_by_directory.py
├── preprocessing_db/
│   └── data_sources/
│       ├── transformed_data_btc_coinbase/
│       │   └── transformed_data_btc_coinbase_script.py
│       ├── sentiment_data/
│       │   └── sentiment_data_script.py
│       ├── eco_data_alpha_vantage/
│       │   └── eco_data_alpha_vantage_script.py
│       ├── data_world_bank/
│       │   └── data_world_bank_script.py
│       ├── inxdata_alpha_vantage/
│       │   └── inxdata_alpha_vantage_script.py
│       └── data_marketstack/
│           └── data_marketstack_script.py
├── src/
│   ├── alphavantage/
│   │   ├── crypto_data/
│   │   │   ├── btc_price_data_collector.py
│   │   │   └── fetch_crypto_intraday.py
│   │   └── sentiment_retriever/
│   │       ├── sentiment_data_processor.py
│   │       ├── sentiment_data_fetcher.py
│   │       └── sentiment_fetch_log.txt
│   ├── worldbank/
│   │   ├── direct_calls.py
│   │   ├── retrievabledata.py
│   │   ├── retrieve_features.py
│   │   └── wbdataretriever.py
│   ├── transformations/
│   │   ├── ma/
│   │   │   └── moving_average_tf.py
│   │   ├── rsi/
│   │   │   └── rsi_tf.py
│   │   ├── macd/
│   │   │   └── macd_tf.py
│   │   └── exploreCsvStruct/
│   │       └── explore_csv.py
│   ├── marketstack/
│   │   ├── list_tickers.py
│   │   ├── test_ticker_interval.py
│   │   ├── list_exchanges.py
│   │   ├── marketstack_retriever.py
│   │   ├── nyse_lse_tickers.py
│   │   └── list_index.py
│   └── marketdata/
│       └── coinbase/
│           ├── csv_inspector.py
│           ├── pairs.py
│           ├── btc_schemas.sql
│           ├── json_inspector.py
│           └── time_series_fetcher.py
├── .git/
└── README.md
```

## Setup

### Prerequisites

- Python 3.x
- Required Python packages (can be installed using `pip`):
  - `requests`
  - `pandas`
  - `numpy`
  - `matplotlib`

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/financeScraper.git
    cd financeScraper
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Data Collection

Scripts in the `src/alphavantage`, `src/marketstack`, `src/worldbank`, and `src/marketdata/coinbase` directories are used to collect data from various sources.

Example:
```sh
python src/alphavantage/crypto_data/btc_price_data_collector.py
```

### Data Processing

Scripts in the `preprocessing_db/data_sources` directory process and transform the collected data.

Example:
```sh
python preprocessing_db/data_sources/transformed_data_btc_coinbase/transformed_data_btc_coinbase_script.py
```

### Technical Analysis

Scripts in the `src/transformations` directory perform technical analysis on the processed data.

Example:
```sh
python src/transformations/ma/moving_average_tf.py
```

### Utilities

- `raw_collected_data/find_csv.sh`: Find CSV files in a directory.
- `raw_collected_data/group_by_directory.py`: Group files by directory.
- `src/transformations/exploreCsvStruct/explore_csv.py`: Explore the structure of CSV files.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to all the data providers and API services used in this project.

---

Feel free to reach out for any questions or suggestions!

---

## Contact

- Name: [nikhil_rs@live.com](mailto:nikhil_rs@live.com)
- GitHub: [NikhilNRS]([https://github.com/yourusername](https://github.com/NikhilNRS))

---

Happy Coding! 🚀
