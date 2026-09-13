"""
Python functions to replicate the MATLAB files for Laboration 2 in MA069G
Authors: Eric Johansson, Can Kupeli, Samuel Greenberg
Last Modified: 2022-10-15
"""
import numpy as np
from numpy import random, matlib
import matplotlib.pyplot as plt


def python_normal(N=100, medel=0, varians=1):
    arr = random.normal(medel, np.sqrt(varians), N)

    count, bins, ignored = plt.hist(arr, 100, density=False)

    plt.plot(
        bins,
        1
        / (np.sqrt(varians) * np.sqrt(2 * np.pi))
        * np.exp(-((bins - medel) ** 2) / (2 * np.sqrt(varians) ** 2)),
        linewidth=0,
        color="r",
    )
    plt.title(
        f"{N} slumptal ur normalfördelning. Medelvärde = {medel}, Varians = {varians}"
    )
    plt.xlabel("Värde")
    plt.ylabel("Frekvens")
    plt.show()


def python_likform(N=100, low=0, high=1):
    arr = random.uniform(low=low, high=high, size=N)

    count, bins, ignored = plt.hist(arr, 100, density=False)

    plt.plot(bins, np.ones_like(bins), linewidth=0, color="r")
    plt.title(f"{N} slumptal ur likformig fördelning från {low} till {high}")
    plt.xlabel("Värde")
    plt.ylabel("Frekvens")
    plt.xlim(low, high)
    plt.show()


def tarning_upprepa(n=10, N=[10**3, 10**4, 10**5]):
    for i in N:
        r = np.zeros(i)
        for k in range(i):
            y = np.floor(1 + 6 * random.random(n))
            r[k] = np.mean(y)
        plt.figure(i)
        count, bins, ignored = plt.hist(r, 100, density=False)
        plt.plot(bins, np.ones_like(bins), linewidth=0, color="r")
        plt.title(f"{n} kast per medelvärde med {i} upprepningar")
        plt.xlabel("Medelvärden")
        plt.ylabel("Frekvensen")

    plt.show()


def tarning_egen(n=10, N=[10**5], f=0, x=0):

    r = np.zeros(N)
    for k in range(N):
        y = np.floor(1 + 6 * random.random(n))
        r[k] = np.mean(y)
    count, bins, ignored = plt.hist(r, 100, density=False)
    plt.plot(bins, np.ones_like(bins), linewidth=0, color="r")
    plt.title(f"{n} kast per medelvärde med {N} upprepningar")
    plt.xlabel("Medelvärden")
    plt.ylabel("Frekvensen")

    plt.plot(x, f, color="r")
    plt.show()


def mc_conv(D=np.array([[-5, 5]]), N=int(1e5)):
    f = lambda x: np.exp(-np.sum(x**2, axis=0))
    M = 50
    V = np.cumprod(D[:, 1] - D[:, 0])
    dim = np.size(V)
    V = V[-1]

    r = np.zeros((dim, N))
    I = np.zeros(M)
    for i in range(M):
        r[:, :] = np.transpose(
            matlib.repmat(D[:, 0], N, 1)
            + random.rand(N, dim) * matlib.repmat(D[:, 1] - D[:, 0], N, 1)
        )
        I[i] = V * np.mean(f(r))

    return N, np.mean(I), np.std(I)


def BlackJackStrategy(hand, dealer_card):
    hard_count = sum(hand)
    cards = len(hand)
    aces_count = 1 * (1 in hand)
    soft_count = hard_count
    good_cards = [1, 7, 8, 9, 10]

    if cards < 2:
        return "Not enough cards"

    if hard_count <= 11:
        soft_count = hard_count + 10 * aces_count

    if cards == 2 and soft_count == 21:
        return "Blackjack"

    if soft_count >= 19:
        return "Stay"

    if hand == [9, 9] and dealer_card not in [1, 7, 10]:
        return "Split"

    if hard_count >= 17:
        return "Stay"

    if cards > 2:
        if hard_count == soft_count:
            if hard_count <= 11:
                return "Hit"

            if hard_count == 12 and dealer_card <= 3:
                return "Hit"

            if dealer_card in good_cards:
                return "Hit"

            return "Stay"

        if soft_count <= 17:
            return "Hit"

        if soft_count == 18 and dealer_card in [1, 9, 10]:
            return "Hit"

        return "Stay"

    if cards == 2:

        if hand[0] == hand[1]:
            card = hand[0]

            if card == 1:
                return "Split"

            if card == 8 and dealer_card != 1:
                return "Split"

            if card in [2, 3, 7] and dealer_card not in [1, 8, 9, 10]:
                return "Split"

            if card == 6 and dealer_card not in good_cards:
                return "Split"

            if card == 4 and dealer_card in [5, 6]:
                return "Split"

        if hard_count == soft_count:

            if hard_count == 11 and dealer_card != 1:
                return "Double"

            if hard_count == 10 and dealer_card not in [1, 10]:
                return "Double"

            if hard_count == 9 and dealer_card not in ([2] + good_cards):
                return "Double"

            if hard_count <= 11:
                return "Hit"

            if hard_count == 12 and dealer_card <= 3:
                return "Hit"

            if dealer_card in good_cards:
                return "Hit"

            return "Stay"

        if hard_count != soft_count:

            if soft_count == 18:

                if dealer_card not in ([2] + good_cards):
                    return "Double"

                if dealer_card in [2, 7, 8]:
                    return "Stay"

            if soft_count == 17 and dealer_card in [3, 4, 5, 6]:
                return "Double"

            if soft_count in [15, 16] and dealer_card in [4, 5, 6]:
                return "Double"

            if soft_count in [13, 14] and dealer_card in [5, 6]:
                return "Double"

            return "Hit"


def blackjack_hand_result(bet=10,player_hand='q', dealer_card='q', hard_code= 4):
    #Deck of cards, 4 types of 10
    
    deck=np.array([1,2,3,4,5,6,7,8,9,10,10,10,10])
    
    #hard stay condition for split aces
    
    hard_stay=False
    
    
    player_hand=[random.choice(deck), random.choice(deck)]
        
    if player_hand==[1]:
        hard_stay==True
        
    #Adding a 2nd card to hand after splits    
        
    while len(player_hand)<2:
        player_hand.append(random.choice(deck))
        
        
    
    dealer_card=random.choice(deck)
        
    dealer_cards=[dealer_card]
    
        
    if hard_stay==False:
        
        
        
        if BlackJackStrategy(player_hand, dealer_card) == 'Blackjack':
            
            dealer_cards.append(random.choice(deck))
            if 1 in (dealer_cards):
                if sum(dealer_cards)==11:
                    return 0
                
            return bet*1.5
        
        else:
            while BlackJackStrategy(player_hand, dealer_card) == 'Hit':
                player_hand.append(random.choice(deck))

                if sum(player_hand)>21:
                    return 0- bet


            if BlackJackStrategy(player_hand, dealer_card)=='Double':
                player_hand.append(random.choice(deck))
                bet= bet * 2
                if sum(player_hand)>21:
                    return 0- bet


            if BlackJackStrategy(player_hand, dealer_card)== 'Split':
                res= blackjack_hand_result(bet, [player_hand[0]], dealer_card) 
                res+= blackjack_hand_result(bet, [player_hand[0]], dealer_card)
                return res
        
        while True:
            #Plays out the blackjack hand from dealer's side
            
            dealer_cards.append(random.choice(deck))
            dealer_score= sum(dealer_cards)
            soft_score= dealer_score
            if dealer_score<=11 and 1 in dealer_cards:
                soft_score+=10

            if len(dealer_cards)==2 and soft_score==21:
                return 0-bet
                
            player_score=sum(player_hand)
            
            if player_score<=11 and 1 in player_hand:
                player_score+=10
                
            
            if soft_score>=17:
                if soft_score>21:
                    return bet
                
                if player_score>soft_score:
                    return bet
                
                if player_score==soft_score:
                    return 0
                
                if player_score<soft_score:
                    return 0 - bet
                

       
    
    if hard_stay==True:
        #Plays out only dealer's side, as player has to stop after 1 card
        
        while True:
            dealer_cards.append(random.choice(deck))
            
            dealer_score= sum(dealer_cards)
            
            soft_score= dealer_score
            if dealer_score<=11 and 1 in dealer_cards:
                soft_score+=10
                
            if len(dealer_cards)==2 and soft_score==21:
                return 0-bet
                
            player_score=sum(player_hand)
            
            if player_score<=11 and 1 in player_hand:
                player_score+=10
                
            if soft_score>=17:
                
                if soft_score>21:
                    return bet
                
                if player_score>soft_score:
                    return bet
                
                if player_score==soft_score:
                    return 0
                
                if player_score<soft_score:
                    return 0 - bet
                

 
def blackjack_sim(n_hands=50_000, bet=10):
    pnl=0
    for i in range(n_hands):
        pnl+= blackjack_hand_result(bet=bet)
    return pnl
    