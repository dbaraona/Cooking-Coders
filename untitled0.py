"""
Irene Corrin 
15310-002
11/05/19
"""
print (__doc__)
import pandas 

data = pandas.read_csv('C:/Users/13302/Downloads/.csv')
http://www.bit.ly/ffxv_cookbook
def main(): 
    """ This function opens a menu which allows an imput to be entered. There is no argument though will accept a selection until option 8 is selected """
    endProgram = 'no'
    while endProgram == 'no':
            print ('0 for About:')
            print ('1 for Appetizers: ')
            print ('2 for Sandwiches: ')
            print ('3 for Soups: ')
            print ('4 for Meatless: ')
            print ('5 for Chicken: ')
            print ('6 for Beef: ')
            print ('7 for Pork: ')
            print ('8 for Fish: ')
            print ('9 for Shellfish: ')
            print ('10 for Desserts: ')
            print ('11 for FastFood & Others:' )
            print ('12 for Exit:')
            choice = int(input('enter your selection: '))
            if choice == 0:
                print('')
            elif choice == 1:
                
                print ('Here are some appetizer options for you: TOASTY RICE BALLS, MYSTERY MEAT SUSHI, DISH AND CHIPS, SALMON-IN-A-SUIT, BEANBALL CROQUETTES, KARLABOS CREAM CROQUETTE, ROYAL BANQUET CANAPÉ, KEYCATRICH SALAD TOAST')


            elif choice == 2:
                
                print ('Here are some sandwich options for you: CROQUE MADAME, CHARCUTERIE ON TOAST, GARULESSANDWICH, GREASE MONKEY’S SCHNITZEL SANDWICH, MULTI-MEAT SANDWICH, CRISPY FISH FRITTERWICH, STACKED HAM SANDWICH, CANNEDWICH')
            elif choice == 3:
                 
                print ('Here are some soup options for you: VEGGIE MEDLEY STEW, DRY-AGED TENDER ROAST STEW,QUILLHORN SOUP, GOLDEN TAIL SOUP, ROBUST BEAN SOUP, MEAT-AND-BEET BOUILLON, PACKED MUSHROOM STEW, GREEN SOUP, CURRY DEVILFIN SOUP, MARROWSHROOM CHOWDER')
            elif choice == 4:
                
                print ('Here are some meatless options for you: CLASSIC TOMATO AND EGG STIR-FRY, TRIPLE TRUFFLE RISOTTO, THREE-MUSHROOM KEBABS, CHEESE PIZZA, PLUMP N PUNGENT TOFU, CREAMY MILK RISOTTO, BREADED CUTLET WITH TOMATO')
            elif choice == 5:
                
                print ('Here are some chicken options for you: PRAIRIE-STYLE SKEWERS, CREAMY FOWL SAUTÉ, PEPPERY DAGGERQUILL RICE, GARDEN CURRY, FREE-RANGE FOWL OVER RICE, HOT HOPPER SKEWERS, MOTHER AND CHILD RICE BOWL, SEASONED MIDGARDSORMR, ROC OF RAVATOGH, RIC CRISPY ZU SKEWERS, PAPA BIRD AND BABY BOWL')
            elif choice == 6:
                
                print ('Here are some beef options for you: BURLY BEAN BOWL, SPICY LONG-BONE RIB STEAK, ACE HUNTER’S SCHNITZEL, LESTALLUM STEWED TRIPE, CROAKER IN BROWN SAUCE, MELDACIO MEAT PIE, HORNTOOTH MEAT PIE, HUNTERS KRAZY KEBABS,PRIME GARULA RIB, THICK N JUICY STEAK, SMOKED BEHEMOTH, LASAGNA AL FORNO, LONGWYTHES PEAK SEMUR SKEWERS')
            elif choice == 7:
                
                print ('Here are some pork options for you: CROWN CITY DIVE-STYLE DUMPLINGS, FRIED FRONTIER SKEWERS, GOLDEN EGG GALETTE, HEARTY CUTLET ON RICE, CROWN CITY ROAST, KINGS STEW')
            elif choice == 8:
                
                print ('Here are some fish options for you: OIL-DRIZZLED STEAMED FISH, GRILLED WILD TREVALLY, BATTERED BARRAMUNDI, GRILLED WILD BARRAMUNDI, NEBULA SALMON, TERIYAKI SKEWERED WILD TROUT, KENNYS ORIGINAL RECIPE, CARP OF THE DIEM, GRILLED MIGHTY BARRAMUNDI, FIRE-SAUCE FILLET, FISHSTICKS ON STICKS, SEA BASS SAUTÉ, ANOINTED ALLURAL SEA BASS, TIDE GROUPER CARPACCIO, LEGENDARY HERB-GRILLED WHOPPER, FRIED TIDE GROUPER, BROILED KING-ON-A-STICK, EXCELLENT OVEN-ROASTED TROUT, KENNYS SECRET RECIPE, OAK-SMOKED DEVIL GAR')
            elif choice == 9:
                
                print('Here are some shelfish options for you: FRIED ROOKIE ON RICE, EGG-FRIED CRUSTACEAN BOWL, CREAMY CRUSTACEAN OMELETTE, FISHERMAN’S FAVORITE, PAELLA ROYAL ROAD PAELLA, DARKSHELLS MARIENIERES SWEET & SPICY CYGILLAN CRAB, CREAMY BISQUE, TOMALLEY-FILLED DUMPLINGS, SWEET SALTWATER CRUSTACEAN CURRY')
            elif choice == 10:
                
                print ('Here are some dessert options for you: FLUFFY CHIFFON CAKE, ELEGANT ORANGE CAKE, MOIST TOMATO CAKE, TAELPAR HARVEST GALETTE, MEMORY LANE PASTRY, GOLDEN CHOCOBO TART, KUPOBERRY CHEESECAKE')
            elif choice == 11:
                
                print ('Here are some fast food options for you: CUP NOODLES CUP, NOODLES WITH BEEF, CUP NOODLES WITH EGG, CUP NOODLES WITH SHRIMP, RAMEN NOODLES, MCDONALDS, BURGER KING, OLIVE GARDEN, KFC, CHIPOTLE, TACO BELL, WENDYS, FIVE GUYS, RASING CANES, BUFFALO WILD WINGS, BOB EVANS, CHILIS, APPLEBEES, WINKING LIZARD, MELT, PANINIS, PENN STATION, DENNYS, CHICK-FIL-A, SWENSONS, DUNKIN, STARBUCKS, PIZZA HUT, PAPA JOHNS, DOMINOS') 
            elif choice == 12:
                endProgram == 'yes'

