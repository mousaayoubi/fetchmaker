import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

#Get rottweiler tail length
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

#Show no of whippet rescue dogs
whippet_rescue = fetchmaker.get_is_rescue("whippet")

num_whippet_rescues = np.count_nonzero(whippet_rescue)
print(num_whippet_rescues)

num_whippets = np.size(whippet_rescue)
print(num_whippets)

#Run a binomial test for 6% vs 8%
pvalue = binom_test(num_whippet_rescues, num_whippets, 0.08)
print(pvalue)

print("The result is not statistically significant.")

w = fetchmaker.get_weight("whippet")
t = fetchmaker.get_weight("terrier")
p = fetchmaker.get_weight("pitbull")

#Test significance of two groups agains each other using ANOVA test
tstat, pval_w = f_oneway(w, t,p)
print(pval_w)

#See which two groups are statistically significant using Tukeyhsd test

values = np.concatenate([w, t, p])
labels = ["whippet"] * len(w) + ["terrier"] * len(t) + ["pitbull"] * len(p)
result = pairwise_tukeyhsd(values, labels, 0.05)
print(result)

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

pood_bl = np.count_nonzero(poodle_colors == "black")
pood_br = np.count_nonzero(poodle_colors == "brown")
pood_go = np.count_nonzero(poodle_colors == "gold")
pood_gr = np.count_nonzero(poodle_colors == "grey")
pood_wh = np.count_nonzero(poodle_colors == "white")

shih_bl = np.count_nonzero(shihtzu_colors == "black")
shih_br = np.count_nonzero(shihtzu_colors == "brown")
shih_go = np.count_nonzero(shihtzu_colors == "gold")
shih_gr = np.count_nonzero(shihtzu_colors == "grey")
shih_wh = np.count_nonzero(shihtzu_colors == "white")

color_table = [[pood_bl, shih_bl], [pood_br, shih_br], [pood_go, shih_go], [pood_gr, shih_gr], [pood_wh, shih_wh]]

print(color_table)

_, pval_chi2, _, _ = chi2_contingency(color_table)
print(pval_chi2)

#Check if weights of pitbull vs chihuahua is statsitcally significant 
c = fetchmaker.get_weight("chihuahua")
tstat, pval_pc = f_oneway(p, c)
print(pval_pc)