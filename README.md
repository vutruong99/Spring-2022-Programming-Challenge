Happy holiday!

Firstly, I tried matching the messages with only "SHIB" and "DOGE" (v1), resulting in the visualizations without numbers (date_vs_scores, date_vs_counts, date_scores_counts). Then I tried to match more permutation of those key words like Shib, doge, sHib, dOGe (v2), resulting in the visualizations with 2s in their names. 

Conclusion:
* As for the number of messages, the spike was on May 8 (v1: 23, v2: 170). Something must have happened to the price of those two coins. 
* Regarding the sentiment score, in v1, the peek was on May 1 (0.458) and there were clearer indications of negative sentiments on May 4, 9, and 13. In v2, when I included more key words, the variance of the average of sentiment was lower and no day has negative average score. Peak for v2 = 0.155. 
* I attached the actual prices of these two coins for reference and it looks like DOGE coin also peak on May 8. Though there is not a clear correlation between the sentiment scores and the price.

Code overview:
* Firstly, I fetched all the text from the messages, including the link and command - type messages
* Secondly, I filtered non English words out because I thought it would not make sense to eliminate a sentence just because one word is not English.
* Next, I matched the key words
* After that, I calculated the average sentiment scores and messages.
* Lastly, I put them on a graph with dates.

To run my code:
* pip install -r requirements.txt
* python main.py

Thank you so much for reviewing my assignment. Merry Christmas and Happy New Year!