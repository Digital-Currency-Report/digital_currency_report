if __name__ == '__main__':
    from uvicorn import run
    run(app='digital_currency_report.api.rule:app', host="0.0.0.0", port=8000, debug=True, reload=True)
