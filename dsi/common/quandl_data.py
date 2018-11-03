import quandl


class QuandlDataSource:
    def __init__(self, api_key):
        quandl.ApiConfig.api_key = 'xM6Bh-vY7JsUncDqo7SE'

    def get_wti_daily(self):
        data = quandl.get("EIA/PET_RWTC_D", returns='numpy')
        return data

    def get_cpi_usa(self):
        data = quandl.get("RATEINF/CPI_USA", returns='numpy')
        return data

    def get_us_stock_daily_close(self, ticker):
        data = quandl.get_table(
            'WIKI/PRICES', qopts={'columns': ['ticker', 'date', 'close']}, ticker=[ticker])
        return data

    def get_bitfinex_btcusd_daily(self):
        data = quandl.get('BITFINEX/BTCUSD', returns='numpy')
        return data

    def get_bitstamp_btcusd_daily(self):
        data = quandl.get('BITSTAMP/USD', returns='numpy')
        return data
