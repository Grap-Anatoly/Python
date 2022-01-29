# The p-value is about the strength of a hypothesis.
# We build hypothesis based on some statistical model and compare the model's validity using p-value.

from scipy import stats

rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
print(stats.ttest_1samp(rvs,5.0))

# In the following examples, there are two samples, which can come either from the same or from different distribution,
# and we want to test whether these samples have the same statistical properties.

# ttest_ind − Calculates the T-test for the means of two independent samples of scores.
# This is a two-sided test for the null hypothesis that two independent samples have identical average (expected) values.
# This test assumes that the populations have identical variances by default.

# We can use this test, if we observe two independent samples from the same or different population.
# Let us consider the following example.

rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
print(stats.ttest_ind(rvs1,rvs2))