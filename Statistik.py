import statistics
#Spannweite = Differenz zwischen dem höchsten und dem niedrigsten Wert
#List 1 = Textlaenge_in_Token
#List 2 = Datum
list_1 = [49187, 48439, 43280, 45497, 71645, 43060, 85843, 52027, 74420, 125538, 87914, 61348, 61950, 50119, 46896, 49396, 44586, 31474, 91713, 46689, 75402, 96948, 156095, 52566, 107955, 63717,61333, 101045, 58883, 26112, 37687, 53216, 70478, 59758, 72250, 90161, 123851, 106183, 72264, 70107, 52995, 65837, 93833, 149560, 91478, 71399, 71698, 79765, 91999, 84714, 50508, 132303, 67458, 52544, 79060, 64064, 75358, 47205, 64171, 63988]
list_2 = [2009, 2012, 2009, 2011, 2014, 2006, 2013, 2013, 2015, 2009, 2015, 2014, 2013, 2007, 2006, 2008, 2009, 2012, 2007, 2014, 2013, 2009, 2012, 2011, 2012, 2010, 2008, 2013, 2012, 2008, 2009, 2010, 2013, 2013, 2006, 2004, 2016, 2010, 2012, 2014, 2015, 2008, 2015, 2013, 2013, 2010, 2010, 2013, 2009, 2014, 2013, 2014, 2006, 2014, 2012, 2016, 2008, 2005, 2005, 2003]
range_list_1 = max(list_1) - min(list_1)
range_list_2 = max(list_2) - min(list_2)

print("Spannweite Textlaenge in Token:", range_list_1)
print("Spannweite Datum:", range_list_2)

#Arithmetisches Mittel = mean
ArithmetischeMittel_list_1 = statistics.mean(list_1)
print("Arithmetische Mittel Textlaenge in Token:", round(ArithmetischeMittel_list_1, 2)) #Zum Runden auf 2te Nachkommazahlen
ArithmetischeMittel_list_2 = statistics.mean(list_2)
print("Arithmetische Mittel Datum:", round(ArithmetischeMittel_list_2,2))

#Median = median = Wert genau in der Mitte
median_list_1 = statistics.median(list_1)
print("Median: Textlaenge in Token:", median_list_1)
median_list_2 = statistics.median(list_2)
print("Median Datum:", median_list_2)

#Modus = mode = Der Modus (auch Modalwert genannt) einer Datenreihe ist das Merkmal bzw. der Wert mit der größten Häufigkeit.
modus_list_1 = statistics.mode(list_1)
print("Modus: Textlaenge in Token:", round(modus_list_1))
modus_list_2 = statistics.mode(list_2)
print("Modus: Datum:", modus_list_2)

#Streuungsmaße = stdev
streuung_list_1 = statistics.stdev(list_1)
print("Steuung Textleange:", streuung_list_1)
streuung_list_2 = statistics.stdev(list_2)
print("Streuung Datum:", streuung_list_2)

list_linguistik = [49187, 48439, 43280, 45497, 71645, 43060, 85843, 52027, 74420, 125538, 87914, 61348, 61950, 50119, 46896, 49396, 44586, 31474, 91713, 46689, 75402, 96948, 156095, 52566, 107955, 63717,61333, 101045, 58883, 26112]
list_literaturwissenschaften =[37687, 53216, 70478, 59758, 72250, 90161, 123851, 106183, 72264, 70107, 52995, 65837, 93833, 149560, 91478, 71399, 71698, 79765, 91999, 84714, 50508, 132303, 67458, 52544, 79060, 64064, 75358, 47205, 64171, 63988]
#Streuung
streuung_linguistik = statistics.stdev(list_linguistik)
print("Streuung Linguistik:", streuung_linguistik)
streuung_literaturwissenschaften = statistics.stdev(list_literaturwissenschaften)
print("Streuung Literaturwissenschaft:", streuung_literaturwissenschaften)
#ArithmetichesMittel
am_linguistik = statistics.mean(list_linguistik)
print("Arithmetisches Mittel Linguistik:", round(am_linguistik, 2))
am_literaturwissenschaften = statistics.mean(list_literaturwissenschaften)
print("Arithmetisches Mittel Literaturwissenschaft:", round(am_literaturwissenschaften, 2))