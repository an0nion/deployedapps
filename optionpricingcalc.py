import streamlit as st
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


st.title("Option Pricing Calculator")
st.caption("_by :blue[Ananya Salian]_")

st.caption('This web app will be a tool to calculate the theoretical price of \
           financial options using several pricing models including the Black-Scholes model.\
           This will increase understanding of the factors that influence option prices. \
           This web app has been created as a passion project, to further my understanding of the foundations and implementation of financial models while increasing my coding proficiency.\
           The provided information should _not_ be taken as a substitute for professional advice.')
tab1, tab2 = st.tabs(["Black-Scholes Model", "Geometric Brownian Motion"])
with tab1:
    st.write("""
             The Black-Scholes Model (BSM) estimates the theoretical values of derivatives and requires the following input variables:
              - The current price of an asset
              - The strike price of the asset's option
              - The time to expiration
              - The risk-free rate
              - The volatility of an asset
             """)
    st.write("This BSM model can _only_ be used to price the value of European options, as it assumes that options can only be exercised at the expiration date,\
             unlike American options, which allow for options to be exercised at any time between\
             the current time and the expiration date.")
    st.write("Furthermore, this model does not take into account the influence that the payment\
             of dividends have on the value of a stock or asset's option contract.\
             As such, this model should only be used to price options of non-paying dividend stocks and assets. ")
    st.write("""
             The Black-Scholes Model assumes the following about the assets:
              - _Riskless Rate_: The rate of return on our riskless asset is constant and thus called the risk-free interest rate.
              - _Random Walk_: The instantaneous log return of a stock price (the continuous compounding rate of return of said stock) follows a :blue[Geometric Brownian Motion], which is explained and demonstrated at my next tab. It is assumed that drift and volatility of the motion are constant.
              - _Non dividend paying_: The underlying stock or asset does not pay a dividend.
             """)
    st.write("""
             Moreover, the following assumptions are made about the market:
              - There are no arbitrage opportunities, meaning that there is no way to make a riskless profit through arbitrage
              - All participants have the ability to borrow and lend, buy and sell any amount of cash at the riskless rate, and any amount of stock
              - The transactions listed above, do not incur any fees, costs and taxes, resulting in a frictionless market.
             """)
    
    underlying = st.number_input(label = "Underlying Price of the asset",help = "The current market price of your asset of choice")
    strikeprice = st.number_input(label = "Strike Price of asset", help = "This should be labelled on the graph of your call option")
    timetoex = st.number_input(label = "Number of months to expiry", help = "This is the amount of time (in months) until the options contract becomes void/expires" )
    riskfree = st.number_input(label = "Current riskfree rate, as a **decimal** number", help = "This is the theoretical rate of return received on assets with 0 risk. You can often calculate your real risk-free rate by subtracting the inflation rate from the yield of the Treasury bond matching your option contract duration.")
    volatility = st.number_input(label = "Volatility (σ) as a **decimal** number", help = "This can be calculated from obtaining the annualised standard deviation of price returns for your chosen asset")

    if st.button("Calculate"):
        try:
            S = underlying
            K = strikeprice
            T = timetoex/12
            R = riskfree
            vol = volatility

            d1 = (math.log(S/K) + (R + 0.5 * vol**2)*T)/(vol * math.sqrt(T))
            d2 = d1 - (vol * math.sqrt(T))
            C = (S * norm.cdf(d1)) - (K * math.exp(-R * T) * norm.cdf(d2))
            # C = Price of Call Option
            # P = Price of Put Option
            P = (K * math.exp(-R * T) * norm.cdf(-d2)) - (S * norm.cdf(-d1))
        except:
            st.error("An error has occurred. Please ensure all inputs are non-zero values before trying again. ")

        inmoney = d1 * 100
        exerc = d2 * 100
        st.write(f"The risk-adjusted probability of receiving your aseet at the expiration, given the option expires 'in the money' is: {inmoney:.3}%")
        st.write(f"The risk-adjusted probability that the option will be exercised is: {exerc:.3}%")
        st.write(f"The price of your call option is: ${C:.3}")
        st.write(f"The price of your put option is: ${P:.3}")

with tab2:
    st.write("Geometric Brownian Motion is a continuous-time stochastic process\
          (a mathematical model that described how a variable changes \
         over time in a probability space), that is also a fundamental \
         concept in financial mathematics, often used to model the random \
         movement of asset prices, usually in the context of stock prices within\
          financial markets. The GBM assumes that stock prices move randomly, \
         but with a general trend (referred to as drift) and random fluctuations\
          (referred to as volatility). Furthermore, the GBM operates by\
          continuously calculating very small changes in stock prices of \
         very short time intervals, allowing for a more precise and\
          flexible representation of price dynamics of our selected\
          stock or asset")
    st.write("""
            The two main components of Geometric Brownian Motion are drift and volatility.
            - _Drift_: The drift of a stock or asset represents\
            its average rate of return of the stock over time. 
            - _Volatility_: The volatility of a stock or asset measures the degree of variation\
            in price of an asset or stock over time.
            
            The Geometric Brownian Motion (GBM) is used to model stock\
            prices in the Black-Scholes model, and is the _most_ widely\
            used model of stock price behaviour. Furthermore, it is also used for the following:
            - _Option Pricing & Derivatives Trading_: GBM is a key component of the Black-Scholes model, one of the most\
            widely used models for pricing options contracts. You can find my Options Pricing Calculator\
            on this web app, at the _Black-Scholes Model_ tab.
            - _Portfolio Optimsation_: The GBM is used to model the behaviour of diversified investment portfolios\
            over time. 
            """)
    st.write("""
            Non-financial uses:
            - _Biostatistics and Population Modelling_: The GBM can also be used to model population growth, disease spread, and other biological diffusion processes
            - _Physics and Brownian Motion_: GBM is particularly applicable in the study of Brownian motion\
            , which is the study of random movement of particles suspended in fluid. the GBM can be used to\
            model the trajectory of particles undergoing Brownian motion. 
            """)
    # drift coefficient (E(r))
    mu = st.number_input(label = "Expected return as a decimal number", value = 0.1)
    T = st.number_input(label = "Time in years", value = 1.0)
    S0 = st.number_input(label = "Initial stock price in dollars", value = 100.0)
    vol = st.number_input(label = "Volatility of the stock as a decimal number", value = 0.2)

    # number of steps
    n = 100
    #number of simulations
    M = 100

    #calc GBM paths
    #calculate time steps
    if T <= 0:
        st.error("Time in years must be positive.")
    elif S0 <= 0:
        st.error("Initial stock price must be positive.")
    elif vol < 0:
        st.error("Volatility must be non-negative.")
    else:
        # Calculate time steps
        dt = T / n

    #simulation usin numpy arrays
    # create matrix Q with shape (n, M) for random normal values
    Q = np.random.normal(0, 1, (n, M))
    St = np.exp((mu - 0.5 * vol ** 2) * dt + vol * Q * np.sqrt(dt))
    #include array of 1s, thus including our initial stock price
    St = np.vstack([np.ones(M), St])

    #multilpy through by S0 and return cumulative product of elements along a given simulation path (axis = 0)
    # THis is the daily/timestep changes in terms of drift and variance we need to accumulate these over time
    # we us ethe cumulative product along each simulation path, thus we need to multiply by St
    # multiple through my s_ and return cumulative product of elements along a given simulation path which is our axis = 0
    St = S0 * St.cumprod(axis=0)

    #consider time intervals in years

    # define time interval correctly
    time = np.linspace(0, T, n+1)

    meanpath = St.mean(axis=1)

    meaner = meanpath[-1]

    st.write(f"The mean expected value of the stock after {T} years is ${meaner:.6}")


    #plot
    plt.figure(figsize=(10, 6))
    plt.plot(time, St, color = 'darkgrey', alpha = 0.5)
    plt.plot(time, meanpath, color = 'red', label = 'Trend Line')
    plt.xlabel("Years $(t)$")
    plt.ylabel("Stock Price $(S_t)$")
    plt.title(
        f"Realisations of Geometric Brownian Motion\n"
        f"$dS_t = \\mu S_t df + \\sigma S-t dW_t$\n"
        f"$S_0 = {S0}, \\mu = {mu}, \\sigma = {vol}$"
    )
    st.pyplot(plt)



st.caption("By Ananya Salian")


# WRITE HERE BEFORE FINALISATION
