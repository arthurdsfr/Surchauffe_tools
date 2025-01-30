from data.recover_data.coin_from_dbeaver import *
from data.recover_data.coin_from_excel import *
from vizualisation.plot_indicators import *
from model.predict_model import predict_model


#fetch les variables
df, coin_prices, marketcap, volume = fetch_60d_from_excel()

#liste predictions
prediction = predict_model(coin_prices, marketcap, volume)

#plot rsi, sma, ema, vp
plot_indicators(df, coin_prices)

#plot les prédictions
plot_results(df, prediction)