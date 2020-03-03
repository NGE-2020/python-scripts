get_robinhood_stocks()
  """
  Take the list of my stocks from Robinhood
  """
  return(my_stocks)

get_robinhood_watchlist()
  """
  Take the list of my stocks from Robinhood
  """
  return(my_watchlist)

get_actual_stock_value()
  """
  Read the value from alphavantage
  """

buy_robinhood_stocks()

sell_robinhood_stocks()




main()
    my_stocks = get_robinhood_stocks()
    my_watchlist = get_robinhood_watchlist()

    last_query_stock_value = Read a dict with key:stock value:stock_value in write mode
    
    

    for stock in my_stocks:
        
        actual_stock_value = get_actual_stock_value(stock)
        
        if stock not in last_query_stock_value:
            last_query_stock_value.append(['stock':0)

        elif last_query_stock_value([stock]) > actual_stock_value:
            
            last_query_stock_value.append(['stock':0)
        


if __name__ if __name__ == '__main__':
    main()

    ### run this script every 5 minutes
