#!/usr/bin/env python
###############################################################
##   jDate.py  (29/4/1392) - (20/7/2013)
##
##   Copyright (C) 2013 dotpy.ir
##   jelodari iraj (iraj.jelo@gmail.com)
##   
##
##   This program is free software you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation either version 2, or (at your option)
##   any later version.
##
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.
## 
###############################################################

import math

J0000 = 1721424.5            # Julian date of Gregorian epoch: 0000-01-01
J1970 = 2440587.5            # Julian date at Unix epoch: 1970-01-01
JMJD  = 2400000.5            # Epoch of Modified Julian Date system
J1900 = 2415020.5            # Epoch (day 1) of Excel 1900 date system (PC)
J1904 = 2416480.5            # Epoch (day 0) of Excel 1904 date system (Mac)


##  Frequently-used constants


J2000             = 2451545.0,              ## Julian day of J2000 epoch
JulianCentury     = 36525.0,                ## Days in Julian century
JulianMillennium  = (JulianCentury * 10),   ## Days in Julian millennium
AstronomicalUnit  = 149597870.0,            ## Astronomical unit in kilometres
TropicalYear      = 365.24219878           ## Mean solar tropical year

#  ASTOR  --  Arc-seconds to radians. 

def astor(a):
    return a * (math.pi / (180.0 * 3600.0))


#  DTR  --  Degrees to radians.  

def dtr(d):
    return (d * math.pi) / 180.0


#  RTD  --  Radians to degrees.  */

def rtd(r):
    return (r * 180.0) / math.pi


#  FIXANGLE  --  Range reduce angle in degrees.  */

def fixangle(a):
    return a - 360.0 * (math.floor(a / 360.0))


#  FIXANGR  --  Range reduce angle in radians.  */

def fixangr(a):
    return a - (2 * math.pi) * (math.floor(a / (2 * math.pi)))


##  DSIN  --  Sine of an angle in degrees

def dsin(d):

    return math.sin(dtr(d))


##  DCOS  --  Cosine of an angle in degrees

def dcos(d):

    return math.cos(dtr(d))


#  MOD  --  Modulus def which works for non-integers.  */

def mod(a, b):

    return a - (b * math.floor(a / b))


##  AMOD  --  Modulus def which returns numerator if modulus is zero

def amod(a, b):

    return mod(a - 1, b) + 1


#  JHMS  --  Convert Julian time to hour, minutes, and seconds,
              #returned as a three-element array.  */

def jhms(j):

    j += 0.5                 # Astronomical to civil */
    ij = ((j - math.floor(j)) * 86400.0) + 0.5
    return [
                     math.floor(ij / 3600),
                     math.floor((ij / 60) % 60),
                     math.floor(ij % 60)]


##  JWDAY  --  Calculate day of week from Julian day

Weekdays = [ "Sunday", "Monday", "Tuesday", "Wednesday",
                          "Thursday", "Friday", "Saturday" ]

def jwday(j):

    return mod(math.floor((j + 1.5)), 7)


NormLeap = ["Normal year", "Leap year"]


#  MOD  --  Modulus function which works for non-integers.  
def mod(a, b):
    return a - (b * math.floor(a / b))


#  AMOD  --  Modulus function which returns numerator if modulus is zero
def amod(a, b):
    return mod(a - 1, b) + 1
   
#  WEEKDAY_BEFORE  --  Return Julian date of given weekday (0 = Sunday)
#                        in the seven days ending on jd.  

def weekday_before(weekday, jd):
    return jd - jwday(jd - weekday)


##  SEARCH_WEEKDAY  --  Determine the Julian date for: 
##
##            weekday      Day of week desired, 0 = Sunday
##            jd           Julian date to begin search
##            direction    1 = next weekday, -1 = last weekday
##            offset       Offset from jd to begin search

def search_weekday(weekday, jd, direction, offset):
    return weekday_before(weekday, jd + (direction * offset))

##  Utility weekday functions, just wrappers for search_weekday

def nearest_weekday(weekday, jd):
    return search_weekday(weekday, jd, 1, 3)

def next_weekday(weekday, jd):
    return search_weekday(weekday, jd, 1, 7)

def next_or_current_weekday(weekday, jd):
    return search_weekday(weekday, jd, 1, 6)


def previous_weekday(weekday, jd):

    return search_weekday(weekday, jd, -1, 1)


def previous_or_current_weekday(weekday, jd):
    return search_weekday(weekday, jd, 1, 0)


def TestSomething():

    pass


##  LEAP_GREGORIAN  --  Is a given year in the Gregorian calendar a leap year ?

def leap_gregorian(year):
    return ((year % 4) == 0) and (not (((year % 100) == 0) and ((year % 400) != 0)))


##  GREGORIAN_TO_JD  --  Determine Julian day number from Gregorian calendar date

GREGORIAN_EPOCH = 1721425.5

def gregorian_to_jd(year, month, day):
    return (GREGORIAN_EPOCH - 1) +(365 * (year - 1)) + math.floor((year - 1) / 4) +(-math.floor((year - 1) / 100)) + math.floor((year - 1) / 400) +  math.floor((((367 * month) - 362) / 12) +           (0 if(month <= 2) else -1 if leap_gregorian(year) else -2) +day)

##  JD_TO_GREGORIAN  --  Calculate Gregorian calendar date from Julian day

def jd_to_gregorian(jd):


    wjd = math.floor(jd - 0.5) + 0.5
    
    depoch = wjd - GREGORIAN_EPOCH
    quadricent = math.floor(depoch / 146097)
    dqc = mod(depoch, 146097)
    cent = math.floor(dqc / 36524)
    dcent = mod(dqc , 36524)
    quad = math.floor(dcent / 1461)
    dquad = mod(dcent , 1461)
    yindex = math.floor(dquad / 365)
    year = (quadricent * 400) + (cent * 100) + (quad * 4) + yindex

##    print 'wjd: '      ,wjd
##    print 'depoch: '   ,depoch
##    print 'quadricent:',quadricent 
##    print 'dqc:'   ,dqc
##    print 'cent:'  ,cent
##    print 'dcent:' ,dcent
##    print 'quad:'  ,quad
##    print 'dquad:' ,dquad    
##    print 'yindex' ,yindex
##    print 'year: ' , year

    if (not(cent == 4 or yindex == 4 )):
        year +=  1
        
    yearday = wjd - gregorian_to_jd(year, 1, 1)
##    print 'yearday:',yearday
    leapadj = 0 if wjd < gregorian_to_jd(year, 3, 1) else 1 if leap_gregorian(year) else 2
##    print 'leapadj:',leapadj

    month = math.floor((((yearday + leapadj) * 12) + 373) / 367)
    day = (wjd - gregorian_to_jd(year, month, 1)) + 1

    return [year, month, day]

##  ISO_TO_JULIAN  --  Return Julian day of given ISO year, week, and day

def n_weeks(weekday, jd, nthweek):
    
    j = 7 * nthweek

    if (nthweek > 0):
        j += previous_weekday(weekday, jd)
    else :
        j += next_weekday(weekday, jd)
    
    return j


def iso_to_julian(year, week, day):
    
    return day + n_weeks(0, gregorian_to_jd(year - 1, 12, 28), week)


##  JD_TO_ISO  --  Return array of ISO (year, week, day) for Julian day

def jd_to_iso(jd):

    year = jd_to_gregorian(jd - 3)[0]
    if (jd >= iso_to_julian(year + 1, 1, 1)):
        year += 1

    week = math.floor((jd - iso_to_julian(year, 1, 1)) / 7) + 1
    day = jwday(jd)
    if (day == 0):
        day = 7
    return [year, week, day]

##  ISO_DAY_TO_JULIAN  --  Return Julian day of given ISO year, and day of year

def iso_day_to_julian(year, day):
    return (day - 1) + gregorian_to_jd(year, 1, 1)

##  JD_TO_ISO_DAY  --  Return array of ISO (year, day_of_year) for Julian day

def jd_to_iso_day(jd):

    year = jd_to_gregorian(jd)[0]
    day = math.floor(jd - gregorian_to_jd(year, 1, 1)) + 1
    return [year, day]

##  PAD  --  Pad a string to a given length with a given fill character.  

def pad(str, howlong, padwith):
    s = str.toString()

    while (s.length < howlong):
        s = padwith + s
    return s

##  JULIAN_TO_JD  --  Determine Julian day number from Julian calendar date

JULIAN_EPOCH = 1721423.5

def leap_julian(year):
    return year % 4 == ( 0 if(year > 0) else 3)

def julian_to_jd(year, month, day):

    ## Adjust negative common era years to the zero-based notation we use.  

    if (year < 1):
        year += 1
    

    ## Algorithm as given in Meeus, Astronomical Algorithms, Chapter 7, page 61 */

    if (month <= 2):
        year -= 1
        month += 12

    return ((math.floor((365.25 * (year + 4716))) +
            math.floor((30.6001 * (month + 1))) +
            day) - 1524.5)

##  JD_TO_JULIAN  --  Calculate Julian calendar date from Julian day

def jd_to_julian(td):

    td += 0.5
    z = math.floor(td)

    a = z
    b = a + 1524
    c = math.floor((b - 122.1) / 365.25)
    d = math.floor(365.25 * c)
    e = math.floor((b - d) / 30.6001)

    print a,b,c,d,e
    month = math.floor((e - 1) if (e < 14) else (e - 13))
    year = math.floor((c - 4716) if (month > 2) else (c - 4715))
    day = b - d - math.floor(30.6001 * e)

##        If year is less than 1, subtract one to convert from
##        a zero based date system to the common era system in
##        which the year -1 (1 B.C.E) is followed by year 1 (1 C.E.).  

    if (year < 1):
        year -=1


    return [year, month, day]



##  HEBREW_TO_JD  --  Determine Julian day from Hebrew date

HEBREW_EPOCH = 347995.5

##  Is a given Hebrew year a leap year ?

def hebrew_leap(year):
    return ((year * 7) + 1) % 19 < 7


##  How many months are there in a Hebrew year (12 = normal, 13 = leap)

def hebrew_year_months(year):
    
    return 13 if hebrew_leap(year)  else 12


##  Test for delay of start of new year and to avoid
##  Sunday, Wednesday, and Friday as start of the new year.

def hebrew_delay_1(year):


    months = math.floor(((235 * year) - 234) / 19)
    parts = 12084 + (13753 * months)
    day = (months * 29) + math.floor(parts / 25920)

    if ((3 * (day + 1)) % 7 < 3):
        day +=1
    
    return day


##  Check for delay in start of new year due to length of adjacent years

def hebrew_delay_2(year):


    last = hebrew_delay_1(year - 1)
    present = hebrew_delay_1(year)
    next = hebrew_delay_1(year + 1)

    return ( 2 if (next - present) == 356  else 1 if ((present - last) == 382)  else 0)


##  How many days are in a Hebrew year ?

def hebrew_year_days(year):

    return hebrew_to_jd(year + 1, 7, 1) - hebrew_to_jd(year, 7, 1)


##  How many days are in a given month of a given year

def hebrew_month_days(year, month):

    ##  First of all, dispose of fixed-length 29 day months

    if (month == 2 or month == 4 or month == 6 or
        month == 10 or month == 13):
        return 29


    ##  If it's not a leap year, Adar has 29 days

    if (month == 12 and not hebrew_leap(year)) :
        return 29
    

    ##  If it's Heshvan, days depend on length of year

    if (month == 8 and not(mod(hebrew_year_days(year), 10) == 5)) :
        return 29
    

    ##  Similarly, Kislev varies with the length of year

    if (month == 9 and (hebrew_year_days(year) % 10) == 3):
        return 29
    

    ##  Nope, it's a 30 day month

    return 30


##  Finally, wrap it all up into...

def hebrew_to_jd(year, month, day):


    months = hebrew_year_months(year)
    jd = HEBREW_EPOCH + hebrew_delay_1(year) +   hebrew_delay_2(year) + day + 1

    if (month < 7):
        for mon in range(7,months+1):
            jd += hebrew_month_days(year, mon)
        
        for mon in range(1,month):
            jd += hebrew_month_days(year, mon)
        
    else :
        for mon in range(7,month):
            jd += hebrew_month_days(year, mon)
        

    return jd

##
##    JD_TO_HEBREW  --  Convert Julian date to Hebrew date
##                      This works by making multiple calls to
##                      the inverse def, and is this very
##                      slow.  

def jd_to_hebrew(jd):

    jd = math.floor(jd) + 0.5
    count = math.floor(((jd - HEBREW_EPOCH) * 98496.0) / 35975351.0)
    year = count - 1
    i = count
    while jd >= hebrew_to_jd(i, 7, 1):
        i += 1
        year += 1
    
    first = 7 if (jd < hebrew_to_jd(year, 1, 1)) else 1
    month = first
    i = first
    while jd > hebrew_to_jd(year, i, hebrew_month_days(year, i)):
        i += 1
        month += 1
    day = (jd - hebrew_to_jd(year, month, 1)) + 1
    return [year, month, day]


##    EQUINOXE_A_PARIS  --  Determine Julian day and fraction of the
##                          September equinox at the Paris meridian in
##                          a given Gregorian year.  

def equinoxe_a_paris(year):
    ##  September equinox in dynamical time
    equJED = equinox(year, 2)

    ##  Correct for delta T to obtain Universal time
    equJD = equJED - (deltat(year) / (24 * 60 * 60))

    ##  Apply the equation of time to yield the apparent time at Greenwich
    equAPP = equJD + equationOfTime(equJED)

    ##  Finally, we must correct for the constant difference between
    ##  the Greenwich meridian and that of Paris, 2##B020'15" to the
    ##  East.  

    dtParis = (2 + (20 / 60.0) + (15 / (60 * 60.0))) / 360
    equParis = equAPP + dtParis

    return equParis

##    PARIS_EQUINOXE_JD  --  Calculate Julian day during which the
##                           September equinox, reckoned from the Paris
##                           meridian, occurred for a given Gregorian
##                           year.  */

def paris_equinoxe_jd(year):
    ep = equinoxe_a_paris(year)
    epg = math.floor(ep - 0.5) + 0.5

    return epg

##    ANNEE_DE_LA_REVOLUTION  --  Determine the year in the French
##                                revolutionary calendar in which a
##                                given Julian day falls.  Returns an
##                                array of two elements:

##                                    [0]  Ann##E9e de la R##E9volution
##                                    [1]  Julian day number containing
##                                         equinox for this year.


FRENCH_REVOLUTIONARY_EPOCH = 2375839.5

def annee_da_la_revolution(jd):
    guess = jd_to_gregorian(jd)[0] - 2,

    lasteq = paris_equinoxe_jd(guess)
    while (lasteq > jd):
        guess -= 1
        lasteq = paris_equinoxe_jd(guess)
    
    nexteq = lasteq - 1
    while (not((lasteq <= jd) and (jd < nexteq))):
        lasteq = nexteq
        guess += 1
        nexteq = paris_equinoxe_jd(guess)
    
    adr = round((lasteq - FRENCH_REVOLUTIONARY_EPOCH) / TropicalYear) + 1

    return [adr, lasteq]

##    JD_TO_FRENCH_REVOLUTIONARY  --  Calculate date in the French Revolutionary
##                                    calendar from Julian day.  The five or six
##                                    "sansculottides" are considered a thirteenth
##                                    month in the results of this def.  

def jd_to_french_revolutionary(jd):

    jd = math.floor(jd) + 0.5
    adr = annee_da_la_revolution(jd)
    an = adr[0]
    equinoxe = adr[1]
    mois = math.floor((jd - equinoxe) / 30) + 1
    jour = (jd - equinoxe) % 30
    decade = math.floor(jour / 10) + 1
    jour = (jour % 10) + 1

    return [an, mois, decade, jour]


##  FRENCH_REVOLUTIONARY_TO_JD  --  Obtain Julian day from a given French
##                                  Revolutionary calendar date.  

def french_revolutionary_to_jd(an, mois, decade, jour):

    guess = FRENCH_REVOLUTIONARY_EPOCH + (TropicalYear * ((an - 1) - 1))
    adr = [an - 1, 0]

    while (adr[0] < an):
        adr = annee_da_la_revolution(guess)
        guess = adr[1] + (TropicalYear + 2)

    equinoxe = adr[1]

    jd = equinoxe + (30 * (mois - 1)) + (10 * (decade - 1)) + (jour - 1)
    return jd


##  LEAP_ISLAMIC  --  Is a given year a leap year in the Islamic calendar ?

def leap_islamic(year):
    
    return (((year * 11) + 14) % 30) < 11


##  ISLAMIC_TO_JD  --  Determine Julian day from Islamic date

ISLAMIC_EPOCH = 1948439.5
ISLAMIC_WEEKDAYS = ["al-'ahad", "al-'ithnayn",
                                 "ath-thalatha'", "al-'arb`a'",
                                 "al-khamis", "al-jum`a", "as-sabt"]


def islamic_to_jd(year, month, day):

    return (day +
            math.ceil(29.5 * (month - 1)) +
            (year - 1) * 354 +
            math.floor((3 + (11 * year)) / 30) +
            ISLAMIC_EPOCH) - 1


##  JD_TO_ISLAMIC  --  Calculate Islamic date from Julian day

def jd_to_islamic(jd):


    jd = math.floor(jd) + 0.5
    year = math.floor(((30 * (jd - ISLAMIC_EPOCH)) + 10646) / 10631)
    month = math.min(12,
                math.ceil((jd - (29 + islamic_to_jd(year, 1, 1))) / 29.5) + 1)
    day = (jd - islamic_to_jd(year, month, 1)) + 1
    return [year, month, day]


##  LEAP_PERSIAN  --  Is a given year a leap year in the Persian calendar ?

def leap_persian(year):

    return ((((((year - (474 if(year > 0) else 473)) % 2820) + 474) + 38) * 682) % 2816) < 682


##  PERSIAN_TO_JD  --  Determine Julian day from Persian date

PERSIAN_EPOCH = 1948320.5
PERSIAN_WEEKDAYS = ["Yekshanbeh", "Doshanbeh",
                                 "Seshhanbeh", "Chaharshanbeh",
                                 "Panjshanbeh", "Jomeh", "Shanbeh"]

def persian_to_jd(year, month, day):
    epbase = year - 474 if year >= 0 else 473
    epyear = 474 + (epbase % 2820)

    return day +            (((month - 1) * 31) if (month <= 7) else(((month - 1) * 30) + 6)) +            math.floor(((epyear * 682) - 110) / 2816) +            (epyear - 1) * 365 +            math.floor(epbase / 2820) * 1029983 +            (PERSIAN_EPOCH - 1)


##  JD_TO_PERSIAN  --  Calculate Persian date from Julian day

def jd_to_persian(jd):

    jd = math.floor(jd) + 0.5

    depoch = jd - persian_to_jd(475, 1, 1)
    cycle = math.floor(depoch / 1029983)
    cyear = (depoch %1029983)
    if (cyear == 1029982):
        ycycle = 2820
    else :
        aux1 = math.floor(cyear / 366)
        aux2 = mod(cyear, 366)
        ycycle = math.floor(((2134 * aux1) + (2816 * aux2) + 2815) / 1028522) +                    aux1 + 1
    
    year = ycycle + (2820 * cycle) + 474
    if (year <= 0):
        year -= 1
    
    yday = (jd - persian_to_jd(year, 1, 1)) + 1
    month = math.ceil(yday / 31) if (yday <= 186) else math.ceil((yday - 6) / 30)
    day = (jd - persian_to_jd(year, month, 1)) + 1
    return [year, month, day]


##  MAYAN_COUNT_TO_JD  --  Determine Julian day from Mayan long count

MAYAN_COUNT_EPOCH = 584282.5

def mayan_count_to_jd(baktun, katun, tun, uinal, kin):

    return MAYAN_COUNT_EPOCH +           (baktun * 144000) +           (katun  *   7200) +           (tun    *    360) +           (uinal  *     20) +           kin


##  JD_TO_MAYAN_COUNT  --  Calculate Mayan long count from Julian day

def jd_to_mayan_count(jd):

    jd = math.floor(jd) + 0.5
    d = jd - MAYAN_COUNT_EPOCH
    baktun = math.floor(d / 144000)
    d = (d %144000)
    katun = math.floor(d / 7200)
    d = (d % 7200)
    tun = math.floor(d / 360)
    d = (d % 360)
    uinal = math.floor(d / 20)
    kin = (d % 20)

    return [baktun, katun, tun, uinal, kin]


##  JD_TO_MAYAN_HAAB  --  Determine Mayan Haab "month" and day from Julian day

MAYAN_HAAB_MONTHS = ["Pop", "Uo", "Zip", "Zotz", "Tzec", "Xul",
                                  "Yaxkin", "Mol", "Chen", "Yax", "Zac", "Ceh",
                                  "Mac", "Kankin", "Muan", "Pax", "Kayab", "Cumku", "Uayeb"]

def jd_to_mayan_haab(jd):


    jd = math.floor(jd) + 0.5
    lcount = jd - MAYAN_COUNT_EPOCH
    day = mod(lcount + 8 + ((18 - 1) * 20), 365)

    return [math.floor(day / 20) + 1, mod(day, 20)]


##  JD_TO_MAYAN_TZOLKIN  --  Determine Mayan Tzolkin "month" and day from Julian day

MAYAN_TZOLKIN_MONTHS = ["Imix", "Ik", "Akbal", "Kan", "Chicchan",
                                     "Cimi", "Manik", "Lamat", "Muluc", "Oc",
                                     "Chuen", "Eb", "Ben", "Ix", "Men",
                                     "Cib", "Caban", "Etznab", "Cauac", "Ahau"]

def jd_to_mayan_tzolkin(jd):


    jd = math.floor(jd) + 0.5
    lcount = jd - MAYAN_COUNT_EPOCH
    return [amod(lcount + 20, 20), amod(lcount + 4, 13)]


##  BAHAI_TO_JD  --  Determine Julian day from Bahai date

BAHAI_EPOCH = 2394646.5
BAHAI_WEEKDAYS = ["Jam\E1l", "Kam\E1l", "Fid\E1l", "Id\E1l",
                               "Istijl\E1l", "Istiql\E1l", "Jal\E1l"]

def bahai_to_jd(major, cycle, year, month, day):

    gy = (361 * (major - 1)) + (19 * (cycle - 1)) + (year - 1) +         jd_to_gregorian(BAHAI_EPOCH)[0]
    return gregorian_to_jd(gy, 3, 20) + (19 * (month - 1)) +           (0 if (month != 20) else  -14 if leap_gregorian(gy + 1) else -15)  +           day


##  JD_TO_BAHAI  --  Calculate Bahai date from Julian day

def jd_to_bahai(jd):
    

    jd = math.floor(jd) + 0.5
    gy = jd_to_gregorian(jd)[0]
    bstarty = jd_to_gregorian(BAHAI_EPOCH)[0]
    bys = gy - (bstarty +   (1 if(  ( gregorian_to_jd(gy, 1, 1) <= jd ) and ( jd <= gregorian_to_jd(gy, 3, 20) )   )else 0))
    major = math.floor(bys / 361) + 1
    cycle = math.floor(mod(bys, 361) / 19) + 1
    year = mod(bys, 19) + 1
    days = jd - bahai_to_jd(major, cycle, year, 1, 1)
    bld = bahai_to_jd(major, cycle, year, 20, 1)
    month =  20 if (jd >= bld) else (math.floor(days / 19) + 1)
    day = (jd + 1) - bahai_to_jd(major, cycle, year, month, 1)

    return [major, cycle, year, month, day]


##  INDIAN_CIVIL_TO_JD  --  Obtain Julian day for Indian Civil date

INDIAN_CIVIL_WEEKDAYS = [
    "ravivara", "somavara", "mangalavara", "budhavara",
    "brahaspativara", "sukravara", "sanivara"]

def indian_civil_to_jd(year, month, day):


    gyear = year + 78
    leap = leap_gregorian(gyear)     ## Is this a leap year ?
    start = gregorian_to_jd(gyear, 3, 21 if leap else 22)
    Caitra = 31 if leap else 30

    if (month == 1):
        jd = start + (day - 1)
    else :
        jd = start + Caitra
        m = month - 2
        m = math.min(m, 5)
        jd += m * 31
        if (month >= 8):
            m = month - 7
            jd += m * 30
        
        jd += day - 1
    

    return jd


##  JD_TO_INDIAN_CIVIL  --  Calculate Indian Civil date from Julian day

def jd_to_indian_civil(jd):

    Saka = 79 - 1                    ## Offset in years from Saka era to Gregorian epoch
    start = 80                       ## Day offset between Saka and Gregorian

    jd = math.floor(jd) + 0.5
    greg = jd_to_gregorian(jd)       ## Gregorian date for Julian day
    leap = leap_gregorian(greg[0])   ## Is this a leap year?
    year = greg[0] - Saka            ## Tentative year in Saka era
    greg0 = gregorian_to_jd(greg[0], 1, 1) ## JD at start of Gregorian year
    yday = jd - greg0                ## Day number (0 based) in Gregorian year
    Caitra = 31 if leap else 30          ## Days in Caitra this year

    if (yday < start):
        ##  Day is at the end of the preceding Saka year
        year -=1
        yday += Caitra + (31 * 5) + (30 * 3) + 10 + start


    yday -= start
    if (yday < Caitra):
        month = 1
        day = yday + 1
    else :
        mday = yday - Caitra
        if (mday < (31 * 5)):
            month = math.floor(mday / 31) + 2
            day = (mday % 31) + 1
        else :
            mday -= 31 * 5
            month = math.floor(mday / 30) + 7
            day = (mday % 30) + 1
        
    

    return [year, month, day]


########################### examples ##########################
##
## import jdate
##
## shamsi be miladi
## jd = jdate.persian_to_jd(1367,11,21)
## print jdate.jd_to_gregorian(jd)
## >>> [1989.0, 2.0, 10.0]
##
## miladi be shamsi
## jd = jdate.gregorian_to_jd(1989,2,10)
## print jdate.jd_to_persian(jd
## >>> 1367.0, 11.0, 21.0]
##
###############################################################
