from sklearn.metrics import classification_report

from data.recover_data.coin_from_excel import *
import data.labeled_data.clean_labeled_data as clean
import data.calculated_data.rsi as rs
import data.calculated_data.moving_average as ma
import data.calculated_data.variation_price as vp
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from joblib import dump
import warnings

warnings.filterwarnings('ignore')

def selection_model(coin_prices, number_trades, volume_24h, k_folds=5):
    # Feature engineering
    rsi = rs.rsi(coin_prices)
    sma50 = ma.sma_50(coin_prices)
    sma200 = ma.sma_200(coin_prices)
    ema50 = ma.ema_50(coin_prices)
    ema200 = ma.ema_200(coin_prices)
    vp_1d = vp.price_variation_1d(coin_prices)
    vp_7d = vp.price_variation_7d(coin_prices)
    vp_30d = vp.price_variation_30d(coin_prices)
    labels = clean.labelled_average(coin_prices, number_trades, volume_24h)


    # Dataset
    df = pd.DataFrame({
        'Close': coin_prices,
        'Number of Trades': number_trades,
        'Volume': volume_24h,
        'RSI': rsi,
        'SMA50': sma50,
        'SMA200': sma200,
        'EMA50': ema50,
        'EMA200': ema200,
        'VP_1d': vp_1d,
        'VP_7d': vp_7d,
        'VP_30d': vp_30d,
        'Labels': labels
    })

    # Nettoyage des NaN
    df = df.dropna()

    X = df.drop(columns=['Labels'])
    y = df['Labels']

    # Standardisation (car SMOTE est sensible aux données non standardisées)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

    # Appliquer SMOTE pour équilibrer les classes
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

    models = {
        "Naive Bayes": GaussianNB(),
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)
    mean_scores = {}

    print(f"\nÉvaluation des modèles avec K-Fold (k={k_folds}) :")
    for name, model in models.items():
        scores = cross_val_score(model, X_resampled, y_resampled, cv=kf, scoring='f1_macro')
        mean_score = np.mean(scores)
        mean_scores[name] = mean_score
        print(f" {name} : {mean_score:.4f} (std: {np.std(scores):.4f})")

    best_name = max(mean_scores, key=mean_scores.get)
    best_score = mean_scores[best_name]

    print(f"\n Meilleur modèle : {best_name} avec F1-Score moyen de {best_score:.4f}")
    return best_score


def train_model(coin_prices, number_trades, volume_24h):
    rsi = rs.rsi(coin_prices)
    sma50 = ma.sma_50(coin_prices)
    sma200 = ma.sma_200(coin_prices)
    ema50 = ma.ema_50(coin_prices)
    ema200 = ma.ema_200(coin_prices)
    vp_1d = vp.price_variation_1d(coin_prices)
    vp_7d = vp.price_variation_7d(coin_prices)
    vp_30d = vp.price_variation_30d(coin_prices)
    labels = clean.labelled_average(coin_prices, number_trades, volume_24h)

    df = pd.DataFrame({
        'Close': coin_prices,
        'Number of Trades': number_trades,
        'Volume': volume_24h,
        'RSI': rsi,
        'SMA50': sma50,
        'SMA200': sma200,
        'EMA50': ema50,
        'EMA200': ema200,
        'VP_1d': vp_1d,
        'VP_7d': vp_7d,
        'VP_30d': vp_30d,
        'Labels': labels
    })

    df = df.dropna()

    X = df.drop(columns=['Labels'])
    y = df['Labels']

    # Standardisation
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

    # SMOTE pour équilibrer les classes
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

    # Split train / test
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

    # Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    # Sauvegarde du modèle
    dump(rf, 'btc_random_forest_model.joblib')
    print("Modèle sauvegardé sous le nom : 'btc_random_forest_model.joblib'")

    # Évaluation simple
    test_score = rf.score(X_test, y_test)
    print(f"Score du modèle sur le test : {test_score:.4f}")
    print("Rapport de classification :")
    print(classification_report(y_test, rf.predict(X_test)))

    return test_score



df, coin_prices, number_trades, volume_24h = fetch_data_from_excel()

#best_score = selection_model(coin_prices, number_trades, volume_24h)


test_score = train_model(coin_prices, number_trades, volume_24h)







