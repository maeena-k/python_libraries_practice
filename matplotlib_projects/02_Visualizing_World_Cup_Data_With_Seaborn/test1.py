load_file_in_context('script.py')

try:
  sns.barplot
except:
  fail_tests('Did you remember to `import seaborn as sns`?')
  
pass_tests()