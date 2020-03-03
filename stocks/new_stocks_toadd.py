one_y_premonition_yahoo(stock):
    """ enter to yahoo page and take the stock today and the premonition """
    return(one_y_premonition, stock_today)
    
top20_1y_premonition_from_yahoo(all_stocks):
    """ Find the top 20 based in yahoo 1 year premonition  """
    stock_today = 

    huge_top_20 = []
    nine_times_top_20 = []
    eight_times_top_20 = []
    seven_times_top_20 = []
    six_times_top_20 = []
    five_times_top_20 = []
    four_times_top_20 = []
    tree_times_top_20 = []
    two_times_top_20 = []

    for stock in all_stocks:
        
        one_y_premonition = one_y_premonition_yahoo(stock)
        times_grow = one_y_premonition / stock_today

        if times_grow >= 2.0 and times_grow < 3.0:
            two_times_top_20.append(stok)
        elif times_grow >= 3.0 and times_grow < 4.0:
            tree_times_top_20.append(stok)
        elif times_grow >= 4.0 and times_grow < 5.0:
            four_times_top_20.append(stok)
        elif times_grow >= 5.0 and times_grow < 6.0:
            five_times_top_20.append(stok)
        elif times_grow >= 6.0 and times_grow < 7.0:
            six_times_top_20.append(stok)
        elif times_grow >= 7.0 and times_grow < 8.0:
            seven_times_top_20.append(stok)
        elif times_grow >= 8.0 and times_grow < 9.0:
            eight_times_top_20.append(stok)
        elif times_grow >= 9.0 and times_grow < 10.0:
            nine_times_top_20.append(stok)
        else:
            huge_top_20.append(stok)

    top20_list = [ten_times_top_20, nine_times_top_20, eight_times_top_20, seven_times_top_20, six_times_top_20, five_times_top_20, four_times_top_20, tree_times_top_20, two_times_top_20]

    return(top20_list)


get_robinhood_stocks()
  """
  Take the list of my stocks from Robinhood
  """
  return(my_stocks, my_watchlist)

add_robinhood_whatchlist()

remove_robinhood_whatchlist()

buy_robinhood_stocks()

sell_robinhood_stocks()




main()
    all_stocks = open a file and readlines
        """ Try to find a way to fetch all stocks automatically """
    
    my_stocks , my_watchlist = get_robinhood_stocks()
        """ Do not know if this is possible """

    top20_list = top20_1y_premonition_from_yahoo(all_stocks)

    top20_table = []
    for stock in top20_list:
        """ 
        Ver
            Cuanto tiempo tiene la empresa
            Cuanta es su ganancia en el ultimo anio y mes
            Entender lo de el volumen para cuantificarlo
            Ver los stackeholders
            obtener el website
            Numero de empleados
            numero de shares 'floatShares"
             'fiftyDayAverage': 173.32559,
             'fiftyTwoWeekHigh': 190.7,
             'fiftyTwoWeekLow': 108.8,
            'enterpriseValue'
             'enterpriseToEbitda': 19.345,
             'enterpriseToRevenue': 8.828,
             'earningsQuarterlyGrowth': 0.383,
             'averageDailyVolume10Day': 75622200,
             'averageVolume': 31802203,
             'averageVolume10days': 75622200,
        """
        append values in an ordered way to top20_table

    print(top20_table) """ As a pretty table """


if __name__ if __name__ == '__main__':
    main()
