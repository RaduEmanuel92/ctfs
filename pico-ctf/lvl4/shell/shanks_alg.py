#!/usr/bin/env python
# encoding: utf-8
"""
chapter_2.py
Created by Daniel O'Donovan on 2008-10-09.
Copyright (c) 2008 University of Cambridge. All rights reserved.
"""

import sys
import os
import math
import gmpy
import sys
#sys.maxsize = pow(2,1025) -1
# Test case:
# the non-trivial factors of 27595893247589237508237458728307 are
# 5253107790730936 and 5253250903452230


def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def alg_231( n, improved=True ):
    """ Page 197: Trial Division """
    # [1]
    t = 0
    k = 2
    dk = 2
    sqrt_n = math.sqrt( n )
    count = 0
    while True:

        if count > sqrt_n: break
        if int(n) == 1: break    # [2]
        
        if improved:
            dk = int( gmpy.next_prime( dk ) )
        
        # [3]
        if improved:
            q =  n / dk
            r = n % dk
        else:
            q =  n / k
            r = n % k

        if r != 0:

            if improved:
                if q > dk:
                    k += 1
                else:
                    t += 1
                    pt = n
            else:
                if q > k:       # [4]
                    k += 1
                else:
                    t += 1
                    pt = n
        else:
            t += 1
            if improved:
                pt = dk
            else:
                pt = k
            n = q
            break

        count += 1
        # print( q, r )

    print( n, pt )

def FermatFactAlg( n ):
    """ Fermat's factoring algorithm 2.5.3 p 196 """
    n = gmpy.mpz( n )
    if n % 2 == 0:
        print( "%d is even" % n )
    # gmpy.sqrt is largest truncated sqrt
    # k = int( math.sqrt(n) ) + 1
    k = gmpy.sqrt(n) + 1
    y = k ** 2 - n
    d = 1
    
    while True:
        # floor_sqrt_y = float( int( math.sqrt(y) ) )
        floor_sqrt_y = gmpy.sqrt(y) 
        if ((floor_sqrt_y ** 2) ** 2) == (y ** 2): 
            break
        else:
            y = y + 2 * k + d
            d += 2

        # print floor_sqrt_y, gmpy.qdiv( n, 2.0)
        # print ((floor_sqrt_y ** 2) ** 2), (y ** 2)

        if floor_sqrt_y > gmpy.qdiv( n, 2.0):
            print( "No factor found " )
            return
    
    x = gmpy.sqrt( n + y )
    y = gmpy.sqrt( y )
    
    print( " the non-trivial factors of %d are" % n )
    print( " %d and %d" % (x-y, x+y) )    
            
def PollardsRho( N ):
    """ Pollard's Rho method for factoring """
    from exercises import Alg_improved_Euclid as gcd
    from random import randint

    N = gmpy.mpz( N )

    """ generator function """
    def f( x, N ): return (( (x ** 2) + 1) % N)
    
    t = 75 * gmpy.sqrt( N )
    sqrt_t = gmpy.sqrt( t )

    factor_found = False
    while not factor_found:
        xim1 = randint( 1, gmpy.sqrt( N ) / 10 ) # seed 
        yim1 = f( f( xim1, N), N)

        i = 0
        while i < sqrt_t:
            xi =    f( xim1, N )
            yi = f( f( yim1, N ), N )
            # yi =    f( yim1, N )
            # xi = f( f( xim1, N ), N )
            
            # print( 'gcd( xi - yi ) = gcd( %d )' % abs(xi - yi) )
            d = gcd( abs(xi - yi), N )
            if d != 1: 
                print('Non trivial factor found: ', d)
                factor_found = True
                break
            if xi == yi % N:
                print('Running with new seed')
                break

            xim1 = xi
            yim1 = yi
            i += 1
    
def shanks( y, a, n):
    """ Shanks' baby-step giant-step for finding discrete logarithms 
        of form : x = log_a ( y mod n )
    """
    s = gmpy.sqrt( n )

    S = {} # calculate the baby steps
    T = {} # calculate the giant steps
    for i in xrange( s ): 
        S['%s' % gmpy.mpz( ( y * (a ** i))      % n ) ] = int( i ) 
        T['%s' % gmpy.mpz( ( a ** ((i+1) * s) ) % n ) ] = int( i )
        
    # mathching and computing
    for key in S.keys():
        if key in T:
            r  =  S[key]
            st = (T[key] + 1) * s
            break
    x = st - r
    
    print 'So        log_%d %d\t(mod %d) =\t%d ' % ( a, y, n, x)
    print 'or equiv.     %d^%d\t(mod %d) =\t%d ' % ( a, x, n, y)
    return x
    
if __name__ == '__main__':
    # FermatFactAlg( 278153 )
    # FermatFactAlg( 340282366920938463463374607431768211457L )    
    # FermatFactAlg( 3248523672894567297 )

    # PollardsRho( 1387 )
    # PollardsRho( 278153 )
    # PollardsRho( 3248523672894567297)

    # x = shanks( 67, 59, 113 )

    p =  174807157365465092731323561678522236549173502913317875393564963123330281052524687450754910240009920154525635325209526987433833785499384204819179549544106498491589834195860008906875039418684191252537604123129659746721614402346449135195832955793815709136053198207712511838753919608894095907732099313139446299843
    g =  41899070570517490692126143234857256603477072005476801644745865627893958675820606802876173648371028044404957307185876963051595214534530501331532626624926034521316281025445575243636197258111995884364277423716373007329751928366973332463469104730271236078593527144954324116802080620822212777139186990364810367977
    A =  118273972112639120186970068947944724773714770611796145560317038505039351377800437911584090954295445815108415228076067419564334318734103894856428799576147989726840111816497674618324630523684004675727128364154281009934628997112127793757633331795515579928803348552388657916707518365689221161578522942036857923828
    B =  93745993751447503346396377281638158212564483727794429481438000562251573416232023154361841727945097797806065461693048826773559972703901706048613213733868461602449808032567839707922022630860776385491198101215693030172217682493643125763047405649582118389305170287200364245392146359258691658118945747317260110074

    #x = shanks( 6, 2, 19 )
    #x = shanks(A, g, p)
    FermatFactAlg(g)
    FermatFactAlg(A)
    PollardsRho(g)
    PollardsRho(A)
'''    
    def shanks( y, a, n):
    """ Shanks' baby-step giant-step for finding discrete logarithms 
        of form : x = log_a ( y mod n )
'''        