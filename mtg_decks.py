#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 22:10:48 2017

@author: usr1
"""
from collections import defaultdict
import codecs

class Deck:
    def __init__(self, decklist):
        self.deck = defaultdict(dict)
        for n, card in decklist:
            card = ' '.join(card)
            self.deck[card] = n
        
    def get_cmatrix(self):
        pass
    
    def get_card(self, card):
        return modern_cards[card]
    
    def display(self):
        return self.deck

def deck_features(deck, modern):
    return {x:modern[x] for x in deck.display()}
    
def read_file(file):
    cards = []
    with open(file) as file:
        for ln in file:
            ln = ln.lower().split()
            cards.append((ln[0], ln[1:]))
    return cards

def get_deck_info(decklist, modern_cards):
    deck = defaultdict(dict)
    for n, name in decklist:
        name = ' '.join(name)
        modern_cards[name]['count'] = n
        deck[name] = modern_cards[name]
    return deck
        

def get_modern(file):
    basics = ['island','forest','swamp','plains','mountain']
    cards = defaultdict(dict)
    card = {'mana':'','pw':'','type':''}
    with open(file, encoding='ISO-8859-14') as file:
        track_c = 0
        for i, ln in enumerate(file):

            if ln != '\n':
                track_c += 1
                ln = ln.rstrip('\n').lower()

                if len([x for x in ln.split()]) == 1 and ln in basics:
                    cards[ln] = {'mana':None,'pw':None,'type':['basic', 'land']}
                    continue

                if track_c == 2 and 'land' in ln:
                    card = {'mana':None,'pw':None,'type':ln.replace('-','').split()}
                    track_c = 10
                    continue

                if track_c == 1:
                    name = ln
                elif track_c == 2:
                    card['mana'] = [x for x in ln]
                elif track_c == 3:
                    card['type'] = ln.replace('-','').split()
                elif track_c == 4:
                    if any(x for x in ln if x.isdigit()) and '/' in ln:
                        card['pw'] = ln.split('/')
                    else:
                        card['pw'] = None
                else:
                    pass
            else:
                track_c = 0
                cards[name] = card
                card = {'mana':'','pw':'','type':''}
    return card

def define_features():
    feature = defaultdict(dict)
    return feature

if __name__ == '__main__':
    dlist = read_file('/home/usr1/pypypy/00_mtg_deck.txt')

    modern_cards = get_modern('/home/usr1/pypypy/Modern-2017-07-13.txt')

    get_deck_info(dlist, modern_cards)
    deck = Deck(dlist)
    print(deck.display())
    deck_f = deck_features(deck, modern_cards)

    for c in deck_f:
        print(c)
        for f in deck_f[c]:
            if deck_f[c][f] != None: print(f, deck_f[c][f])
        print('')
