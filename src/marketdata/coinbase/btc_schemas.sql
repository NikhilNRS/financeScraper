CREATE TABLE btc_data_hourly (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    low NUMERIC(10, 2) NOT NULL,
    high NUMERIC(10, 2) NOT NULL,
    open NUMERIC(10, 2) NOT NULL,
    close NUMERIC(10, 2) NOT NULL,
    volume NUMERIC(14, 8) NOT NULL
);

CREATE TABLE btc_data_6hr (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    low NUMERIC(10, 2) NOT NULL,
    high NUMERIC(10, 2) NOT NULL,
    open NUMERIC(10, 2) NOT NULL,
    close NUMERIC(10, 2) NOT NULL,
    volume NUMERIC(14, 8) NOT NULL
);

CREATE TABLE btc_data_daily (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    low NUMERIC(10, 2) NOT NULL,
    high NUMERIC(10, 2) NOT NULL,
    open NUMERIC(10, 2) NOT NULL,
    close NUMERIC(10, 2) NOT NULL,
    volume NUMERIC(14, 8) NOT NULL
);
