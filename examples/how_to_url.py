from pywikihow import HowTo

how_to = HowTo("https://www.wikihow.com/Train-a-Dog")

data = how_to.as_dict()

print("# URL")
print(how_to.url)
print("\n# TITLE")
print(how_to.title)
print("\n# INTRO")
print(how_to.intro)
print("\n# NUMBER OF STEPS")
print(how_to.n_steps)
print("\n# SUMMARY")
print(how_to.summary)


print("\n\n# FIRST STEP")
first_step = how_to.steps[0]
first_step.print()

# a dict, useful for saving/sending
data = first_step.as_dict()

print("\n\n# FULL HOW TO")
how_to.print(extended=True)
