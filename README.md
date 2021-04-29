# antecedent-basis
Program seeks out 35 U.S.C. 112, second paragraph issues in claims
Final Project - 35 U.S.C. 112 (b) and pre-AIA 35 U.S.C. 112, second paragraph,  Analyzer
By Ross Varndell

This project takes an input claim text and outputs issues that need to be corrected to satisfy 35 U.S.C. 112(b).  35 U.S.C. 112(b) is often called “antecedent basis.”  This statute reads as follows:

35 U.S.C. 112
The following is a quotation of 35 U.S.C. 112(b):
(B) CONCLUSION.—The specification shall conclude with one or more claims particularly pointing out and distinctly claiming the subject matter which the inventor or a joint inventor regards as the invention.

This project follows this general flow chart:
1.	Input a claim, 
2.	search the text for the words “a”, “an”, “the” and “said,”
3.	search and save the adjectives and nouns after the “a” or “the,”
4.	determine if the adjective and nouns match,
5.	if the adjectives do not match, inform the user there is an antecedent basis issue under 35 USC 112(b),
6.	if the claim recites a limitation that grammatically incorrect, inform the user there is a claim objection.

For example, if the program is fed the following input text in step 1:

A vehicle containing: a first passenger and a second passenger, where the passenger jumps out the window of the vehicle.

The program will search for the “a”, “an”, “the” and “said” in the claim in step 2. 

Then, in step 3, the program saves the following groups of words:

vehicle, a first passenger, a second passenger, passenger, window, vehicle.

In step 4, the program sees if the words following the “a” or “an” match the words following the “the” or “said.”

first passenger ≠ passenger
second passenger ≠ passenger
? = window
vehicle = vehicle

In step 5, the program finds that "passenger" has a 35 USC 112(b) antecedent basis issue and prints:

a first passenger <-> the passenger -- Possible 112 2nd issue!

a second passenger <-> the passenger -- Possible 112 2nd issue!

In step 6, the program identifies that “window” has a grammatical issue and prints: 

? <-> the window -- claim objection -- 'the/said' should be 'a/an'


There are several sample claims in the markup cells at the top of the program. These claims can be cut and paste into the input to show the program runs and find the 35 U.S.C. 112(b) issues. 
